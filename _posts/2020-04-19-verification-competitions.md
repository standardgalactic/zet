---
title: Verification Competitions
layout: post
---

Since [joining Google]({{ site.baseurl }}{% post_url 2019-11-02-joining-google %})
in September, I have spent a lot of time
[reading about software verification tools]({{ site.baseurl }}/RelatedWork/)
and one of the things that keeps coming up is that
there are competitions between different verification tools.

These competitions are interesting for several reasons

1. You can see which tools can solve the most problems
   in the least amount of time in graphs like this
   graph from the [SV-COMP 2020] competition.

   ![cactus plot for SV-COMP overflow verification results](https://sv-comp.sosy-lab.org/2020/results/results-verified/quantilePlot-NoOverflows.svg)

   Each curve shows how many problems were solved by a given tool
   in a particular amount of time.  So the winner is the tool that
   goes furthest to the right (solves more problems) and is lower
   (takes less time to solve them).
   Most curves end with a near vertical line where they are not able to
   solve any more problems no matter how much more time you give them.

2. The categories on which the tools are evaluated give you some idea
   of what tools entering this competition are good at.

   For example, the [categories in the SV-COMP
   competition](https://sv-comp.sosy-lab.org/2020/benchmarks.php)
   are
   - ReachSafety: is it possible to reach some part of the code?
     In particular, this is often used to show that it is impossible
     to fail an assertion or call some error function.
   - MemSafety: is malloc/free used correctly and are there any space
     leaks?
   - Overflow: do any signed integer arithmetic operations cause overflow?
     (In C, it is not an error for unsigned integers to overflow.)
   - Termination: does the program terminate?
   - SoftwareSystems: are some of the above properties but applied to
     real world software from busybox, Linux drivers, OpenBSD and SQLite.

   So, very quickly, you get an idea on what this class of tools is
   able to help you with.

3. You can learn about new, actively developed tools by looking at the
   list of entrants.
   Before I looked at the above graph, I know about CBMC but, straight away,
   I know about ten more tools and I can quickly see the top few tools and
   how they stack up on different problem classes.

4. It encourages tools to adopt a standard interface so that they can
   take part in the competition.

5. It helps drive progress in the field because instead of just
   claiming that some technique lets you solve more problems or
   solve problems more quickly, you are now expected to show it
   by reporting your performance on these benchmarks.

6. To turn prototypes into mature tools.
   For example, to enter SV-COMP, you have to be able to cope with a large
   part of the C language, not just a subset.

[Martin Nyx Brain](https://www.city.ac.uk/people/academics/martin-nyx-brain)
has written
[an explanation of how these competitions are organized](http://www.sc-square.org/CSA/workshop2-papers/RP3-FinalVersion.pdf).

Here is a list of all the verification competitions that I have been able to find.
Some of the competitions have particular input formats or output formats that
are interesting so I listed them as well.
For example, the SAT competition became concerned about bugs in verifiers
skewing the result so they have adopted the DRAT output format that
allows external tools to check any UNSAT results.

In addition, I found a paper that gives an overview of competitions:
[TOOLympics 2019: An Overview of Competitions in Formal Methods](https://link.springer.com/chapter/10.1007/978-3-030-17502-3_1)
([pdf](https://www.sosy-lab.org/research/pub/2019-TACAS.TOOLympics_2019_An_Overview_of_Competitions_in_Formal_Methods.pdf))


|----------------------------|----------------|---------------|
| Competition                | Input format   | Output format |
|----------------------------|----------------|---------------|
| [SAT Competition](http://www.satcompetition.org) | [DIMACS](http://www.satcompetition.org/2009/format-benchmarks2009.html) | [DRAT](https://satcompetition.github.io/2020/certificates.html) |
| [SMT Competition](https://boolector.github.io/smt-comp.html) | [SMT-LIB](http://smtlib.cs.uiowa.edu) | |
| [Hardware Model Checking competition](http://fmv.jku.at/hwmcc19/) | [BTOR2](https://github.com/Boolector/btor2tools), [AIGER](http://fmv.jku.at/aiger/) | |
| [Competition on Software Verification (SV-COMP)](https://sv-comp.sosy-lab.org/2020/)  | | |
| [MaxSAT](https://maxsat-evaluations.github.io) | | |
| [Pseudo-Boolean Competition](http://www.cril.univ-artois.fr/PB16/) | | |
| [Quantified boolean formula (QBF) evaluation](http://www.qbflib.org/index_eval.php) | | |
| [Constraint Satisfaction](http://xcsp.org/competition) | [XCSP](http://xcsp.org/) | |
| [MiniZinc challenge](https://www.minizinc.org/challenge2017/call_for_problems.html) | [MiniZinc](https://www.minizinc.org) | |
| [Termination competition](http://termination-portal.org/wiki/Termination_Competition) | | |
| [Tableaux and non-classical system comparision](http://www.cs.man.ac.uk/~schmidt/mspass/problems.html) | | 
| [World championship for automated theorem proving](http://www.tptp.org/CASC/)  | | |
| [Answer Set Programming challenge](https://sites.google.com/view/aspcomp2019/) | | |
| [Reactive sythesis competition](http://www.syntcomp.org) | LTL, TLSF, AIGER, HOA | |
| [Syntax Guided Synthesis (SyGuS)](https://sygus.org) | [SyGuS-IF](https://sygus.org/language/) | |
|----------------------------|----------------|----------------|

In addition to these tool competitions, there are also contests that pit teams
of users against each other.
So these competitions test both the skills of the participants and
the power/flexibility of their tools.


|----------------------------|-------|
| Contests                   | Tool  |
|----------------------------|-------|
| [VerifyThis]               | Any Auto-active theorem prover |
| [Proof Ground interactive proving contest](https://www21.in.tum.de/~wimmers/proofground/) | Any Interactive theorem prover |
| [Proving for fun](https://competition.isabelle.systems) | Isabelle |
|----------------------------|-------|

If you know of any other competitions, please DM me [on
twitter](https://www.twitter.com/alastair_d_reid)
or send me [an email](mailto:adreid@google.com).

---------------

*Acknowledgements for pointing me at some of the above*:
Claire Wolf,
John Regehr,
Hernan Ponce De Leon,
Martin Nyx Brain,
SidiMohamed Beillahi.


[Coq]: https://coq.inria.fr
[CBMC]: https://github.com/diffblue/cbmc
[CVC4]: https://cvc4.github.io
[Dafny]: http://research.microsoft.com/dafny
[ESC]: https://en.wikipedia.org/wiki/Extended_static_checking
[Facebook Infer]: https://fbinfer.com
[Frama-C]: https://frama-c.com
[HOL]: https://hol-theorem-prover.org
[Isabelle]: https://isabelle.in.tum.de
[KLEE]: https://klee.github.io
[SAGE]: https://queue.acm.org/detail.cfm?id=2094081
[Serval]: https://unsat.cs.washington.edu/projects/serval/
[SMACK]: https://smackers.github.io
[VCC]: https://www.microsoft.com/en-us/research/project/vcc-a-verifier-for-concurrent-c/
[VeriFast]: https://github.com/verifast/verifast
[Viper]: https://www.pm.inf.ethz.ch/research/viper.html
[Z3]: https://github.com/Z3Prover/z3

[SMT-LIB]: http://smtlib.cs.uiowa.edu
[SV-COMP 2020]: https://sv-comp.sosy-lab.org/2020/
[VerifyThis]: https://www.pm.inf.ethz.ch/research/verifythis.html

