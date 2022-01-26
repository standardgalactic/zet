---
layout: post
title: Machine readable specifications at scale
---

There are lots of [potential uses for machine readable specifications][Spec uses]
so you would think that every major real world artifact like long-lived
hardware and software systems, protocols, languages, etc. would have
a formal specification that is used by all teams extending the design,
creating new implementations, testing/verifying the system, verifying
code that uses the system, doing security analyses or any of the other
potential uses.
But, in practice, this is usually not true: most real world systems do not
have a well tested, up to date, machine readable specification.

This article is about why you might want to change this and some things to
consider as you go about it.  In particular, it is about the use and creation
of machine readable specifications at scale: when the number of engineers
affected is counted in the thousands.  This sort of scale leads to different
problems and solutions than you would see in a 5--10 person project and both
the challenges and the potential benefits are significantly larger.

The main things I want to explain are

- Why your specification language should be weak and inexpressive
- Don't expect that the specification to meet 100% of the the needs of any
  individual team but aim to meet almost all the needs of almost all of the
  teams.
- That specifications of long lived real world systems need clear, precise mechanisms
  to be explicitly vague and imprecise.
- Specifications must be great documentation: even as we enable the use of
  specifications in tools, the primary purpose of a specification is still
  communication between human beings.
- We create a specification by *distilling* multiple existing "sources of truth"
  into a single specification and by validating the result against all of the
  sources.
- Try to create a virtuous cycle where every additional user increases the
  quality of the specification and this, in turn, attracts more users.
- The downside of machine readable specifications.

## The benefits of machine readable specifications

* Given all the potential uses of specifications, the most obvious benefit that
  we hope for is higher quality implementations of the specification.  This is
  especially important when developing systems where bugs have a major impact on
  users and fixing them is hard or expensive.
  Depending on when the problem is found, it can delay release (affecting time to market),
  require "respins" (having to manufacture the product again), or affect reputation.
  Areas with these issues include chip design and building secure systems.
  
* Important real world systems have lots of implementations: earlier versions
  going back decades in time, different teams in a single company creating independent
  implementations for different market niches, and teams at different companies creating
  competing implementations.  All of these implementations have to be consistent
  with each other: users depend on backwards compatibility, on compatibility across
  implementations and on compatibility between the products of different companies.
  
* If designers start with a low quality or ambiguous specification, problems will
  be found late during development by the validation team. The later the
  problems are found, the more impact it has on the release date which reduces
  how much of the market that product can capture and also increases the engineering costs
  for that product and delays when the team can start building the next product.
  
* Most importantly, machine readable specifications improve communication within
  the company, with any surrounding ecosystem (e.g., compiler writers, OS teams, or malware
  analysis tools), and with users.
  Real world systems are regularly extended with new features,
  the specifications often change in the process of developing the first implementation
  and those changes have to be communicated to all the other
  teams adding support for the new features.
  While "diffing" a paper document will catch some of those changes,
  automated uses of machine readable specifications let teams
  automatically update everything that they generate from the specifications.


## What makes a good machine readable specification?

The benefits of having machine readable specifications come from having
many different users. Those users all use the specifications in different ways:
architects test the spec as they are building it;
RTL designers read the specification to check what they have to build;
verification teams use the spec as a *golden reference* or *test oracle*;
security analysts verify security properties of the specification;
simulation engineers transform the specifications into simulators
or feed them to JIT engines for really high performance simulators;
anti-malware teams turn the specification into tools for symbolically
simulating the specification;
technical communication teams turn the specification into accessible,
readable, well structured, accessible documentation for users of the system;
etc.

And those different users all need to use the specification
in a different way:
transforming it into specifications for their favourite formal verification tool;
transforming the specification into C;
transforming the specification into Verilog;
generating tests from the specification;
measuring coverage of their tests;
performing forwards, backwards or bidirectional static analyses;
performing information flow analyses to find "surprising" information flows;
and there are many, many readers of the documentation from a variety of
backgrounds: hardware engineers, compiler engineers, OS engineers, security engineers,
etc.

### Should specification languages be rich, powerful and concise?

This diversity of uses has a surprising impact on the choice of
specification notation

> Weak, inexpressive languages are significantly better for
> writing specifications than rich, powerful languages.

