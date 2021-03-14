---
layout: post
title: Using SMT to check specifications for errors
---

![ARM logo]({{ site.baseurl }}/images/ARM_logo.svg){: style="float: left; width: 10%; padding: 1%"}
SMT solvers are incredibly flexible tools for analyzing complex systems.  In
[my previous post]({{ site.baseurl }}{% post_url 2019-02-02-tracing-smt %}),
I showed how you can: generate a symbolic execution trace from running an
instrumented interpreter on some input values;  turn the trace into an SMT
circuit; and use an SMT solver to check that the SMT circuit matches
your original trace.
This post will explore how we can check assertions, array index bounds, etc.
to find bugs in the specification and how we can enumerate all the paths
through a specification.


## Checking assertions

The "AddWithCarry" function that I am using as my running example does not
contain any assertions --- but it does contain this line

    result = unsigned_sum[0 +: N]; // same value as signed_sum[0 +: N]

So, for the sake of continuing the example, let's turn that comment into an
assertion

    assert unsigned_sum[0 +: N] == signed_sum[0 +: N];

In the execution trace, this will generate something like this:

    %14 = getslice_bits(0, 32, %8)
    %t15 = getslice_bits(0, 32, %13)
    %t16 = eq_bits(%14, %t15)
    assert %t17 "functions/AddWithCarry.asl" 8

Saying that line 8 of file "functions/AddWithCarry.asl" asserts that condition `%t16`
holds.
As we are translating the trace to SMT, we can generate a metadata file
that contains information about this assertion:

    AWC.json:
        {
            "assertions" : [
                ("t17", "functions/AddWithCarry.asl", 8)
            ]
        }

We can use this list of assertions to check that the assertions all hold for
all possible inputs that follow the same path

    ; only consider inputs that lead to this path
    (assert (not v16))
    (assert v19)

    ; check for any input that causes the assertion to fail
    (assert (not t17))

When we run z3 on this check, it can't find any failing inputs

    $ z3 t2.smt
    unsat

This is good news: it means that the comment is actually true!


### Implicit assertions

Of course, programs have lots of implicit assertions too:

- array indexes must be in bounds
- bitslice indexes must be in bounds
- bitslices must have a non-negative width
- division by zero is not allowed

For each of these, we can add checks to check for failures.
For example, given the expression `x[N-1]`, we will generate 
a check that `0 <= N-1 < N`.
This is going to result in a lot of checks --- many of which will trivially
pass.  But SMT solvers are very efficient at dealing with trivial checks like
this so let's just go ahead and spray the code with checks like this, use Z3 to
check them all and then, once we know that they all pass we could generate
a fresh SMT file that omits the checks.  (Or maybe we just leave them in?)


## Finding other paths

So far, all we are doing is exploring one path at a time.
So we have checked that an assertion does not fail on one
path but that does not guarantee that it does not fail on
any of the other paths that may exist.

This series of threads is focussed on _concolic execution_ where we generate
a symbolic execution trace by executing an instrumented interpreter on some
concrete input values.  On the running example from the previous post, the
trace recorded that it hit two conditional branches

    branch %16 = FALSE
    branch %19 = TRUE

The trace is only valid for inputs that would take the same path
so I added these assertions to restrict execution to the same path through
the code.

    (assert (not v16))
    (assert v19)

More generally, I might have a long list of branches b1, b2, b3, ... bm.  And
what I want to do is to explore paths that differ in at least one of these
conditions.  So I am going to use the SMT solver to try to find several
different branch condition sequences:

    !b1
    b1, !b2
    b1, b2, !b3
    ...
    b1, b2, b3, ... !bm

On my running example, this gives me two sets of assertions to try:

    (assert v16)

and

    (assert (not v16))
    (assert (not v19))

Running with these two sets of assertions generates two sets of input values

    #xfffffffe #x00000001 #b0
    #xb9d1fe83 #xc60f00ff #b1

Once we have these values, we can rerun the interpreter to generate new traces
and then we can repeat the process of generating alternative branch sequences
to generate traces for alternative paths through the function under test.
It's not long before this finds a fourth (final) path through the function
and an input value that can trigger it.

    #x7bfbff67 #x0403fe96 #b0


## Going further

Checking assertions, indexes, etc. is good --- but we can go further.
An obvious thing to do is to try to write down any invariants that you
expect to hold about the overall processor state.
Another option is to scour the natural language part of the
specification looking for more properties we can check.
I wrote a couple of posts about doing that
[here]({{ site.baseurl }}{% post_url 2017-08-19-natural-specs %})
and [here]({{ site.baseurl }}{% post_url 2017-09-24-validating-specs %})
and I wrote [a paper]({{ site.url }}/papers/OOPSLA_17/) about it.


### Related posts and papers

* Paper: [End-to-End Verification of ARM Processors with ISA-Formal]({{ site.url }}/papers/CAV_16/), CAV 2016.
* [Verifying against the official ARM specification]({{ site.baseurl }}{% post_url 2016-07-26-using-armarm %})
* [Finding Bugs versus Proving Absence of Bugs]({{ site.baseurl }}{% post_url 2016-07-18-finding-bugs %})
* [Limitations of ISA-Formal]({{ site.baseurl }}{% post_url 2016-07-30-isa-formal-limitations %})
* Paper: [Trustworthy Specifications of ARM v8-A and v8-M System Level Architecture]({{ site.url }}/papers/FMCAD_16/), FMCAD 2016.
* [ARM's ASL Specification Language]({{ site.baseurl }}{% post_url 2016-08-17-specification_languages %})
* [ARM Releases Machine Readable Architecture Specification]({{ site.baseurl }}{% post_url 2017-04-20-ARM-v8a-xml-release %})
* [Dissecting the ARM Machine Readable Architecture files]({{ site.baseurl }}{% post_url 2017-04-29-dissecting-ARM-MRA %})
* Code: [MRA Tools](https://github.com/alastairreid/mra_tools)
* [ASL Lexical Syntax]({{ site.baseurl }}{% post_url 2017-05-07-asl-lexical-syntax %})
* [Arm v8.3 Machine Readable Specifications]({{ site.baseurl }}{% post_url 2017-07-31-arm-v8_3 %})
* Paper: [Who guards the guards?  Formal Validation of the Arm v8-M Architecture Specification]({{ site.url }}/papers/OOPSLA_17/)), OOPSLA 2017.
* [Are Natural Language Specifications Useful?]({{ site.baseurl }}{% post_url 2017-08-19-natural-specs %})
* [Formal validation of the Arm v8-M specification]({{ site.baseurl }}{% post_url 2017-09-24-validating-specs %})
* [Bidirectional ARM Assembly Syntax Specifications]({{ site.baseurl }}{% post_url 2017-12-24-bidirectional-assemblers %})
* Talk: [[How can you trust formally verified software (pdf)](/talks/using-arm-specs-34C3-2017-12-27.pdf)], Chaos Communication Congress, 2017.
* This series (part 1): [Generating SMT from traces]({{ site.baseurl }}{% post_url 2019-02-02-tracing-smt %})
* This series (part 2): [Using SMT to check specifications for errors]({{ site.baseurl }}{% post_url 2019-02-09-tracing-smt2 %})
* This series (part 3): [Generating multiple solutions with SMT]({{ site.baseurl }}{% post_url 2019-02-17-tracing-smt3 %})
