---
layout: post
title: Specification Terminology
---

I have spent the last 5 years working on ARM's processor specifications:
making them executable, testable, mechanizing them, formalizing them,
making them trustworthy, etc.

But what exactly do those words mean?  If you read papers about
specifications, you find that there are lots of adjectives
attached to specifications and it can be a bit hard to pin down
the exact meanings.
So this post is my attempt to figure out exactly what they all mean.

* **Applicability**
    refers to whether a specification applies to a given processor.
    Obviously, one would not apply an ARM specification to an x86
    processor or vice versa.  But you should also be wary of using
    an ARM v7-A specification with an ARM v8-A processor or
    using an ARM v7-A specification with an ARM v7-M processor.

    Beware of the interaction between trustworthiness and applicability:
    testing a specification against ARM v8-M processors would not guarantee
    that they are trustworthy against ARM v7-M processors.

* **Concurrency Semantics**
    is a semantics of how programs running on different
    processors interact.  In particular, it refers to the
    guarantees the programmer can expect when concurrent programs
    communicate through shared memory.

* **ISA** (short for Instruction Set Architecture)
    refers to the instruction set part of a processor specification.
    An ISA specification is sufficient to reason about the output
    of a compiler or other user-level code.

    Some authors seem to use "ISA" to mean a "System Level Specification"
    but it is useful to distinguish because most "ISA" specifications
    contain only a subset of the instructions and no
    system level behaviour at all.

* **Executable**
    refers to whether the specification can be executed.
    If the specification is non-deterministic, this execution
    will usually have to implement one legal interpretion
    of the specification instead of describing all legal
    interpretations.
    See "Test Oracle".

* **Formal**
    refers to whether the specification can be used for formal
    verification.
    Note that this does not necessarily mean that it is "mechanized":
    one can do pencil and paper verification with a formal spec.

* **Mechanized**
    refers to whether the specification can be parsed, typechecked,
    and used for computer aided formal verification either directly
    or by mechanically translating it to another language and
    then performing computer aided formal verification.

    "Mechanized" implies "Formal" but not vice versa.

* **Memory Transistency Model**
    refers to the behaviour of concurrent accesses to virtual memory
    and captures the impact of aliasing caused by the virtual to physical
    address mapping.

    This is a generalization of "Concurrency Semantics".

* **Scope**
    refers to what is included in the specification.
    To verify a compiler, you might only need 40-60 instructions;
    to disassemble arbitrary user-mode binaries, you need
    the entire instruction set (a full ISA spec); to reason
    about operating systems, microkernels, etc., you need
    most/all of the System Level Architecture spec; and
    to reason about multiprocessor programs, you need
    a concurrency semantics as well.

* **System Level Architecture**
    is the part of the architecture that implements the
    operating system, virtualization, security and debug support.
    A System Level Architecture is required to reason
    about OS kernels, microkernels, page faults, interrupts, etc.
    A System Level Architecture specification includes
    an "ISA" specification.

* **Test Oracle**
    refers to whether the specification can be used to (mechanically)
    determine whether the behaviour of an alleged implementation of
    the specification is correct.
    That is, it tests the observable behaviour of a program.

    Test Oracles are useful when the specification is non-deterministic
    or when the specification allows implementation defined behaviour.
    See "Executable".

* **Trustworthy**
    refers to whether the specification matches the processors
    it claims to specify.  Specifications are usually made trustworthy
    by manually comparing them against manufacturer's specifications,
    by testing against simulators and one or more different
    processors.  They can also be made trustworthy by using them
    to verify a processor.

    Beware of the interaction between trustworthiness and applicability:
    testing a specification against ARM v8-M processors would not guarantee
    that they are trustworthy against ARM v7-M processors.

