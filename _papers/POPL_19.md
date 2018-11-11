---
layout: paper
year: 2019
volume: 3
title: ISA Semantics for ARMv8-A, RISC-V, and CHERI-MIPS
publisher: ACM
pages: 711--7131
numpages: 31
number: POPL
month: January
location: Cascais/Lisbon, Portugal
journal: PACMPL
file: popl19-isasemantics.pdf
doi: 10.1145/3290384
day: 13-19
booktitle: Proc. 46th ACM SIGPLAN Symposium on Principles of Programming Languages
author:  Alasdair Armstrong, Thomas Bauereiss, Brian Campbell, Alastair Reid, Kathryn E. Gray, Robert M. Norton, Prashanth Mundkur, Mark Wassell, Jon French, Christopher Pulte, Shaked Flur, Ian Stark, Neel Krishnaswami, Peter Sewell
ar_shortname: POPL 19
ar_file: POPL_19
address: New York, NY, USA
abstract: |
    Architecture specifications notionally define the fundamental
    interface between hardware and software: the envelope of
    allowed behaviour for processor implementations, and the basic
    assumptions for software development and verification.  But in
    practice, they are typically prose and pseudocode documents,
    not rigorous or executable artifacts, leaving software and
    verification on shaky ground.
    <p>
    In this paper, we present rigorous semantic models for the sequential behaviour
    of large parts of the mainstream ARMv8-A, RISC-V, and MIPS architectures, and
    the research CHERI-MIPS architecture, that are complete enough to boot
    operating systems, variously Linux, FreeBSD, or seL4.  Our ARMv8-A models are
    automatically translated from authoritative ARM-internal definitions, and (in
    one variant) tested against the ARM Architecture Validation Suite.
    <p>
    We do this using a custom language for ISA semantics, Sail, with a lightweight
    dependent type system, that supports automatic generation of emulator code in
    C and OCaml, and automatic generation of proof-assistant definitions for
    Isabelle, HOL4, and (currently only for MIPS) Coq.  We use the former for
    validation, and to assess specification coverage.  To demonstrate the usability
    of the latter, we prove (in Isabelle) correctness of a purely functional
    characterisation of ARMv8-A address translation.  We moreover integrate the
    RISC-V model into the RMEM tool for (user-mode) relaxed-memory concurrency
    exploration.  We prove (on paper) the soundness of the core Sail type system.
    <p>
    We thereby take a big step towards making the architectural abstraction
    actually well-defined, establishing foundations for verification and reasoning.
ENTRYTYPE: inproceedings
ID: conf/popl19/armstrong
bibtex: |
    @inproceedings{conf/popl19/armstrong
        , abstract = {Architecture specifications notionally define the fundamental
    interface between hardware and software: the envelope of
    allowed behaviour for processor implementations, and the basic
    assumptions for software development and verification.  But in
    practice, they are typically prose and pseudocode documents,
    not rigorous or executable artifacts, leaving software and
    verification on shaky ground.
    <p>
    In this paper, we present rigorous semantic models for the sequential behaviour
    of large parts of the mainstream ARMv8-A, RISC-V, and MIPS architectures, and
    the research CHERI-MIPS architecture, that are complete enough to boot
    operating systems, variously Linux, FreeBSD, or seL4.  Our ARMv8-A models are
    automatically translated from authoritative ARM-internal definitions, and (in
    one variant) tested against the ARM Architecture Validation Suite.
    <p>
    We do this using a custom language for ISA semantics, Sail, with a lightweight
    dependent type system, that supports automatic generation of emulator code in
    C and OCaml, and automatic generation of proof-assistant definitions for
    Isabelle, HOL4, and (currently only for MIPS) Coq.  We use the former for
    validation, and to assess specification coverage.  To demonstrate the usability
    of the latter, we prove (in Isabelle) correctness of a purely functional
    characterisation of ARMv8-A address translation.  We moreover integrate the
    RISC-V model into the RMEM tool for (user-mode) relaxed-memory concurrency
    exploration.  We prove (on paper) the soundness of the core Sail type system.
    <p>
    We thereby take a big step towards making the architectural abstraction
    actually well-defined, establishing foundations for verification and reasoning.
    }
        , address = {New York, NY, USA}
        , ar_file = {POPL_19}
        , ar_shortname = {POPL 19}
        , author = {
    Alasdair Armstrong and
    Thomas Bauereiss and
    Brian Campbell and
    Alastair Reid and
    Kathryn E. Gray and
    Robert M. Norton and
    Prashanth Mundkur and
    Mark Wassell and
    Jon French and
    Christopher Pulte and
    Shaked Flur and
    Ian Stark and
    Neel Krishnaswami and
    Peter Sewell
    }
        , booktitle = {Proc. 46th ACM SIGPLAN Symposium on Principles of Programming Languages}
        , day = {13-19}
        , doi = {10.1145/3290384}
        , file = {popl19-isasemantics.pdf}
        , journal = {PACMPL}
        , location = {Cascais/Lisbon, Portugal}
        , month = {January}
        , number = {POPL}
        , numpages = {31}
        , pages = {71:1--71:31}
        , publisher = {ACM}
        , title = {I{S}A {S}emantics for {A}RMv8-{A}, {R}IS{C}-V, and {C}HE{R}I-{M}IP{S}}
        , volume = {3}
        , year = {2019}
    }
---
