---
layout: post
title: Are natural language specifications useful?
---

In my efforts to create a formal specification of the Arm architecture, I have
focussed on the parts written in "pseudocode".  I have  reverse engineered [the
ASL language hiding inside the pseudocode]({{ site.baseurl }}{% post_url
2016-08-17-specification_languages %}) to create a formal, executable
specification that I can execute and test.  In the process, I have tended to
ignore all the natural language prose that makes up the bulk of the 6,000 page
Arm Architecture Reference Manual.  In defiance of [Betteridge's
Law](https://en.wikipedia.org/wiki/Betteridge%27s_law_of_headlines), this
article is going to explain how I finally found a use for all that prose.

(This post is based on some of the ideas in my forthcoming OOPSLA 2017 paper
["Who guards the guards?  Formal Validation of the Arm v8-M Architecture
Specification"]({{ site.url }}/papers/oopsla2017-whoguardstheguards.pdf).)

# A thought experiment

Suppose that last year I did a really careful audit of the architecture
specification and checked that every privileged register had an appropriate
check preventing access from unprivileged code.  I find a couple of
minor problems in the architecture specification and fix them; I worry that
these problems had not been caught by the tests we run on processors (and also
on the architecture spec) so I get the test team to write extra tests; and I
worry that the formal verification team had also missed these problems so I
work with them to update the formal testbench.  With that all taken care of, I
congratulate myself on making the specification that little bit better and
for taking the extra care required to get the fixes into the verification
frameworks.  I celebrate with a tall glass of ginger ale.

Now, this year, I have a new task: adding a really cool set of instructions
that greatly increases performance.  With all my focus on achieving performance
improvements, I don't notice that one of the new instructions
can read one of those privileged registers, even if the processor is in
unprivileged mode.

Since I went that extra mile last year to get the tests improved, I might
hope that those tests would catch this mistake.  Alas, the test suite
only checks the instructions that existed last year, not the new instructions
I just added so those tests and even the improved formal testbench cannot
catch my mistake.

This limitation of our testing methods to only checking backwards compatibility
is the kind of thing that keeps me up at night.  I started wondering whether
there was anything I could do to prevent it from happening?


# Specifying architectural intent

The problem is that the ASL specification that I work with is not good at
specifying "architectural intent."  The architect's intention was that a privileged register
"R" could not be accessed in unprivileged mode but the way that the
specification ensures this property is by adding a suitable check in every
place that accesses that register.  If someone else were to examine the
specification closely, they could  see that the checks are always performed
before accesses to "R" and might guess that "R" is meant to be privileged.  But
that intention is not part of the ASL specification that I write so there is no
way to see when I break it.

While pondering this problem, I realized that the natural language part of the
Arm architecture specification held part of the answer to the problem.  Some
parts of the natural language specification simply replicate information
written in ASL and is therefore not very useful but some parts of the natural
language specification describe overall properties of the specification such
as invariants.  So all I have to do is sift through the specification looking
for these statements of architectural intent.

For my first attempt at this,  I decided to bypass the 6,000 page v8-A
specification, and focus on the 1,200 page v8-M specification.  Even that felt
like too much so I decided to focus on the 50 pages that describe the v8-M
exception/interrupt and security mechanisms: a much more feasible task.

What I found was that the v8-M architecture specification had been written
in a more structured way than the v8-A spec.  It consists of a series of
short labelled statements such as:

    JRJC: Exit from lockup is by any of the following:
    - A Cold reset.
    - A Warm reset.
    - Entry to Debug state.
    - Preemption by a higher priority exception.

Without trying to explain what the terminology in that rule means, you can
hopefully see that this is not too bad as a specification.  It is clear what it
means.  It is falsifiable.  And, crucially, it is stating something about the
specification as a whole (there is no other way to exit lockup) so it is
capturing some of the architectural intent that is missing from the ASL.

The only problem is that even though they use a much more structured
style of English, I still don't have a formal semantics for rules written
in this style.
So I started playing around with some syntax that I could parse and
assign a meaning to.  What I came up with is this:

    rule JRJC
        assume Fell(LockedUp);
        Called(TakeColdReset)
        || Called(TakeReset)
        || Rose(Halted)
        || Called(ExceptionEntry);

What this says is that if, at any step, we assume that the "LockedUp" variable
fell (from TRUE to FALSE) then one of the following must be true:

* the specification must have called the function "TakeColdReset";
* the specification must have called the function "TakeReset";
* the "Halted" variable (that indicates that we are in Debug state) must rise
  (from FALSE to TRUE); or
* an exception must be taken.

The formalisation has the same structure and similar terminology to the English
prose so, if you have a bit of an understanding of the terminology of the
architecture and the structure of the specification, you can put them side by
side with each other and see that they are basically saying the same thing.
(Some people would describe them as being "eyeball close".)

Encouraged by this example, I started mining the specification for
more rules that I could formalize.  More typical was my experience
with this rule:

    rule VGNW: Entry to lockup from an exception causes:
        * Any Fault Status Registers associated with the
          exception to be updated.
        * No update to the exception state, pending or active.
        * The PC to be set to 0xEFFFFFFE.
        * EPSR.IT to be become UNKNOWN.
        In addition, HFSR.FORCED is not set to 1.

The first three bullets are easy enough to formalize.  The fourth bullet is
tricky because it basically says that "EPSR.IT" can be assigned any value;
this is not a falsifiable statement because one possibility is that EPSR.IT is
unchanged.  The final line was a bit of a puzzle since I could think of two
incompatible interpretations --- I decided to try them both.

    rule VGNW
        assume Rose(LockedUp);
        property a  HaveMainExt() ==> CFSR != 0;
        property b1 Stable(ExnPending);
        property b2 Stable(ExnActive);
        property c  PC == 0xEFFF_FFFE;
        property e1 HFSR.FORCED == '0';
        property e2 Stable(HFSR.FORCED);

When I checked which of these were actually true, only properties (a) and (e2)
passed the test.

* Properties (b1) and (b2) had been true about the v7-M specification but,
  for the v8-M specification, Arm had decided that the exception state should be
  updated.
* Property (c) was almost right, except that the English rule was
  implicitly referring to the _debug view_ of the program counter,
  not the _normal view_.  (The normal view is always 4 greater than
  the debug view.)
* Properties (e1) and (e2) were guesses about what the last line
  of the English meant.  By trying both, I had now figured out that
  the statement
  "HFSR.FORCED is not set to 1" meant that HFSR.FORCED was unchanged.

Hmmmm, so this was not as easy as the first example suggested; it
was going to take a bit more work than I had hoped to formalize the
rules so I used a classic research technique that I learned when
I worked at the University of Utah:

> Retroactively redefine your goal and declare success!

So, massive success, I now have a very effective way of finding errors and
ambiguities in the English rules in Arm's specifications!

And, as a bonus, I found that some of the rules could catch bugs in the
specification --- I have found about a dozen bugs so far.

# Are natural language specifications useful?

So how do I feel about natural language specifications now?

* The natural language part of Arm's architecture specifications
  adds some of the architectural intent that is missing from the more
  executable style of specification that I have focussed my efforts on
  until now.

* The additional structure of Arm's new rule-based specification style
  makes it easier to understand and formalize the rules.

* The natural language specification is able to express concepts that
  are harder to express in a formal language.  A small example is the
  statement "EPSR.IT to be become UNKNOWN" that I could not translate
  but that is useful information to programmers.  A larger example
  would be something like memory concurrency semantics that we are
  only now learning how to formalize.

* The inherent ambiguity of natural language remains a problem --- it is only
  by trying to formalize rule VGNW above that it became clear how
  ambiguous some of the statements were.

* The untestability of natural language remains a problem --- it is only
  when I formalized rule VGNW and tried to prove that it held that
  I found that properties (b1) and (b2) are not true.

So natural language specs are playing a useful role but all the traditional
objections to natural language specifications still remain.
I see two ways past this.

1. Since Arm is adopting a more structured approach to writing these natural
   language statements, I wonder if it is possible to have our cake and eat it
   too?  Could we write at least part of our specifications in a formal language
   and then automatically translate it to English.
   It sounds fanciful but I recently came across [an intriguing paper by
   Burke and Johannisson](http://i12www.iti.uni-karlsruhe.de/~key/oclnl/lacl05.pdf)
   that showed that it is possible to do a reasonable job in some cases.

2. We could write two versions of every rule: one in natural language and
   one in a formal language.  This has the advantage that it could be applied
   today but the disadvantage that it would take more work in the long run
   and there would inevitably be differences between the two.

This would still leave some statements that we cannot formalize yet or whose
formalization is so tricky that a direct translation between English
and math is not viable.  We still need those: hopefully someday we will
find a way to formalize them.

So, are natural language specifications useful?  Yes, but they would be even
more useful if they were a bit more formal.

------

This post was discussed on
[reddit](https://www.reddit.com/r/programming/comments/6uyd0j/are_natural_language_specifications_useful/?st=j6tdagae&sh=d88098f4)
and on [Hacker News](https://news.ycombinator.com/item?id=15060355).

### Related posts and papers

* Paper: [End-to-End Verification of ARM Processors with ISA-Formal]({{ site.url }}/papers/cav2016_isa_formal.pdf), CAV 2016.
* [Verifying against the official ARM specification]({{ site.baseurl }}{% post_url 2016-07-26-using-armarm %})
* [Finding Bugs versus Proving Absence of Bugs]({{ site.baseurl }}{% post_url 2016-07-18-finding-bugs %})
* [Limitations of ISA-Formal]({{ site.baseurl }}{% post_url 2016-07-30-isa-formal-limitations %})
* Paper: [Trustworthy Specifications of ARM v8-A and v8-M System Level Architecture]({{ site.url }}/papers/fmcad2016-trustworthy.pdf), FMCAD 2016.
* [ARM's ASL Specification Language]({{ site.baseurl }}{% post_url 2016-08-17-specification_languages %})
* [ARM Releases Machine Readable Architecture Specification]({{ site.baseurl }}{% post_url 2017-04-20-ARM-v8a-xml-release %})
* [Dissecting the ARM Machine Readable Architecture files]({{ site.baseurl }}{% post_url 2017-04-29-dissecting-ARM-MRA %})
* Code: [MRA Tools](https://github.com/alastairreid/mra_tools)
* [ASL Lexical Syntax]({{ site.baseurl }}{% post_url 2017-05-07-asl-lexical-syntax %})
* [Arm v8.3 Machine Readable Specifications]({{ site.baseurl }}{% post_url 2017-07-31-arm-v8_3 %})
* Paper: [Who guards the guards?  Formal Validation of the Arm v8-M Architecture Specification]({{ site.url }}/papers/oopsla2017-whoguardstheguards.pdf)), OOPSLA 2017.
* This post: [Are Natural Language Specifications Useful?]({{ site.baseurl }}{% post_url 2017-08-19-natural-specs %})
* [Formal validation of the Arm v8-M specification]({{ site.baseurl }}{% post_url 2017-09-24-validating-specs %})

