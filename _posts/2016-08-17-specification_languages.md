---
layout: post
title: ARM's Architecture Specification Language
---

What language should you write a specification in?  Should you use the language
supported by your favourite verification tool (HOL, Verilog, ...)?
Or should you write it in a DSL and translate that to whatever your
verification tool needs?

I have been formalizing ARM's processor architecture specification, with the
primary aim of enabling formal verification of ARM processors.
My basic approach has been to create a specification in one language
and then, with some difficulty, translate the specification to Verilog
so that I can use commercial Verilog model checkers.
This article explains why I didn't just write the specification in Verilog to begin with.

The most important reason for not using Verilog is that it is really hard to
create a specification that you trust.  It takes a lot of work to create
a specification because after you write it, you have to test it in multiple
ways (see my upcoming paper ["Trustworthy Specifications of ARM v8-A and v8-M
System Level Architecture"]({{ site.url }}/papers/fmcad2016-trustworthy.pdf)).
To test it, you will have to persuade some very busy engineers to help you with
the testing.  And then you have to fix the bugs and get the senior architects
to approve your changes. And just when you think you are all done, you have to
come up with a plan to make sure that the specification will be maintained
after you have moved onto a new research project.  This is critical because
processor specifications gain new instructions and new system-level features
nearly every year.

I think the only way to do all this is to make sure that the specification
meets multiple purposes so it has to be usable:

  * As documentation because that is one of the most critical existing
    deliverables.

  * To help the people creating test programs because they will be the most
    useful to you.  So I added features to measure architectural test coverage
    since that was a feature they really valued.

  * To help the people defining new architecture extensions to check that
    the specification meets their intention.  So I added a Read-Eval-Print
    loop interface to let them quickly experiment with the specification.

  * To formally verify the processor both because that is your primary goal
    and because this is the hardest test that the specification is correct.

And if you can make it useful to teams creating assemblers, compilers, JITs,
operating systems, etc. then so much the better.

In addition to meeting these different needs, our specification language has a few
unusual properties.

  * To meet all the above needs, requires that the language is easy to
    understand unambiguously by engineers from many different backgrounds:
    hardware engineers, software engineers, technical writers, etc.

  * All programming languages should be designed with the expectation that the
    program will have 10 times more readers than writers.  For specification
    languages, this ratio shifts to 100s or 1000s more readers than writers.

  * The other unusual thing about our case is that we only have two programs we
    need to write in this language: the ARM v8-A/R specification and the ARM
    v8-M specification.  Nothing else matters.  (This is a bit of a challenge
    both for designing the language and for testing the tools: some features of
    the language only have a few examples of their use and some combinations of
    features have no examples at all.)

With all this in mind, our specification language (called "ASL") is
a fairly simple language:

* ASL is an indentation-sensitive language: it uses the indentation of the code
  to define the structure of the code.  This serves two purposes.  First, it
  avoids a small but subtle source of confusion where the braces (or other
  structure indications) in more conventional languages don't match the
  indentation of the program.  Secondly, the specification is sometimes
  printed on paper and being indentation-sensitive avoids the need for
  multiple lines containing one brace each when exiting multiple
  levels of structure.

  Worrying about the amount of vertical space when printed may seem like
  an unusual thing in language design but it perfectly illustrates the
  need to think about all the possible uses of the specification.
  An even more vivid example of this was an early code review which
  included comments on whether the change created widow lines ---
  a review comment I had never heard in 30 years of programming.

* ASL is an imperative rather than a functional language.
  Functional languages are often simpler for use during verification
  but functional languages and the coding tricks used to describe
  state changes are not familiar to many programmers so imperative
  languages are an obvious choice.

* ASL supports unbounded integers, infinite precision reals, fixed-size
  bitvectors, booleans, enumerations, records (aka structs) and arrays.
  Virtually all processor state is defined using the bitvectors but most
  instructions start by unpacking the bitvector into an integer, perform
  calculations on the unbounded types and then rounds or truncates the final
  result at the end to pack it back into the bitvectors.

  Using the more mathematical types "integer" and "real" means that
  as you read the specification you don't need to be distracted by
  corner cases due to overflow or wraparound: all rounding, truncation,
  wraparound, etc. is explicit in the conversion back to bitvectors.

* ASL does not have a concise syntax for dereferencing pointers.
  In a processor, there are many different flavours of memory accesses:
  aligned or unaligned, cached or uncached, secure or non-secure, etc.
  and it is critical that every memory access is explicit about what
  type of memory access is being used.  A side effect of this is that
  there in no type representing a pointer to some type: there
  are only bitvectors.

* ASL is strongly typed but uses type inference to give the
  early error-detection of strong typing without the clutter of having
  to annotate every variable declaration.

* The combination of fixed-size bitvectors and strong typing requires
  a slightly unusual type system where the length of the bitvector
  can depend on values calculated earlier in the code.  A simple
  example is the function "Replicate(x,n)" which creates n copies
  of a vector x so if x has type "bits(8)" then "Replicate(x, 4)"
  has type "bits(32)".

  When implementing the type inference system, this requires that bitvector
  lengths are represented as polynomials.

* ASL has support for throwing and catching exceptions.  As you would expect,
  exceptions allow us to focus on the normal (non-exceptional) case
  when specifying instructions that might raise exceptions.
  The one downside is that it is more difficult to think about the tricky
  cases that happen if an exception does occur.

* Finally, ASL is used to write _executable specifications_.  This
  is not necessary when using specifications for verification but for most of the
  other uses, it is critical.
  ASL does have some non-determinism though so executing specifications
  aims to follow _one correct interpretation of the specification_
  while for verification we use _all correct interpretations of
  the spec._

Other people creating formal architecture specifications have made other
choices;

* Anthony Fox, Magnus Myreen and Kathy Gray at Cambridge University has been
  creating formal specifications of ARM, MIPS, Power and CHERI processors for
  many years.  Their original specifications were written in HOL (a pure
  functional language) but as their specifications became more complete (and
  therefore larger), they switched to writing functional specifications in
  a monadic style and then created the imperative languages L3 and SAIL to
  define specifications.  Their specifications are also strongly typed with
  dependent types to reason about the length of bitvectors.

  None of their specification languages use exceptions: trading clutter for
  clarity.

* Shilpi Goel at University of Texas at Austin has been creating a formal
  specification of the x86 instructions set and system behaviour.
  I have not seen this specification but I believe that it is written
  in ACL2 which is a language and theorem prover based on a pure subset
  of LISP.  This choice would not have worked for me because of the impact
  on its use for documentation, by hardware teams and by teams creating
  tests but it is well suited to Shilpi's goal of formally reasoning
  about low level software.

* Those creating specifications just of the instruction set often use a purely
  functional language or equivalent to describe the state transition of each
  instruction.  For example, this is what the CompCERT machine specification
  does.  Compilers only use part of the behaviour of some of the instructions
  and can treat all exceptions as fatal so a purely functional specification
  works well for compilers but I don't think this style would scale well to
  full system specifications such as you would need to reason about operating
  systems without having to resort to encoding tricks such as using monads.

---

This article was inspired by one of the questions asked on [Hacker
News](https://news.ycombinator.com/item?id=12168894) in response to my article
about [Formal Verification of ARM Processors]({{ site.baseurl }}{% post_url
2016-07-26-using-armarm %}).
