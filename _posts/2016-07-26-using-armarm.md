---
layout: post
title: Verifying against the official ARM specification
---

Part of the reason why  the [ISA-Formal technique for verifying ARM
processors]({{ site.url }}/papers/CAV_16/) is so effective and
so portable across different ARM processors is the fact that we directly use the
ARM Instruction Set Architecture (ISA) Specification in our flow.
That is, I translate ARM's official printed documentation into something that
I can load into a model checker alongside ARM's processor Verilog and I verify
that the two match each other.

It takes a lot of effort to create a processor specification.  The ARM v8-A and
ARM v8-M specifications we use in the paper are over 50,000 lines of code.
Even if we restrict our attention to the instruction parts, there are still
more than 31,000 of code and more than 1,500 instruction encodings.

And if you think you can write that much code without introducing errors, then
you are fooling yourself.  So you either need to hope that you make different
errors in the specification than in the processor or you need a plan for how
you will test your specification.  (That is the subject of my other paper
["Trustworthy Specifications of ARM v8-A and v8-M System Level
Architecture"]({{ site.url }}/papers/FMCAD_16/) that I just had
accepted by the [Formal Methods in Computer-Aided Design (FMCAD 2016)
conference](http://www.cs.utexas.edu/users/hunt/FMCAD/FMCAD16/index.shtml).)

So what I decided to do is to take advantage of the fact that ARM already
produced a specification that they invested a lot of effort into producing and
that was _almost_ parseable, _almost_ type checkable and _almost_ executable.
"All I had to do" was to implement the tools, fill the gaps and fix the bugs so
that I could delete all occurences of the word "almost" from the previous
sentence.

Once I had done that, I had a specification of the ARM ISA that I trusted --- but
it was in a language that model checkers did not support.  So, before we could
use it with ISA-Formal, I had to write a translator that converted the ARM
specification into a language that model checkers did accept.

Since the overall goal of ISA-Formal is to verify processors written in
Verilog, that meant that I had to learn Verilog so that I could translate the
specification to Verilog.  Here I was in for a shock.  In software
development, I am used to compilers being fairly reliable, implementing
the entire language they claim to implement and detecting and reporting
most of the obvious errors which make compilation impossible.
Despite the fact that Verilog implementations have a significantly
higher price tag than C compilers, I found that none of these properties
held for Verilog implementations.  None of them implement the full language,
there is little agreement between them about which subset they will support
or which subset they implement correctly and they will happily accept code
with very obvious errors without complaint.

Cynical people, might suspect that tool vendors do this so that
they can sell you linting tools, testing tools, formal tools, etc. to check for
these errors.  But I choose to believe the happier story that EDA vendors think
of Verilog as a scripting language, not a compiled language and discovering
errors is just part of the wild adventure of building a chip.  After all, if it
was easy, everybody would be doing it.

The upshot of all this is that, as I was learning how to generate
Verilog, I also had to experimentally figure out which subset was supported by
all the tools I wanted to use and seemed to be implemented correctly by all of
them.

The final bit of the puzzle was figuring out the interface between the
machine-generated code, the processor and the checking infrastructure.  The
main trick here was that we needed the interfaces to match the concepts in the
architecture.  So we had to find functions in the architecture spec that were
a good match for interfaces in the processor and find variables in the
architecture spec that were a good match for registers in the processor.  It
was not obvious that this was going to be possible when we started: there is no
reason that the interface should match and lots of reasons why it should not
match.  And it seemed likely that the exact interface would have to be changed
from one processor to another which would make it more work to port the method
between processors.  Fortunately, we found that all processors seem to have
a few common pinch points where they all provide roughly equivalent interfaces
and those interfaces carry approximately the same information as some function
call interface in the architecture spec For example, the memory interface, the
FPU interface, the decode interface, etc.  (I'm not saying they don't have their
quirks --- but the semantic gap to be bridged is not too large.)

Once we had figured out how to generate Verilog and how to attach it to the
processor and verification framework, we could finally start
[bug hunting]({{ site.baseurl }}{% post_url 2016-07-18-finding-bugs %})
and after a few weeks of warmup, we started detecting bugs at
a steady rate.

![Picture]({{ site.baseurl }}/images/cav2016-graph.png)

And as a bonus, we create a _virtuous circle_ where not only do we find bugs in
the processor but we also find bugs in the specification.  So the specification
(and my tools to process the specification) become even more accurate
formalizations of the (informal) architecture specification expressed in the
rest of the ARM Architecture Reference Manual.

---

_This is one of several notes I am writing about the key ideas in our
paper ["End-to-End Verification of ARM Processors with ISA-Formal"]({{ site.url
}}/papers/CAV_16/) which I am presenting at the [2016
International Conference on Computer Aided
Verification](http://i-cav.org/2016/) on Friday 22nd July.  There is nothing
quite like trying to squeeze a 16 page paper into a 16 minute presentation for
figuring out what the important messages are and how to present them._

