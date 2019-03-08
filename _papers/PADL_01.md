---
layout: paper
year: 2001
volume: 1990
title: FVision - A Declarative Language for Visual Tracking
series: Lecture Notes in Computer Science
publisher: Springer
pages: 304--321
month: March
location: Las Vegas, Nevada, USA
file: fvision-padl01-2.pdf
editor: I. V. Ramakrishnan
doi: 10.1007/3-540-45241-9_21
day: 11-12
booktitle: Practical Aspects of Declarative Languages, Third International Symposium (PADL 2001)
author: John Peterson, Paul Hudak, Alastair Reid, Gregory D. Hager
ar_shortname: PADL 01
ar_file: PADL_01
affiliation: Yale University
abstract: |
    
    Functional programming languages are not generally associated
    with computationally intensive tasks such as computer vision. We show
    that a declarative programming language like Haskell is effective for
    describing complex visual tracking systems. We have taken an existing
    C++ library for computer vision, called XVision, and used it to build
    FVision (pronounced ``fission''), a library of Haskell types and
    functions that provides a high-level interface to the lower-level
    XVision code. Using functional abstractions, users of FVision can
    build and test new visual tracking systems rapidly and reliably. The
    use of Haskell does not degrade system performance: computations are
    dominated by low-level calculations expressed in C++ while the
    Haskell ``glue code'' has a negligible impact on performance.
    <p>
    FVision is built using functional reactive programming (FRP) to
    express interaction in a purely functional manner. The resulting
    system demonstrates the viability of mixed-language programming:
    visual tracking programs continue to spend most of their time
    executing low-level image-processing code, while Haskell's advanced
    features allow us to develop and test systems quickly and with
    confidence. In this paper, we demonstrate the use of Haskell and FRP
    to express many basic abstractions of visual tracking.
ENTRYTYPE: inproceedings
ID: DBLPconf/padl/PetersonHRH01
bibtex: |
    @inproceedings{DBLP:conf/padl/PetersonHRH01
        , abstract = {
    Functional programming languages are not generally associated
    with computationally intensive tasks such as computer vision. We show
    that a declarative programming language like Haskell is effective for
    describing complex visual tracking systems. We have taken an existing
    C++ library for computer vision, called XVision, and used it to build
    FVision (pronounced \textasciigrave \textasciigrave fission\textquotesingle \textquotesingle ), a library of Haskell types and
    functions that provides a high-level interface to the lower-level
    XVision code. Using functional abstractions, users of FVision can
    build and test new visual tracking systems rapidly and reliably. The
    use of Haskell does not degrade system performance: computations are
    dominated by low-level calculations expressed in C++ while the
    Haskell \textasciigrave \textasciigrave glue code\textquotesingle \textquotesingle  has a negligible impact on performance.
    <p>
    FVision is built using functional reactive programming (FRP) to
    express interaction in a purely functional manner. The resulting
    system demonstrates the viability of mixed-language programming:
    visual tracking programs continue to spend most of their time
    executing low-level image-processing code, while Haskell\textquotesingle s advanced
    features allow us to develop and test systems quickly and with
    confidence. In this paper, we demonstrate the use of Haskell and FRP
    to express many basic abstractions of visual tracking.
    }
        , affiliation = {Yale University}
        , ar_file = {PADL_01}
        , ar_shortname = {PADL 01}
        , author = {John Peterson and
    Paul Hudak and
    Alastair Reid and
    Gregory D. Hager}
        , booktitle = {Practical Aspects of Declarative Languages, Third International Symposium
    (PADL 2001)}
        , day = {11-12}
        , doi = {10.1007/3-540-45241-9\_21}
        , editor = {I. V. Ramakrishnan}
        , file = {fvision-padl01-2.pdf}
        , location = {Las Vegas, Nevada, USA}
        , month = {March}
        , pages = {304--321}
        , publisher = {Springer}
        , series = {Lecture Notes in Computer Science}
        , title = {F{V}ision: {A} Declarative {L}anguage for {V}isual {T}racking}
        , volume = {1990}
        , year = {2001}
    }
---
