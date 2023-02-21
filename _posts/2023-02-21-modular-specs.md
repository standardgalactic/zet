---
layout: post
title: "Modularizing ISA specifications"
---

Programming languages provide modules as a way of splitting large programs
up into small, separate pieces.
Modules enable *information hiding* that prevents one part of the program
from using and becoming dependent on some internal detail of how
other parts of the program are implemented.
Almost every major language designed in the last 50 years has some
form of module system.

Specifications of modern ISAs weigh in at around 50,000 -- 100,000
lines of specification and yet, despite that, they are specified
in languages (ASL and SAIL) that do not have a module system.
Why not? When is that a problem? And, most importantly, what can we do about it?

## Why ISA specs don't use modules

Early in the process of turning Arm's pseudocode language into a language that
can be parsed, typechecked and executed, I was keen to add a module system.  We
added qualified names like "AArch64.TakeException" but we never introduced
module boundaries or any other form of information hiding mechanisms.

The problem with information hiding is that it is a poor match for the primary
way that ISA specifications are used.
Their original use and still their most important use is as a PDF document.
ISA specifications weigh in at around 11,000 pages (for the Arm architecture)
or 5,000 pages (for the Intel architecture).
At this scale, the usual way to find information is by searching or using the
index. But, when you navigate the specification this way, you are just
jumping from one page to another and you have little
idea what chapter of the document you are in and you therefore have little
idea what module you are looking at.
So any module structure that may be present in the specification does
nothing to help the reader understand the specification and may
even cause confusion if the meaning of part of the specification depends
on knowing what module a given part of the specification is in.

So, rather to my surprise, I concluded that modules would not help
us write better, more easily understood specifications.

## When would modules be useful

There is one other important aspect of modules that I did not mention above: reuse.
Module systems promote reuse by splitting a large, monolithic system into
pieces with clearly defined interfaces.

All module systems clearly define the *exports* of a module: making it clear
what parts of the module are available for use outside the module.
The better module systems also clearly define the *imports* of a module:
making it possible to use the code in radically different contexts.
A good example of this is Matthew Flatt's "units" [[flatt:pldi:1998]]
where each "unit" defines a set of imports and a set of exports
and units can be connected to any other unit provided that it has
the right interfaces.

I first saw the power of this in operating system research.
Mike Jones [[jones:sosp:1993]] extending operating systems by "interposing"
on OS interfaces; and
Edoardo Biagioni [[biagioni:sigcomm:1994]] creating flexible, layered network stacks
using Standard ML's module system to define each layer in the stack as
a separate module that can be stacked on top of any other module.
The ultimate in this was Bryan Ford's "Microkernels meet recursive virtual machines"
[[ford:sosp:1996]] that let you build a range of operating systems
supporting features like isolation, process recovery and migration, etc. out of a form
of module system.
(This same idea of building an OS out of many small modules
is also the foundation of CertiKOS [[gu:osdi:2016]].)

In previous articles about [Uses for ISA specifications] and
[Machine readable specifications at scale], I have emphasized the
importance of being able to use the specifications in many different ways:
as documentation, to verify hardware, to build simulators, etc.
A modular ISA specification would make it significantly easier to achieve
this high level of reuse in different applications.

For example, in the "ISA-Formal" method for formally verifying Arm processors
we needed specifications of instructions.
We didn't want other parts of the architecture spec such as virtual memory,
taking exceptions, instruction fetch, IEEE floating point, etc.
(See "[Verifying against the official ARM specification]" and my paper [[reid:cav:2016]] for details
of the ISA-Formal method.)
So what we really wanted was to split the ISA specification into separate modules
for  each instruction, for the virtual memory system, for exceptions, for instruction fetch, etc.

Having a modular ISA specification would also make it easier to integrate
the specification into simulators.
For example, suppose you want to extend an existing simulator with
some new instructions. You don't want to add all of the instructions
in your ISA spec (because you already have those in the simulator);
and you don't want to add a new memory hierarchy (because you want
the new instructions to access the same memory as the old instructions).
If the ISA spec was modular (and the module boundaries were in roughly
the right place) then you could easily grab just the new instructions that
you want and ignore all the rest of the specification.


## How to modularize an operating system

Given a non-modular ISA specification, how can we split it into a number
of modules?
I tackled a similar problem when I was at the University of Utah.
The Flux OSKit [[ford:sosp:1997]] was based on the idea that operating
systems like Linux and FreeBSD would be more useful to researchers if
they were composed of modules that were designed for reuse.
The original OSKit used COM to define module interfaces but this was a bit heavyweight and
awkward so programmers reacted by creating relatively few module interfaces
to avoid excessive performance and programming overhead.
My variation of the OSKit (a system called "Knit") 
adapted Flatt's "units" to the C programming language to create a much lighter weight
system that encouraged the creation of very small modules
because there was no performance overhead and very little programmer overhead.
One of the big demonstrations in the paper [[reid:osdi:2000]] was
a network router where each component typically consisted of 5--10 lines
of code.

The key idea behind the Knit system was that we could re-modularize
a monolithic system by parsing the entire system, constructing the function call graph
and then discarding those parts of the system that did not belong in a particular module.
That is, I automated what programmers normally do when we ask them to break
a large system into modules.

