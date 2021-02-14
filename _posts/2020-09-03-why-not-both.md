---
title: "Rust testing or verifying: Why not both?"
layout: post
---

![Rust logo]{: style="float: left; width: 10%; padding: 1%"}
Dijkstra famously dissed testing by saying "Program testing can be used to show
the presence of bugs, but never to show their absence!"
As if you should choose one over the other.
I don't see them as opposites but as complementary techniques that
should both be used to improve the quality of your code.

I am a big fan of formal verification.
Formal verification tools can be the best bug-finding tools you have
ever used.
And they can completely eliminate entire classes of bugs from your code.
But, formal verification won't find bugs in your
specification; or in your assumptions about your dependencies; or in your
build/CI harness, etc. (See [Fonseca][fonseca:ecs:2017] for more examples
of where testing has found bugs in formally verified systems.)

And, we all reluctantly agree that Dijkstra was right: even a thorough,
perfectly executed test plan can miss bugs.

So, for the last few months, I have been trying to have both.
We (my team and I at Google) have been reimplementing Jason Lingle's
[proptest] property-testing library for use with Rust formal verification tools.
The original proptest lets you write test harnesses to test that your code
(probably) satisfies properties.
Today, we are releasing [a reimplementation of the proptest interface][RVT]
that enables you to use exactly the same test harnesses to
formally verify that the properties hold.
So far, we have only tried this with the [KLEE symbolic execution engine][KLEE]
but our implementation is based on the verification
interface used in [verification competitions] so it should be
possible to port our library to many other verification tools.[^for-Rust]

[^for-Rust]:
    Ok, I have to admit that there are not many
    [verification tools for Rust][Rust verification tools].
    Most of our time so far has been spent submitting
    patches to [KLEE] so that KLEE could be used to verify Rust programs.


*[Before I go any further, I should mention that what we are [releasing this
week][RVT] is a very early research prototype.  It is not ready for serious use
and it is definitely not an official, supported Google product.  We are
releasing it now, in its current, immature state because we want to have
a conversation about how programmers want to formally verify Rust code
and we think that it is helpful to have something to push against.
We welcome pull requests that add support for other verifiers, or that
push the design in a better direction.]*


## A proptest test harness

To get an idea for what property testing looks like in `proptest`,
we'll look at an example from the [proptest book].

```rust
fn add(a: i32, b: i32) -> i32 {
    a + b
}

proptest! {
    #[test]
    fn test_add(a in 0..1000i32, b in 0..1000i32) {
        let sum = add(a, b);
        assert!(sum >= a);
        assert!(sum >= b);
    }
}
```

This example defines a property called `test_add` that tests a function called
`add`.  In particular, it checks that, for non-negative values `a` and `b`, the
result of `sum(a, b)` is at least as large as `a` and as `b`.

The notation `0..1000i32` represents the set of all values in the range `[0 ..
1000)` and the notation `a in 0..1000i32` says that a value `a` should be
chosen from that set.

The `proptest!` macro converts this property into a test function
that repeatedly generates random values for `a` and `b` and executes the
body of the property.

