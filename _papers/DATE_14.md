---
layout: paper
year: 2014
title: Advanced SIMD - Extending the reach of contemporary SIMD architectures
publisher: European Design and Automation Association
png: date2014_adv_simd.png
pages: 1-4
month: March
location: Dresden, Germany
file: date2014_adv_simd.pdf
editor: Gerhard Fettweis, Wolfgang Nebel
doi: 10.7873/DATE.2014.037
day: 24-28
booktitle: Design, Automation & Test in Europe Conference & Exhibition (DATE 2014)
author: Matthias Boettcher, Bashir M. Al-Hashimi, Mbou Eyole, Giacomo Gabrielli, Alastair Reid
ar_shortname: DATE 14
ar_file: DATE_14
affiliation: ARM Ltd and University of Southampton
acceptance: 22
abstract: |
    
    SIMD extensions have gained widespread acceptance in modern
    microprocessors as a way to exploit data-level parallelism in
    general-purpose cores. Popular SIMD architectures (e.g., Intel
    SSE/AVX) have evolved by adding support for wider registers and
    datapaths, and advanced features like indexed memory
    accesses, per-lane predication and inter-lane instructions, at
    the cost of additional silicon area and design complexity.
    <p>
    This paper evaluates the performance impact of such advanced
    features on a set of workloads considered hard to vectorize for
    traditional SIMD architectures. Their sensitivity to the most
    relevant design parameters (e.g. register/datapath width and L1
    data cache configuration) is quantified and discussed.
    <p>
    We developed an ARMv7 NEON based ISA extension (ARGON),
    augmented a cycle accurate simulation framework for it, and
    derived a set of benchmarks from the Berkeley dwarfs. Our
    analyses demonstrate how ARGON can, depending on the structure
    of an algorithm, achieve speedups of 1.5x to 16x.
ENTRYTYPE: inproceedings
ID: DBLPconf/date/BoettcherAEGR14
bibtex: |
    @inproceedings{DBLP:conf/date/BoettcherAEGR14
        , abstract = {
    SIMD extensions have gained widespread acceptance in modern
    microprocessors as a way to exploit data-level parallelism in
    general-purpose cores. Popular SIMD architectures (e.g., Intel
    SSE/AVX) have evolved by adding support for wider registers and
    datapaths, and advanced features like indexed memory
    accesses, per-lane predication and inter-lane instructions, at
    the cost of additional silicon area and design complexity.
    <p>
    This paper evaluates the performance impact of such advanced
    features on a set of workloads considered hard to vectorize for
    traditional SIMD architectures. Their sensitivity to the most
    relevant design parameters (e.g. register/datapath width and L1
    data cache configuration) is quantified and discussed.
    <p>
    We developed an ARMv7 NEON based ISA extension (ARGON),
    augmented a cycle accurate simulation framework for it, and
    derived a set of benchmarks from the Berkeley dwarfs. Our
    analyses demonstrate how ARGON can, depending on the structure
    of an algorithm, achieve speedups of 1.5x to 16x.
    }
        , acceptance = {22}
        , affiliation = {ARM Ltd and University of Southampton}
        , ar_file = {DATE_14}
        , ar_shortname = {DATE 14}
        , author = {Matthias Boettcher and
    Bashir M. Al-Hashimi and
    Mbou Eyole and
    Giacomo Gabrielli and
    Alastair Reid}
        , booktitle = {Design, Automation \& Test in Europe Conference \& Exhibition
    (DATE 2014)}
        , day = {24-28}
        , doi = {10.7873/DATE.2014.037}
        , editor = {Gerhard Fettweis and
    Wolfgang Nebel}
        , file = {date2014_adv_simd.pdf}
        , location = {Dresden, Germany}
        , month = {March}
        , pages = {1-4}
        , png = {date2014_adv_simd.png}
        , publisher = {European Design and Automation Association}
        , title = {{A}dvanced {S}IM{D}: {E}xtending the reach of contemporary {S}IM{D} architectures}
        , year = {2014}
    }
---
