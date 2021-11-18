---
title: "Automatic Rust verification tools (2021)"
layout: post
---

![Rust logo]{: style="float: left; width: 10%; padding: 1%"}
Last year, I wrote [a summary of all the Rust verification tools
that I knew about][RVT 2020].
But formal verification of Rust is a fast-changing field so I took advantage
of all the experts at the 2021 [Rust Verification Workshop][RV2021]
to make [an up to date list][RVT 2021 doc] of tools.
This post focuses on the automatic verification tools.


*[If you know of any tools that should be added or you want to correct
the description of a tool, please suggest a change by email
or [on twitter](https://www.twitter.com/alastair_d_reid)
or by changing the edit mode of [the RVT list][RVT 2021 doc]
to "suggesting" and making the change.]*


### Organization and limitations

[My own research project][RVT website] focuses on tools that that are easily
used by mainstream Rust developers.
In our paper ["Towards making formal methods normal: meeting developers where they are"][HATRA 2020],
we talked about the benefits of tools that build on the experience
that developers already have and the advantages of specialized tools.
So, in this survey, I am going to try to start with the tools that best
fit that vision even if they achieve this accessibility by not catching
all bugs.

I will try to mention all verification tools that I know about but
any tools or projects that seem to be dead or inactive will just get
a brief mention.
Please let me know if I have got it wrong.
On a related note: I am mostly relying on the authors' descriptions of their own tools so
this list will not be strictly in order of increasing complexity.  And, of
course, complexity is subjective and influenced by what you are already
familiar with.

Finally, it's worth saying that software verification is such a mature field
that simple taxonomies don't really work because many tools use a hybrid
approach to reasoning about code. They may primarily use one technique but
borrow ideas from some other technique to fix some weakness in the primary
technique.  Nevertheless, I have tried to group tools by (my best understanding
of) the primary technique that they rely on to give some structure to this list
and some insight into what their relative strengths and weaknesses are.



## Linters and static analyses

> The best camera is the one that's with you
> -- Chase Jarvis (2009)

Although my focus is mostly on tools developed by the formal verification
community, it is worth mentioning that most bugs are caught by the
Rust typesystem, the borrow-checker, the 'linter' [clippy]
and [rust analyzer].
These give immediate feedback in your editor or when you build your code
and linters can be built into the CI process so that anyone
reviewing your code can see whether your code introduced any new
warning messages. Teams at both Google and Facebook have found
that feedback during the CI process can be highly effective
[[sadowski:cacm:2018], [distefano:cacm:2019]].

At the [Rust verification workshop], I learned that it is actually quite easy
to write your own lint check and integrate it into the compiler
because the compiler has a flexible plugin mechanism that makes
it easy to extend.
So, if you find that you and the people you work with are
often making the same mistake or you want to migrate your code
away from bad programming practices [[wright:icsm:2013]] or you
have a favourite static analysis that you want to apply to Rust,
then it is fairly easy to do so.
See Niko Matsaki's [presentation](https://hackmd.io/RiztubvfT4eOk4-4nM8Y7Q?view)
/ [video](https://www.youtube.com/watch?v=B1vbeXsRux4&list=PL-uEDsw-7yRLYMEdlvh4udnjK3JtGJgSh)
or read [the linter section of the rustc-dev book](https://rustc-dev-guide.rust-lang.org/diagnostics.html#lints).


## Instrumented interpreters

The [Miri] instrumented Rust interpreter executes your program while checking very carefully
for Undefined Behaviour (UB) and includes enforcement of the
Stacked-Borrows aliasing model [[jung:popl:2020]].
Miri stands out as being one of the few tools that you can use to check
that an 'unsafe' block is actually obeying the Rust safety rules so,
if you are using 'unsafe' in your code, you really should be using Miri.

Compared with formal verification tools, the weakness of Miri is that it
executes your code in much the same way as it would normally run (just with
extra checks and a bit slower), it is up to you to figure out what input values
to test with.
The huge strength of formal verification tools is that they consider all
input values including the weird corner cases that you might otherwise
forget to test with.

While on the subject of tools that execute your code rather than doing some
form of static check, I should mention the concurrency checkers
[Loom] which focuses on exhaustive checking
and
[Shuttle] which focuses on randomized checking.
These are important because, although Rust [encourages use of concurrency][fearless concurrency] by making it easy and data-race free to write
concurrent programs, most formal verification tools for Rust
do not support concurrency (yet).


## Dynamic symbolic execution


Turning to tools from the formal verification community,
I think that the easiest tools to use are dynamic symbolic execution tools.
What makes these tools easy to use is that they can be thought of
as more powerful variants of techniques and tools that
developers are already familiar with: testing and fuzz-testing.
In fact, Godefroid describes tools like this as "whitebox fuzzing" [[godefroid:acmq:2012]]
because of the way that they choose input values to test with based on a deep analysis
of the code.

Like an instrumented interpreter, a [dynamic symbolic execution] (DSE) tool explores paths through your program. The difference is that you do not have to create
test values to test with: DSE automatically identifies viable paths through
your program and reasons about all possible values that could follow that same
path.

DSE has two main weaknesses

- Path explosion: The number of paths through a program can be (and often is) exponential in the size
  of the program so, unless you analyse your program in small pieces, you
  cannot check all possible paths through your program.
  To handle this, DSE tools are often run with a timeout.

- Loops: In general DSE cannot show that a loop will always behave correctly:
  it only checks some of the possible executions of a loop.

As a result of this, DSE tools are usually used as very effective bug-finding tools
rather than proof tools.
Since DSE tools can only consider a sample of all possible paths through a program
in a limited amount of time,
they typically have ways of biasing the sample to focus on "interesting" paths,
maximizing code coverage, etc.


The main DSE tools for Rust are

- [RVT][RVT website] converts Rust to LLVM-IR and uses the [KLEE] DSE tool to check.
  RVT has a particular focus on scaling, handling the full range of Rust features, etc.
  RVT also provides a [proptest]-compatible DSL for creating verification harnesses that can also be
  used with a fuzzer so you can use your verification harnesses as fuzzing harnesses and
  vice-versa. (See my earlier post "[Rust testing or verifying: why not both]".)

- [Cargo-KLEE] also converts Rust to LLVM-IR and uses [KLEE].
  This project focuses more on embedded systems where it is more feasible to
  explore all paths through the code. [[lindner:indin:2018], [lindner:indin:2019]]

- [Seer] a MIR-based symbolic execution tool (inactive)

- [KLEE Rust] provides KLEE bindings for Rust (inactive)


Given that DSE is like fuzzing, there has been work on 
hybrid tools that combine symbolic execution with fuzzing (e.g.,
[[yun:usenix:2018]]). Unfortunately, I don't know of any for Rust yet.  This is a shame
because I think that it would be a really useful.


## Bounded model checkers

Another relatively easy to use class of  verification tools is bounded model
checkers (BMC).
While a DSE tool explores paths in a more or less depth-first manner[^DSE-caveats],
a BMC tool explores paths in a breadth-first manner: exploring all possible execution paths
that can occur in the first iteration of a loop before considering the execution paths of
the second iteration.

The advantage of BMC is that this gives some partial guarantees about your code: if there is
no way for a loop to fail within the first few iterations, then maybe the code cannot fail?
The larger this bound 'k', the more confidence you can have in your code.
And, if the loop is bounded and you explore enough iterations, then you can prove that
the loop is correct.

[^DSE-caveats]:
    To be more accurate, only the very simplest DSE would explore paths in
    pure depth-first order.
    As DSE executes, it tends to have hundreds or thousands of paths to explore
    and most DSE tools have a bunch of heuristics and controls for deciding
    which path to execute and for how long.
    Nevertheless, between these context switches, DSE executes each path
    in the same depth-first order that at an interpreter would execute it.

BMC has three main weaknesses

- Loops: like DSE, it cannot show that a loop will always behave correctly:
  it only checks up to some loop bound 'k'.

- External calls: if your program makes an external call such as invoking
  an external library or an operating system call then it cannot reason
  about that piece of code unless you create a specification of that
  external call or your BMC tool can perform BMC on your OS (not likely).


- Problem paths: if one branch of a conditional has some feature
  that the tool does not support (e.g., external calls or inline assembly code),
  then a BMC tool typically cannot reason
  about the conditional at all.
  In contrast, DSE can skip the problem branch and explore the other branch.


The main BMC tools for Rust are

- [Rust Model Checker][RMC] (RMC)
  converts Rust's MIR intermediate language to [CBMC]'s intermediate representation.
  ([CBMC] is a mature, well-supported bounded model checker that supports several
  languages including C and Verilog.)

- [SMACK] converts MIR to Microsoft Research's [Boogie] &nbsp;  [Intermediate Verification Language]
  providing access to a range of different verification tools.

- [SeaHorn] is verification tool based on the LLVM intermediate representation.
  Interestingly, SeaHorn has several different modes of operation including
  bounded model checking.
  The [RVT tools][RVT website] include support for verifying with SeaHorn
  as an alternative to [KLEE].

- [Crux-MIR] converts MIR to Galois' [SAW] representation and performs an adaptive form
  of BMC that automatically determines the bound 'k' on how many iterations of a loop to
  consider.

- [CRUST] (inactive)


## Abstract interpreters

Instrumented interpreters, Dynamic Symbolic Execution tools (DSE) and Bounded
Model Checkers (BMC) reason about loops one iteration at a time.  If your
program has an infinite loop (e.g., server code), they cannot explore all
iterations and, if your program has a loop with a large number of iterations
then it may take the tool a *very* long time to finish.

Abstract interpreters avoid this limitation by (very roughly) exploring a few
iterations of the loop and then calculating the effect of executing the
remaining iterations using something analogous to loop invariants. (For a more
technical and precise description, see
[the Wikipedia page](https://en.wikipedia.org/wiki/Abstract_interpretation).)

They can also avoid the exponential growth in the number of paths seen in DSEs
and they can handle external function calls by asking the user to provide
a "function summary" for each external call.

The main weaknesses of abstract interpreters are

- Abstract interpreters can typically only reason about properties of a certain
  form. For example, for an integer, they may reason about the range of
  an integer but be unable to reason about whether an integer is odd/even
  or a multiple of 10 or a prime number.
  Or, they may be able to reason about the relationship between two variables
  but not three variables.
  (e.g., "a <= b + 10" but not "a <= b + c")
  So they may work really well on some code and quite badly on other code.

- The more different that a tool's operation is from directly executing
  code, the less precise the analysis gets and the harder it is
  to handle some language features.
  e.g., if the interpreter cannot accurately resolve what functions a function pointer
  could point to, then they will struggle with code that calls that function
  pointer.
  Instrumented interpreters, DSE, etc. have less problem resolving function
  pointers because they are more concrete.

The main abstract interpreters for Rust are

- [MIRAI] is a hybrid tool that combines  abstract interpretation and
  dynamic symbolic execution that can find whether
  a program can panic and can also track the flow of data through a program.
  It handles function calls by constructing "function summaries" on demand:
  allowing modular verification.

- [SeaHorn] can exploit abstract interpretation for verification
  as an alternative to bounded model checking.
  Although the [RVT tools][RVT website] include support for verifying with SeaHorn
  they have not been tested with SeaHorn's abstract interpretation.

## Verification tools written in Rust


- [Haybale] is a DSE kit for LLVM-IR written in Rust.
  Unlike most verification tools, this is more of a library that you can
  use to build a wide variety of tools rather than a finished tool - a very
  interesting design choice that I am keen to explore.
  AFAIK, there is no description of how to use Haybale to verify Rust
  but I know that it has been used to analyze parts of the
  [Tock] embedded OS.

- [StateRight][https://github.com/stateright/stateright]
  is an Embedded Domain Specific Language (EDSL) that lets you describe what you want to verify.

## What is the best automatic tool?

This depends on two things: what you are trying to do; and
how complex your code is.

In general, the higher the level of assurance that you want
to achieve, the simpler and smaller your code has to be.
If you want to show that your program precisely implements
a specification, you might
not be able to handle more advanced/dynamic features like
traits and closures or more complex interactions like calls to
C/C++ code.
Or you might have to put in extra work like writing function contracts to split the
task into smaller parts.

Instrumented interpretation and dynamic symbolic execution give
the weakest guarantees but the tools generally handle more of the language with
less difficulty.

BMC and abstract interpretation give stronger guarantees but the tools tend
to be more restricted although this will improve a bit as the tools mature.

The only tool that I have used myself is [the tool that I work on myself][RVT website]
but, from talking to others, I think the tools to consider using are
[Miri],
[RVT/KLEE][RVT website],
[RMC] and
[MIRAI].
If you are doing something specialized like developing crypto code, you should
also look at [Crux-MIR].


-----------

[RVT website]: {{site.RVTurl}}/
[RVT github]: https://github.com/project-oak/rust-verification-tools/
[RVT 2020]: {% post_url 2020-05-08-rust-verification-tools %}
[RV2021]: https://sites.google.com/view/rustverify2021
[Rust language]: https://www.rust-lang.org
[Rust book]: https://doc.rust-lang.org/book/
[Cargo tool]: https://doc.rust-lang.org/cargo/
[Rust fuzzing]: https://github.com/rust-fuzz
[Rustonomicon]: https://doc.rust-lang.org/nomicon/
[Sealed Rust]: https://ferrous-systems.com/blog/sealed-rust-the-pitch/

[astrauskas:oopsla:2019]: {{site.RWurl}}/papers/astrauskas:oopsla:2019/
[baranowski:atva:2018]: {{site.RWurl}}/papers/baranowski:atva:2018/
[jung:popl:2017]: {{site.RWurl}}/papers/jung:popl:2017/
[jung:popl:2020]: {{site.RWurl}}/papers/jung:popl:2020/
[lindner:indin:2018]: {{site.RWurl}}/papers/lindner:indin:2018/
[lindner:indin:2019]: {{site.RWurl}}/papers/lindner:indin:2019/
[matsushita:esop:2020]: {{site.RWurl}}/papers/matsushita:esop:2020/
[toman:ase:2015]: {{site.RWurl}}/papers/toman:ase:2015/

[Rust verification papers]: {{site.RWurl}}/notes/rust-language/

[verification competitions]: {% post_url 2020-04-19-verification-competitions %}

[Lean]: {{site.RWurl}}/notes/lean-theorem-prover/
[SV-COMP]: {{site.RWurl}}/notes/sv-competition/
[Haskell]: https://haskell.org/
[nofib benchmark suite]: https://link.springer.com/chapter/10.1007/978-1-4471-3215-8_17

[Rust verification working group]: https://rust-lang-nursery.github.io/wg-verification/
[Rust verification workshop]: https://sites.google.com/view/rustverify2020

[CBMC]: https://github.com/diffblue/cbmc/pull/4894
[Creusot]: https://github.com/xldenis/creusot
[Crust]: https://github.com/uwplse/crust
[Crux-mir]: https://github.com/GaloisInc/mir-verifier
[Electrolysis]: https://github.com/Kha/electrolysis
[Ferrite]: https://maybevoid.com/pdf/ferrite-draft-2020.pdf 
[Ferrous Systems]: https://ferrous-systems.com/
[hacspec]: https://hacspec.github.io/
[Haybale]: https://github.com/PLSysSec/haybale
[Cargo-KLEE]: https://gitlab.henriktjader.com/pln/cargo-klee
[KLEE Rust]: https://github.com/jawline/klee-rust
[LibHoare]: https://github.com/nrc/libhoare
[MIRAI]: https://github.com/facebookexperimental/MIRAI
[Miri]: https://github.com/rust-lang/miri
[Polonius]: http://smallcultfollowing.com/babysteps/blog/2018/04/27/an-alias-based-formulation-of-the-borrow-checker/
[PRUSTI]: https://github.com/viperproject/prusti-dev
[RustBelt]: https://plv.mpi-sws.org/rustbelt/
[RustFuzz]: https://github.com/rust-fuzz
[RustHorn]: https://github.com/hopv/rust-horn
[Rustv]: https://github.com/pandaman64/sabi
[Seer]: https://github.com/dwrensha/seer
[SMACK]: https://github.com/smackers/smack

[contracts crate]: https://gitlab.com/karroffel/contracts
[Viper rust-contracts]: https://github.com/viperproject/rust-contracts
[arbitrary crate]: https://github.com/rust-fuzz/arbitrary
[librarification]: http://smallcultfollowing.com/babysteps/blog/2020/04/09/libraryification/
[verifier crate]: https://crates.io/crates/verifier
[verifier benchmarks]: https://github.com/soarlab/rust-benchmarks

[Rust logo]: {{site.baseurl}}/images/Rust_programming_language_black_logo.svg

[KLEE]: https://klee.github.io/
[SeaHorn]: https://seahorn.github.io/

[RVT 2021 doc]: https://docs.google.com/document/d/1KlHeawNg4UDzvNLByv7RxYTGTVLBGIdfg8532pfuJKU/edit?usp=sharing

[distefano:cacm:2019]: {{site.RWurl}}/papers/distefano:cacm:2019
[godefroid:acmq:2012]: {{site.RWurl}}/papers/godefroid:acmq:2012/
[jung:popl:2020]:      {{site.RWurl}}/papers/jung:popl:2020/
[sadowski:cacm:2018]:  {{site.RWurl}}/papers/sadowski:cacm:2018/
[wright:icsm:2013]:    {{site.RWurl}}/papers/wright:icsm:2013/
[yun:usenix:2018]:     {{site.RWurl}}/papers/yun:usenix:2018/

[HATRA 2020]: {{site.baseurl}}/papers/HATRA_20/
[clippy]: https://rust-lang.github.io/rust-clippy/master/index.html
[rust analyzer]: https://rust-analyzer.github.io/

[Loom]: https://github.com/tokio-rs/loom
[Shuttle]: https://crates.io/crates/shuttle
[Tock]: https://www.tockos.org/
[proptest]:      https://github.com/AltSysrq/proptest
[Rust testing or verifying: why not both]: {% post_url 2020-09-03-why-not-both %}
[fearless concurrency]: https://blog.rust-lang.org/2015/04/10/Fearless-Concurrency.html
[dynamic symbolic execution]: https://en.wikipedia.org/wiki/Symbolic_execution
[RMC]: https://github.com/model-checking/rmc
[Boogie]: {{site.RWurl}}/notes/boogie-verifier/
[Intermediate Verification Language]: {{site.RWurl}}/notes/intermediate-verification-language/
[SAW]: https://saw.galois.com/
