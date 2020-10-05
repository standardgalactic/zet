---
title: Summarizing 12 months of reading papers
layout: post
---

This is an overview of [the papers that I have read over the last 12 months][papers]
since I [joined Google Research][joining Google].
Over the last year, I have read 122 papers and I have added 364 to my paper
backlog.
You can read [my summaries of all the papers][RelatedWork],
read [notes on common themes in the papers][notes],
and download [BibTeX][bibfile] for all the papers.
As the number of papers grew, I reorganized several times and
[the site][RelatedWork] became a bit like a [Zettelkasten].


## How I organize my notes about papers

I started the year by trying to define a few topics that the papers I read
would fit into and trying to maintain overviews of each topic that linked to
each paper.  This is how I used to organize papers in filing boxes, filing
cabinets, stacks on my desk, etc. but it doesn't work very well.  The most
obvious reason that it doesn't work is that some papers span multiple research
topics so, whichever topic I assign them to, it will be wrong.
More seriously though, I am often reading because I don't understand the field so
how can I possibly know how to organize papers when I first start
reading.
I also found that I was not updating the overviews because each time I read
a paper, I would need to restructure the overview to accomodate what I had just
learned.

After a few months, the original system was starting to fail, and I learned
about the [ZettelKasten] method of making
notes about papers and concepts. I have not fully adopted this method
but I have adopted some of the ideas:

- If a paper introduces an important looking concept, I create a new
  page in my [notes] and link the paper to the note.
  This avoids duplication of the information and, by adding links to
  all the referring pages, it makes it easy to find all the papers
  related to the concept.

- I vigorously add links between papers and notes: going back to previously
  read papers and adding links when I add a new concept.

- I rely on the links to define the structure of the site.
  That is, I allow topics to emerge and evolve organically as I read
  papers instead of trying to impose structure on a topic before
  I even understand it.

The main way that my approach differs from [ZettelKasten] is that
a true ZettelKasten would create notes for every concept whereas
I tend to create notes only if I think multiple papers will link
to the concept.
I should probably follow the ZettelKasten approach more closely
and move a lot of the information I currently put in paper summaries
into notes about concepts.


## What I read

