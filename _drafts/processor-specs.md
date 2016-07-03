---
layout: post
title: Processor Specifications
---

Processor specifications take a lot of work to create, test and maintain so
I thought it would be useful to make a list of all the formal specifications
that I know about so that people can pool resources or use existing good
specifications.

| Specification || Architecture || Language  || ISA || System |
| ------------- || ------------ || --------- || --- || ------ |
| [ARM-HOL]     || ARMv7        || HOL       || yes || no     |


ARM Specifications
------------------

The main source of ARM specifications is Cambridge University which, as they
tackled larger and larger parts of the ARM architecture, has developed
3 specification languages capable of concisely describing the architecture.

* Most projects use Cambridge University's HOL model of the ARM ISA.  They have
  an ARMv7-A and an integer-only, AArch64 specification in the [ARM-HOL].
  Their ARMv7-A spec has been tested using a mix of directed and random testing
  against real hardware so it is pretty reliable.
  This specification is being used by [SeL4], [CakeML], [CodeSonar], [D-RisQ].

* More recent projects use Cambridge University's [L3] model of the ARM ISA.
  Instead of writing the specification directly in HOL, this is written
  in a language [L3] specifically designed for writing ISA specifications
  which makes it more concise and allows it to be used with tools other than
  HOL.

* Cambridge University's most recent specification is written in 

x86 Specifications
------------------



[CakeML]:    https://cakeml.org
[CodeSonar]: http://www.grammatech.com/products/codesonar/
[CompCERT]:  http://compcert.inria.fr
[D-RisQ]:    http://www.drisq.com
[ARM-HOL]: https://github.com/HOL-Theorem-Prover/HOL/tree/master/examples/ARM/v7
[L3]:        http://www.cl.cam.ac.uk/~acjf3/l3/
[PROSPER]:   http://prosper.sics.se
[SAIL]:      http://www.cl.cam.ac.uk/~pes20/sail/
[SeL4]:      https://sel4.systems