The reason for this counterintuitive claim is that we need to be able to
convert the specification into many different languages to meet the needs of
all the different users.  The more features the specification language has, the
more likely we are to hit problems during this conversion process and the more
likely it is that the result will be buggy, slow or inconvenient to work with.

Moreover, the more powerful a language is, the more likely that it will confuse
readers of the specification. Higher order functions, monads, polymorphism,
overloaded operators, and the like make the specification more concise and
readable to those familiar with those features but they cause confusion and
risk misinterpretation for everyone else.  If readers of the specification need
to read more than a few pages of documentation for the specification language
before they can read the specification
then we are in trouble.
We need all readers to be able to easily understand the specification
and to arrive at the same interpretation of the specification as every other reader
of the specification.
And if readers of the
specification ever need to consult a "language lawyer" to distinguish between
two interpretations, then we have failed.  (Note that I am specifically talking
about *readers* of the specification.  There are many more *readers* than there
are *writers* and it is reasonable to demand a bit more of the architects who
are specifying the system than of all the people who have to implement, verify,
analyze and use the system.)

I often say that the best specification language is a table.
It is usually obvious how to read a table;
to check whether the table is complete (are all the boxes filled in);
how to invert a table (reading it as a mapping from outputs to inputs);
and how to convert the table to a range of different languages (e.g., as
an array, as an if-statement or as a case-statement.)
After that, restricted languages like finite state machines (ideally
specified using a table!) are great.
And there are various special purpose notations to describe things like
instruction encodings, register fields, packet formats, etc. that capture
the intended meaning in a high level way that is easy to explain,
easy to understand and easy to use in a variety of different ways.
You should only (reluctantly!) fall back on something like a programming language if
you need to specify something that is quite irregular.


### Which use case should be prioritized?

Another important consequence of having many users using the specification
in different ways is that 

> Specifications (and the languages that they are written in)
> are, necessarily, a *compromise* between the needs of all the
> different users.
> Every individual use would be better served by a different
> specification in a different specification language.

For example, if I'm verifying hardware with the Coq theorem prover, a commercial bounded model checker for Verilog,
or the [Forte symbolic simulation system][FORTE], it would be better to write the 
specification in Gallina, in System Verilog or in reFLect respectively.
Or if I'm writing a simulator, it would be better to write the specification in
C or C++.
And so on for every other use.
The only problem is that while this would be the perfect specification for one
team, it would be hard or impossible to use by most other teams.
Instead, we aim for a good engineering compromise: one that delivers
*almost* all of the benefit to *almost* every team.

A consequence of this is that although we aim to use 100% of the specification to
automate some task that was previously done manually, we should accept that we may
only manage to automate 97--99% of the task.
For example, it is hard to write a specification of floating point operations that is
simultaneously clear and easy to read and also a good reference for automatic
formal verification of a high performance floating point unit or that will
give adequate performance in a simulator.
In situations like these, where the most readable possible specification is not the best for other uses, we have two
choices. One choice is that we might write two versions of the specification: one that
we want to publish in documentation and one that we want to execute, verify against or whatever.
The second choice is to hand-write code for the 1--3% of the task that we cannot automate.
In both cases, we will want to thoroughly test or formally verify that the two versions
are equivalent to each other. And we will hope that this awkward 1--3% does not take too
much effort!

Although it is not strictly necessary, I think that it is much easier to find
the right notation if the specification is created by a team with a central
role in the company such as a research team.
The specification could reasonably be built by the team designing new architecture,
by the team writing documentation, or by the team verifying implementations but
each team will be tempted to write a specification that perfectly suits their
needs instead of a specification that is sufficiently good for all the potential users
of the specification.
(Once the initial specification has been created and a diverse set of users
are using the specification and asking for (potentially inconsistent) improvements,
you will probably want to setup a committee to refine and extend the compromise
between their different needs.)

### Explicit underspecification

Different implementations of real world systems have slightly different behaviour
from each other.
Later implementations may use opcodes or register fields that were reserved in
early versions of the specifications;
implementations targeting different markets may have different sets of features,
different cache sizes, etc.;
and implementations may have accidental variations for a variety of reasons.
If a specification is to be useful to users of the system, it needs to describe
most of the implementations that the users are likely to come across: those implemented
10 years ago; those that will be implemented 10 years in the future; perhapse even those implemented
by rival companies.

