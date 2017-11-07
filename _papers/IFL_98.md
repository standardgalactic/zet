---
layout: paper
abstract: |
    Interrupt handling is a tricky business in lazy functional
    languages: we have to make sure that thunks that are being evaluated can
    be halted and later restarted if and when they are required. This is
    a particular problem for implementations which use black-holing.
    Black-Holing deliberately makes it impossible to revert such thunks
    to their original state to avoid a serious space leak. Interactive
    Haskell implementations such as Hugs and hbi catch interrupts and
    avoid the problem by omitting or disabling black-holing. Batch mode
    Haskell implementations such as HBC and the Glasgow Haskell Compiler
    (GHC) avoid this problem by disabling black-holing or by providing no
    way to catch interrupts. This paper describes a modification to GHC's
    abstract machine (the Spineless Tagless G-Machine) which
    simultaneously supports both interrupts and black-holing.
affiliation: Yale University
ar_file: IFL_98
ar_shortname: IFL 98
author: Alastair Reid
booktitle: Implementation of Functional Languages, 10th International Workshop (IFL'98) Selected Papers
day: 9-11
doi: 10.1007/3-540-48515-5_12
editor: Kevin Hammond, Antony J. T. Davie, Chris Clack
file: spine-ifl98.pdf
location: London, UK
month: September
pages: 186--199
publisher: Springer
series: Lecture Notes in Computer Science
title: Putting the Spine Back in the Spineless Tagless G-Machine An Implementation of Resumable Black-Holes
volume: 1595
year: 1998
ENTRYTYPE: inproceedings
ID: DBLPconf/ifl/Reid98
bibtex: |
    @inproceedings{DBLP:conf/ifl/Reid98
        , abstract = {Interrupt handling is a tricky business in lazy functional
    languages: we have to make sure that thunks that are being evaluated can
    be halted and later restarted if and when they are required. This is
    a particular problem for implementations which use black-holing.
    Black-Holing deliberately makes it impossible to revert such thunks
    to their original state to avoid a serious space leak. Interactive
    Haskell implementations such as Hugs and hbi catch interrupts and
    avoid the problem by omitting or disabling black-holing. Batch mode
    Haskell implementations such as HBC and the Glasgow Haskell Compiler
    (GHC) avoid this problem by disabling black-holing or by providing no
    way to catch interrupts. This paper describes a modification to GHC\textquotesingle s
    abstract machine (the Spineless Tagless G-Machine) which
    simultaneously supports both interrupts and black-holing.}
        , affiliation = {Yale University}
        , ar_file = {IFL_98}
        , ar_shortname = {IFL 98}
        , author = {Alastair Reid}
        , booktitle = {Implementation of Functional Languages, 10th International Workshop
    ({IFL}\textquotesingle 98) Selected Papers}
        , day = {9-11}
        , doi = {10.1007/3-540-48515-5\_12}
        , editor = {Kevin Hammond and
    Antony J. T. Davie and
    Chris Clack}
        , file = {spine-ifl98.pdf}
        , location = {London, UK}
        , month = {September}
        , pages = {186--199}
        , publisher = {Springer}
        , series = {Lecture Notes in Computer Science}
        , title = {{P}utting the {S}pine {B}ack in the {S}pineless {T}agless {G}-Machine: {A}n {I}mplementation
    of {R}esumable {B}lack-{H}oles}
        , volume = {1595}
        , year = {1998}
    }
---
