---
title: Rust verification tools
layout: post
---

The [Rust language] and the Rust community are really interesting if you are interested
in building better quality systems software.

- The language is specifically designed to make it easier to build reliable
  software.
- The [Rust book] and the [Cargo tool] actively promote the idea that good
  Rust code includes documentation and tests.
- There is an active [Rust fuzzing] community to improve the state
  of Rust packages and other software.

Over the last few months, I have been trying to understand one more part
of the story:
_what is the state of formal verification tools for Rust?_

The clean, principled language design and, in particular, the Rust type system
[fit really well with recent work on formal verification][astrauskas:oopsla:2019].
Academic researchers are showing a lot of interest in Rust and
and it seems that the community should be receptive to the idea of formal verification.

So what tools are out there?
What can you do with them?
Are they complete?
And are they being maintained?

Here is a list of the tools that I know about (more details below):
- CBMC:
  [Pull Request][CBMC]
- Crust:
  [repository][Crust],
  [paper][toman:ase:2015]
- Crux-mir:
  [repository][Crux-mir],
- Electrolysis:
  [blog post](https://kha.github.io/2016/07/22/formally-verifying-rusts-binary-search.html),
  [repository][Electrolysis],
  [thesis](https://pp.ipd.kit.edu/uploads/publikationen/ullrich16masterarbeit.pdf),
  [slides](http://kha.github.io/electrolysis/presentation.pdf)
- MIRAI:
  [repository][MIRAI]
- Prusti:
  [website](https://www.pm.inf.ethz.ch/research/prusti.html)
  [repository][Prusti],
  [VS code extension](https://marketplace.visualstudio.com/items?itemName=viper-admin.prusti-assistant),
  [paper][astrauskas:oopsla:2019]
- RustBelt:
  [website][RustBelt],
  [paper][jung:popl:2017]
- RustHorn:
  [repository][RustHorn],
  [paper][matsushita:esop:2020]
- SMACK:
  [website](https://smackers.github.io),
  [repository][SMACK],
  [paper][baranowski:atva:2018]

I should also mention [Miri] ([paper][jung:popl:2020]).
Miri is not a formal verification tool
but it can be used to detect undefined behaviour
and it is important in defining what "unsafe" Rust
is and is not allowed to do.




_Before I go any further, I should probably add a disclaimer:
Although I have spent some time looking at what is available and
reading [Rust verification papers],
I am not an expert in this area so I have probably got things wrong, missed
out important tools, etc.
Do please [contact me](mailto:adreid@google.com)  with additions and
corrections._


## What can the tools verify?

There are three major categories of software verification tool
in roughly increasing order of how hard it is to use them:
automatic (aka extended static checkers),
auto-active verifiers
and deductive verifiers.


### Automatic verification tools

These tools are good for checking for what some call "Absence of Run-Time
Exception" (AoRTE).
Runtime errors includes things like the following
(not all of these apply to safe Rust code).

- No division by zero
- No integer overflow
- No failing assertions
- Memory safety
  - All array accesses in bounds
  - No null dereferences
  - No buffer overflows
  - No use after free
  - No memory leaks
- Lock safety of concurrent code

While not all tools aim to check all of the above,
the automatic verification tools I know of are
[CBMC],
[Crux-mir],
[MIRAI],
[RustHorn],
[SMACK].
It is worth saying that the [Crust] tool is different from the other
tools in that it is designed to check that a library that contains
unsafe Rust code is externally safe.

One of the appealing features of the automatic verification tools
is that you don't have to write specifications.
Typically, all you have to do is build a verification harness
(that looks a wee bit like a fuzzing harness)
and maybe add some extra assertions into your code.


### Auto-active verification tools

While automatic tools focus on things not going wrong,
auto-active verification tools help you verify some key
properties of your code: data structure invariants,
the results of functions, etc.
The price that you pay for this extra power is that
you may have to assist the tool by adding function
contracts (pre/post-conditions for functions),
loop invariants, type invariants, etc. to your code.

The only auto-active verification tool that I am
aware of is [Prusti].
Prusti is a [really interesting tool][astrauskas:oopsla:2019] because
it exploits Rust's unusual type system to help it verify code.
Also Prusti has the slickest user interface:
a [VSCode extension](https://marketplace.visualstudio.com/items?itemName=viper-admin.prusti-assistant)
that checks your code as you type it!


### Deductive verification tools

These tools can be used to show things like "full functional correctness":
that the outputs are exactly what they should be.
Deductive verification tools typically generate a set of "verification
conditions" that are then proved using an interactive theorem prover.

The deductive verification tools for Rust that I know of are
[Electrolysis] and [RustBelt].
The goal of [RustBelt] is to verify unsafe Rust code but,
strictly speaking, RustBelt does not actually verify Rust code:
you manually transcribe Rust code into &lambda;-Rust and
then use RustBelt to verify that code using IRIS and
the Coq theorem prover.


## How much Rust do these tools support?

As far as I can tell, no verification tool currently
supports the full Rust language.
(In contrast, C verification tools are complete enough to verify
things like OS device drivers.)
Some of the big challenges are:
- Unsafe code
- Closures
- Stdlib

The Electrolysis repository has the [clearest statement of
language coverage](http://kha.github.io/electrolysis/)
of all the tools.
It uses the language reference manual as a guide to what
has to be covered and it uses test code from the manual
(as well as some hand-written tests) to confirm that
that feature is supported.


### Unsafe code

> THE KNOWLEDGE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF UNLEASHING
> INDESCRIBABLE HORRORS THAT SHATTER YOUR PSYCHE AND SET YOUR MIND ADRIFT IN THE
> UNKNOWABLY INFINITE COSMOS.
> <br>--- The [Rustonomicon].[^irrelevant]

[^irrelevant]:
    That quote from the Rustinomicon isn't really relevant – but it is fun!

The problem with unsafe code is that it eliminates the big advantage
of Rust code: that the type system gives you a bunch of guarantees that
you can rely on while reasoning about your code.
This means that every tool that takes advantage of the Rust typesystem
is going to have a problem with unsafe code.
In particular, I think that this is a problem for [Electrolysis],
[Prusti] and [RustHorn].
On the other hand, tools like [SMACK] that are based on the LLVM IR
have no problem with unsafe code.


### Closures

While "unsafe" code raises some fundamental barriers for some tools,
as far as I can tell, closures just seem to take more effort.
They bring in a degree of indirection / higher-order behaviour that
is harder for tools to handle.

The only tools that I am aware of that can handle closures at the moment
are [Electrolysis] and, I suspect, [SMACK].
(But I could easily have missed some.)


### Standard library

The standard library is complicated in two ways:
1. Some of it uses unsafe code
2. Some of it is highly optimized

So, many verification tools replace the standard library with
something simpler such as a simpler implementation or
a function contract.
It is quite a lot of work to create and maintain this verification
version of the library so standard library support can be quite
incomplete.

Two tools that I know are affected by this are
- the [RustHorn] tool cannot handle the RefCell and Rc
- and the [SMACK] tool has only a
  [small subset of the standard library](https://github.com/smackers/smack/blob/master/share/smack/lib/smack.rs).
But, as far as I know, all tools have problems with incomplete
standard library support.


## Which tools are being maintained?

These tools all vary in how actively they are being developed.
Here is what I know about them.
(Please tell me if I got this wrong.)

- Actively developed: 
  [Crux-mir],
  [MIRAI],
  [Miri],
  [Prusti],
  [RustBelt],
  [RustHorn],

- Seems to have stalled:
  Pull request for [CBMC],
  (Rust support in) [SMACK].

- Appears to be abandoned: 
  [Crust],
  [Electrolysis].


## Other thoughts

While I was looking at all these different tools, I noticed
a few other challenges with the tools.
Some of the tools have solutions for these issues.

- [Cargo tool] integration: Many of the tools seem to act on a single file
  but if I want to verify a Rust package, I really want something
  that is integrated with Cargo.

- Standard verification interfaces for automatic verification tools:
  The automatic verification tools all seem to have different ways
  of creating symbolic values and specifying assumptions.
  I wonder whether the [arbitrary crate] used by fuzzers could
  provide some inspiration for a standard symbolic value API?

- Standard verification interfaces for function contracts:
  The [MIRAI] tool is using the [contracts crate] for function
  contracts. Is this a good choice? Are/should other tools
  use the same crate?


## Conclusion

Is looks as though Rust is a very active area for verification tools.
I am not sure yet whether any of the tools are complete enough for
me to use them in anger but it seems that some of them are getting close.

&#x1F576;
The Rust verification future looks very bright!
&#x1F576;


------------

_Where did I get this list from?_
As you might imagine, I searched the Google Scholar and the 
web for things like "Rust verification tool"
This finds things like
- The [Rust verification working group] which seems to be dormant,
- The [Rust verification workshop] – I planned to attend this but it has been
  delayed.  The list of talks was helpful in finding some of the tools
  listed on this page.

Also, Martin Nyx Brain pointed me at the CBMC pull request for Rust support.

----------------

[Rust language]: https://www.rust-lang.org
[Rust book]: https://doc.rust-lang.org/book/
[Cargo tool]: https://doc.rust-lang.org/cargo/
[Rust fuzzing]: https://github.com/rust-fuzz
[Rustonomicon]: https://doc.rust-lang.org/nomicon/

[astrauskas:oopsla:2019]: {{ site.baseurl }}/RelatedWork/papers/astrauskas:oopsla:2019/
[baranowski:atva:2018]: {{ site.baseurl }}/RelatedWork/papers/baranowski:atva:2018/
[jung:popl:2017]: {{ site.baseurl }}/RelatedWork/papers/jung:popl:2017/
[jung:popl:2020]: {{ site.baseurl }}/RelatedWork/papers/jung:popl:2020/
[matsushita:esop:2020]: {{ site.baseurl }}/RelatedWork/papers/matsushita:esop:2020/
[toman:ase:2015]: {{ site.baseurl }}/RelatedWork/papers/toman:ase:2015/

[Rust verification papers]: {{ site.baseurl }}/notes/rust-language/

[Rust verification working group]: https://rust-lang-nursery.github.io/wg-verification/
[Rust verification workshop]: https://sites.google.com/view/rustverify2020

[CBMC]: https://github.com/diffblue/cbmc/pull/4894
[Crust]: https://github.com/uwplse/crust
[Crux-mir]: https://github.com/GaloisInc/mir-verifier
[Electrolysis]: https://github.com/Kha/electrolysis
[MIRAI]: https://github.com/facebookexperimental/MIRAI
[PRUSTI]: https://github.com/viperproject/prusti-dev
[RustBelt]: https://plv.mpi-sws.org/rustbelt/
[RustHorn]: https://github.com/hopv/rust-horn
[SMACK]: https://github.com/smackers/smack

[Miri]: https://github.com/rust-lang/miri
[contracts crate]: https://gitlab.com/karroffel/contracts
[arbitrary crate]: https://github.com/rust-fuzz/arbitrary
