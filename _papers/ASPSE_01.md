---
layout: paper
year: 2001
title: Aspect Weaving as Component Knitting - Separating Concerns with Knit
png: knit-icse01-wasc.png
month: May
location: Toronto, Ontario, Canada
file: knit-icse01-wasc.pdf
booktitle: Workshop on Advanced Separation of Concerns in Software Engineering
author: Eric Eide, Alastair Reid, Matthew Flatt, Jay Lepreau
ar_shortname: ASPSE 01
ar_file: ASPSE_01
affiliation: University of Utah
abstract: |
    
    Knit is a new component specification and linking language. It
    was initially designed for low-level systems software, which
    requires especially flexible components with especially
    well-defined interfaces. For example, threads and virtual memory
    are typically implemented by components within the system,
    instead of being supplied by some execution environment.
    Consequently, components used to construct the system must expose
    interactions with threads and memory. The component composition
    tool must then check the resulting system for correctness, and
    weave the components together to achieve reasonable performance.
    <p>
    Component composition with Knit thus acts like aspect weaving: component
    interfaces determine the ``join points'' for weaving, while components (some of
    which may be automatically generated) implement aspects. Knit is not limited to
    the construction of low-level software, and to the degree that a set of
    components exposes fine-grained relationships, Knit provides the benefits
    of aspect-oriented programming within its component model.
ENTRYTYPE: inproceedings
ID: EEide01Aspect
bibtex: |
    @inproceedings{EEide01Aspect
        , abstract = {
    Knit is a new component specification and linking language. It
    was initially designed for low-level systems software, which
    requires especially flexible components with especially
    well-defined interfaces. For example, threads and virtual memory
    are typically implemented by components within the system,
    instead of being supplied by some execution environment.
    Consequently, components used to construct the system must expose
    interactions with threads and memory. The component composition
    tool must then check the resulting system for correctness, and
    weave the components together to achieve reasonable performance.
    <p>
    Component composition with Knit thus acts like aspect weaving: component
    interfaces determine the ``join points'' for weaving, while components (some of
    which may be automatically generated) implement aspects. Knit is not limited to
    the construction of low-level software, and to the degree that a set of
    components exposes fine-grained relationships, Knit provides the benefits
    of aspect-oriented programming within its component model.
    }
        , affiliation = {University of Utah}
        , ar_file = {ASPSE_01}
        , ar_shortname = {ASPSE 01}
        , author = {Eric Eide and Alastair Reid and Matthew Flatt and Jay Lepreau}
        , booktitle = {Workshop on Advanced Separation of Concerns in Software Engineering}
        , file = {knit-icse01-wasc.pdf}
        , location = {Toronto, Ontario, Canada}
        , month = {May}
        , png = {knit-icse01-wasc.png}
        , title = {{A}spect {W}eaving as {C}omponent {K}nitting: {S}eparating {C}oncerns with {K}nit}
        , year = {2001}
    }
---
