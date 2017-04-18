---
layout: page
title: Professional Experience
permalink: /activities/
---

| Position                           || Institution                      || Date           |
| :--------------------------------- || :------------------------------- || :------------- |
| Senior Principal Research Engineer || ARM Ltd                          || 2017 - present |
| - Patent Review Committee          ||                                  || 2014 - present |
| Principal Research Engineer        || ARM Ltd                          || 2004 - 2017    |
| - Skill Group Leader               ||                                  || 2011 - 2014    |
| Director                           || Reid Consulting (UK) Ltd         || 2002 - 2004    |
| Research Associate                 || Flux group, University of Utah   || 1998 - 2001    |
| Systems Programmer                 || Haskell Project, Yale University || 1994 - 1998    |

* Table of contents
{:toc}

## Program committees

I have served on the following conference program committees.

- [SPIN 2012](http://qav.cs.ox.ac.uk/spin2012/)
- [RTAS 2012](http://2014.rtas.org/wp-content/uploads/archives/2012/)
- [LCTES 2011](http://lctes2011.elis.ugent.be/?file=kop1.php)
- [LCTES 2008](http://lctes08.flux.utah.edu)
- [RTAS 2007](http://2014.rtas.org/wp-content/uploads/archives/2007/)
- HiPEAC 2007
- [RTAS 2006](http://2014.rtas.org/wp-content/uploads/archives/2006/index.htm)

---

## ARM Ltd. Projects (selected)

I joined ARM Research in 2004 and initiate and lead research projects.  As
a supplier of commercial IP, we don't publish details of all our projects so
the following is only a selection.


### Processor Formal Verification

I am currently looking at how to use ARM's architecture specifications to
verify ARM's processors and related IP.  This is running concurrently with the
project on mechanising ARM's processor specifications

Working with verification engineers in ARM's processor division, I developed
the ISA-Formal processor verification technique that is based on:

- Machine generation of verification IP from ARM's official processor
  specification documents
- Using model checking for end-to-end verification of processor pipelines

This technique has proven very effective at detecting complex bugs early in the
design process.

1 paper published, 1 tool released.


### Mechanised Processor Specification

Concurrently with the Processor Verification project, I work on improving and
extending how ARM specifies its processor architecture.

- Can we make the specification more precise without reducing readability?
- Can we automatically generate some of the objects currently manually derived
  from the specification?
- Can we detect omissions/errors in the specification?

(This is an offshoot of the concurrent vector processing project. We got tired
of having to update compilers, assemblers, simulators, etc. each time we tried
out a new instruction.)

As a result of this work, the specification is executable instead of just being
a static document and we generate parts of simulators, assemblers,
disassemblers, etc. from the specification.
It is now standard practice for new architecture extensions
to be tested as they are being designed and for specifications to undergo
regression testing during maintenance.

2 architecture specifications mechanised, 2 major architecture extensions mechanised,
1 tool tech transferred, 1 paper published.


### Vector Processing

Building on the experience from NEON and from the Software Defined Radio
project, I spent some time working on how to make vector processing more
flexible and on how to implement it more efficiently.
This led to a major architecture extension and multiple architecture and
microarchitecture patents.

Since vector architecture projects always lead to large ISA extensions, I also
created a language and tool to describe large ISAs in a compact, structured
way.

4 patents granted, 4 patents pending, 1 paper published, 1 tool tech
transferred.


### Software Defined Radio

I led the team developing software tools for ARM's Software Defined Radio
platform. This included developing C language extensions to support
heterogeneous multiprocessors ('System-on-chip C' or just SoC-C), developing
the SoC-C compiler and linker and driving the specification of the toolchain
for individual processors. I also contributed to the initial design of the
Vector (SIMD) instructions for the DSP engine we developed and to both hardware
and software aspects of the trace generation system for low overhead monitoring
of parallel real-time systems. The platform has been spun out into another
company (http://www.cognovo.co.uk/) which has since been acquired by u-blox.

7 patents granted, 1 patent pending, 4 papers published, 3 tools released,
numerous training sessions provided.


### Thread Support

A chance discussion over coffee lead to an interesting idea on how to share
resources between hardware threads of different priorities. 

1 patent granted, 1 paper published.


### Reliability/Security

Another team had developed an interesting circuit for running processors faster
by detecting and recovering from errors. This short project looked at how this
circuit could be used to detect that someone is tampering with the chip. 

1 patent granted.


### Parallel H.264 decoder

This project explored use of ideas from stream computation to structure
a parallel H.264 decoder. Observations of the difficulty handling control in
stream computation fed into the later development of SoC-C (see Software
Defined Radio project).

1 patent filed.


### Vectorizing Compiler for NEON

I joined an existing hardware-software project developing ARM's Advanced SIMD
extensions (NEON). The software component was to improve/test/demonstrate the
design by showing that a vectorizing compiler could be written. My role was to
add floating point support and make the compiler robust enough for release to
partners. One of the nicest comments we received was that our prototype R&D
compiler was more reliable than many production quality commercial tools that
the partner uses.

1 tool released.

---

## University of Utah Projects

I joined the University of Utah's Flux research group in 1999 where I worked on
microkernels, component-based operating systems and embedded systems.

### Embedded Systems

I developed a variety of tools for analyzing embedded systems including
a binary analysis tool to identify which interrupts were enabled/disabled and
a worst-case stack-depth analysis (which accounted for interrupt-handlers).

4 papers published.

### Component-Based Operating Systems

I designed and implemented a component extension for C which could handle the
needs of low-level code with complex interconnections and even more complex
component initialization requirements. I used this to develop a more modular
version of the operating system toolkit 'OSKit' previously developed at Utah.

3 papers published, 2 open source projects released.

---

## Yale University Projects

I joined Yale University's Haskell research group in 1994.

### Robotics

I applied the principles of Functional Reactive Programming to the tasks of
Visual Tracking and Robotics.

2 papers published.

### Haskell Compiler Development

I worked on the Yale Haskell Compiler, the Hugs (Haskell) Compiler, the Glasgow
Haskell Compiler, the standard Haskell libraries, graphics libraries, exception
handling and the foreign function interface.

6 papers published, 1 open source project released, 1 open source project
maintained.

---

## University of Glasgow Projects

I earned an M.Sc. by research in formal methods from the University of Glasgow.

### GUIs

I implemented a widget library for Haskell using the recently developed 'monad
programming' technique and an early version of Haskell's foreign function
interface.

1 paper published.

### Foreign Function Interface

I extended the Glasgow Haskell Compiler's garbage collector to better support
the foreign function interface,

1 paper published, contributed to 1 open source project.

