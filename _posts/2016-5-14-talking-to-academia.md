---
layout: post
title: Talking more to academia
---

The difficult thing about Industrial Research Labs is that you don't always get
to talk about what you are doing so, for the last five years or so, I haven't
published anything except the occasional patent and I have given only abstract
descriptions to most of my friends.

Fortunately, ARM's R&D group has been rebranded as ARM Research and we have
a new mission to engage more with academia, to be more open and to publish
papers and give talks about our work.

A few of the things I am doing towards this are:

- We have provided the [REMS group at the University of
Cambridge](https://www.cl.cam.ac.uk/~pes20/rems/) with
a machine-readable copy of the ARM v8-A Architecture specification.  The
immediate plan is for them to convert from ARM's proprietary specification
language (ASL) to the REMS group's specification language (SAIL) from which it
will be possible to translate to ML, HOL, Coq, etc.  Once that is done, they
will release the SAIL specification publicly.

- I wrote a paper about how we are using ARM architecture specifications as part
of the formal verification of ARM processors.  This will be presented at the
[International Conference on Computer Aided
Verification](http://i-cav.org/2016/) in July 2016.

- I included a summary of recent work at Yale University as part of a talk about
how [Paul Hudak](http://haskell.cs.yale.edu/paul-hudak-symposium/)
continues to influence my research.

- I am submitting another paper to another formal verification conference.  The
new paper is about the process we went through to turn ARM's documentation into
a formal specification and the four different types of testing we applied to
ensure that the result was trustworthy.

It is really good to be able to talk about what I work on again - and hopefully
it will trigger a lot of useful collaboration.
