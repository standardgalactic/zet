---
title: "Rust Design-for-Testability: a survey"
layout: post
---

What can we do when designing Rust code to make it easier to test?
This is a survey of everything I could find[^survey-method] about
testing Rust with a particular focus on design for testability for
correctness.  Some of the articles show multiple things to do on a
worked example, some are more focused on a particular trick.

[^survey-method]:
     By “everything I could find”, I mean that I searched for terms
     relating to “design for test”, “testability”, “Rust”, etc. and
     followed links in other blogs. I also searched the archives of
     “[This week in Rust](https://this-week-in-rust.org/)” for the
     word “test” and followed any promising links.

There doesn’t seem to be a single place that describes all the testing
ideas: it is scattered across book chapters, blog articles, medium
articles, etc. but here are the main sources that I have found.

*   [The Rust book](https://doc.rust-lang.org/book/ch11-01-writing-tests.html) chapter on testing
*   [Testing command line applications in Rust](https://rust-cli.github.io/book/tutorial/testing.html)
    (significant overlap with the [Rust book](https://doc.rust-lang.org/book/ch11-01-writing-tests.html))
*   [How to organize your Rust tests](https://blog.logrocket.com/how-to-organize-your-rust-tests/)
    Probably the most exhaustive / thorough
*   [Testing sync at Dropbox](https://dropbox.tech/infrastructure/-testing-our-new-sync-engine) --
    what they did in their Rust rewrite to improve testability
*   [Rust by example book](https://doc.rust-lang.org/stable/rust-by-example/testing.html) chapter on testing
*   [Writing fuzzable code](https://blog.regehr.org/archives/1687) --
    John Regehr’s blog (not specifically about Rust)
*   [Testable Component Design in Rust](https://www.zcfy.cc/original/testable-component-design-in-rust-iextendable)
*   [Rust 2020: Testing](https://knowitlabs.no/rust-2020-testing-4ab3d80112ba)
*   [How to use the Rust compiler as your integration testing framework](https://blog.logrocket.com/using-the-rust-compiler-as-your-integration-testing-framework/)
*   [Awesome Rust: Testing](https://github.com/rust-unofficial/awesome-rust#testing) (collection of links)
*   [Writing Correct, Readable and Performant (CRaP) Rust code](https://blog.logrocket.com/how-to-write-crap-rust-code/)
*   [Rust testing tricks](https://blog.cyplo.dev/posts/2018/09/rust-testing-tricks/)
*   [Awesome Rust: testing tools/libraries](https://github.com/rust-unofficial/awesome-rust#testing)
*   [A practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) -- Martin Fowler’s blog (not specifically about Rust)

I am not going to try to summarize what these sources say: the rest of
this post is a list of some common / interesting topics and which of
these sources describe it in more detail.

Although my main focus is on how to write Rust programs so that they are easy
to test, I touch on the other half of the problem: how to do the testing.



*[I am new to Rust and my own testing habits are somewhat ad-hoc so this is
definitely not a recommendation of how to write software by me.  I hope it is
useful and that you will tell me what I have missed
[on twitter](https://twitter.com/alastair_d_reid) or
[by email](mailto:alastair.d.reid@gmail.com)
so that I can update this post.
I would love to hear about any team that has published recommendations for
design-for-testability.]*


## Design techniques for improving testability

The sources listed above have a bunch of common suggestions that I
explore in more detail below. Many of the sources I found have great
discussions so I will not try to repeat their explanations in this
document but will link to some of the better discussions of each idea
that I found.


### Use intermediate data structures

See:
[Testing sync](https://dropbox.tech/infrastructure/-testing-our-new-sync-engine),
[Rust book](https://doc.rust-lang.org/book/ch11-01-writing-tests.html),
[Testing CLI applications](https://rust-cli.github.io/book/tutorial/testing.html),
[use the Rust compiler for integration testing](https://blog.logrocket.com/using-the-rust-compiler-as-your-integration-testing-framework/)

*   Use intermediate data structures to separate deciding what to do
    from performing the action: allowing tests to check that the right
    decision is being made and avoiding the need to mock/fake the
    filesystem, etc.
*   Aggressively use newtypes, structs, enums
*   Parse and validate inputs early (eg convert strings to enums)
*   Also, #[must\_use], parse/validate early
*   [Writing I/O-Free (Sans-I/O) Protocol Implementations](https://sans-io.readthedocs.io/how-to-sans-io.html) (not Rust specific)


### Abstract testable code into separate functions

See:
[Rust book](https://doc.rust-lang.org/book/ch11-01-writing-tests.html),
[Testing CLI applications](https://rust-cli.github.io/book/tutorial/testing.html)

*   Cleanly separate command line parsing from code that implements functionality


### Abstract I/O and state side effects out of functions

See:
[Testing CLI applications](https://rust-cli.github.io/book/tutorial/testing.html),
[Writing fuzzable code](https://blog.regehr.org/archives/1687),
[Testing sync](https://dropbox.tech/infrastructure/-testing-our-new-sync-engine)

*   Use of std::io::Write trait and writeln! instead of println! (and handle resulting potential error)


### Avoid / reduce non-determinism

See:
[Testing sync](https://dropbox.tech/infrastructure/-testing-our-new-sync-engine),
[Writing fuzzable code](https://blog.regehr.org/archives/1687)

*   Use Futures with a custom executor to eliminate the
    non-determinism of threads
*   All randomized testing systems should be fully deterministic
    and easily reproducible
*   Beware of additional randomness in libraries:
    e.g., Rust’s HashMap uses randomized hashing to protect against denial of service attacks.
    This makes testing harder.
*   Determinism enables minimization of random tests
    (cf. [proptest](https://altsysrq.github.io/proptest-book/proptest/tutorial/shrinking-basics.html))


### Defining correct behavior

See:
[Writing fuzzable code](https://blog.regehr.org/archives/1687)

*   [Oracles for random testing](https://blog.regehr.org/archives/856) (not Rust specific)
    *   Use Function inverse pairs (eg print/parse functions)
    *   Compare two implementations
*   Use asserts liberally
*   Turn on sanitizers (todo: how do you do this in Rust?)
*   [Contracts.rs](https://docs.rs/contracts/0.6.0/contracts/)
    / [(crates.io link)](https://crates.io/crates/contracts) -- code contract library
*   [inactive?] [libhoare](https://github.com/nrc/libhoare) compiler plugin


### Dependency injection and mock testing

See:
[Rust 2020: Testing](https://knowitlabs.no/rust-2020-testing-4ab3d80112ba),
[Testable Component Design in Rust](https://www.zcfy.cc/original/testable-component-design-in-rust-iextendable)

*   Abstraction can be based on Higher order functions or objects
*   Traits and [mockall](https://github.com/asomers/mockall)
*   Module mocks using [mocktopus](https://github.com/CodeSandwich/Mocktopus)


### API design

See:
[Testing CLI applications](https://rust-cli.github.io/book/tutorial/testing.html),
[Rust API guidelines](https://rust-lang.github.io/api-guidelines/about.html),
[If you use Unsafe, …](http://erickt.github.io/blog/2015/09/22/if-you-use-unsafe/),
[Testable Component Design](https://www.zcfy.cc/original/testable-component-design-in-rust-iextendable),
[Writing Correct, Readable and Performant (CRaP)](https://blog.logrocket.com/how-to-write-crap-rust-code/)

API design strongly affects testability of that API

*   The component should provide a stable contract composed of traits, structs, and enums
*   Always implement Clone and fmt::Debug for public types
    *   types like failure::Error should be converted to something that is cloneable
*   Use ‘newtype’ to let the type system statically test for errors and use
    [compiletest.rs](https://github.com/laumann/compiletest-rs) to test that this is done correctly
*   Use #![warn(missing\_doc\_code\_examples)]
    (and other [Rust API guidelines](https://rust-lang.github.io/api-guidelines/about.html))


## Writing tests

See:
[How to organize your Rust tests](https://blog.logrocket.com/how-to-organize-your-rust-tests/),
[Testing CLI applications](https://rust-cli.github.io/book/tutorial/testing.html),
[Rust by example](https://doc.rust-lang.org/stable/rust-by-example/testing.html),

Having structured your software to enable tests, there are a lot of
different tools and libraries to support writing tests.

*   Documentation tests
*   [How to organize your Rust tests](https://blog.logrocket.com/how-to-organize-your-rust-tests/)
*   [Fuzzing book](https://rust-fuzz.github.io/book/):
    describes use of [cargo-fuzz](https://rust-fuzz.github.io/book/cargo-fuzz.html)
    and [afl.rs](https://github.com/rust-fuzz/afl.rs).
    See: [Rust Fuzzing Authority](https://github.com/rust-fuzz)
*   Use [QuickCheck](https://docs.rs/quickcheck) or [proptest](https://docs.rs/proptest)
    for generative testing / property-based testing
*   Unit tests vs integration tests
*   Using [assert\_cmd](https://docs.rs/assert_cmd) crate to test applications
    (link has links to other useful crates)
*   [anyhow crate](https://docs.rs/anyhow/1.0.33/anyhow/) -- adding context to error messages
*   Use the {:?} and {:x?} Debug string formats in test harnesses
    (see [std/fmt](https://doc.rust-lang.org/std/fmt/#formatting-traits))
*   [Rutenspitz](https://github.com/jakubadamw/rutenspitz):
    procedural macros for testing (fuzzing) equivalence of two
    stateful models (e.g., data structures)


### Test / Behavior driven design (TDD and BDD)

See: [Rust testing tricks](https://blog.cyplo.dev/posts/2018/09/rust-testing-tricks/),
[From @test to #[test]: Java to Rust](https://mateuscosta.me/testing-between-java-and-rust)

Obviously, there are many, many articles about TDD, BDD, Agile, etc.
in the context of Java and other OO languages. The following links are
Rust specific but they are a bit random and need to be improved.

*   [Laboratory.rs](https://crates.io/crates/laboratory) --
    BDD-inspired test library (todo: are other BDD libraries maybe more popular?)
*   [Speculate](https://github.com/utkarshkukreti/speculate.rs)
    RSpec inspired testing library
*   Fluent assertions: [spectral](https://github.com/cfrancia/spectral)
    (last updated 2017)
*   [TDD with Rust](https://matthewkmayer.github.io/blag/public/post/tdd-with-rust/) (2017) –
    a small example


## Specific topics

Note: links in this section are more likely to be out of date.

### Code coverage

*   [cov-mark crate](https://crates.io/crates/cov-mark) --
    adding explicit coverage annotations to code
    ([blog](https://matklad.github.io/2018/06/18/a-trick-for-test-maintenance.html),
    [blog](https://ferrous-systems.com/blog/coverage-marks/))
*   Code coverage tools and crates
    *   [Grcov](https://github.com/mozilla/grcov) -- Mozilla’s coverage tool
    *   [cargo-cov](https://github.com/kennytm/cov)
    *   [Tarpaulin](https://crates.io/crates/cargo-tarpaulin) (x86 only)
*   [Measuring test coverage of Rust programs](https://jbp.io/2017/07/19/measuring-test-coverage-of-rust-programs.html)
    (I think it is now easier than in 2017?)
*   [Rust Code Coverage Guide: kcov + Travis CI + Codecov / Coveralls](https://sunjay.dev/2016/07/25/rust-code-coverage) (2016)


### Testing embedded systems

*   [Using `cargo test` for embedded testing with `panic-probe`](https://ferrous-systems.com/blog/cargo-test-with-panic-probe/)
*   [defmt, a highly efficient Rust logging framework for embedded devices](https://ferrous-systems.com/blog/defmt/):
    a deferred formatting library that encodes I/O over a hardware trace port to reduce binary size on embedded systems
*   [Test setup/teardown without a framework](https://medium.com/@ericdreichert/test-setup-and-teardown-in-rust-without-a-framework-ba32d97aa5ab) --
    using [panic::catch\_unwind](https://doc.rust-lang.org/std/panic/fn.catch_unwind.html)
*   [RFC 2318: Custom test frameworks](https://github.com/rust-lang/rfcs/blob/master/text/2318-custom-test-frameworks.md) --
    [now in unstable](https://doc.rust-lang.org/beta/unstable-book/language-features/custom-test-frameworks.html)
*   [Writing an OS in Rust: testing](https://os.phil-opp.com/testing/) (uses custom test frameworks)
*   [Utest](https://github.com/japaric/utest) (is this still active?)


### Concurrency, futures and async

*   [Two easy ways to test async functions in Rust](https://blog.x5ff.xyz/blog/async-tests-tokio-rust/)
*   [Async book -- testing a web server](https://rust-lang.github.io/async-book/09_example/03_tests.html)
*   [Tokio-test](https://crates.io/crates/tokio-test)
    ([docs](https://docs.rs/tokio-test/0.3.0/tokio_test/index.html))
*   [actix async example](https://github.com/actix/examples/blob/master/hello-world/src/main.rs)
*   [Our first integration test](https://www.lpalmieri.com/posts/2020-08-09-zero-to-production-3-how-to-bootstrap-a-new-rust-web-api-from-scratch/#4-our-first-integration-test) --
    Actix\_rt::test based chapter in book [Zero to production in Rust (book)](https://zero2prod.com/)


### Testing frameworks

*   [Serializing Rust tests](https://tech.labs.oliverwyman.com/blog/2019/01/14/serialising-rust-tests/)
    ([github](https://github.com/palfrey/serial_test)) --
    annotations to prevent some tests being run in parallel
*   [Skeptic](https://github.com/budziq/rust-skeptic) --
    run doctest-like tests on README.md
*   [Trust automated test runner](https://github.com/Wmaxlees/trust): reruns tests when files change
*   [Test-case](https://crates.io/crates/test-case)
    procedural macro to generate tests from test-case annotations
*   [Artifact (aka RST)](https://github.com/vitiral/artifact) --
    requirement tracking software where comments in code are linked (in lightweight way) to
    requirements, specs and tests in a markdown document
*   [Fake.rs](https://github.com/cksac/fake-rs) --
    interesting #derive option to describe how to generate fake values for structs.
    Can this be adapted to specify invariants for legal values of a type?


### Testing GUIs

*   [Gtk-rs testing](https://gtk-rs.org/blog/2018/05/02/who-talked-about-testing.html):
    testing UIs by being able to send events to gtk and observe results
*   [Dinghy: testing iOS and Android](https://medium.com/snips-ai/dinghy-painless-rust-tests-and-benches-on-ios-and-android-c9f94f81d305):
    challenges when you don’t have a command line


### Testing APIs

*   [Compiletest.rs](https://github.com/laumann/compiletest-rs) -- for testing compiler plugins and similar
    *   In particular, checking that type system (etc) rejects misuse of APIs:
        [If you use unsafe ...](http://erickt.github.io/blog/2015/09/22/if-you-use-unsafe/)
*   [Rust API guidelines](https://rust-lang.github.io/api-guidelines/about.html)
    (not so much about testing here -- but useful)


### Mutation testing

*   [Mutagen](https://github.com/llogiq/mutagen) --
    mutation testing tool implemented using procedural macros


### Test generation

*   [Writing a testcase generator for a programming language](https://fitzgeraldnick.com/2020/08/24/writing-a-test-case-generator.html)
    Generate random wasm with “wasm-smith” in Rust


### Mocking libraries

There are _a lot_ of mocking / faking libraries -- this is a limited
list of what I found.

*   [Rust mock shootout](https://asomers.github.io/mock_shootout/):
    a fairly thorough survey of Rust mocking libraries.
    This lead to the development of
    [mockall](https://github.com/asomers/mockall)
    that is one of (the?) most popular mocking library.
*   [mockall](https://github.com/asomers/mockall) mocking library
*   [mocktopus](https://github.com/CodeSandwich/Mocktopus)
*   [Httpmock](https://docs.rs/httpmock/0.5.0/httpmock/)
*   [Partial-io](https://lib.rs/crates/partial-io)
    wraps Read/Write implementations, optional Future and quickcheck support


### Error handling

See:
[CLI applications in Rust](https://rust-cli.github.io/book/tutorial/errors.html),
[Structuring and using errors in 2020](https://nick.groenen.me/posts/rust-error-handling/)

Not quite about testing -- but semi-relevant.

*   Use of ?
*   [Anyhow](https://docs.rs/anyhow/1.0.33/anyhow/) -- adding context to error messages
*   [Error handling survey](https://blog.yoshuawuyts.com/error-handling-survey/)


## More information

My interest in Rust testing is a hope/belief that a good way of making formal
verification more accessible to software developers is to build on what they
are already familiar with: testing.
I described this [last month][Rust testing or verifying: Why not both].

If you found this article interesting, you might also enjoy these related posts

* [Rust testing or verifying: Why not both]
* [Rust verification tools]
* [Verification competitions]

---

[verification competitions]: {% post_url 2020-04-19-verification-competitions %}
[Rust verification tools]:   {% post_url 2020-05-08-rust-verification-tools %}
[Rust testing or verifying: why not both]: {% post_url 2020-09-03-why-not-both %}


