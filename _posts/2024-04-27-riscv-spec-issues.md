---
layout: post
title: How to improve the RISC-V specification
---

![RISC-V logo]({{site.baseurl}}/images/riscv-logo.png){: style="float: left; width: 13%; padding: 1%"}
My main project is to create an executable spec of the Intel Architecture
but, every now and then, I get to take a broader look at ISA specifications
and think about the strengths and weaknesses of other ISA specs:
what makes them work well; and what techniques they could borrow
from other specifications.
Earlier this month, someone asked me for my thoughts on the RISC-V
specification and I thought that it would be useful to share
what I found out.

This post is about the RISC-V specification.
This specification effectively consists of several different parts
each an essential part of defining the RISC-V architecture.
The most obvious part of the specification are
[RISC-V Instruction Set Manual, volume 1]
and [RISC-V Instruction Set Manual, volume 2]: PDF documents that
describe the unprivileged and privileged parts of the architecture.
If you are developing a RISC-V processor, you will probably make heavy
use of the [RISC-V Test Suites] to check that your processor correctly
implements the architecture.
And you will probably be using the [Spike RISC-V ISA Simulator] as a "golden
reference model" to compare the behavior of your processor against.
And, finally, you might be using the [SAIL RISC-V model] as a formal
specification of the architecture. (Although, I think this has mostly
used to reason about software, rather than hardware.)

## What's wrong with this picture?

Overall, the specification is not in a very healthy state.

The two PDF documents rely heavily on natural language
text in the specification with the result that the description is
not always very precise and it is impossible to test the descriptions
to determine whether they match the other artifacts.

A common complaint about the test suites is that the RISC-V
architecture is very highly configurable with many subsets and
implementation choices allowed but the test suites is not
easily configured to check the full envelope of allowed behaviors.
Some of these issues stems from the challenge of creating a machine-readable
description of which particular configuration you intended to build.
(This also limits the ability to use Spike as a golden reference model.)
If you intend to build something outside the range of configurations
that Spike and the test suite support, you will end up with a large
number of "waivers" documenting the places where your processor is
expected to fail the tests.

Finally, there is the SAIL model written in the
[SAIL ISA specification language].
This is a precise, executable, formal specification of the architecture
but it is not used as much as it should be.
Ideally, parts of the SAIL specification would be included in the
official PDF documents so that the SAIL code can add the precision
that the natural language spec lacks and the natural language
specification can make up for the almost total absence of comments
in the SAIL specification.

A complaint that I often hear about the SAIL specification is
that it is a bit inaccessible for normal users. The SAIL language
design builds on a number of popular academic languages
and programming language research ideas
such as the [OCaml Functional Programming Language],
[Liquid types], [Monads], and [Effect Systems].
The challenge with drawing on these different sources
is that the primary audience for the specification is
not programming language researchers but people who
work on hardware design, hardware validation, OS developers,
compiler developers, etc. --- many of whom are not familiar with
the academic programming language literature and are confused and
put off by the syntax of SAIL.
To illustrate this, consider the following SAIL example
from early in the SAIL reference manual:

```
val my_replicate_bits : forall 'n 'm, 'm >= 1 & 'n >= 1.  (int('n), bits('m)) -> bits('n * 'm)
```

If you are not familiar with OCaml and liquid types, some questions that
you might ask are "What are the quote marks for in `'m` and `'n`?" and
"What does `forall 'n 'm` mean?"


## Connecting the pieces: machine-readable formats

The most important problem is that these four artifacts seem to be completely disconnected from
each other. They are maintained as four separate codebases in four separate repositories
and no part of one artifact is generated from part of any other artifact.
If you are writing an architecture extension, you have to write the same thing four times in four
separate formats and then you have to use testing and review to check that all four copies
are the same.

But worse than this, there is a whole ecosystem around RISC-V who will also be writing
code in response to your architecture extension. There are hardware designers,
hardware validation teams,
developers of software tools (such as assemblers, compilers and JITs), OS hackers and
debugger developers, etc. that are all going to have to write some code to support
or benefit from any architecture extension. They also have to write all this code by
hand and then review and test the code to make it consistent with the official spec.

It is worth noting that most architecture extensions evolve between the first design and the final,
ratified design: evaluating that design requires tool support; socializing and reviewing the
design requires documentation. So each extension is typically implemented many times
and each revision requires updates in many places.

The easiest way to improve this would be to capture as much of the architecture
as possible in formats that are easy to read and manipulate.
In particular, instruction encodings and control/status registers are
easily described by simple JSON/YAML/XML/... formats.
It doesn't take long to figure out what data you need to include to
support generation of many different artifacts from such files:

- The name and a short description (for generating documentaton).
- The size, bitfields, fixed bits, etc.
- For registers, there will be a numeric id that is used to identify
  the register.
- What constraints are there on using the instruction or register?
  Is it usable in hypervisor mode? supervisor mode? usermode?
- For register fields, is the field readable? is it writable?
  what is its reset value? what is the meaning of different values
  that this field can have?
* For instructions, what is the assembly syntax? (See [Bidirectional ARM Assembly Syntax Specifications])
- Which configurations support each entry, field or value?

I've probably missed a few important pieces of information but you get the idea.

