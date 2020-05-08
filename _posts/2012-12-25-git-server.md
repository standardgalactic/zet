---
layout: post
title: A Home Git Server
---

I've been using a Synology Diskstation for a while as a Network Attached Storage box for sharing music and photos and as a TimeMachine server but I've always known that it can do a lot more and I wanted a private git server so I googled and found these useful pages:

I won't repeat their instructions because they're quite clear (if a little long).  Once that was done, adding a new repository was pretty simple:

    > login to diskstation
    > mkdir -p /volume1/git/test
    > cd /volume1/git/test
    > git init --bare
    Initialized empty Git repository in /volume1/git/test/

And then I could use it from my home machine in the usual way

    > git clone ssh://diskstation/volume1/git/test

Woohoo!
