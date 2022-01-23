---
layout: post
title: What is RVT?
---

![Rust logo](https://www.rust-lang.org/static/images/rust-logo-blk.svg){: style="float: left; width: 10%; padding: 1%"}
The goal of our Rust Verification project is to help programmers be more
productive using tools and techniques derived from the formal verification community.
We wrote about this in the paper "[Towards making formal methods normal: meeting developers where they are][HATRA 2020]"
and I described it recently in the [Building Better Systems podcast][podcast] but
I think there's a few things that did not come over clearly in those.

- The project is primarily a usability project.
  This is not always obvious because we have spent most of the last year
  working on tools and (for reasons), the project is called "Rust Verification Tools"
  but we are only working on tools because the tools we need
  don't already exist.

- Our focus is on the cost-benefit ratio of using formal tools.

    - On the benefit side, our focus is on what hardware designers call "Shift Left": reducing costs
      by finding bugs early.
      Software engineering 101 teaches us that the longer a bug sits in your
      codebase, the more it costs to fix it.
      If we can find the bugs early, we can save costs.

    - On the cost side, our focus is on reducing the cost of verification:
      we want to minimize the amount of specification you need to write,
      the amount of annotation you need to add to your code, etc.
      If we want to make developers more productive, we need to pay attention
      to the cost-benefit ratio.

- We are *not* focused on correctness: it is about making developers more
  productive at achieving their existing quality goals.

  We think that this goal will make it easier to get a sufficiently
  high cost-benefit ration than focusing on correctness.
  In particular, most code does not have a specification and we
  do not think that is likely to change.

- We want to be able to use a wide variety of tools:
  bounded model checkers,
  abstract interpreters,
  symbolic execution,
  fuzzers,
  hybrid tools that combine multiple techniques,
  etc.

  We have mostly been working with [KLEE] because it is a robust,
  well-maintained, feature-rich tool.
  But we have also tried
  [SeaHorn],
  [Crux-MIR],
  RMC
  and MIRAI.

  Being able to easily switch from one tool to another makes it
  easier to use the right tool for a given piece of code,
  or a given property.

- One of the early inspirations for the project was Google's [OSS Fuzz]
  which helps and encourages developers of common open source software
  to add fuzzing harnesses to their projects.

  If we can find a way to make verification easy and effective enough, then
  maybe we could create an "OSS-Verify" program?
  (Note that this is just a dream - but we think it is a nice dream to have!)

- Some of the main risks we worried about in the project are

  - How much of the Rust language are different tools able to accept?

    We don't know any tools that support reasoning about concurrent code
    at the moment. This is a problem given the "fearless concurrency"
    tagline.

  - Can tools handle realistic sizes of code?

    Even if your program is small, its dependencies often pull in a lot of
    other crates.
    The two main ways of dealing with this are to create a specification
    of each crate and verify it separately
    or to verify the entire program and all of its dependencies.
    Even if verification is free, creating specifications for each
    crate increases the costs so we would prefer tools that can handle
    large amounts of code at once.

  - Can we split program verification tasks into many small sub-tasks
    that can be separately verified and verified in parallel.

  - Can we really create a continuum of verification tools or
    are the differences between bounded model checking,
    symbolic execution, etc. to big to overcome?










[HATRA 2020]:                     {{site.baseurl}}/papers/HATRA_20/
[podcast]: https://www.youtube.com/watch?v=yXEVO-26eC8
[OSS Fuzz]: https://google.github.io/oss-fuzz/
[KLEE]:                           https://klee.github.io/
[Crux-MIR]:                       https://github.com/GaloisInc/mir-verifier/
[SeaHorn]:                        https://seahorn.github.io/

*[This post was originally posted as part of the [Rust verification project]({{site.RVTurl}}/)]*
