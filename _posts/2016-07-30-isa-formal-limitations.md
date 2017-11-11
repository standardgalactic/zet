---
layout: post
title: Limitations of ISA-Formal
---

As I was explaining the [ISA-Formal technique for verifying ARM processors]({{
site.url }}/papers/CAV_16/) to people, I realized that it was
important to be clear about what ISA-Formal does not verify and why.

(I need to emphasize that this does not imply gaps in the overall verification
story: other parts of the ARM verification teams verify  the other parts of the
processors.  I just want to be clear about which parts are verified using the
ISA-Formal method.)


* Floating point

   In the paper, we have this table of where we found bugs in processors
   so you might think that we are checking the floating point unit.

    | Defect Area     || Fraction     |
    | --------------- || -----------: |
    | FP/SIMD         ||          25% |
    | Memory          ||          21% |
    | Branch          ||          21% |
    | Integer         ||          18% |
    | Exception       ||           8% |
    | System          ||           7% |
    | --------------- || ------------ |

    But if you read the section on checking complex functional units, you
    will see that all
    we are doing is checking that the floating point unit is correctly
    connected to the pipeline, that FP forwarding logic works correctly,
    that FP dependencies are detected correctly, etc.
    Apart from a small subset of FP values, we don't use ISA-Formal to check that
    the FPU does the right thing.

    The reason we don't check this with ISA-Formal is that ISA-Formal is
    primarily about checking the interactions between instructions
    while checking the FPU is primarily about checking an individual
    instruction.
    More importantly, there are better ways of verifying FPUs.


* Instruction Fetch

    ISA-Formal works by using a model checker to feed sequences of instructions
    into the instruction decoder.  Which means that ISA-Formal explicitly
    excludes instruction fetch from consideration.

* Exceptions

    When a processor takes an exception, it modifies a large number of
    registers: PC, SP, the current mode and privilege level, exception
    syndrome registers, fault address registers, etc.  (On M-class, it
    even pushes values onto the stack.)
    And those changes depend on quite a lot of processor state.

    So checking every single aspect of exception handling requires
    significant extension of the "pipeline followers" which extract
    the architectural pre-state and post-state of an instruction.

    At the time we wrote the paper, we were only
    just scratching the surface of checking exception behaviour
    with ISA-Formal: checking that we pushed the correct return
    address or that we returned from exceptions correctly.

* Instruction Ordering

    One of the most subtle limitations is that ISA-Formal does not check that
    all instructions retire in order or even that all the instructions that
    should retire (non-speculative, not-cancelled, etc) do retire and only
    retire once.  All it checks is that, if an instruction does retire, then it
    has the correct effect.

    You can also specify the necessary properties to check that instructions
    are not reordered, lost or duplicated to some processors so
    this is not a fundamental limitation but it doesn't just fall out
    of the rest of the ISA-Formal flow.

* Memory Accesses

    To improve performance of the pipeline checker, we treat the memory system
    as a black box into which we feed addresses and which gives
    back memory faults or data values.
    And we use memory interface specifications to ensure that this black
    box has the full range of legal behaviours that the actual memory
    system can exhibit.

    We omit the memory system because it is very large and stateful
    (making it a challenge for model checkers) and because the concurrency
    between the processor on one side and the bus/cache on the other side
    is better checked using other techniques.

All verification techniques have limitations in what they can check.
The important thing is understanding those limitations so that you
can find some other technique to fill the gaps.

---

_This is one of several notes I am writing about the key ideas in our
paper ["End-to-End Verification of ARM Processors with ISA-Formal"]({{ site.url
}}/papers/CAV_16/) which I presented at the [2016
International Conference on Computer Aided
Verification](http://i-cav.org/2016/) on Friday 22nd July, 2016.  There is nothing
quite like trying to squeeze a 16 page paper into a 16 minute presentation for
figuring out what the important messages are and how to present them._

