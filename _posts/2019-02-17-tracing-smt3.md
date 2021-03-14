---
layout: post
title: Generating multiple solutions with SMT
---

![ARM logo]({{ site.baseurl }}/images/ARM_logo.svg){: style="float: left; width: 10%; padding: 1%"}
You can use an SMT solver to find a solution to a set of constraints.
But what happens if you want to find multiple solutions?
My previous posts in this series have looked at
[how you can turn execution traces into SMT problems]({{ site.baseurl }}{% post_url 2019-02-02-tracing-smt %})
and at how you can
[use an SMT solver to enumerate all paths through a specification]({{ site.baseurl }}{% post_url 2019-02-09-tracing-smt2 %}).
In this post, I'll look at how you can generate multiple inputs that will
trigger each path.
This can be useful if you are trying to generate testcases although it is good
for other things too.

_(This post was inspired by a visit to John Regehr in early January where we talked about
[solving synthesis problems](https://blog.regehr.org/archives/1636)
for which it is very useful to generate multiple solutions to a set of
constraints.
John and I implemented several variations on the ideas in this post and John
encouraged me to post about it --- which was the inspiration for this entire
series of posts.)_


## Finding other input values

In 
[my previous post]({{ site.baseurl }}{% post_url 2019-02-02-tracing-smt %}),
we ran a function with some concrete values, generated an SMT script and
then used the SMT solver to confirm that it produced the same output
if it starts with the same concrete values.

Let's now use the SMT solver to find other input values that follow the same
path through the code.
To do that, we need to add some assertions that constrain each branch in the
trace.

    ; SMT generated from trace omitted (see part 1)

    (assert (not v16))
    (assert v19)

    (check-sat)
    (get-value (input.x))
    (get-value (input.y))
    (get-value (input.carry_in))

Rerunning Z3 produces this output:

    $ z3 t3.smt2
    sat
    ((input.x #x7fffffff))
    ((input.y #x80000000))
    ((input.carry_in #b1))

If we would like some different solutions, we can add assertions to get Z3 to
produce different solutions.

    (assert (not (= input.x #x7fffffff)))

Which leads to another solution:

    $ z3 t3.smt2
    sat
    ((input.x #x7ffffffe))
    ((input.y #x80000001))
    ((input.carry_in #b1))

So we add another assertion

    (assert (not (= input.x #x7ffffffe)))

and we get another solution

    $ z3 t3.smt2
    sat
    ((input.x #x7ffffffd))
    ((input.y #x80000002))
    ((input.carry_in #b1))

But, these different solutions seem to be tightly clustered: #x7fffffff, #x7ffffffe,
 #x7ffffffd, ...
Can we generate solutions that are less tightly clustered?


## Generating less clustered solutions

Instead of just asking for a different solution, we want to ask for a solution
that is "far away" from the previous solution.  One way of doing this is to
apply a hash function to the input values and then solve for inputs that hash
to different values.
There are lots of hash functions we could use but a [universal hash
function](https://en.wikipedia.org/wiki/Universal_hashing#Hashing_vectors)
seems like a good choice.
A common hash function for bit-vectors is to pick half the bits and xor them
all together.
But I am feeling lazy so I will write a few hash functions based on 3 of the
bits --- just pretend that there are 32 bits there and that they were chosen
at random.

    (define-const input (_ BitVec 65)
        (concat (concat input.x input.y) input.carry_in))

    ; todo: these hashes are a bit small
    ; should sample around 32 bits
    (define-const hash0 (_ BitVec 1)
        (bvxor (bvxor
            ((_ extract 0 0) input)
            ((_ extract 24 24) input))
            ((_ extract 49 49) input))
    )

    (define-const hash1 (_ BitVec 1)
        (bvxor (bvxor
            ((_ extract 2 2) input)
            ((_ extract 16 16) input))
            ((_ extract 57 57) input))
    )

    (define-const hash2 (_ BitVec 1)
        (bvxor (bvxor
            ((_ extract 13 13) input)
            ((_ extract 17 17) input))
            ((_ extract 52 52) input))
    )

    (define-const hash3 (_ BitVec 1)
        (bvxor (bvxor
            ((_ extract 23 23) input)
            ((_ extract 27 27) input))
            ((_ extract 42 42) input))
    )

    (define-const hash (_ BitVec 4)
        (concat (concat hash0 hash1) (concat hash2 hash3)))

    (check-sat)
    (get-value (input.x))
    (get-value (input.y))
    (get-value (input.carry_in))
    (get-value (hash))

When we rerun the SMT solver now, it produces the original solution and displays
the hash value

    $ z3 t4.smt2
    sat
    ((input.x #x7fffffff))
    ((input.y #x80000000))
    ((input.carry_in #b1))
    ((hash #x7))

Now to generate a new input, all we need to do is require a solution that
hashes to a different value

    (assert (not (= hash #x7)))

Which produces this much more random-looking input

    $ z3 t4.smt2
    sat
    ((input.x #x7fbe6dfd))
    ((input.y #x80419202))
    ((input.carry_in #b1))
    ((hash #xf))

    (assert (not (= hash #x7)))

Which produces this much more random-looking input.
So let's keep going and add another assertion:

    (assert (not (= hash #x7)))
    (assert (not (= hash #xf)))

Which produces this solution

    result: #xfffeefff #xffffcfff #b0    hash: #xd

If we keep going like this and add constraints to prevent repetition of
previously seen hash values, we can keep on generating solutions

    result: #x7fffffff #x80000000 #b1    hash: #x7
    result: #x7fbe6dfd #x80419202 #b1    hash: #xf
    result: #xfffeefff #xffffcfff #b0    hash: #xd
    result: #x7fd5be6b #x802a4194 #b1    hash: #x5
    ...

Of course, it is a bit tedious adding assertions one by one --- so you
will want to write a script to automate all this.
And you will also want to generate better hash functions.
And you will want to run multiple times using different hash functions
each time.
You might also want to experiment with other hash functions such as "popcount",
"(a\*x + b) mod p", etc.


## Using our solutions

So now we have a bunch of different solutions, what can we do with them?

The most obvious thing we can do with these extra solutions is to use them to
test the tools for generating SMT from execution traces.

But even more important is to use them to test other tools: simulators, processors, etc.
Get as many different processors, simulators, specifications, etc. as you can
and check that they all agree on the behaviour of each instruction.
To do this, you will need to add a few more things:

1. Instead of generating traces from the "AddWithCarry" function, you
   need to generate traces from the "ADC" instruction.
2. To test processors, etc., you need to generate assembly language
   sequences that initialize the processor to the desired input state,
   run the instruction, and test the final values of the registers.


## Generating uniformly distributed solutions

From the examples above, you can see that the solutions being generated have
no obvious pattern.  And, for most purposes, that is all you need.
But, if you are generating tests, you might want something better: inputs
that are uniformly distributed across the input space.

I am not going to go through this in detail but, if you want to follow this up,
you might want to look at these
[slides by Moshe Vardi about uniform random
sampling](https://www.cs.rice.edu/~vardi/papers/cav16tk.pdf)
or read this 
[paper by Chakraborty, Meel and Vardi about Uniform generation of solutions](https://www.cs.rice.edu/~vardi/papers/cav13.pdf).


## Summary

The first part of this series looked at how I can translate execution
traces into SMT constraints for use with SMT solvers.
In this post, I tried to generate multiple solutions for the SMT constraints
but, disappointingly the solutions were quite tightly clustered.
To fix this, I made up some random hash functions and used those to generate
more solutions --- each solution hashing to a different value.
By choosing enough hash functions, we can generate as many different solutions
as we wish.




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


