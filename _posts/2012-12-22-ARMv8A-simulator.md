---
layout: post
title: Installing the ARM v8-A simulator
---

I have been wanting to experiment with ARM's new 64-bit architecture for a while and now ARM has released a simulator.

What you have to do is

Download a Linux image from Linaro

> mkdir linaro-armv8
>
> cd linaro-armv8/
>
> gunzip vexpress64-openembedded_sdk-armv8_20121125-96.img.gz

Download the ARMv8 Foundation Model (i.e., simulator) from ARM: 

Run the simulator

> ~/linaro-armv8/Foundation_v8pkg/Foundation_v8 --image ~/linaro-armv8/img-foundation.axf --block-device ~/linaro-armv8/vexpress64-openembedded_sdk-armv8_20121125-96.img --network=nat

It will open an X window containing a Linux console - takes 5-10 minutes to boot when I run it in a 64-bit Ubuntu machine running as a virtual machine in my Mac.
