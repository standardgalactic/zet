---
title: "Rust verification part 1: using KLEE"
layout: post
---

This series of posts is looking at how can we use [Rust verification tools] to
increase our confidence in Rust programs.  The first tool I tried using was the
[KLEE] symbolic execution tool.
In [the first post in this series]({% post_url 2020-08-15-rust-verification-part0 %})
I described how to build KLEE;
this post is about using KLEE to verify Rust programs.

The process is a bit complicated and it took me a while to figure out (based on
reading many random posts full of instructions that no longer work) so I am
going to dive into all the details.
(In later post, I will introduce scripts and libraries that that hide
a lot of the complexity so that you can focus on the task of verification.)

The Rust compiler is based on the LLVM platform and
KLEE is based on LLVM so the steps involved in using
KLEE to verify Rust programs are:

1. Compile the program to generate LLVM bitcode.
2. Run KLEE on the bitcode file.
3. Examine the output of KLEE.


## Compiling Rust for verification

The Rust compiler normally deletes the bitcode

1. Bitcode
2. Containing error checks (maybe add those later)
3. (Optionally?) using panic abort
4. With x86 features disabled (may not need this yet)
5. Optimized just the right amount (may not need this yet)


```
RUSTFLAGS =
      '-Clto',                 # Generate linked bitcode for entire crate
      '-Cembed-bitcode=yes',
      '--emit=llvm-bc',

      '-Copt-level=1',         # Avoid generating SSE instructions
                               # Any value except 0 seems to work

      # '-Ccodegen-units=1',     # Optimize a bit more?

      '-Zpanic_abort_tests',   # Panic abort is simpler
      '-Cpanic=abort',

      '-Warithmetic-overflow', # Detecting errors is good!
      '-Coverflow-checks=yes',

      '-Cno-vectorize-loops',  # KLEE does not support vector intrinisics
      '-Cno-vectorize-slp',
      '-Ctarget-feature=-mmx,-sse,-sse2,-sse3,-ssse3,-sse4.1,-sse4.2,-3dnow,-3dnowa,-avx,-avx2',

cd crate
RUSTFLAGS=...  cargo build --target=x86_64-unknown-linux-gnu
```


## Using the KLEE API

1. Symbolic values, assumptions, assertions
2. KLEE FFI


## Running KLEE

1. Running KLEE on bitcode
2. Exploring paths and assumptions
   Maybe note that KLEE is not usually used to explore all paths
   and has a rich set of options for controlling which paths to
   explore and in what order.
3. Entry point
4. Library
5. Working round KLEE issues

```
klee
 '--entry-point='+entry,
 '--exit-on-error',
 # '--posix-runtime',
 # '--libcxx',
 '--libc=klee',
 '--silent-klee-assume',
 '--disable-verify', # workaround https://github.com/klee/klee/issues/937
+[bcfile],
```


## Examining KLEE output

1. stdout/stderr
   a. Unreachable
   b. Assertion failure
   c. Overflow
   d. Panic
2. klee-last
3. maybe revisit which paths we execute?


## Replaying programs on test outputs

1. replay
2. klee_is_replay and the FFI

```
KTEST_FILE=... cargo run
```


# Rust verification part 2: automating use of KLEE

In the previous post

## The cargo-verify script

todo: extend script with profiling: # paths and time 

## klee-annotations

1. u8, ... i128
2. ranges



# Rust verification part 3: data structures

Any interesting program involves not just scalar values like ints and chars but
data structures like arrays, vectors, btrees, etc.
So, this post in the series on Rust verification takes a first look at
how to reason about programs that use data structures.
We'll develop a small library for building symbolic values which
later posts in this series will develop into an alternative implementation
of the [proptest] property-based testing/fuzzing library.

## How to verify array and vector functions?

1. arrays, vecs, ranges, etc.
   Note that arrays _could_ use existing initialization mechanisms
   Note that symbolic sized allocations blow up

   Note that we have a range primitive to help
   create interesting arrays, etc.
   composite data structures are parameterized

## How to verify btreemap functions

2. avoiding path explosion in btreemap, etc.

## What about user-defined types like structs and enums

4. compose, union, boxing, oneof?


# Rust verification part 4: a DSL for building complex values

1. QuickCheck and property based testing
2. Property based testing in Rust: proptest, etc.
3. Implementing proptest for Rust

   a. The Strategy trait
      value and Value
      slightly incompatible - may not be important

   b. Using last week's library to implement Strategy

   c. The proptest! macro

