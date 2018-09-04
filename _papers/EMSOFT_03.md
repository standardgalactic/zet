---
layout: paper
year: 2003
volume: 2855
title: Eliminating Stack Overflow by Abstract Interpretation
series: Lecture Notes in Computer Science
publisher: Springer
pages: 306--322
month: October
location: Philadelphia, PA, USA
file: emsoft03-preprint.pdf
editor: Rajeev Alur, Insup Lee
doi: 10.1007/978-3-540-45212-6_20
day: 13-15
booktitle: Embedded Software, Third International Conference (EMSOFT 2003)
author: John Regehr, Alastair Reid, Kirk Webb
ar_shortname: EMSOFT 03
ar_file: EMSOFT_03
affiliation: University of Utah
abstract: |
    
    An important correctness criterion for software running on
    embedded microcontrollers is stack safety: a guarantee that the
    call stack does not overflow. We address two aspects of the
    problem of creating stack-safe embedded software that also makes
    efficient use of memory: statically bounding worst-case stack
    depth, and automatically reducing stack memory requirements. Our
    first contribution is a method for statically guaranteeing stack
    safety by performing whole-program analysis, using an approach
    based on context-sensitive abstract interpretation of machine
    code. Abstract interpretation permits our analysis to accurately
    model when interrupts are enabled and disabled, which is
    essential for accurately bounding the stack depth of typical
    embedded systems. We have implemented a stack analysis tool that
    targets Atmel AVR microcontrollers, and tested it on embedded
    applications compiled from up to 30,000 lines of C. We
    experimentally validate the accuracy of the tool, which runs in
    a few seconds on the largest programs that we tested. The second
    contribution of this paper is a novel framework for automatically
    reducing stack memory requirements. We show that goal-directed
    global function inlining can be used to reduce the stack memory
    requirements of component-based embedded software, on average, to
    40% of the requirement of a system compiled without inlining, and
    to 68% of the requirement of a system compiled with aggressive
    whole-program inlining that is not directed towards reducing
    stack usage.
ENTRYTYPE: inproceedings
ID: DBLPconf/emsoft/RegehrRW03
bibtex: |
    @inproceedings{DBLP:conf/emsoft/RegehrRW03
        , abstract = {
    An important correctness criterion for software running on
    embedded microcontrollers is stack safety: a guarantee that the
    call stack does not overflow. We address two aspects of the
    problem of creating stack-safe embedded software that also makes
    efficient use of memory: statically bounding worst-case stack
    depth, and automatically reducing stack memory requirements. Our
    first contribution is a method for statically guaranteeing stack
    safety by performing whole-program analysis, using an approach
    based on context-sensitive abstract interpretation of machine
    code. Abstract interpretation permits our analysis to accurately
    model when interrupts are enabled and disabled, which is
    essential for accurately bounding the stack depth of typical
    embedded systems. We have implemented a stack analysis tool that
    targets Atmel AVR microcontrollers, and tested it on embedded
    applications compiled from up to 30,000 lines of C. We
    experimentally validate the accuracy of the tool, which runs in
    a few seconds on the largest programs that we tested. The second
    contribution of this paper is a novel framework for automatically
    reducing stack memory requirements. We show that goal-directed
    global function inlining can be used to reduce the stack memory
    requirements of component-based embedded software, on average, to
    40\% of the requirement of a system compiled without inlining, and
    to 68\% of the requirement of a system compiled with aggressive
    whole-program inlining that is not directed towards reducing
    stack usage.
    }
        , affiliation = {University of Utah}
        , ar_file = {EMSOFT_03}
        , ar_shortname = {EMSOFT 03}
        , author = {John Regehr and
    Alastair Reid and
    Kirk Webb}
        , booktitle = {Embedded Software, Third International Conference (EMSOFT 2003)}
        , day = {13-15}
        , doi = {10.1007/978-3-540-45212-6\_20}
        , editor = {Rajeev Alur and
    Insup Lee}
        , file = {emsoft03-preprint.pdf}
        , location = {Philadelphia, PA, USA}
        , month = {October}
        , pages = {306--322}
        , publisher = {Springer}
        , series = {Lecture Notes in Computer Science}
        , title = {{E}liminating {S}tack {O}verflow by {A}bstract {I}nterpretation}
        , volume = {2855}
        , year = {2003}
    }
---