Of course, creating this easy-to-use, highly-reusable machine readable spec
is just the first part.
To make a difference, you have to modify the architecture reference manual,
the Spike simulator, the testsuite and the SAIL specification to use this data.
You have to find every part of these artifacts that currently contains
information about instructions or CSRs and refactor them around
code that is automatically generated from the json/yaml/xml file.
Doing this is critical to making it equally possible to auto-generate
code for any new architecture extensions.

And, as that is being done, people should be looking at the extended
ecosystem of build tools, libraries, OSes, etc. to autogenerate
as much of them as possible from the machine readable data files.

## Making SAIL usable in documentation

I have already touched on the problems for readers from a broad
range of backgrounds reading SAIL specifications.
There are a range of improvements that can be made here from
changing the syntax to applying sensible defaults to reduce
the amount of clutter from the type system.
(Ideally, this would be done by adopting some of the syntax
of the [ASL-1.0] ISA specification language which has many
of the same features but was designed with more focus on
use in documentation.)

But there is another issue that is both more fundamental and also easier to solve:
the SAIL specification
is currently a large, monolithic specification.
There is no easy way to extract an individual instruction specification
or function definition to include in a particular place in the
documentation.
The easiest option to include the SAIL spec into the current spec would be
to include the entire spec as a giant appendix at the back of the architecture manual.
But it is much better to put each part of the SAIL spec on the same page
as the natural language description of the same feature so that
the SAIL spec can amplify your understanding of the natural language spec and
the natural language spec can help you understand the SAIL spec.

Fortunately, the fix is easy:
either split the SAIL spec into smaller pieces (e.g., one definition per file)
or write a tool to do it for you.
This makes it easy to include the relevant part of the SAIL spec into
the the documentation.

*[Note that there has been  some work in the  direction of using the SAIL specs
in documentation such as the [SAIL-to-ASCIIdoc] tool.]*


## Using SAIL in tools

Why do we have two executable parts to the specification:
the SAIL specification and the Spike golden reference simulator?
The historical reasons for this are clear but it would be
good if Spike support for future extensions was generated
from their SAIL specification.

This will take a bit of work to do.  Mostly, this will consist of defining the
interface that code generated from the SAIL specs uses to access parts of the
state that are represented in Spike.


## Conclusion

The RISC-V architecture was developed in classic startup/academic style:
innovating quickly and avoiding too much investment in long-term engineering.
This has resulted in the current situation where the architecture specification
is, in effect, scattered over four different artifacts and each
downstream tool/library/application has to transcribe information from
those sources instead of being able to use architect-provided machine-readable
formats to generate the code instead.

This was not too big a problem for the original base architecture of just
47 instructions and 32 registers but there have been many [RISC-V ISA extensions]
added since then.


### Related posts and papers

* [Goals of a modern ISA specification]({{site.baseurl}}/talks/goals-of-modern-ISA-spec-PLARCH-2023-06-17.pdf)
  (presented at [PLARCH 2023]({{site.baseurl}}{% post_url 2023-07-01-plarch-2023 %}))
* [What can you do with an ISA specification?]({{site.baseurl}}{% post_url 2021-11-24-uses-for-isa-specs %})
* [Machine readable specifications at scale]({{site.baseurl}}{% post_url 2022-01-25-mrs-at-scale %})
* [Bidirectional ARM Assembly Syntax Specifications]({{site.baseurl}}{% post_url 2017-12-24-bidirectional-assemblers %})


[RISC-V Instruction Set Manual, volume 1]: https://github.com/riscv/riscv-isa-manual/releases/download/Ratified-IMAFDQC/riscv-spec-20191213.pdf
[RISC-V Instruction Set Manual, volume 2]: https://github.com/riscv/riscv-isa-manual/releases/download/Priv-v1.12/riscv-privileged-20211203.pdf
[RISC-V Test Suites]:                      https://github.com/riscv-non-isa/riscv-arch-test/blob/main/riscv-test-suite/README.md
[Spike RISC-V ISA Simulator]:              https://github.com/riscv-software-src/riscv-isa-sim
[SAIL RISC-V model]:                       https://github.com/riscv/sail-riscv
[RISC-V ISA extensions]:                   https://en.wikipedia.org/wiki/RISC-V#ISA_base_and_extensions

[SAIL-to-ASCIIdoc]:                        https://github.com/Alasdair/asciidoctor-sail/blob/master/doc/built/sail_to_asciidoc.pdf
[SAIL ISA specification language]:         https://github.com/rems-project/sail?tab=readme-ov-file
[SAIL Language Reference Manual]:          https://alasdair.github.io/manual.html

[ASL-1.0]:                                 https://developer.arm.com/ASL1
[Bidirectional ARM Assembly Syntax Specifications]: ({{site.baseurl}}{% post_url 2017-12-24-bidirectional-assemblers %})

[OCaml Functional Programming Language]:   https://ocaml.org/
[Liquid Types]:                            https://goto.ucsd.edu/~ucsdpl-blog/liquidtypes/2015/09/19/liquid-types/
[Monads]:                                  https://en.wikipedia.org/wiki/Monad_(functional_programming)
[Effect Systems]:                          https://en.wikipedia.org/wiki/Effect_system

[Pydrofoil]: https://www.pypy.org/posts/2023/05/rpython-used-to-speed-up-risc-v-simulation-over-15x.html
[lockhart:ispass:2015]: {{site.baseurl}}/RelatedWork/papers/lockhart:ispass:2015
[PyPy]: https://www.pypy.org/