4. Some proptest examples.


# Rust verification part 5: directed testing, fuzzing and verification

Pros and cons
All depends how rare the failure is
whether you can anticipate failures
or are worried about the failures you did not anticipate

Verification's strength: finding unusual corner cases

(Can proptest find btreemap that has key collisions?
Only if you restrict key range?)


# Rust verification part 6: cargo test

But what about #[test]

1. How cargo test works
2. Invoking the entry-point
3. Finding entry points (name mangling)
4. `cargo test -- --list`
5. ??
6. #[should_panic]
7. parallel testing




## Summary


### Footnotes

[Overify]: {{ site.baseurl }}/RelatedWork/papers/wagner:hotos:2013

[Rust language]: https://www.rust-lang.org
[Rust book]: https://doc.rust-lang.org/book/
[Cargo tool]: https://doc.rust-lang.org/cargo/
[Rust fuzzing]: https://github.com/rust-fuzz
[Rustonomicon]: https://doc.rust-lang.org/nomicon/
[Sealed Rust]: https://ferrous-systems.com/blog/sealed-rust-the-pitch/

[astrauskas:oopsla:2019]: {{ site.baseurl }}/RelatedWork/papers/astrauskas:oopsla:2019/
[baranowski:atva:2018]: {{ site.baseurl }}/RelatedWork/papers/baranowski:atva:2018/
[jung:popl:2017]: {{ site.baseurl }}/RelatedWork/papers/jung:popl:2017/
[jung:popl:2020]: {{ site.baseurl }}/RelatedWork/papers/jung:popl:2020/
[lindner:indin:2018]: {{ site.baseurl }}/RelatedWork/papers/lindner:indin:2018/
[lindner:indin:2019]: {{ site.baseurl }}/RelatedWork/papers/lindner:indin:2019/
[matsushita:esop:2020]: {{ site.baseurl }}/RelatedWork/papers/matsushita:esop:2020/
[toman:ase:2015]: {{ site.baseurl }}/RelatedWork/papers/toman:ase:2015/

[Rust verification papers]: {{ site.baseurl }}/RelatedWork/notes/rust-language/

[verification competitions]: {% post_url 2020-04-19-verification-competitions %}
[Rust verification tools]: {% post_url 2020-05-08-rust-verification-tools %}
[joining Oak post]: {% post_url 2019-11-02-joining-google %}

[Project Oak]: https://github.com/project-oak/oak/blob/main/README.md
[Lean]: {{ site.baseurl }}/RelatedWork/notes/lean-theorem-prover/
[SV-COMP]: {{ site.baseurl }}/RelatedWork/notes/sv-competition/
[Haskell]: https://haskell.org/
[nofib benchmark suite]: https://link.springer.com/chapter/10.1007/978-1-4471-3215-8_17

[Rust verification working group]: https://rust-lang-nursery.github.io/wg-verification/
[Rust verification workshop]: https://sites.google.com/view/rustverify2020

[CBMC]: https://github.com/diffblue/cbmc/pull/4894
[Crust]: https://github.com/uwplse/crust
[Crux-mir]: https://github.com/GaloisInc/mir-verifier
[Electrolysis]: https://github.com/Kha/electrolysis
[Haybale]: https://github.com/PLSysSec/haybale
[Cargo-KLEE]: https://gitlab.henriktjader.com/pln/cargo-klee
[KLEE Rust]: https://github.com/jawline/klee-rust
[KLEE]: https://klee.github.io
[LibHoare]: https://github.com/nrc/libhoare
[MIRAI]: https://github.com/facebookexperimental/MIRAI
[Miri]: https://github.com/rust-lang/miri
[PRUSTI]: https://github.com/viperproject/prusti-dev
[RustBelt]: https://plv.mpi-sws.org/rustbelt/
[RustFuzz]: https://github.com/rust-fuzz
[RustHorn]: https://github.com/hopv/rust-horn
[SeaHorn]: https://seahorn.github.io
[Seer]: https://github.com/dwrensha/seer
[SMACK]: https://github.com/smackers/smack

[contracts crate]: https://gitlab.com/karroffel/contracts
[Viper rust-contracts]: https://github.com/viperproject/rust-contracts
[arbitrary crate]: https://github.com/rust-fuzz/arbitrary
[librarification]: http://smallcultfollowing.com/babysteps/blog/2020/04/09/libraryification/
[verifier crate]: https://crates.io/crates/verifier
[verifier benchmarks]: https://github.com/soarlab/rust-benchmarks
