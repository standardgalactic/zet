---
layout: post
title: Farewell to Arm
---

After [15 great years at Arm](/about#arm-ltd-projects-selected), I’m making a change.
![Farewell to Arms ><](/images/farewell_to_arms.png)

I have learned about how processors work,
how they are designed and
[how they are verified]({{ site.url }}/papers/CAV_16/).
I have learned about [how architectures are designed](/papers/IEEE_Micro/)
and how hard it is to change things you get wrong.

I have learned how you nurture the tools and software ecosystem, where you
compete and where you choose to let others build their businesses.
I have worked in a company that aims to “be Switzerland”,
and watched the internal dismay and rapid correction the one time we
deviated from that.

I have worked on
[compilers](/papers/CASES_08/),
runtimes,
[vector architecture](/about#vectorizing-compiler-for-neon),
[VLIW](/papers/MICRO_08/),
parallelism,
[software defined radio](/about#software-defined-radio),
DSP,
trace,
[formal verification](/about#processor-formal-verification)
and
security.

And today is my last day at Arm.

I will miss the people I worked with and working on the most widely deployed
processor architecture in the world.

But I am looking forward to what is next.

---------------

When I posted the above to Twitter, I got a bunch of questions.
So here are some answers:

* Arm has teams in place to carry on some of the work I have done there:
  [creating and testing formal architecture specifications]({{ site.url }}/papers/FMCAD_16/);
  and
  [formal validation of processors against these formal specifications]({{ site.url }}/papers/CAV_16/).

  These teams have actually owned this work for several years.
  That is a commmon pattern in industrial research: if a project is successful,
  teams grow to strengthen, maintain and extend the project and
  the people that created it gradually move on to other things.

* Over the last three years or so, I have spent about half of my time
  worrying about what would happen if Arm committed to using formal processor
  specs to generate everything.
  This would remove a lot of the redundancy in the specification development
  process: no second model to compare against, less experience/skill needed
  to create tests, simulators, documentation, etc.
  (My ["Who guards the guards?"]({{ site.url }}/papers/OOPSLA_17/)
  paper and my recent blog posts are part of what came out of that.)

* I do know where I will be working next.

  The next job will involve formal specification and verification.  But, first,
  I have a nice period of "funemployment" to decompress and catch up before
  I start.

