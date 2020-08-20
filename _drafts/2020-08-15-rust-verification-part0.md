---
title: "Rust verification part 0: installing KLEE"
layout: post
---

I'm writing a sequence of posts about using
[formal verification tools][Rust verification tools]
with Rust with the plan that I will show you all the steps required
to start using a variety of formal verification tools with Rust.
Since this is the first in the series,
the meat of this post is going to be about setting up Rust
and one tool ([KLEE])
so that future posts can focus on using the tools.

And, in case any of you are working on Rust
verification tools yourselves,
I'll describe some of the problems that I ran into when
trying to get some LLVM-based tools that are normally used
with C to work with Rust: maybe the issues I hit apply to the
tool you work on?

One quick disclaimer before I get going...
Everything I describe here is changing very quickly: the
Rust compiler, Rust verification tools, etc.
Also, I am new to Rust and I am new to using the verification
tools so I have probably made things more complicated than
they need to be, or I have missed critical steps or
this is all out of date by the time you read this.
If you see a mistake, please [email me](mailto://adreid@google.com)
and I'll try to fix it.[^extra-steps]

[^extra-steps]:
    Since I have been working with several different tools,
    I may also have added some extra steps that are needed with
    tools not discussed in this post.
    Fortunately, disk space is cheap so installing an unneeded
    dependency should not do too much harm.


## Context

Before I get going, I should give a bit of context.
I'm working on a research project at Google called
[Project Oak]
which is creating a runtime to support secure transfer, storage and processing of data.
[When I joined the project][joining Oak post] last year,
the code was all written in C++.

Early this year, we rewrote all that C++ code in Rust.
The entire codebase is around 20k lines of code. But, at least for
now, it depends on around 100 external, open-source crates
and, of course, Rust's rather rich standard library.
So the total amount of code that we have to worry about is
much, much larger.

Formal verification is a critical part of the Oak story,
since security and privacy are the core of the project
and we want to convince ourselves and others that the system
will work as intended.
In theory, the switch to Rust makes formal verification much better
because Rust is both technically and socially much better suited
to creating trustworthy code.
My goal has been to try to turn that theory into practice and,
unsurprisingly, there is a bit of a gap.

In my previous post about [Rust verification tools],
I found that there were a number of verification tools for Rust
but some had only just started, some only supported a subset
of the language and other projects looked really
promising but seemed to be abandoned.

Over the last 3--4 months, I have been digging into some of those tools and
trying to figure out how to use them on code like Oak.
That is, on a non-trivial (though still quite modest),
that uses a lot of the Rust language and depends on libraries
that probably use the entire language.


## Installing the Rust compiler

One of the great things about Rust is that it only has one compiler
and a single standard library.
This means that verification tools can all use the Rust compiler
as the frontend for parsing, typechecking, handling modules, etc.

The [Rust compiler works](https://blog.rust-lang.org/2016/04/19/MIR.html)
in three stages[^not-three]:
first, it compiles Rust source code to MIR (the mid-level IR);
then it compiles MIR to LLVM IR (the low-level virtual machine IR);
and, finally, it compiles LLVM IR down to machine code.

[^not-three]:
    Actually, the Rust compiler has four stages: before
    generating MIR, it first generates HIR.
    But, as far as I know, that is not used by verification
    tools.

There seem to two main classes of verification tool for Rust:
those that use MIR code and those that use LLVM IR code.
Several verification tools for C already use LLVM IR code
so I decided to focus my initial efforts on using LLVM-based tools
with Rust.

Whichever type of tool you are using, you are probably going to
have to do two things:

1. Link any tools you are using against the version of LLVM being
   used in the Rust compiler.

2. Ensure that you have either MIR or LLVM IR for the standard
   Rust libraries (libcore, libstd, etc.)

So, the first step is building the Rust compiler and libraries
from source.
This is not too hard but it is quite slow so you should plan
on starting the build process before lunch/dinner and hoping that it is
finished by the time you are done.

I'm going to do all this work in a directory called "rust" so let's start by
creating that directory, installing a few tools and downloading the Rust source code.

```
mkdir $HOME/rust && cd $HOME/rust

# On Linux, do this
sudo apt-get install build-essential curl libcap-dev git cmake \
  libncurses5-dev python-minimal python-pip unzip libtcmalloc-minimal4 \
  libgoogle-perftools-dev libsqlite3-dev doxygen

# On OSX, do this (not tested as thoroughly)
brew install curl git cmake python unzip gperftools sqlite3 doxygen bash

pip3 install tabulate wllvm lit

# Download the Rust source code
git clone https://github.com/rust-lang/rust.git
```


By default, The Rust compiler and libraries support all targets.
But you probably only need one (probably X86) so the first step is
configuring the build configuration so that you don't spend (a lot of)
time building versions that you don't need.

```
cd rust
cp config.toml.example config.toml

# It is a good idea to edit config.toml to change this line 
#     #targets = "AArch64;ARM;Hexagon;MSP430;Mips;NVPTX;PowerPC;RISCV;Sparc;SystemZ;WebAssembly;X86"
# to this line 
#     targets = "X86"
# it will make the build process significantly shorter
```

Now the slow bit: building Rust.

Since I am interested in LLVM, I want to make sure that the library includes
LLVM IR "bitcode" for the libraries.
So I am going to pass the `-Cembed-bitcode=yes` flag to make sure this
happens.[^may-not-be-needed]

[^may-not-be-needed]:
    It is possible that the Rust standard libraries include LLVM IR bitcode
    by default?
    This all seemed to be in flux in April/May 2020 as I was figuring
    out how to do things so I wanted to be doubly-sure that the
    libraries would include the information that I needed.
    So, it is possible that you don't need the `RUSTFLAGS_STAGE_NOT_0`
    flag. But it shouldn't do any harm.

Verification tools [have different optimization needs from normal
compilation][Overify].
When compiling, you want to generate code that takes full advantage
of any special features of your hardware: the cache, special instructions,
loop unrolling, etc.
But, when verifying, you just want your code to be simple and uncluttered.
I haven't really explored what this means yet but one thing that I might want
to try is disabling some of the architecture-specific optimizations such as
vectorization and the use of architecture specific features like Intel's SSE,
AVX, etc.

```
# RUSTFLAGS_STAGE_NOT_0="-Cembed-bitcode=yes" 
# todo: disable vectorization, sse, avx, etc.
./x.py build
```

That will take a while to build but, once it is done, let's make it the default
compiler.

```
rustup toolchain link stage1 build/x86*/stage1
rustup toolchain link stage2 build/x86*/stage2
rustup default stage2
```

We're now done building Rust so let's add the LLVM compiler inside Rust to our
path and pop up into the parent directory.

```
export PATH=$PATH:`echo $HOME/rust/rust/build/x86_*/llvm/bin`

cd ..
```

## Which LLVM-based verification tool to try first?

From my earlier survey of [Rust verification tools],
I knew there were at least three LLVM-based verification tools that
I might consider using: [KLEE], [SMACK] and [SeaHorn].

As far as I can tell, nobody has tried using [SeaHorn] with Rust so, while I
might _consider_ using SeaHorn at this stage, I figured that I would be
much, much happier if I started with something else.

Something that I will be expanding on during this series of posts is that I am
interested in having a continuum of verification tools: starting with tools
that support more traditional techniques like testing and fuzzing, then
shifting to solver-based tools that that focus on testing and finding bugs and
then building up to more and more powerful tools that provide proofs of
stronger and stronger properties.

So I decided to start with [KLEE] since it is often used to find bugs and
generate tests. I'll say more about what KLEE can do in future posts
and I plan to try the other tools sometime in the future.


### Extending KLEE to support Rust

This was not an entirely painless choice.
As I have been working my way up from small examples to
larger, more realistic examples, I have run into a number
of places where KLEE needed extensions to support the kind
of LLVM code that the Rust compiler produces.
Here is a quick list that might be useful to anybody else
trying to bring up some Rust verification tools.

- KLEE has been around for over 12 years and LLVM has changed
  a lot since then.
  The KLEE developers have made an impressive commitment to
  maintaining backwards compatibility with older versions of
  LLVM: using conditional compilation to only enable features
  supported by the LLVM version they use.

  To do this, they need to figure out which version of LLVM
  they are linked against and they do this by checking the
  output of the `llvm-config --version` command.
  The only problem is that the version of LLVM used by the
  Rust compiler reports versions like `10.0.1-rust-dev`
  and KLEE's configuration script did not recognize versions
  of that form.

  And [here is a fix](https://github.com/klee/klee/pull/1291).

- LLVM has thousands of "intrinsic functions" to support
  things like floating point operations, copying memory, etc.
  KLEE supports the intrinsics that are common in C code but
  it was missing some intrinsics found in Rust binaries.

  The missing intrinsics included
  `fshl`, `fshr`,
  `minnum`, `maxnum`,
  `x86_sse2_pause`
  and about ten other intrinsics corresponding to obscure
  x86 AVX and SSE instructions.

  Before I realized how many intrinsics were missing
  (and how complex they were),
  I started off by trying to implement some of the missing
  intrinsics such as `fshl` and `fshr`
  ([pull request](https://github.com/klee/klee/pull/1278)).

  But then I realized that the way KLEE worked, it was
  halting if there was any unrecognized intrinsic anywhere
  in the program even if that intrinsic was not actually
  used by the program.
  So it would be better to change KLEE to only reject
  programs if it actually encountered an unknown
  intrinsic while verifying the program
  ([pull request](https://github.com/klee/klee/pull/1295)).

- The C language was born in the days of single processors.
  Multiprocessors and, in particular, symmetric multiprocessing (SMP)
  and threads came much later.
  As a result, most C code is not thread safe.

  By the time Rust was being designed, almost every computer
  you would want to run Rust on was an SMP machine and so
  Rust is designed for "[fearless concurrency](https://blog.rust-lang.org/2015/04/10/Fearless-Concurrency.html)".
  There are many aspects to this but one is that Rust's
  libraries are thread safe.

  When I first started trying to verify Rust programs in
  KLEE, I couldn't run any of them successfully.
  Even if they seemed to run fine at the start, they would
  all crash at the end.
  It is so frustrating to watch a program run all the way
  to the end and then trip up as it is about to cross the
  finish line!

  When I dug into this, I found that when Rust programs
  exited, they were cleaning up after themselves using
  a variant of the [C library's
  atexit](https://www.man7.org/linux/man-pages/man3/atexit.3.html)
  function.
  This should be fine because KLEE already supported `atexit`.
  But, of course, KLEE was designed for C so it supported
  the non-thread-safe version
  but Rust was, of course, using the thread safe version.
  ([pull request](https://github.com/klee/klee/pull/1290))

- One of the incredibly useful things about modern verification tools like KLEE
  is that many of them can show you what input values would cause your program
  to break.

  When you run KLEE on your program, it explores a number of paths through your
  code and, for each interesting path, it dumps out a file of
  inputs that trigger that path.
  Afterwards, you can either examine the file or you can rerun your
  program using one of those input files to rerun that path.

  For unstructured inputs like ints or strings, this works pretty
  well: it is easy to understand the list of input values.
  But, Rust has a rich standard library that provides types like
  tuples, options, BTrees, sets, maps, heaps, etc.
  The best way to view values of these types is using
  the Rust library's printing functions to print them.

  I wanted the code I was testing to behave two different ways:
  when KLEE is running the program, I don't want to print
  the values and when I am replaying the program, I want to
  print the values.
  So I extended KLEE with a way to tell whether the program was
  running in KLEE or was being replayed on test inputs.
  ([pull request](https://github.com/klee/klee/pull/1288))



### Installing KLEE's dependencies

We are going to build KLEE from source for two reasons:

1. KLEE is built on top of LLVM and we want to make sure that
   it is built on top of the same version of LLVM that Rust
   is built with so we build from source.

2. In the process of doing this work, I had to fix/extend KLEE
   to deal with several minor issues so we need to use a
   development version of KLEE.
   Specifically, we need to use a version from late August 2020.
   (TODO: put the exact date and a git link in once all the
   pending PR's stabilize.)

The KLEE installation process is described
[on these pages](https://klee.github.io/build-llvm9/).
In practice though, I find it slightly easier to
consult the [Dockerfile](https://hub.docker.com/r/klee/klee/dockerfile)
and the [Dockerfiles of all of KLEE's dependencies](https://hub.docker.com/u/klee).

For convenience, I am going to give instructions but, if my instructions don't
work for you, you should consult one of those sources.

We are going to install
Minisat,
STP,
KLEE's micro-libc,
and KLEE itself.

Let's start by fetching the git repos of all the dependencies

```
cd $HOME/rust
# git clone https://github.com/msoos/cryptominisat
git clone https://github.com/stp/minisat.git
git clone https://github.com/stp/stp.git
git clone https://github.com/klee/klee-uclibc.git
git clone https://github.com/klee/klee.git
```

I am going to install all the tools in my
home directory, so you will want to setup your
environment variables to look in `$HOME/{bin,include,lib}`
(or omit the `--prefix` options in the instructions below).

```
export PATH=$PATH:$HOME/bin
export C_INCLUDE_PATH=$C_INCLUDE_PATH:$HOME/include
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/lib
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:$HOME/lib
```


### Building minisat

```
# from https://github.com/stp/stp
cd minisat
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$HOME ../
make install
cd ../..
```


### Building STP

```
# from https://klee.github.io/build-stp/
cd stp
git checkout tags/2.3.3
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=$HOME ../
sudo make install
cd ../..
```



### Building KLEE's uclibc

It is not clear whether this step is actually needed and, in any case, you will
need to skip the following step on MacOS.

```
cd klee-uclibc
# enable pthreads
./configure --make-llvm-lib
echo HAS_NO_THREADS=n >> .config
echo UCLIBC_HAS_THREADS=y >> .config
make -j
cd ..
```


### Building KLEE

Building KLEE is pretty much the same as
[on these pages](https://klee.github.io/build-llvm9/)
except that we are going to make KLEE use the
LLVM compiler used by Rust.
This LLVM/Rust compiler source is in `rust/src/llvm-project/llvm`
and it will have been built int `rust/build/x86_*/llvm/bin`.

A minimal install of KLEE looks something like this.

```
cd klee
mkdir build && cd build
cmake \
  --prefix=$HOME \
  -DENABLE_SOLVER_STP=ON \
  -DLLVMCC=`which clang` \
  -DKLEE_RUNTIME_BUILD_TYPE=Release \
  -DENABLE_KLEE_UCLIBC=OFF \
  -DLLVM_CMAKE_DIR=$HOME/rust/rust/src/llvm-project/llvm/cmake/modules \
  -DLLVM_CONFIG_BINARY=`ls $HOME/rust/rust/build/x86_*/llvm/bin/llvm-config` \
  ..
```

But I normally configure it with these additional configuration flags

```
  -DKLEE_UCLIBC_PATH=$HOME/rust/klee-uclibc \
  -DENABLE_UNIT_TESTS=ON \
  -DGTEST_SRC_DIR=$HOME/rust/googletest-release-1.7.0 \
  -DENABLE_POSIX_RUNTIME=ON \
  -DENABLE_TCMALLOC=OFF \
```

Once configured, build it, run the testsuite and install.

```
make -j
make check
make install
```

You should now be able to run `klee --help` and see a myriad of
verification options.


## Summary

This post was about setting up the tools that we are going
to need in the next post.
Rust verification is pretty near the bleeding edge so I
had to extend KLEE a little to support Rust better
and we built all the tools from source.
The main things we built are the Rust compiler, the standard Rust
libraries and the [KLEE] symbolic execution engine.


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