To extract a module from a big system, the programmer defines an
initial set of exports and imports for that module.
The Knit tool uses the callgraph to find all the code that is reachable from
the exports without going through the imports.
The first run of the Knit tool usually reveals a dependency that the
programmer has forgotten about and the modularization tool pulls
in far too much code.
The programmer then refines the import list and checks whether
the resulting module is closer to what they want.
After a few iterations, they have something pretty close to what they want.

Once we had split our OS into modules, 
Eric Eide [[eide:icse:2002]]
used a variation on Mike Jones's interposition trick to achieve something like
[Aspect Oriented Programming].

## How to modularize an ISA specification

Given that background, it should be no surprise that I am using the same
basic idea to slice up the monolithic ASL specifications into modules.
That is, I define module boundaries by listing the imports and
exports of each module and then create the module by discarding
everything that is outside of those boundaries.

Since ISA specifications are large and the various implementations and uses are
also large (processors, verification IP, simulators, etc.), it is important
that the whole process [works at scale][Machine readable specifications at
scale]. To make it easy to automate the process of defining module boundaries
as far as possible, I define the list of imports and
exports in JSON files so that the module interfaces can be automatically generated.

The module boundaries themselves consist of several kinds of object.
The main ones are functions, types, constants and variables.
These need slightly different handling.

- Functions are the easiest: they are usually just exported exactly
  as they are.

  However, when transforming ASL/SAIL specifications to C, Verilog or
  SMT, it is useful to *monomorphize* ASL: turning a single polymorphic
  function into a family of monomorphic instances.
  For example, we might transform a polymorphic floating point function
  into separate instances for half, single and double precision
  by creating a 16-, 32- and 64-bit instance of the function.
  Depending on the application, it might be useful to export the
  original polymorphic function or some of the monomorphic instances.
  (See [Formal validation of the Arm v8-M specification] for detail on
  monomorphization.)

- Types are also fairly straightforward.
  But sometimes a function mentions a type but does not really
  depend on the definition of the type.
  In this case, we could potentially import the type abstractly
  which would allow the module to be used with other types that
  provide the same interface.

- Constants can be imported/exported exactly as they are.
  But, as with types, it can be useful to abstract them so that
  modules that import them can be instantiated with different
  values for the constants.

- The most tricky are variables.
  Instead of importing / exporting the variable directly, it is
  helpful to introduce a pair of functions: one to read the variable
  and one to write to the variable.
  Changing the interface to involve these access functions makes
  it easier to adapt how the specification is used.
  For example, in verification applications it is often useful to record
  whether a variable was written to by an execution.
  Or, if extending a simulator with some extra instructions,
  if a new instruction accesses the processor state, we want it to
  call a function in the original simulator when it performs that access.

  So, when importing/exporting a variable, it can be useful to create
  access functions to read/write the variable and transform all
  references to the variable into a call to the appropriate access function.

Each use of the specification turns out to need a slightly different module
interface.

## Summary

Module systems are a poor match for the way that ISA specifications
are published (embedded in a document that is 1000s of pages long).
But they are great for enabling reuse of different parts of the specification.

Many of the different applications of ISA specifications are based on
extracting the parts of the specification that are needed by that application.
That is, by dividing the large, monolithic ISA spec up into a number of smaller
modules in a way that is better suited to the application on hand.

*[We often don't really know what we are doing until after we have finished
doing it and try to explain it to others. I have been slicing
specifications up in the way I describe above for almost a decade now
and I have usually called it "callgraph surgery."
It was only when I tried explaining the technique to my colleagues that
I realized that what I was really doing was introducing module boundaries
in the middle of the specification, and that I made the connection to the work
that I did on modular operating systems back in the late '90s,
and wrote this article.]*


[Verifying against the official ARM specification]: {% post_url 2016-07-26-using-armarm %}
[Uses for ISA specifications]: {% post_url 2021-11-24-uses-for-isa-specs %}
[Machine readable specifications at scale]: {% post_url 2022-01-25-mrs-at-scale %}
[Formal validation of the Arm v8-M specification]: {% post_url 2017-09-24-validating-specs %}

[jones:sosp:1993]: {{ site.baseurl }}/RelatedWork/papers/jones:sosp:1993/
[biagioni:sigcomm:1994]: {{ site.baseurl }}/RelatedWork/papers/biagioni:sigcomm:1994/
[ford:sosp:1996]: {{ site.baseurl }}/RelatedWork/papers/ford:sosp:1996/
[ford:sosp:1997]: {{ site.baseurl }}/RelatedWork/papers/ford:sosp:1997/
[flatt:pldi:1998]: {{ site.baseurl }}/RelatedWork/papers/flatt:pldi:1998/
[reid:osdi:2000]: {{ site.baseurl }}/RelatedWork/papers/reid:osdi:2000/
[eide:icse:2002]: {{ site.baseurl }}/RelatedWork/papers/eide:icse:2002/
[gu:osdi:2016]: {{ site.baseurl }}/RelatedWork/papers/gu:osdi:2016/
[reid:cav:2016]: {{ site.baseurl }}/RelatedWork/papers/reid:cav:2016/

[Aspect Oriented Programming]: {{ site.baseurl }}/RelatedWork/notes/aspect-oriented-programming

