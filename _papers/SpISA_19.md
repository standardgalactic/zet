---
layout: paper
year: 2019
title: The State of Sail
png: spisa2019.png
month: September
location: Portland, Oregon, USA
file: spisa2019.pdf
booktitle: SpISA 2019 Workshop on Instruction Set Architecture Specification
author: Alasdair Armstrong, Thomas Bauereiss, Brian Campbell, Alastair Reid, Kathryn E. Gray, Robert Norton, Prashanth Mundkur, Mark Wassell, Jon French, Christopher Pulte, Shaked Flur, Ian Stark, Neel Krishnaswami, Peter Sewell
ar_shortname: SpISA 19
ar_file: SpISA_19
abstract: |
    
    <p>
    Sail is a custom domain-specific language for ISA semantics, in which we have
    developed formal models for ARMv8-A, RISC-V, and MIPS, as well as CHERI-based
    capability extensions for both RISC-V and MIPS. In particular, our model of
    ARMv8-A is automatically translated from ARM-internal definitions and tested
    against the ARM Architecture validation suite. All the above models contain
    enough system-level features to boot various operating systems, including Linux
    and FreeBSD, but also various smaller microkernels and hypervisors.
    <p>
    In this short paper, we present the ways in which Sail enables us to bridge the
    gap between our various ISA models and the myriad use cases for such models. By
    using Sail, we are able to generate emulators for testing and validation,
    generate theorem prover definitions across multiple major tools (Isabelle,
    HOL4, and Coq), translate Sail to SMT for automatic verification, and integrate
    with both operational models for relaxed-memory concurrency via our RMEM tool.
    <p>
    We will also present our current work to extend Sail to support axiomatic
    concurrency models, in the style of Alglave and Maranget’s herd7 tool, with the
    intent being to explore the behaviour of concurrent litmus tests that span the
    full behaviour of the architecture. As an illustrative example, one could
    consider how instruction cache maintenance instructions interact with
    self-modifying code in an axiomatic setting, or other interesting cases that
    are not well-covered by existing tools
ENTRYTYPE: article
ID: conf/spisa19/armstrong
bibtex: |
    @article{conf/spisa19/armstrong
        , abstract = {
    <p>
    Sail is a custom domain-specific language for ISA semantics, in which we have
    developed formal models for ARMv8-A, RISC-V, and MIPS, as well as CHERI-based
    capability extensions for both RISC-V and MIPS. In particular, our model of
    ARMv8-A is automatically translated from ARM-internal definitions and tested
    against the ARM Architecture validation suite. All the above models contain
    enough system-level features to boot various operating systems, including Linux
    and FreeBSD, but also various smaller microkernels and hypervisors.
    <p>
    In this short paper, we present the ways in which Sail enables us to bridge the
    gap between our various ISA models and the myriad use cases for such models. By
    using Sail, we are able to generate emulators for testing and validation,
    generate theorem prover definitions across multiple major tools (Isabelle,
    HOL4, and Coq), translate Sail to SMT for automatic verification, and integrate
    with both operational models for relaxed-memory concurrency via our RMEM tool.
    <p>
    We will also present our current work to extend Sail to support axiomatic
    concurrency models, in the style of Alglave and Maranget’s herd7 tool, with the
    intent being to explore the behaviour of concurrent litmus tests that span the
    full behaviour of the architecture. As an illustrative example, one could
    consider how instruction cache maintenance instructions interact with
    self-modifying code in an axiomatic setting, or other interesting cases that
    are not well-covered by existing tools
    }
        , ar_file = {SpISA_19}
        , ar_shortname = {SpISA 19}
        , author = {Alasdair Armstrong and
    Thomas Bauereiss and
    Brian Campbell and
    Alastair Reid and
    Kathryn E. Gray and
    Robert Norton and
    Prashanth Mundkur and
    Mark Wassell and
    Jon French and
    Christopher Pulte and
    Shaked Flur and
    Ian Stark and
    Neel Krishnaswami and
    Peter Sewell}
        , booktitle = {SpISA 2019: Workshop on Instruction Set Architecture Specification}
        , file = {spisa2019.pdf}
        , location = {Portland, Oregon, USA}
        , month = {September}
        , png = {spisa2019.png}
        , title = {{T}he {S}tate of {S}ail}
        , year = {2019}
    }
---