(After adding in [some additional glue code](https://altsysrq.github.io/proptest-book/proptest/tutorial/macro-proptest.html)) we can run this example with the command

```shell
cargo test
```

which produces the following output

```
running 1 test
test test_add ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

and, if we deliberately write a property that doesn't hold, then `cargo test`
produces output more like this

```
running 1 test
test test_add ... FAILED

failures:

---- test_add stdout ----
thread 'test_add' panicked at 'assertion failed: sum >= a + 100', src/main.rs:11:9
thread 'test_add' panicked at 'Test failed: assertion failed: sum >= a + 100; minimal failing input: a = 0, b = 0
        successes: 0
        local rejects: 0
        global rejects: 0
', src/main.rs:7:1


failures:
    test_add

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out
```

## Verifying with propverify

Proptest checks the above property by generating random values and testing.
But we can also interpret the property as saying that for all values
`a` and `b` in the sets, the body of the property will not panic.
That is, we can interpret it as a universally quantified specification.

To verify the above property, we use a script that compiles the Rust
code, invokes the [KLEE symbolic execution engine][KLEE] and filters
the output of KLEE to determine whether there is any choice of `a` and
`b` that can cause the body of the property to panic.

```shell
cargo-verify . --tests
```

This produces output like this: confirming that the property does hold

```
Running 1 test(s)
test test_add ... ok

test result: ok. 1 passed; 0 failed
VERIFICATION_RESULT: VERIFIED
```

And, if we change the example property so that the property does not hold,
`cargo-verify` produces this output.

```
thread 'test_add' panicked at 'assertion failed: sum >= a + 100', src/main.rs:11:9

running 1 test
  Value a = 0
  Value b = 0
test test_add ... FAILED

failures:

failures:
    test_add

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out
```

On this example, random testing and formal verification produced similar
results.
I could have chosen an example where formal verification found a bug that
random testing misses.
Or I could have chosen an example where random testing easily finds
a bug but formal verification spins forever.
But, in this post, I wanted to focus on the similarity between the two
approaches, not the differences.


## Learning more

In this article, we used an example that was easy to explain but
does not really show off the power of `propverify`.
Some slightly better examples are

* [collections.rs](https://github.com/project-oak/rust-verification-tools/blob/main/compatibility-test/src/collections.rs#L60)
  where we check properties involving standard Rust collection
  types such as vectors and B-trees.
  (This should be read in conjunction with the [proptest
  documentation](https://altsysrq.github.io/rustdoc/proptest/latest/proptest/collection/index.html).)

* [dynamic.rs](https://github.com/project-oak/rust-verification-tools/blob/0a6a0ff2b3880eb4a19d8161bfae8d163b0a65ec/compatibility-test/src/dynamic.rs#L82)
  where we check properties involving trait objects by
  quantifying over a subset of the possible instances of the trait.

And, we have more documentation about

* [Using the propverify library](https://github.com/project-oak/rust-verification-tools/blob/main/docs/using-propverify.md)

* [Using the lower level `verification-annotations` API](https://github.com/project-oak/rust-verification-tools/blob/main/docs/using-annotations.md)

* [The many, many flags we use when compiling Rust code so that it can be verified with KLEE](https://github.com/project-oak/rust-verification-tools/blob/main/docs/using-klee.md)

The latter two are mostly for the benefit of verification tool developers.


## Our next steps

*[You can either read this as a sketch of what we plan to do or
as an admission of what we have not yet done.
As [Fred and Ginger said](https://www.youtube.com/watch?v=LOILZ_D3aRg),
"Tomato. Tomato."]*

- The tools have a horrifically complicated set of dependencies.

  This is partly because formal verification is not quite popular
  enough for enough Debian/Homebrew packages to exist and partly
  because we need some very specific versions.
  (It may also be possible to remove some dependencies!)

- We are in the process of adding [Crux-MIR] support to the library
  and tool.
  Crux-MIR is a new part of Galois'
  [Software Analysis Workbench (SAW)](https://galois.com/project/software-analysis-workbench/)
  that verifies the MIR code generated by the Rust compiler.

  This is taking us a bit longer than using KLEE
  because the functionality of our `cargo-verify` script
  overlaps with the functionality of Crux-MIR but they have slightly different
  approaches – we're still working on the best way to handle the resulting
  conflicts.

- It can be useful to focus our attention on a single crate at a time.
  We have some ideas for how to do that with fuzzing and verification
  but we have not had a chance to try them yet.

- We have not looked seriously at how well this approach scales.

  The collections support in the `propverify` library has a few
  tricks to avoid some obvious scaling issues, but we don't know if
  those tricks work well for all verification tools and they
  probably only scratch the surface of what needs to be done.



## Summary

Testing and formal verification are usually portrayed as mortal enemies.
I think that misses a huge opportunity to use your existing familiarity and
comfort with testing to let you get value out of formal verification tools.

I encourage you to download [our library and tool][RVT],
try it out and give us feedback.
If you are working on a Rust verification tool, we would love it
if you tried to use our library with your tool.
And we would love it even more if you sent us a pull request.

It's probably not a good idea to commit to using the library at this stage:
it is not very robust at the moment and I expect that it will change a lot
as we gain experience from porting the library to other types of
formal verification tools.

Enjoy!

---------------

## More information

If you found this article interesting, you might also enjoy these related posts

* [Verification competitions]
* [Rust verification tools]

And these papers:

* The style of test used is a lot like [property-based testing]
  that started with [claessen:icfp:2000] for Haskell and has since spread
  to many other languages.

  In strongly-typed languages, property-based testing usually uses the type to
  determine how to generate values
  but proptest is inspired by MacIver's "Hypothesis" for Python [maciver:ecoop:2020]
  that provides a set of fuzzing-constructors ("strategies") for
  describing how to construct values and also to control "shrinking"
  (simplification) of random values.

* The general approach of using test harnesses with symbolic execution
  goes back (at least) as far as [tillmann:fse:2005] with
  more recent work by
  [garg:icse:2013] and [dimjasevic:ifm:2018].

* [goodman:ndss:2018] applied some very similar ideas to C++ testing
  in 2018 using the [GoogleTest] DSL as a starting point and providing
  support for [angr], [Manticore] and [Dr. Fuzz].

  They ran into and solved problems related to logging (causing a path
  explosion), symbolic loop bounds and symbolic array indices (causing
  a path explosion) and how to combine swarm testing with verification.

  Highly recommended!


---------------

[property-based testing]:    {{ site.baseurl }}/RelatedWork/notes/property-based-testing
[claessen:icfp:2000]:        {{ site.baseurl }}/RelatedWork/papers/claessen:icfp:2000
[dimjasevic:ifm:2018]:       {{ site.baseurl }}/RelatedWork/papers/dimjasevic:ifm:2018
[fonseca:ecs:2017]:          {{ site.baseurl }}/RelatedWork/papers/fonseca:ecs:2017
[garg:icse:2013]:            {{ site.baseurl }}/RelatedWork/papers/garg:icse:2013
[goodman:ndss:2018]:         {{ site.baseurl }}/RelatedWork/papers/goodman:ndss:2018
[maciver:ecoop:2020]:        {{ site.baseurl }}/RelatedWork/papers/maciver:ecoop:2020
[tillmann:fse:2005]:         {{ site.baseurl }}/RelatedWork/papers/tillmann:fse:2005
[verification competitions]: {% post_url 2020-04-19-verification-competitions %}
[Rust verification tools]:   {% post_url 2020-05-08-rust-verification-tools %}

[RVT]:           https://github.com/project-oak/rust-verification-tools
[proptest]:      https://github.com/AltSysrq/proptest
[Crux-MIR]:      https://github.com/GaloisInc/mir-verifier
[KLEE]:          https://klee.github.io
[proptest book]: https://altsysrq.github.io/proptest-book/proptest/tutorial/macro-proptest.html
[GoogleTest]:    https://github.com/google/googletest

[angr]:          https://angr.io
[Manticore]:     https://blog.trailofbits.com/2017/04/27/manticore-symbolic-execution-for-humans/
[Dr. Fuzz]:      https://dynamorio.org/drmemory_docs/page_drfuzz.html

[Hacker News]:   https://news.ycombinator.com/item?id=24372760

[Rust logo]: {{ site.baseurl }}/images/Rust_programming_language_black_logo.svg
