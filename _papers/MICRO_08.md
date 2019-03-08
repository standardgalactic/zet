---
layout: paper
year: 2008
title: From SODA to scotch - The evolution of a wireless baseband processor
publisher: IEEE Computer Society
pages: 152--163
month: November
location: Lake Como, Italy
file: mwoh-micro08.pdf
doi: 10.1109/MICRO.2008.4771787
day: 8-12
booktitle: 41st Annual IEEE/ACM International Symposium on Microarchitecture (MICRO-41 2008)
author: Mark Woh, Yuan Lin, Sangwon Seo, Scott A. Mahlke, Trevor N. Mudge, Chaitali Chakrabarti, Richard Bruce, Danny Kershaw, Alastair Reid, Mladen Wilder, Krisztián Flautner
ar_shortname: MICRO 08
ar_file: MICRO_08
affiliation: ARM Ltd and University of Michigan and Arizona State University
acceptance: 19
abstract: |
    
    With the multitude of existing and upcoming wireless standards, it is becoming
    increasingly difficult for hardware-only baseband processing solutions to adapt
    to the rapidly changing wireless communication landscape. Software Defined
    Radio (SDR) promises to deliver a cost effective and flexible solution by
    implementing a wide variety of wireless protocols in software. In previous
    work, a fully programmable multicore architecture, SODA, was proposed that was
    able to meet the real-time requirements of 3G wireless protocols. SODA consists
    of one ARM control processor and four wide single instruction multiple data
    (SIMD) processing elements. Each processing element consists of a scalar and
    a wide 512-bit 32-lane SIMD datapath. A commercial prototype based on the SODA
    architecture, Ardbeg (named after a brand of Scotch Whisky), has been
    developed. In this paper, we present the architectural evolution of going from
    a research design to a commercial prototype, including the goals, trade-offs,
    and final design choices.
    <p>
    Ardbeg's redesign process can be grouped into the following three major areas:
    optimizing the wide SIMD datapath, providing long instruction word (LIW)
    support for SIMD operations, and adding application-specific hardware
    accelerators. Because SODA was originally designed with 180nm technology, the
    wide SIMD datapath is re-optimized in Ardbeg for 90nm technology. This includes
    re-evaluating the most efficient SIMD width, designing a wider SIMD shuffle
    network, and implementing faster SIMD arithmetic units. Ardbeg also provides
    modest LIW support by allowing two SIMD operations to issue in the same cycle.
    This LIW execution supports SDR algorithms' most common parallel SIMD execution
    patterns with minimal hardware overhead. A viable commercial SDR solution must
    be competitive with existing ASIC solutions. Therefore, algorithm-specific
    hardware is added for performance bottleneck algorithms while still maintaining
    enough flexibility to support multiple wireless protocols. The combination of
    these architectural improvements allows Ardbeg to achieve 1.5-7x speedup over
    SODA across multiple wireless algorithms while consuming less power.
ENTRYTYPE: inproceedings
ID: DBLPconf/micro/WohLSMMCBKRWF08
bibtex: |
    @inproceedings{DBLP:conf/micro/WohLSMMCBKRWF08
        , abstract = {
    With the multitude of existing and upcoming wireless standards, it is becoming
    increasingly difficult for hardware-only baseband processing solutions to adapt
    to the rapidly changing wireless communication landscape. Software Defined
    Radio (SDR) promises to deliver a cost effective and flexible solution by
    implementing a wide variety of wireless protocols in software. In previous
    work, a fully programmable multicore architecture, SODA, was proposed that was
    able to meet the real-time requirements of 3G wireless protocols. SODA consists
    of one ARM control processor and four wide single instruction multiple data
    (SIMD) processing elements. Each processing element consists of a scalar and
    a wide 512-bit 32-lane SIMD datapath. A commercial prototype based on the SODA
    architecture, Ardbeg (named after a brand of Scotch Whisky), has been
    developed. In this paper, we present the architectural evolution of going from
    a research design to a commercial prototype, including the goals, trade-offs,
    and final design choices.
    <p>
    Ardbeg\textquotesingle s redesign process can be grouped into the following three major areas:
    optimizing the wide SIMD datapath, providing long instruction word (LIW)
    support for SIMD operations, and adding application-specific hardware
    accelerators. Because SODA was originally designed with 180nm technology, the
    wide SIMD datapath is re-optimized in Ardbeg for 90nm technology. This includes
    re-evaluating the most efficient SIMD width, designing a wider SIMD shuffle
    network, and implementing faster SIMD arithmetic units. Ardbeg also provides
    modest LIW support by allowing two SIMD operations to issue in the same cycle.
    This LIW execution supports SDR algorithms\textquotesingle  most common parallel SIMD execution
    patterns with minimal hardware overhead. A viable commercial SDR solution must
    be competitive with existing ASIC solutions. Therefore, algorithm-specific
    hardware is added for performance bottleneck algorithms while still maintaining
    enough flexibility to support multiple wireless protocols. The combination of
    these architectural improvements allows Ardbeg to achieve 1.5-7x speedup over
    SODA across multiple wireless algorithms while consuming less power.
    }
        , acceptance = {19}
        , affiliation = {ARM Ltd and University of Michigan and Arizona State University}
        , ar_file = {MICRO_08}
        , ar_shortname = {MICRO 08}
        , author = {Mark Woh and
    Yuan Lin and
    Sangwon Seo and
    Scott A. Mahlke and
    Trevor N. Mudge and
    Chaitali Chakrabarti and
    Richard Bruce and
    Danny Kershaw and
    Alastair Reid and
    Mladen Wilder and
    Kriszti{\'a}n Flautner}
        , booktitle = {41st Annual IEEE/ACM International Symposium on Microarchitecture
    (MICRO-41 2008)}
        , day = {8-12}
        , doi = {10.1109/MICRO.2008.4771787}
        , file = {mwoh-micro08.pdf}
        , location = {Lake Como, Italy}
        , month = {November}
        , pages = {152--163}
        , publisher = {IEEE Computer Society}
        , title = {{F}rom {S}OD{A} to scotch: {T}he evolution of a wireless baseband processor}
        , year = {2008}
    }
---
