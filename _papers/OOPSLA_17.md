---
layout: paper
year: 2017
volume: 1
title: Who guards the guards? Formal Validation of the ARM v8-M Architecture Specification
slides: oopsla2017-whoguardstheguards-slides.pdf
publisher: ACM
pages: 881--8824
numpages: 24
number: OOPSLA
month: October
location: Vancouver, BC, Canada
journal: PACMPL
file: oopsla2017-whoguardstheguards.pdf
doi: 10.1145/3133912
day: 22– 27
authors: Alastair Reid
ar_shortname: OOPSLA 17
ar_file: OOPSLA_17
affiliation: ARM Ltd
address: New York, NY, USA
abstract: |
    
    Software and hardware are increasingly being formally verified
    against specifications, but how can we verify the
    specifications themselves? This talk explores what it means to
    formally verify a specification. We solve three challenges: (1)
    How to create a secondary, higher-level specification that can
    be effectively reviewed by processor designers who are not
    experts in formal verification; (2) How to avoid common-mode
    failures between the specifications; and (3) How to
    automatically verify the two specifications against each other.
    <p>
    One of the most important specifications for software
    verification is the processor specification since it de nes the
    behaviour of machine code and of hardware protection features
    used by operating systems. We demonstrate our approach on ARM's
    v8-M Processor Specification, which is intended to improve the
    security of Internet of Things devices. Thus, we focus on
    establishing the security guarantees the architecture is
    intended to provide. Despite the fact that the ARM v8-M
    specification had previously been extensively tested, we found
    twelve bugs (including two security bugs) that have all been
    fixed by ARM.
ENTRYTYPE: inproceedings
ID: conf/oopsla/Reid17
bibtex: |
    @inproceedings{conf/oopsla/Reid17
        , abstract = {
    Software and hardware are increasingly being formally verified
    against specifications, but how can we verify the
    specifications themselves? This talk explores what it means to
    formally verify a specification. We solve three challenges: (1)
    How to create a secondary, higher-level specification that can
    be effectively reviewed by processor designers who are not
    experts in formal verification; (2) How to avoid common-mode
    failures between the specifications; and (3) How to
    automatically verify the two specifications against each other.
    <p>
    One of the most important specifications for software
    verification is the processor specification since it de nes the
    behaviour of machine code and of hardware protection features
    used by operating systems. We demonstrate our approach on ARM's
    v8-M Processor Specification, which is intended to improve the
    security of Internet of Things devices. Thus, we focus on
    establishing the security guarantees the architecture is
    intended to provide. Despite the fact that the ARM v8-M
    specification had previously been extensively tested, we found
    twelve bugs (including two security bugs) that have all been
    fixed by ARM.
    }
        , address = {New York, NY, USA}
        , affiliation = {ARM Ltd}
        , ar_file = {OOPSLA_17}
        , ar_shortname = {OOPSLA 17}
        , authors = {Alastair Reid}
        , day = {22\textendash 27}
        , doi = {10.1145/3133912}
        , file = {oopsla2017-whoguardstheguards.pdf}
        , journal = {PACMPL}
        , location = {Vancouver, BC, Canada}
        , month = {October}
        , number = {OOPSLA}
        , numpages = {24}
        , pages = {88:1--88:24}
        , publisher = {ACM}
        , slides = {oopsla2017-whoguardstheguards-slides.pdf}
        , title = {{W}ho guards the guards? {F}ormal {V}alidation of the {A}RM v8-{M} Architecture {S}pecification}
        , volume = {1}
        , year = {2017}
    }
---
