---
layout: paper
year: 1999
title: Prototyping Real-Time Vision Systems An Experiment in DSL Design
publisher: ACM
pages: 484--493
month: May
location: Los Angeles, CA, USA
file: fvision-icse99-2.pdf
editor: Barry W. Boehm, David Garlan, Jeff Kramer
doi: 10.1109/icse.1999.841038
day: 16-22
booktitle: Proceedings of the 1999 International Conference on Software Engineering (ICSE '99)
author: Alastair Reid, John Peterson, Gregory D. Hager, Paul Hudak
ar_shortname: ICSE 99
ar_file: ICSE_99
affiliation: Yale University
acceptance: 19
abstract: |
    
    We describe the transformation of XVision, a large library of
    C++ code for real-time vision processing, into FVision (pronounced
    ``fission''), a fully-featured domain-specific language embedded
    in Haskell. The resulting prototype system substantiates the claims
    of increased modularity, effective code reuse, and rapid prototyping
    that characterize the DSL approach to system design. It also
    illustrates the need for judicious interface design: relegating
    computationally expensive tasks to XVision (pre-existing C++
    components), and leaving modular compositional tasks to
    FVision (Haskell). At the same time, our experience demonstrates how
    Haskell's advanced language features (specifically parametric
    polymorphism, lazy evaluation, higher order functions and
    automatic storage reclamation) permit a rapid DSL design that
    is itself highly modular and easily modified. Overall, the resulting
    hybrid system exceeded our expectations: visual tracking programs
    continue to spend most of their time executing low level
    image-processing code, while Haskell's advanced features allow us to
    quickly develop and test small prototype systems within a matter of
    a few days and to develop realistic applications within a few weeks.
ENTRYTYPE: inproceedings
ID: DBLPconf/icse/ReidPHH99
bibtex: |
    @inproceedings{DBLP:conf/icse/ReidPHH99
        , abstract = {
    We describe the transformation of XVision, a large library of
    C++ code for real-time vision processing, into FVision (pronounced
    \textasciigrave \textasciigrave fission\textquotesingle \textquotesingle ), a fully-featured domain-specific language embedded
    in Haskell. The resulting prototype system substantiates the claims
    of increased modularity, effective code reuse, and rapid prototyping
    that characterize the DSL approach to system design. It also
    illustrates the need for judicious interface design: relegating
    computationally expensive tasks to XVision (pre-existing C++
    components), and leaving modular compositional tasks to
    FVision (Haskell). At the same time, our experience demonstrates how
    Haskell\textquotesingle s advanced language features (specifically parametric
    polymorphism, lazy evaluation, higher order functions and
    automatic storage reclamation) permit a rapid DSL design that
    is itself highly modular and easily modified. Overall, the resulting
    hybrid system exceeded our expectations: visual tracking programs
    continue to spend most of their time executing low level
    image-processing code, while Haskell\textquotesingle s advanced features allow us to
    quickly develop and test small prototype systems within a matter of
    a few days and to develop realistic applications within a few weeks.
    }
        , acceptance = {19}
        , affiliation = {Yale University}
        , ar_file = {ICSE_99}
        , ar_shortname = {ICSE 99}
        , author = {Alastair Reid and
    John Peterson and
    Gregory D. Hager and
    Paul Hudak}
        , booktitle = {Proceedings of the 1999 International Conference on Software Engineering
    (ICSE \textquotesingle 99)}
        , day = {16-22}
        , doi = {10.1109/icse.1999.841038}
        , editor = {Barry W. Boehm and
    David Garlan and
    Jeff Kramer}
        , file = {fvision-icse99-2.pdf}
        , location = {Los Angeles, CA, USA}
        , month = {May}
        , pages = {484--493}
        , publisher = {ACM}
        , title = {{P}rototyping {R}eal-{T}ime {V}ision {S}ystems: {A}n {E}xperiment in {D}SL {D}esign}
        , year = {1999}
    }
---
