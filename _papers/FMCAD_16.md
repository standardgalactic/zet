---
layout: paper
year: 2016
url: https//alastairreid.github.io/papers/fmcad2016-trustworthy.pdf
title: Trustworthy Specifications of ARM v8-A and v8-M System Level Architecture
slides: fmcad2016-trustworthy-slides.pdf
png: fmcad2016-trustworthy.png
pages: 161-168
month: October
location: Mountain View, CA, USA
isbn: 978-0-9835678-6-8
file: fmcad2016-trustworthy.pdf
booktitle: Proceedings of Formal Methods in Computer-Aided Design (FMCAD 2016)
authors: Alastair Reid
ar_shortname: FMCAD 16
ar_file: FMCAD_16
affiliation: ARM Ltd
abstract: |
    
    Processor specifications are of critical importance for verifying programs,
    compilers, operating systems/hypervisors, and, of course, for verifying
    microprocessors themselves.  But to be useful, the scope of these
    specifications must be sufficient for the task, the specification must be
    applicable to processors of interest and the specification must be trustworthy.
    <p>
    This paper describes a 5 year project to change ARM's existing architecture
    specification process so that machine-readable, executable specifications can
    be automatically generated from the same materials used to generate ARM's
    conventional architecture documentation.  We have developed executable
    specifications of both ARM's A-class and M-class processor architectures that
    are complete enough and trustworthy enough that we have used them to formally
    verify ARM processors using bounded model checking.  In particular, our
    specifications include the semantics of the most security sensitive parts of
    the processor: the memory and register protection mechanisms and the exception
    mechanisms that trigger transitions between different modes.  Most importantly,
    we have applied a diverse set of methods including ARM's internal processor
    test suites to improve our trust in the specification using many other
    expressions of the architectural specification such as ARM's simulators,
    testsuites and processors to defend against common-mode failure.  In the
    process, we have also found bugs in all those artifacts: testing specifications
    is very much a two-way street.
    <p>
    While there have been previous specifications of ARM processors, their scope
    has excluded the system architecture, their applicability has excluded newer
    processors and M-class, and their trustworthiness has not been established as
    thoroughly.
    <p>
    Our focus has been on enabling the formal verification of ARM processors but,
    recognising the value of this specification for verifying software, we are
    currently preparing a public release of the machine-readable specification.
ENTRYTYPE: inproceedings
ID: conf/fmcad/Reid16
bibtex: |
    @inproceedings{conf/fmcad/Reid16
        , abstract = {
    Processor specifications are of critical importance for verifying programs,
    compilers, operating systems/hypervisors, and, of course, for verifying
    microprocessors themselves.  But to be useful, the scope of these
    specifications must be sufficient for the task, the specification must be
    applicable to processors of interest and the specification must be trustworthy.
    <p>
    This paper describes a 5 year project to change ARM's existing architecture
    specification process so that machine-readable, executable specifications can
    be automatically generated from the same materials used to generate ARM's
    conventional architecture documentation.  We have developed executable
    specifications of both ARM's A-class and M-class processor architectures that
    are complete enough and trustworthy enough that we have used them to formally
    verify ARM processors using bounded model checking.  In particular, our
    specifications include the semantics of the most security sensitive parts of
    the processor: the memory and register protection mechanisms and the exception
    mechanisms that trigger transitions between different modes.  Most importantly,
    we have applied a diverse set of methods including ARM's internal processor
    test suites to improve our trust in the specification using many other
    expressions of the architectural specification such as ARM's simulators,
    testsuites and processors to defend against common-mode failure.  In the
    process, we have also found bugs in all those artifacts: testing specifications
    is very much a two-way street.
    <p>
    While there have been previous specifications of ARM processors, their scope
    has excluded the system architecture, their applicability has excluded newer
    processors and M-class, and their trustworthiness has not been established as
    thoroughly.
    <p>
    Our focus has been on enabling the formal verification of ARM processors but,
    recognising the value of this specification for verifying software, we are
    currently preparing a public release of the machine-readable specification.
    }
        , affiliation = {ARM Ltd}
        , ar_file = {FMCAD_16}
        , ar_shortname = {FMCAD 16}
        , authors = {Alastair Reid}
        , booktitle = {Proceedings of Formal Methods in Computer-Aided Design
    (FMCAD 2016)}
        , file = {fmcad2016-trustworthy.pdf}
        , isbn = {978-0-9835678-6-8}
        , location = {Mountain View, CA, USA}
        , month = {October}
        , pages = {161-168}
        , png = {fmcad2016-trustworthy.png}
        , slides = {fmcad2016-trustworthy-slides.pdf}
        , title = {{T}rustworthy {S}pecifications of {A}RM v8-{A} and v8-{M}
    System {L}evel {A}rchitecture}
        , url = {https://alastairreid.github.io/papers/fmcad2016-trustworthy.pdf}
        , year = {2016}
    }
---
