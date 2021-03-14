---
layout: post
title: Finding Bugs versus Proving Absence of Bugs
---

![ARM logo]({{ site.baseurl }}/images/ARM_logo.svg){: style="float: left; width: 10%; padding: 1%"}
Probably the most important thing I didn't say enough in [my paper about
verifying ARM processors]({{ site.url }}/papers/CAV_16/)
is why we focus on finding bugs.

As John Regehr says in his talk [SQL-Lite with a Fine-Tooth
Comb](https://lipn.univ-paris13.fr/~petrucci/OSIS-Secu-2016/videos/04.mp4), you
don't want to waste time trying to show that a buggy program is bug-free
because dealing with bugs is a major distraction from trying to show that there
are no bugs.  So if you are verifying a processor, you should think of having
two distinct phases with different goals:

* Finding as many bugs as you can.  During this phase, you use as many
techniques as you can to find bugs.

* Proving that there are no bugs.  During this phase, you focus on proving
correctness.

ISA-Formal focusses on that first phase and it is very effective at catching
complex bugs in the processor pipeline.  And it is just one of several
techniques we use.  We use more traditional techniques on the processor
pipeline in parallel with ISA-Formal and we use other techniques for the
floating point unit, for the memory system, etc.

Another important factor is that finding bugs is easy to measure and fits well
into conventional project planning.  This is important when you are trying to
get a new verification technique adopted: you can try to show that it catches
more bugs earlier or with less effort than other techniques.  And it is also
important when you are trying to decide whether you are done: you are done when
the bug curve flattens off.

The third reason is that we have been using the model checker in a bug-finding
mode which is optimized for breadth-first exploration of the search space but
does not attempt to find invariants.  As a result, our usual mode of running
cannot hope to prove absence of bugs because it only goes a finite number of
cycles deep.

So, for now, we are focussing on finding bugs.

---

_This is the first of several notes I am writing about the key ideas in our
paper ["End-to-End Verification of ARM Processors with ISA-Formal"]({{ site.url
}}/papers/CAV_16/) which I am presenting at the [2016
International Conference on Computer Aided
Verification](http://i-cav.org/2016/) on Friday 22nd July.  There is nothing
quite like trying to squeeze a 16 page paper into a 16 minute presentation for
figuring out what the important messages are and how to present them._