It is therefore important to have ways to *underspecify* the system: leaving room
for some of this variation between implementations.
At the same time though, it is unfortunately extremely easy to accidentally write a specification
that is much looser than intended and therefore fails to give users the information that
they need to use the system correctly, securely and efficiently and that gives
implementations far more room for variety than is helpful.

> We need mechanisms for *explicit underspecification: that allow us to be
> extremely clear about which parts of the specification
> are left deliberately vague.

Being *explicit* about underspecification makes it possible to 
write tools that warn when the specification is being accidentally vague.

This explicit underspecification is another example of the necessary
compromise between different uses of the specification.
For programmers using the system, the underspecification makes it easier
to write portable code.
But, validation teams that are checking a particular implementation
will want to check that the implementers built what they intend to build.
Validation teams will therefore want to be able to dial in the particular
choices made by the design team.


### Multiple views of documentation

Specifications must be great documentation since the overall goal is to
aid communication between many different teams of engineers.
To be able to build and validate tools that use the specification formally, engineers first
need to be able to understand the specification informally.
And, of course, many engineers will just want to read the specification
and do not want to automate their flow.


It is important to support multiple views of the specification such as

- Only show features that are supported by versions before or after some version number
  or by some particular product.

- Show a simplified version corresponding to
  how the system behaves in some specific context such as user-level
  execution.

- Where there are two alternative (allegedly equivalent) versions of a piece
  of the specification, select which one to show.

- Only show features that have been publicly announced or are allowed under
  a specific non-disclosure agreement (NDA).

- To comply with [export control regulations](https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States)
  it may be necessary to omit parts of the specification.


These different views might be generated simply by omitting instructions
that are not relevant or, if the specification uses "feature tests"
like "HaveFeatureX() -> bool" to test for a feature, then setting the
feature to FALSE and running a dead code elimination pass can produce
a simplified view.

However, where the purpose of the modified view is to keep information private,
we might want to be doubly sure that the information cannot accidentally
leak out.
For example, we might use separate git branches or repositories for released and unreleased
architecture specs with a "gatekeeper" carefully checking all merges from the unreleased
branch.
There will probably be multiple gatekeepers: senior architects deciding which
extensions are ready to be implemented, product managers deciding which
extensions to put in the product they manage, 
senior documentation engineers deciding when extensions should be incorporated into the master documentation.


## How do we create specifications?

When working on real world systems, the problem is not that there
is no source of truth but that there are so many of them.
For example, there are the actual products, simulators,
test suites, documentation, etc. In a large organization there might
be 10 or more such artifacts with each one capturing some important aspects
of the system but none meeting all users needs.

> The task of creating a specification is to *distill* all the existing
> sources of truth down into a single authoritative specification that
> is higher quality than any other source of truth.

There are two ways to take advantage of an existing source of truth.

1. Every significant product (e.g., processors, simulators, etc.)
   will have a large, thorough testsuite and may have a formal
   verification story.
   This is incredibly valuable because a good testsuite lets you
   check your specification.
   The "easiest" way to use this is to write a tool to convert
   the specification into code that can be inserted into a
   simulator.

2. In a few cases, we can semi-automatically translate existing simulators
   or specifications to our chosen specification language.
   The goal is probably not to get a fully working specification but
   just to reduce the manual effort of transcribing the specification
   into the specification language.

   If we can also generate a simulator from the result, then we can
   "round trip" the spec to check whether either conversion process
   broke anything.

It is inevitable that the initial specification and tools will not be very
good. It will be a bit buggy, it will be incomplete and the tools will generate
relatively slow buggy simulators.  However, once it becomes good enough that it
is useful to one (relatively forgiving) team, that team will start to find issues and
will start to report and fix the bugs.
As problems are fixed, the quality of the specification and tools will improve to the point
where a second wave of users are able to use the specification. These teams are
typically more sensitive to quality problems and they will find new bugs that
were unlikely to affect the early adopters. Fixing this second wave of bugs
will further improve the specification which will enable a third wave of users
with even higher quality requirements.

> Aim to create a "virtuous cycle" of users by looking for users with a broad
> variety of needs.

