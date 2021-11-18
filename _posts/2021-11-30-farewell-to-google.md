---
layout: post
title: Farewell to Google
---


![Google logo]{: style="float: left; width: 10%; padding: 1%"} I've spent the
last couple of years working at Google Research.  For the first 5--6 months, I
was working in London in an office nestled between  King's Cross station and
the iconic St Pancras station.  This location was ideal for me because I was
still living in Cambridge at the time and it was a very easy journey to
either of these stations from Cambridge.

I started off working on privacy and security in operating systems. This led to
fun experiments with
UW's impressive [Serval](https://unsat.cs.washington.edu/projects/serval/)
that automatically verifies machine code
and Bart Jacobs' amazing [VeriFast](https://github.com/verifast/verifast) tool
whose user interface transformed my thinking about [auto-active verification].

After that, I lead the [Rust verification project] at Google: a project focused on usability
of formal verification.
I wrote surveys of the available Rust verification tools in
[2020][Rust verification tools 2020]
and
[2021][Rust verification tools 2021];
I used a [risk based approach to research planning][managing risk in research];
I collaborated with some usability researchers on [a paper about "making formal normal"][HATRA 2020];
and I used [KLEE] to understand some of the infrastructure barriers
to using verification tools on real Rust code.
For example, I found and filled gaps in language feature support, library support, runtime/linker support, etc.
(See the workshop presentation for details
[[pdf]]({{site.baseurl}}/talks/using-KLEE-with-Rust-2021-07-11.pdf)
[[video]](https://youtu.be/zR7oDg7zix0).)
With these extensions in hand, I was able to try to run verification tools on
large, complex, real-world Rust code such as
"Rust for Linux" [[pdf]]({{site.baseurl}}/talks/Kangrejos-2021-09-13.pdf)
and [the Rust rewrite of CoreUtils]({{site.RVTurl}}/2021/07/14/coreutils.html)
to understand the remaining issues.

For the last 2--3 months, I have been working on a hardware-software codesign project.
These are always a lot of fun because you start with a huge design space and then gradually narrow
down what parts of the task are best solved by the programmer, the compiler, the runtime and libraries, or the hardware.
A critical part of these projects is about enabling and encouraging the right kind
of collaboration between subteams with radically different expertise: hardware, software,
tools, systems, etc.
So I built a performance modeling tool to enable software and hardware engineers to
find the right design compromise: discovering the performance bottlenecks in the code
and exploring different microarchitecture and vectorization choices to overcome them.

I've learned a lot of new things over the last two years but
I've decided that it is time to move on.
So, today I bid my colleagues farewell and leave Google Research.


[HATRA 2020]: {{site.baseurl}}/papers/HATRA_20/
[Rust testing or verifying: why not both]: {% post_url 2020-09-03-why-not-both %}
[Rust verification tools 2020]:   {% post_url 2020-05-08-rust-verification-tools %}
[Rust verification tools 2021]: {% post_url 2021-06-03-automatic-rust-verification-tools-2021 %}
[Rust verification project]: {{site.RVTurl}}/
[KLEE]: https://klee.github.io
[Auto-active verification]:   {{site.RWurl}}/notes/auto-active-verification/
[Google logo]: {{ site.baseurl }}/images/Google__G__Logo.svg.png


[Managing risk in research]: {{site.baseurl}}/research-risks/