Over the last year, I have mostly been reading about software verification
and security including
[Information flow control],
[Operating Systems],
[Verification tools],
[Separation logic] (and, more generally, [permission logic]),
[The Rust language],
[Fuzz testing],
the [2005 Bugs workshop](https://www.cs.umd.edu/~pugh/BugWorkshop05/),
[Property-based testing],
[Test generation],
and
[Google]
(in, more or less, chronological order).

Each paper links to my summary of the paper.
A few caveats about my summaries:

- Paper summaries are written fairly quickly, in a single pass, with little/no revision.

- Notes about concepts are always in a state of flux and often contain 'todo' comments
  about how they should be restructured when I find the time.

- Especially when I am reading about a new topic, the summaries will contain errors
  because I don't understand that topic well enough to write a good summary.

- Since the summaries are mostly intended to help my understanding they may skip explaining
  concepts that I already understand well.
  Reading other papers in the same topic may help, or it may not.

- The summaries are not a substitute for reading the paper yourself and forming your own
  understanding and opinion.
  I encourage you to write your own paper summaries and maybe only use my list as one
  source of ideas of what to read.


### [Information flow control]

Tracking and controlling how information moves through a program – usually for security reasons

- Secure information flow by self composition [<a href="{{ site.baseurl }}/RelatedWork/papers/barthe:csfw:2004/">barthe:csfw:2004</a>]
- SecChisel: Language and tool for practical and scalable security verification of security-aware hardware architectures [<a href="{{ site.baseurl }}/RelatedWork/papers/deng:hasp:2019/">deng:hasp:2019</a>]
- Noninterference, transitivity, and channel-control security policies [<a href="{{ site.baseurl }}/RelatedWork/papers/rushby:sri:1992/">rushby:sri:1992</a>]
- A hardware design language for timing-sensitive information flow security [<a href="{{ site.baseurl }}/RelatedWork/papers/zhang:asplos:2015/">zhang:asplos:2015</a>]
- Complete information flow tracking from the gates up [<a href="{{ site.baseurl }}/RelatedWork/papers/tiwari:asplos:2009/">tiwari:asplos:2009</a>]
- Theoretical analysis of gate level information flow tracking [<a href="{{ site.baseurl }}/RelatedWork/papers/oberg:dac:2010/">oberg:dac:2010</a>]
- On the foundations of quantitative information flow [<a href="{{ site.baseurl }}/RelatedWork/papers/smith:fossacs:2009/">smith:fossacs:2009</a>]
- Secure autonomous cyber-physical systems through verifiable information flow control [<a href="{{ site.baseurl }}/RelatedWork/papers/liu:cpsspc:2018/">liu:cpsspc:2018</a>]
- Verifying constant-time implementations [<a href="{{ site.baseurl }}/RelatedWork/papers/almeida:security:2016/">almeida:security:2016</a>]


### [Operating Systems]

Mostly concerned with verification of OSes and information flow control.

- seL4: from general purpose to a proof of information flow enforcement [<a href="{{ site.baseurl }}/RelatedWork/papers/murray:secpriv:2013/">murray:secpriv:2013</a>]
- Scaling symbolic evaluation for automated verification of systems code with Serval [<a href="{{ site.baseurl }}/RelatedWork/papers/nelson:sosp:2019/">nelson:sosp:2019</a>]
- Combining mechanized proofs and model-based testing in the formal analysis of a hypervisor [<a href="{{ site.baseurl }}/RelatedWork/papers/becker:fm:2016/">becker:fm:2016</a>]
- überSpark: Enforcing verifiable object abstractions for automated compositional security analysis of a hypervisor [<a href="{{ site.baseurl }}/RelatedWork/papers/vasudevan:usenix:2016/">vasudevan:usenix:2016</a>]
- Komodo: Using verification to disentangle secure-enclave hardware from software [<a href="{{ site.baseurl }}/RelatedWork/papers/ferraiuolo:sosp:2017/">ferraiuolo:sosp:2017</a>]
- CertiKOS: An extensible architecture for building certified concurrent OS Kernels [<a href="{{ site.baseurl }}/RelatedWork/papers/gu:osdi:2016/">gu:osdi:2016</a>]
- End-to-end verification of information flow security for C and assembly programs [<a href="{{ site.baseurl }}/RelatedWork/papers/costanzo:pldi:2016/">costanzo:pldi:2016</a>]
- Attacking, repairing, and verifying SecVisor: A retrospective on the security of a hypervisor [<a href="{{ site.baseurl }}/RelatedWork/papers/franklin:cmu:2008/">franklin:cmu:2008</a>]
- SecVisor: A tiny hypervisor to provide lifetime kernel code integrity for commodity OSes [<a href="{{ site.baseurl }}/RelatedWork/papers/seshadri:sosp:2007/">seshadri:sosp:2007</a>]
- Verifying security invariants in ExpressOS [<a href="{{ site.baseurl }}/RelatedWork/papers/mai:asplos:2013/">mai:asplos:2013</a>]
- Scalable translation validation of unverified legacy OS code [<a href="{{ site.baseurl }}/RelatedWork/papers/tahat:fmcad:2019/">tahat:fmcad:2019</a>]
- Verifying the Microsoft Hyper-V hypervisor with VCC [<a href="{{ site.baseurl }}/RelatedWork/papers/leinenbach:fm:2009/">leinenbach:fm:2009</a>]
- Sound formal verification of Linux's USB BP keyboard driver [<a href="{{ site.baseurl }}/RelatedWork/papers/penninckx:nfm:2012/">penninckx:nfm:2012</a>]
- Local verification of global invariants in concurrent programs [<a href="{{ site.baseurl }}/RelatedWork/papers/cohen:cav:2010/">cohen:cav:2010</a>]
- The Flask security architecture: System support for diverse security policies [<a href="{{ site.baseurl }}/RelatedWork/papers/spencer:security:1999/">spencer:security:1999</a>]


### [Verification tools]

With a focus on verification tools.

- [Bounded model checking] and [Model checking]

  - Software model checking [<a href="{{ site.baseurl }}/RelatedWork/papers/jhala:compsurv:2009/">jhala:compsurv:2009</a>]
  - Model checking: Algorithmic verification and debugging [<a href="{{ site.baseurl }}/RelatedWork/papers/clarke:cacm:2009/">clarke:cacm:2009</a>]
  - Code-level model checking in the software development workflow [<a href="{{ site.baseurl }}/RelatedWork/papers/chong:icse:2020/">chong:icse:2020</a>]
  - Software verification: Testing vs. model checking [<a href="{{ site.baseurl }}/RelatedWork/papers/beyer:hvc:2017/">beyer:hvc:2017</a>]
  - Model checking [<a href="{{ site.baseurl }}/RelatedWork/papers/mcmillan:ecs:2003/">mcmillan:ecs:2003</a>]
  - A lightweight symbolic virtual machine for solver-aided host languages [<a href="{{ site.baseurl }}/RelatedWork/papers/torlak:pldi:2014/">torlak:pldi:2014</a>]

- [Symbolic execution]

  - Symbolic execution for software testing: Three decades later [<a href="{{ site.baseurl }}/RelatedWork/papers/cadar:cacm:2013/">cadar:cacm:2013</a>]
  - The art, science, and engineering of fuzzing: A survey [<a href="{{ site.baseurl }}/RelatedWork/papers/manes:ieeetse:2019/">manes:ieeetse:2019</a>]
  - A survey of symbolic execution techniques [<a href="{{ site.baseurl }}/RelatedWork/papers/baldoni:compsurv:2018/">baldoni:compsurv:2018</a>]
  - Enhancing symbolic execution with veritesting [<a href="{{ site.baseurl }}/RelatedWork/papers/avgerinos:icse:2014/">avgerinos:icse:2014</a>]
  - Selective symbolic execution [<a href="{{ site.baseurl }}/RelatedWork/papers/chipounov:hotdep:2009/">chipounov:hotdep:2009</a>]
  - -Overify: Optimizing programs for fast verification [<a href="{{ site.baseurl }}/RelatedWork/papers/wagner:hotos:2013/">wagner:hotos:2013</a>]
  - COASTAL: Combining concolic and fuzzing for Java (competition contribution) [<a href="{{ site.baseurl }}/RelatedWork/papers/visser:tacas:2020/">visser:tacas:2020</a>]

- [Auto active verification] – requires input from user but all interaction is in terms of the original program.

  - Extended static checking: A ten-year perspective [<a href="{{ site.baseurl }}/RelatedWork/papers/leino:informatics:2001/">leino:informatics:2001</a>]
  - Dafny: An automatic program verifier for functional correctness [<a href="{{ site.baseurl }}/RelatedWork/papers/leino:lpair:2010/">leino:lpair:2010</a>]
  - Developing verified programs with Dafny [<a href="{{ site.baseurl }}/RelatedWork/papers/leino:icse:2013/">leino:icse:2013</a>]

- [SAT] and [SMT]

  - Boolean satisfiability from theoretical hardness to practical success [<a href="{{ site.baseurl }}/RelatedWork/papers/malik:cacm:2009/">malik:cacm:2009</a>]
  - Satisfiability modulo theories: Introduction and applications [<a href="{{ site.baseurl }}/RelatedWork/papers/demoura:cacm:2011/">demoura:cacm:2011</a>]
  - Benchmarking solvers, SAT-style [<a href="{{ site.baseurl }}/RelatedWork/papers/nyxbrain:sc2:2017/">nyxbrain:sc2:2017</a>]

- SMACK: Decoupling source language details from verifier implementations [<a href="{{ site.baseurl }}/RelatedWork/papers/rakamaric:cav:2014/">rakamaric:cav:2014</a>]
- The Boogie verification debugger [<a href="{{ site.baseurl }}/RelatedWork/papers/legoues:sefm:2011/">legoues:sefm:2011</a>]
- Boogie: A modular reusable verifier for object-oriented programs [<a href="{{ site.baseurl }}/RelatedWork/papers/barnett:fmco:2005/">barnett:fmco:2005</a>]
- Specification and verification: The Spec# experience [<a href="{{ site.baseurl }}/RelatedWork/papers/barnett:cacm:2011/">barnett:cacm:2011</a>]
- VeriFast: Imperative programs as proofs [<a href="{{ site.baseurl }}/RelatedWork/papers/jacobs:vstte:2010/">jacobs:vstte:2010</a>]
- Software verification with VeriFast: Industrial case studies [<a href="{{ site.baseurl }}/RelatedWork/papers/philippaerts:scp:2014/">philippaerts:scp:2014</a>]
- VeriFast: A powerful, sound, predictable, fast verifier for C and Java [<a href="{{ site.baseurl }}/RelatedWork/papers/jacobs:nfm:2011/">jacobs:nfm:2011</a>]
- A solver for reachability modulo theories [<a href="{{ site.baseurl }}/RelatedWork/papers/lal:cav:2012/">lal:cav:2012</a>]
- A precise yet efficient memory model for C [<a href="{{ site.baseurl }}/RelatedWork/papers/cohen:entcs:2009/">cohen:entcs:2009</a>]
- Frama-C: A software analysis perspective [<a href="{{ site.baseurl }}/RelatedWork/papers/cuoq:sefm:2012/">cuoq:sefm:2012</a>]
- Multi-prover verification of C programs [<a href="{{ site.baseurl }}/RelatedWork/papers/filliatre:fem:2004/">filliatre:fem:2004</a>]
- Formal verification of a memory allocation module of Contiki with Frama-C: a case study [<a href="{{ site.baseurl }}/RelatedWork/papers/mangano:crisis:2016/">mangano:crisis:2016</a>]
- SpaceSearch: A library for building and verifying solver-aided tools [<a href="{{ site.baseurl }}/RelatedWork/papers/weitz:icfp:2017/">weitz:icfp:2017</a>]


### [Separation logic] (and, more generally, [permission logic])

For reasoning about heap data structures and aliasing.

- Separation logic [<a href="{{ site.baseurl }}/RelatedWork/papers/ohearn:cacm:2019/">ohearn:cacm:2019</a>]
- VeriFast: Imperative programs as proofs [<a href="{{ site.baseurl }}/RelatedWork/papers/jacobs:vstte:2010/">jacobs:vstte:2010</a>]
- Software verification with VeriFast: Industrial case studies [<a href="{{ site.baseurl }}/RelatedWork/papers/philippaerts:scp:2014/">philippaerts:scp:2014</a>]
- VeriFast: A powerful, sound, predictable, fast verifier for C and Java [<a href="{{ site.baseurl }}/RelatedWork/papers/jacobs:nfm:2011/">jacobs:nfm:2011</a>]
- Viper: A verification infrastructure for permission-based reasoning [<a href="{{ site.baseurl }}/RelatedWork/papers/muller:vmcai:2016/">muller:vmcai:2016</a>]
- Lightweight support for magic wands in an automatic verifier [<a href="{{ site.baseurl }}/RelatedWork/papers/schwerhoff:ecoop:2015/">schwerhoff:ecoop:2015</a>]
- Specified blocks [<a href="{{ site.baseurl }}/RelatedWork/papers/hehner:vstte:2008/">hehner:vstte:2008</a>]
- Local reasoning about while-loops [<a href="{{ site.baseurl }}/RelatedWork/papers/tuerk:vstte:2010/">tuerk:vstte:2010</a>]
- Alias types [<a href="{{ site.baseurl }}/RelatedWork/papers/smith:esop:2000/">smith:esop:2000</a>]
- TALx86: A realistic typed assembly language [<a href="{{ site.baseurl }}/RelatedWork/papers/morrisett:wcsss:1999/">morrisett:wcsss:1999</a>]
- Fractional permissions without the fractions [<a href="{{ site.baseurl }}/RelatedWork/papers/heule:ftfjp:2011/">heule:ftfjp:2011</a>]
- The ramifications of sharing in data structures [<a href="{{ site.baseurl }}/RelatedWork/papers/hobor:popl:2013/">hobor:popl:2013</a>]
- Verifying event-driven programs using ramified frame properties [<a href="{{ site.baseurl }}/RelatedWork/papers/krishnaswami:tldi:2010/">krishnaswami:tldi:2010</a>]
- Separation logic and abstraction [<a href="{{ site.baseurl }}/RelatedWork/papers/parkinson:popl:2005/">parkinson:popl:2005</a>]
- Verification of concurrent programs with Chalice [<a href="{{ site.baseurl }}/RelatedWork/papers/leino:fosad:2007/">leino:fosad:2007</a>]
- Compositional shape analysis by means of bi-abduction [<a href="{{ site.baseurl }}/RelatedWork/papers/calcagno:popl:2009/">calcagno:popl:2009</a>]
- Smallfoot: Modular automatic assertion checking with separation logic [<a href="{{ site.baseurl }}/RelatedWork/papers/berdine:fmco:2005/">berdine:fmco:2005</a>]
- Symbolic execution with separation logic [<a href="{{ site.baseurl }}/RelatedWork/papers/berdine:aplas:2005/">berdine:aplas:2005</a>]
- Implicit dynamic frames: Combining dynamic frames and separation logic [<a href="{{ site.baseurl }}/RelatedWork/papers/smans:ecoop:2009/">smans:ecoop:2009</a>]
- Permission accounting in separation logic [<a href="{{ site.baseurl }}/RelatedWork/papers/bornat:popl:2005/">bornat:popl:2005</a>]
- Separation logic: a logic for shared mutable data structures [<a href="{{ site.baseurl }}/RelatedWork/papers/reynolds:lics:2002/">reynolds:lics:2002</a>]
- Annotation inference for separation logic based verifiers [<a href="{{ site.baseurl }}/RelatedWork/papers/vogels:fmoods:2011/">vogels:fmoods:2011</a>]


### [The Rust language]

Rust is designed to be safer, easier to reason about and the type system has some interesting connections with [separation logic].

- RustBelt: Securing the foundations of the Rust programming language [<a href="{{ site.baseurl }}/RelatedWork/papers/jung:popl:2017/">jung:popl:2017</a>]
- Stacked borrows: An aliasing model for Rust [<a href="{{ site.baseurl }}/RelatedWork/papers/jung:popl:2020/">jung:popl:2020</a>]
- The case for writing a kernel in Rust [<a href="{{ site.baseurl }}/RelatedWork/papers/levy:apsys:2017/">levy:apsys:2017</a>]
- Viper: A verification infrastructure for permission-based reasoning [<a href="{{ site.baseurl }}/RelatedWork/papers/muller:vmcai:2016/">muller:vmcai:2016</a>]
- Leveraging Rust types for modular specification and verification [<a href="{{ site.baseurl }}/RelatedWork/papers/astrauskas:oopsla:2019/">astrauskas:oopsla:2019</a>]
- Verifying Rust programs with SMACK [<a href="{{ site.baseurl }}/RelatedWork/papers/baranowski:atva:2018/">baranowski:atva:2018</a>]
- Verification of safety functions implemented in Rust: A symbolic execution based approach [<a href="{{ site.baseurl }}/RelatedWork/papers/lindner:indin:2019/">lindner:indin:2019</a>]
- No panic! Verification of Rust programs by symbolic execution [<a href="{{ site.baseurl }}/RelatedWork/papers/lindner:indin:2018/">lindner:indin:2018</a>]
- RustHorn: CHC-based verification for Rust programs [<a href="{{ site.baseurl }}/RelatedWork/papers/matsushita:esop:2020/">matsushita:esop:2020</a>]
- Crust: A bounded verifier for Rust [<a href="{{ site.baseurl }}/RelatedWork/papers/toman:ase:2015/">toman:ase:2015</a>]
- Simple verification of Rust programs via functional purification [<a href="{{ site.baseurl }}/RelatedWork/papers/ullrich:msc:2016/">ullrich:msc:2016</a>]


### [Fuzz testing]

Testing a program by throwing random input at it.

- An empirical study of the reliability of UNIX utilities [<a href="{{ site.baseurl }}/RelatedWork/papers/miller:cacm:1990/">miller:cacm:1990</a>]
- Fuzzing: Hack, art, and science [<a href="{{ site.baseurl }}/RelatedWork/papers/godefroid:cacm:2020/">godefroid:cacm:2020</a>]
- FUDGE: Fuzz driver generation at scale [<a href="{{ site.baseurl }}/RelatedWork/papers/babic:fse:2019/">babic:fse:2019</a>]
- The art, science, and engineering of fuzzing: A survey [<a href="{{ site.baseurl }}/RelatedWork/papers/manes:ieeetse:2019/">manes:ieeetse:2019</a>]
- Fuzzing: On the exponential cost of vulnerability discovery [<a href="{{ site.baseurl }}/RelatedWork/papers/bohme2:fse:2020/">bohme2:fse:2020</a>]
- Boosting fuzzer efficiency: An information theoretic perspective [<a href="{{ site.baseurl }}/RelatedWork/papers/bohme:fse:2020/">bohme:fse:2020</a>]
- Feedback-directed unit test generation for C/C++ using concolic execution [<a href="{{ site.baseurl }}/RelatedWork/papers/garg:icse:2013/">garg:icse:2013</a>]
- COASTAL: Combining concolic and fuzzing for Java (competition contribution) [<a href="{{ site.baseurl }}/RelatedWork/papers/visser:tacas:2020/">visser:tacas:2020</a>]


### Papers from the [2005 Bugs workshop](https://www.cs.umd.edu/~pugh/BugWorkshop05/)

- The soundness of bugs is what matters (position statement) [<a href="{{ site.baseurl }}/RelatedWork/papers/godefroid:bugs:2005/">godefroid:bugs:2005</a>]
- False positives over time: A problem in deploying static analysis tools [<a href="{{ site.baseurl }}/RelatedWork/papers/chou:bugs:2005/">chou:bugs:2005</a>]
- Issues in deploying software defect detection tools [<a href="{{ site.baseurl }}/RelatedWork/papers/cok:bugs:2005/">cok:bugs:2005</a>]
- Locating defects is uncertain [<a href="{{ site.baseurl }}/RelatedWork/papers/zeller:bugs:2005/">zeller:bugs:2005</a>]
- Soundness and its role in bug detection systems [<a href="{{ site.baseurl }}/RelatedWork/papers/xie:bugs:2005/">xie:bugs:2005</a>]


### [Property-based testing]

- QuickCheck: A lightweight tool for random testing of Haskell programs [<a href="{{ site.baseurl }}/RelatedWork/papers/claessen:icfp:2000/">claessen:icfp:2000</a>]
- DeepState: Symbolic unit testing for C and C++ [<a href="{{ site.baseurl }}/RelatedWork/papers/goodman:ndss:2018/">goodman:ndss:2018</a>]
- Parameterized unit tests [<a href="{{ site.baseurl }}/RelatedWork/papers/tillmann:fse:2005/">tillmann:fse:2005</a>]
- Test-case reduction via test-case generation: Insights from the Hypothesis reducer [<a href="{{ site.baseurl }}/RelatedWork/papers/maciver:ecoop:2020/">maciver:ecoop:2020</a>]


### [Test generation]

- Feedback-directed unit test generation for C/C++ using concolic execution [<a href="{{ site.baseurl }}/RelatedWork/papers/garg:icse:2013/">garg:icse:2013</a>]
- SUSHI: A test generator for programs with complex structured inputs [<a href="{{ site.baseurl }}/RelatedWork/papers/braione:icse:2018/">braione:icse:2018</a>]
- Study of integrating random and symbolic testing for object-oriented software [<a href="{{ site.baseurl }}/RelatedWork/papers/dimjasevic:ifm:2018/">dimjasevic:ifm:2018</a>]
- TestCov: Robust test-suite execution and coverage measurement [<a href="{{ site.baseurl }}/RelatedWork/papers/beyer:ase:2019/">beyer:ase:2019</a>]
- An introduction to test specification in FQL [<a href="{{ site.baseurl }}/RelatedWork/papers/holzer:hvc:2010/">holzer:hvc:2010</a>]
- FShell: Systematic test case generation for dynamic analysis and measurement [<a href="{{ site.baseurl }}/RelatedWork/papers/holzer:cav:2008/">holzer:cav:2008</a>]


### [Google]

- Lessons from building static analysis tools at Google [<a href="{{ site.baseurl }}/RelatedWork/papers/sadowski:cacm:2018/">sadowski:cacm:2018</a>]
- Modern code review: A case study at Google [<a href="{{ site.baseurl }}/RelatedWork/papers/sadowski:icse-seip:2018/">sadowski:icse-seip:2018</a>]
- Large-scale automated refactoring using ClangMR [<a href="{{ site.baseurl }}/RelatedWork/papers/wright:icsm:2013/">wright:icsm:2013</a>]
- Tricorder: Building a program analysis ecosystem [<a href="{{ site.baseurl }}/RelatedWork/papers/sadowski:icse:2015/">sadowski:icse:2015</a>]
- Why Google stores billions of lines of code in a single repository [<a href="{{ site.baseurl }}/RelatedWork/papers/potvin:cacm:2016/">potvin:cacm:2016</a>]
- Spanner: Google's globally distributed database [<a href="{{ site.baseurl }}/RelatedWork/papers/corbett:tocs:2013/">corbett:tocs:2013</a>]
- API usability at scale [<a href="{{ site.baseurl }}/RelatedWork/papers/macvean:ppig:2016/">macvean:ppig:2016</a>]


### Miscellaneous

- The human in formal methods [<a href="{{ site.baseurl }}/RelatedWork/papers/krishnamurthi:fm:2019/">krishnamurthi:fm:2019</a>]
- Relational test tables: A practical specification language for evolution and security [<a href="{{ site.baseurl }}/RelatedWork/papers/weigl:arxiv:2019/">weigl:arxiv:2019</a>]
- STARS: Rise and fall of minicomputers [scanning our past] [<a href="{{ site.baseurl }}/RelatedWork/papers/bell:procieee:2014/">bell:procieee:2014</a>]
- Bell's law for the birth and death of computer classes [<a href="{{ site.baseurl }}/RelatedWork/papers/bell:cacm:2008/">bell:cacm:2008</a>]
- StkTokens: Enforcing well-bracketed control flow and stack encapsulation using linear capabilities [<a href="{{ site.baseurl }}/RelatedWork/papers/skorstengaard:popl:2019/">skorstengaard:popl:2019</a>]
- Reasoning about a machine with local capabilities [<a href="{{ site.baseurl }}/RelatedWork/papers/skorstengaard:esop:2018/">skorstengaard:esop:2018</a>]
- A type system for expressive security policies [<a href="{{ site.baseurl }}/RelatedWork/papers/walker:popl:2000/">walker:popl:2000</a>]
- An abstract interpretation framework for refactoring with application to extract methods with contracts [<a href="{{ site.baseurl }}/RelatedWork/papers/cousot:oopsla:2012/">cousot:oopsla:2012</a>]
- The existence of refinement mappings [<a href="{{ site.baseurl }}/RelatedWork/papers/abadi:tcs:1991/">abadi:tcs:1991</a>]
- Boost the impact of continuous formal verification in industry [<a href="{{ site.baseurl }}/RelatedWork/papers/monteiro:arxiv:2019/">monteiro:arxiv:2019</a>]


## Reflections

Looking back over my research career, I wish that I had started writing paper summaries
for myself decades earlier.
Some of the benefits I have seen are:

- Writing the summaries turns the *passive* act of reading papers into an
  *active* act and it forces me to try harder to understand what I am writing about.

- When I introduce a new concept, I try to go back to all papers that relate to
  that concept and add links back to the concept.
  This strengthens my understanding of papers and helps me see different ways
  that papers and concepts connect to each other.

- When I am struggling to remember a paper, I can search the repository.
  This is especially useful when the title of the paper doesn't describe
  the content very well or when the part I remember is not the primary
  point of the paper.

- A few weeks ago, I wrote a workshop paper with other members of my team.
  Thanks to the summaries and the way I organize them, I had all of the related work
  available to me: I had a clear memory of it, I could find the papers, I
  could quickly remind myself what the paper was about to confirm that I was
  citing the correct paper.

  Another crucial ingredient was that my project planning documents explained
  the reason for the project, the design decisions, alternatives, etc.
  (These documents are not public.)

  I found the experience of writing the paper to be very productive and satisfying.
  It seemed to match the claims made
  about [ZettelKasten] as a way to organize your research into separate stages of

  - reading related work,
  - forming ideas (through the notes on concepts, the project planning documents, etc.),
  - collecting ideas into a paper,
  - and then, finally, reorganizing and rewriting to make a coherent paper.

  Since I had already done most of the work before we even thought about
  writing the paper, I was mostly able to focus on how to present the ideas
  without being distracted the earlier phases.

- When I summarize a paper, I also capture enough metadata that I can
  construct [BibTeX][bibfile] for all the papers.
  So, if I later cite the paper, I have already done the tedious work
  of finding the citation, finding a doi entry, etc. for all the papers that I cite.
  Again, this lets me focus on the act of writing without being distracted by
  the mechanics of BibTeX files.

  To make citing the papers as easy as possible, I try to make sure that this BibTeX is usable as is by correcting
  the capitalization of paper titles to overcome the
  [BiBTeX design bug](https://tex.stackexchange.com/questions/10772/bibtex-loses-capitals-when-creating-bbl-file).

  An unexpected side effect of using a machine-generated BibTeX file is that
  it is also easy to identify papers that my co-authors cite (so that I can read them too).

After trying this for a year, I am planning to continue the practice
and I would encourage others to do the same.
Whether you choose to make your reading list public or not is up to you.
On the plus side, you can share links with people when you mention a paper;
on the negative side, I am slightly more guarded/diplomatic about papers that
I have problems with.


### Other paper summaries

The focus of [RelatedWork] is on understanding a field so it is about a set of papers,
typically over an extended time period, their shared concepts and how they
interconnect.
Another paper summary site is Adrian Colyer's excellent "[the morning paper]."
Adrian reads a broad sweep of brand new papers to keep abreast of
a much larger subset of computer science.


### Software

The tools I use are just [Jekyll](https://jekyllrb.com/), [some python scripts](https://github.com/alastairreid/RelatedWork/tree/master/_scripts)
and an editor.
But people pointed out some other tools that might work better (most of which I have not tried).

- [The Archive](https://zettelkasten.de/the-archive/)
- [nvAlt](https://brettterpstra.com/projects/nvalt/) for Macs. (This is the tool that first got me hooked on Markdown)
- [Obsidian](https://obsidian.md/features)
- [Roam](https://roamresearch.com/)



---------------

[Information flow control]:   {{ site.baseurl }}/RelatedWork/notes/information-flow/
[Operating Systems]:          {{ site.baseurl }}/RelatedWork/topics/os/
[Verification tools]:         {{ site.baseurl }}/RelatedWork/topics/tools/
[Interactive theorem prover]: {{ site.baseurl }}/RelatedWork/notes/interactive-theorem-prover/
[Auto active verification]:   {{ site.baseurl }}/RelatedWork/notes/auto-active-verification/
[Abstract interpretation]:    {{ site.baseurl }}/RelatedWork/notes/abstract-interpretation/
[Model checking]:             {{ site.baseurl }}/RelatedWork/notes/model-checking/
[Bounded model checking]:     {{ site.baseurl }}/RelatedWork/notes/bounded-model-checking/
[Symbolic execution]:         {{ site.baseurl }}/RelatedWork/notes/symbolic-execution/
[Separation logic]:           {{ site.baseurl }}/RelatedWork/notes/separation-logic/
[Permission logic]:           {{ site.baseurl }}/RelatedWork/notes/permission-logic/
[The Rust language]:          {{ site.baseurl }}/RelatedWork/notes/rust-language/
[Survey papers]:              {{ site.baseurl }}/RelatedWork/notes/survey/
[Fuzz testing]:               {{ site.baseurl }}/RelatedWork/notes/fuzz-testing/
[Test generation]:            {{ site.baseurl }}/RelatedWork/notes/test-generation/
[SAT]:                        {{ site.baseurl }}/RelatedWork/notes/sat-solver/
[SMT]:                        {{ site.baseurl }}/RelatedWork/notes/smt-solver/
[ISA specification]:          {{ site.baseurl }}/RelatedWork/notes/isa-specification/
[Property-based testing]:     {{ site.baseurl }}/RelatedWork/notes/property-based-testing/
[Google]:                     {{ site.baseurl }}/RelatedWork/notes/google/

[leaving Arm]:                {% post_url 2019-08-30-farewell-to-arm %}
[joining Google]:             {% post_url 2019-11-02-joining-google %}
[RelatedWork]:                {{ site.baseurl }}/RelatedWork
[bibfile]:                    {{ site.baseurl }}/RelatedWork/RelatedWork.bib
[papers]:                     {{ site.baseurl }}/RelatedWork/papers
[notes]:                      {{ site.baseurl }}/RelatedWork/notes

[the morning paper]:          https://blog.acolyer.org
[Zettelkasten]:               https://zettelkasten.de/posts/zettelkasten-improves-thinking-writing