Initially, our goal is simply to catch up: just creating high quality
specifications of what exists (or is due to appear in the next generation
of products) and trying to automatically generate as much as possible
of the existing tools and verification collateral.
Once we have caught up though, it is important to sustain the effort.
New architecture extensions should be developed using the specification
as a design tool: taking advantage of the ability to easily add new extensions
into simulator, to generate high quality documentation at an early stage, etc.

## The downside of machine readable specifications

In many ways, having a high quality, authoritative, human readable,
machine readable specification that is used by all major users of existing
documentation is a no-brainer.
It takes work to set it up and to meet everybody's requirements and it takes
some coordination effort to maintain it in a usable state for all users but,
if you can do that, it saves a lot of effort, improves coordination and communication
both within the company and outside and it leads to higher quality products.

However, there is one important disadvantage of removing all the redundant work
that goes on at the moment: that redundancy sometimes catches mistakes in the
specification. This is especially true because the engineers currently
transcribing the documentation into Verilog, C++, test vectors, compilers,
OSes, etc. are experts with many years of experience.  As we automate the more
repetitive parts of the task, we reduce the number of expert eyeballs looking
at the specification and the number of different perspectives from which it is
being viewed.

> The cost of success is that you end up with "all your eggs in one basket."

To overcome this, we need to re-introduce some redundancy (i.e., add another "basket")
but we want to do this in a way that is most likely to find problems.
So, as the number of automated uses of the specification increases, it becomes
important to start formally validating the specification itself: writing down
properties that the current design and any extensions are expected to satisfy
and creating tools to verify that they do, indeed, hold.



### Related posts and papers

* Code: [ASLi](https://github.com/alastairreid/asl-interpreter)
* Code: [MRA Tools](https://github.com/alastairreid/mra_tools)
* Paper: [End-to-End Verification of ARM Processors with ISA-Formal]({{ site.url }}/papers/CAV_16/), CAV 2016.
* Paper: [Trustworthy Specifications of ARM v8-A and v8-M System Level Architecture]({{ site.url }}/papers/FMCAD_16/), FMCAD 2016.
* Paper: [Who guards the guards?  Formal Validation of the Arm v8-M Architecture Specification]({{ site.url }}/papers/OOPSLA_17/)), OOPSLA 2017.
* [Verifying against the official ARM specification]({{ site.baseurl }}{% post_url 2016-07-26-using-armarm %})
* [Finding Bugs versus Proving Absence of Bugs]({{ site.baseurl }}{% post_url 2016-07-18-finding-bugs %})
* [Limitations of ISA-Formal]({{ site.baseurl }}{% post_url 2016-07-30-isa-formal-limitations %})
* [ARM's ASL Specification Language]({{ site.baseurl }}{% post_url 2016-08-17-specification_languages %})
* [ARM Releases Machine Readable Architecture Specification]({{ site.baseurl }}{% post_url 2017-04-20-ARM-v8a-xml-release %})
* [Dissecting the ARM Machine Readable Architecture files]({{ site.baseurl }}{% post_url 2017-04-29-dissecting-ARM-MRA %})
* [ASL Lexical Syntax]({{ site.baseurl }}{% post_url 2017-05-07-asl-lexical-syntax %})
* [Arm v8.3 Machine Readable Specifications]({{ site.baseurl }}{% post_url 2017-07-31-arm-v8_3 %})
* [Are Natural Language Specifications Useful?]({{ site.baseurl }}{% post_url 2017-08-19-natural-specs %})
* [Formal validation of the Arm v8-M specification]({{ site.baseurl }}{% post_url 2017-09-24-validating-specs %})
* [Bidirectional ARM Assembly Syntax Specifications]({{ site.baseurl }}{% post_url 2017-12-24-bidirectional-assemblers %})
* Talk: [[How can you trust formally verified software (pdf)](/talks/using-arm-specs-34C3-2017-12-27.pdf)], Chaos Communication Congress, 2017.
* [Using ASLi with Arm's v8.6-A ISA specification]({{site.baseurl}}{% post_url 2022-01-25-mrs-at-scale %})
* [What can you do with an ISA specification?]({{site.baseurl}}{% post_url 2021-11-24-uses-for-isa-specs %})




[Spec uses]: {{site.baseurl}}{% post_url 2021-11-24-uses-for-isa-specs %}

[FORTE]: https://www.cs.ox.ac.uk/tom.melham/res/forte.html
