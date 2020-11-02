---
layout: paper
year: 2003
title: Evolving real-time systems using hierarchical scheduling and concurrency analysis
publisher: IEEE Computer Society
png: rtss03-preprint.png
pages: 25--36
month: December
location: Cancun, Mexico
file: rtss03-preprint.pdf
doi: 10.1109/REAL.2003.1253251
day: 3-5
booktitle: Proceedings of the 24th IEEE Real-Time Systems Symposium (RTSS 2003)
author: John Regehr, Alastair Reid, Kirk Webb, Michael A. Parker, Jay Lepreau
ar_shortname: RTSS 03
ar_file: RTSS_03
affiliation: University of Utah
abstract: |
    
    We have developed a new way to look at real-time and embedded
    software: as a collection of execution environments created by
    a hierarchy of schedulers. Common schedulers include those that run
    interrupts, bottom-half handlers, threads, and events. We have
    created algorithms for deriving response times, scheduling overheads,
    and blocking terms for tasks in systems containing multiple execution
    environments. We have also created task scheduler logic, a formalism
    that permits checking systems for race conditions and other errors.
    Concurrency analysis of low-level software is challenging because
    there are typically several kinds of locks, such as thread mutexes
    and disabling interrupts, and groups of cooperating tasks may need to
    acquire some, all, or none of the available types of locks to create
    correct software. Our high level goal is to create systems that are
    evolvable: they are easier to modify in response to changing
    requirements than are systems created using traditional techniques.
    We have applied our approach to two case studies in evolving software
    for networked sensor nodes.
ENTRYTYPE: inproceedings
ID: DBLPconf/rtss/RegehrRWPL03
bibtex: |
    @inproceedings{DBLP:conf/rtss/RegehrRWPL03
        , abstract = {
    We have developed a new way to look at real-time and embedded
    software: as a collection of execution environments created by
    a hierarchy of schedulers. Common schedulers include those that run
    interrupts, bottom-half handlers, threads, and events. We have
    created algorithms for deriving response times, scheduling overheads,
    and blocking terms for tasks in systems containing multiple execution
    environments. We have also created task scheduler logic, a formalism
    that permits checking systems for race conditions and other errors.
    Concurrency analysis of low-level software is challenging because
    there are typically several kinds of locks, such as thread mutexes
    and disabling interrupts, and groups of cooperating tasks may need to
    acquire some, all, or none of the available types of locks to create
    correct software. Our high level goal is to create systems that are
    evolvable: they are easier to modify in response to changing
    requirements than are systems created using traditional techniques.
    We have applied our approach to two case studies in evolving software
    for networked sensor nodes.
    }
        , affiliation = {University of Utah}
        , ar_file = {RTSS_03}
        , ar_shortname = {RTSS 03}
        , author = {John Regehr and
    Alastair Reid and
    Kirk Webb and
    Michael A. Parker and
    Jay Lepreau}
        , booktitle = {Proceedings of the 24th IEEE Real-Time Systems Symposium (RTSS 2003)}
        , day = {3-5}
        , doi = {10.1109/REAL.2003.1253251}
        , file = {rtss03-preprint.pdf}
        , location = {Cancun, Mexico}
        , month = {December}
        , pages = {25--36}
        , png = {rtss03-preprint.png}
        , publisher = {IEEE Computer Society}
        , title = {{E}volving real-time systems using hierarchical scheduling and concurrency
    analysis}
        , year = {2003}
    }
---
