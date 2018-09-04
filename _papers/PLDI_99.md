---
layout: paper
year: 1999
title: A Semantics for Imprecise Exceptions
publisher: ACM
pages: 25--36
month: May
location: Atlanta, Georgia, USA
file: except.pdf
editor: Barbara G. Ryder, Benjamin G. Zorn
doi: 10.1145/301618.301637
day: 1-4
booktitle: Proceedings of the 1999 ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI '99)
author: Simon L. Peyton Jones, Alastair Reid, Fergus Henderson, C. A. R. Hoare, Simon Marlow
ar_shortname: PLDI 99
ar_file: PLDI_99
affiliation: Yale University and Microsoft Research and Cambridge University and University of Melbourne
acceptance: 20
abstract: |
    
    Some modern superscalar microprocessors provide only imprecise
    exceptions. That is, they do not guarantee to report the same exception
    that would be encountered by a straightforward sequential execution
    of the program. In exchange, they offer increased performance or
    decreased area (which amount to much the same thing).
    <p>
    This performance/precision tradeoff has not so far been much explored at
    the programming language level. In this paper we propose a design for
    imprecise exceptions in the lazy functional programming language Haskell.
    We discuss various simpler designs, and conclude that imprecision is
    essential if the language is still to enjoy its current rich algebra of
    transformations. We sketch a precise semantics for the language extended
    with exceptions.
    <p>
    From the functional programming point of view, the paper shows how to
    extend Haskell with exceptions without crippling the language or its
    compilers. From the point of view of the wider programming language
    community, we pose the question of whether precision and performance
    can be traded off in other languages too.
ENTRYTYPE: inproceedings
ID: DBLPconf/pldi/JonesRHHM99
bibtex: |
    @inproceedings{DBLP:conf/pldi/JonesRHHM99
        , abstract = {
    Some modern superscalar microprocessors provide only imprecise
    exceptions. That is, they do not guarantee to report the same exception
    that would be encountered by a straightforward sequential execution
    of the program. In exchange, they offer increased performance or
    decreased area (which amount to much the same thing).
    <p>
    This performance/precision tradeoff has not so far been much explored at
    the programming language level. In this paper we propose a design for
    imprecise exceptions in the lazy functional programming language Haskell.
    We discuss various simpler designs, and conclude that imprecision is
    essential if the language is still to enjoy its current rich algebra of
    transformations. We sketch a precise semantics for the language extended
    with exceptions.
    <p>
    From the functional programming point of view, the paper shows how to
    extend Haskell with exceptions without crippling the language or its
    compilers. From the point of view of the wider programming language
    community, we pose the question of whether precision and performance
    can be traded off in other languages too.  }
        , acceptance = {20}
        , affiliation = {Yale University and Microsoft Research and Cambridge University
    and University of Melbourne}
        , ar_file = {PLDI_99}
        , ar_shortname = {PLDI 99}
        , author = {Simon L. Peyton Jones and
    Alastair Reid and
    Fergus Henderson and
    C. A. R. Hoare and
    Simon Marlow}
        , booktitle = {Proceedings of the 1999 ACM SIGPLAN Conference on Programming
    Language Design and Implementation (PLDI \textquotesingle 99)}
        , day = {1-4}
        , doi = {10.1145/301618.301637}
        , editor = {Barbara G. Ryder and
    Benjamin G. Zorn}
        , file = {except.pdf}
        , location = {Atlanta, Georgia, USA}
        , month = {May}
        , pages = {25--36}
        , publisher = {ACM}
        , title = {{A} Semantics for {I}mprecise {E}xceptions}
        , year = {1999}
    }
---
