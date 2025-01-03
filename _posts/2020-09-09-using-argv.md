---
layout: post
title: "Using command-line arguments ('argv')"
permalink: /using-argv/
---

![LLVM logo](https://www.llvm.org/img/DragonSmall.png){: style="float: left; width: 10%; padding: 1%"}
One important difference between C and Rust is that the C main function expects
to be given a list of command line arguments via `argc`/`argv` function
parameters while Rust programs access their command line arguments via the
`sys::env::args()` library function.

This raises the problem when verifying Rust programs of how can we pass
command line arguments to a program when we are verifying it.
This document sketches how Rust's command line arguments work (on Linux)
and how we can set them when verifying Rust programs.

_[Note:
You should not need any of the information in this note to
use `propverify` if you are using the `cargo-verify` script.
These instructions are mostly useful if you want to create your own
tools or if you hit problems.]_


## How Rust handles command-line arguments (on Linux)

_[For more information about this, see [this blog post][Rust's runtime]
and, of course, [the source code][std-env-args source code].]_

The Rust runtime system provides an initializer function
`ARGV_INIT_ARRAY::init_wrapper(argc, argv, envp)` that saves the values of
`argc` and `argv` in global variables so that they can be accessed later by
`std::env::args()` and it places a pointer to this function in a global variable
in an ELF section called `.init_array_000099`.

When the Linux kernel runs a Rust program, it starts by executing code from the GNU C
library.  This library calls some initialization functions before calling the
Rust `main` function.  These initialization functions are found in ELF
sections with names like `.init_array` and they expect to be called with three
arguments: `argc`, `argv` and `envp`.


## How our tools handle command-line arguments

To make it possible to pass command-line arguments to a program when it is being
verified, we need to arrange that the initialization functions are called and that
they are passed the values of `argc` and `argv`.
(I am unsure whether we also need to pass the value of `envp`.)

Since verification tools like `KLEE` are normally used to verify C programs,
they expect to start with a call to `main(argc, argv)` so, to verify Rust programs,
we need to arrange that calling `main` will call any initialization functions.
We do this by transforming the LLVM bitcode file generated by the Rust compiler
so that the first thing that `main` does is to call all the initialization functions
and to pass them the values of `argc/argv`.
The `cargo-verify` script invokes this transformation if any command line arguments
are passed to the program.

This results in an LLVM `main` function like this (the change is the third line that calls `__init_function`).

```
define i32 @main(i32 %0, i8** nocapture readnone %1) unnamed_addr #5 {
top:
  call void @__init_function(i32 %0, i8** %1, i8** null)
  %2 = load volatile i8, i8* getelementptr inbounds ([34 x i8], [34 x i8]* @__rustc_debug_gdb_scripts_section__, i64 0, i64 0), align 1
  %3 = sext i32 %0 to i64
  %4 = call i64 @_ZN3std2rt10lang_start17ha6542edf6afbeb15E(void ()* @_ZN4argv4main17h878bf90218e36557E, i64 %3, i8** %1)
  %5 = trunc i64 %4 to i32
  call void @klee.dtor_stub()
  ret i32 %5
}
```

and the `__init_function` that calls all the initializers looks like this

```
define void @__init_function(i32 %0, i8** %1, i8** %2) {
entry:
  call void @_ZN3std3sys4unix4args3imp15ARGV_INIT_ARRAY12init_wrapper17hac2c035213cf4e54E(i32 %0, i8** %1, i8** %2)
  ret void
}
```

[CC-rs crate]:                    https://github.com/alexcrichton/cc-rs/
[Cargo build scripts]:            https://doc.rust-lang.org/cargo/reference/build-scripts.html
[Clang]:                          https://clang.llvm.org/
[Crux-MIR]:                       https://github.com/GaloisInc/mir-verifier/
[Docker]:                         https://www.docker.com/
[GraalVM and Rust]:               https://michaelbh.com/blog/graalvm-and-rust-1/
[Hypothesis]:                     https://hypothesis.works/
[KLEE]:                           https://klee.github.io/
[Linux driver verification]:      http://linuxtesting.org/ldv/
[LLVM]:                           https://llvm.org/
[MIR blog post]:                  https://blog.rust-lang.org/2016/04/19/MIR.html
[PropTest book]:                  https://altsysrq.github.io/proptest-book/intro.html
[PropTest]:                       https://github.com/AltSysrq/proptest/
[Rust benchmarks]:                https://github.com/soarlab/rust-benchmarks/
[Rust port of QuickCheck]:        https://github.com/burntsushi/quickcheck/
[Rust's runtime]:                 https://blog.mgattozzi.dev/rusts-runtime/
[SMACK]:                          https://smackers.github.io/
[SV-COMP]:                        https://sv-comp.sosy-lab.org/2020/rules.php
[std-env-args source code]:       https://github.com/rust-lang/rust/blob/master/library/std/src/sys/unix/args.rs

[RVT git repo]:                   {{site.RVTurl}}/
[cargo-verify source]:            {{site.RVTurl}}blob/main/cargo-verify/
[compatibility-test]:             {{site.RVTurl}}blob/main/compatibility-test/src
[demos/simple/ffi directory]:     {{site.RVTurl}}blob/main/demos/simple/ffi/
[CONTRIBUTING]:                   {{site.RVTurl}}blob/main/CONTRIBUTING.md
[LICENSE-APACHE]:                 {{site.RVTurl}}blob/main/LICENSE-APACHE
[LICENSE-MIT]:                    {{site.RVTurl}}blob/main/LICENSE-MIT

[Using KLEE]:                     {{site.baseurl}}{% post_url 2020-09-01-using-klee %}
[Using verification-annotations]: {{site.baseurl}}{% post_url 2020-09-02-using-annotations %}
[Using PropVerify]:               {{site.baseurl}}{% post_url 2020-09-03-using-propverify %}
[Using ARGV]:                     {{site.baseurl}}{% post_url 2020-09-09-using-argv %}
[Using FFI]:                      {{site.baseurl}}{% post_url 2020-12-11-using-ffi %}

*[This post was originally posted as part of the [Rust verification project]({{site.RVTurl}}/)]*

