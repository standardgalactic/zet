---
title: Summarizing 12 months of reading papers (2021)
layout: post
---

Last year, I wrote [about the 122 papers that I read in my first year at Google][summary-2020]
and that I summarize on [the RelatedWork site][RelatedWork].
Over the last 18 months or so, I've spent a lot less time doing the one hour train commute between Cambridge and London
so I only read [59 papers][papers] in the last year and added 188 papers to the [backlog of unread papers][backlog].
You can read [my summaries of all the papers][RelatedWork],
read [notes on common themes in the papers][notes],
and download [BibTeX][bibfile] for all the papers.

*[Note that the main motivation for writing these paper summaries
is to help me learn new research fields.
So these summaries are usually not high quality reviews by an expert in the
field but, instead, me trying to make sense of a barrage of terminology,
notation and ideas as I try to figure out whether the paper is useful to my
work.
You should write your own summaries of any of the papers I list that sound interesting.]*


## Zettelkasten

I have found that a great way of organizing my thoughts about papers is as a
[Zettelkasten].  The basic structuring idea is based on creating links between
papers and concepts.  Every time I come across a new concept in a paper, I
create a new page about it and link the paper to that page.  Each paper,
concept or link added to the Zettelkasten refines my understanding of the
research field and that understanding is (partly) captured in the links between concepts,
between papers and between papers and concepts.
And since every page has back-references to the pages that link to it, I can
easily find related papers that have different views of a concept or that improve
upon an idea.

Last year, I had only just adopted the [Zettelkasten] concept and I was often not adding
new concept pages until after I came across the concept a second time.
This year, I have tried to be more aggressive about adding new concepts.
This has turned out to be much easier when I am reading papers in a completely new field
because my ignorance makes it easier to spot new concepts.
For example, when when I started reading about machine learning every page
I read had a bunch of new acronyms like RNN, CNN, ReLU or unfamiliar terms
like Softmax, Activation or Attention and I created pages for each of these concepts,
looked them up, linked to the wikipedia page (or similar) and linked the current
and later papers to the concept.

*[I wrote a lot more about Zettelkasten and the tools that support it [last year][summary-2020]]*


## Rust and verification

I spent most of the year working on the [Rust verification project]({{site.RVTurl}}/) at Google
so, unsurprisingly, many of the papers are about the [Rust language] with a bit of an emphasis around [Rust unsafe code].

- [Rust language]
  - Engineering the Servo web browser engine using Rust [<a href="{{site.RWurl}}/papers/anderson:icse:2016/">anderson:icse:2016</a>]
- [Rust unsafe code]
  - Safe systems programming in Rust: The promise and the challenge [<a href="{{site.RWurl}}/papers/jung:cacm:2021/">jung:cacm:2021</a>]
  - Understanding memory and thread safety practices and issues in real-world Rust programs [<a href="{{site.RWurl}}/papers/qin:pldi:2020/">qin:pldi:2020</a>]
  - How do programmers use unsafe Rust? [<a href="{{site.RWurl}}/papers/astrauskas:oopsla:2020/">astrauskas:oopsla:2020</a>]
  - Is Rust used safely by software developers? [<a href="{{site.RWurl}}/papers/evans:icse:2020/">evans:icse:2020</a>]
- [Phantom types]
  - GhostCell: Separating permissions from data in Rust [<a href="{{site.RWurl}}/papers/yanovski:unknown:2021/">yanovski:unknown:2021</a>]
  - Phantom types and subtyping [<a href="{{site.RWurl}}/papers/fluet:jfp:2006/">fluet:jfp:2006</a>]

Also, some pre-Rust papers that these papers build on.

- Dependent types for low-level programming [<a href="{{site.RWurl}}/papers/condit:esop:2007/">condit:esop:2007</a>]
- Quantifying the performance of garbage collection vs. explicit memory management [<a href="{{site.RWurl}}/papers/hertz:oopsla:2005/">hertz:oopsla:2005</a>]
- The meaning of memory safety [<a href="{{site.RWurl}}/papers/azevedo:post:2018/">azevedo:post:2018</a>]
- Checking type safety of foreign function calls [<a href="{{site.RWurl}}/papers/furr:pldi:2005/">furr:pldi:2005</a>]


## Symbolic execution, verification and testing

The [Rust verification project]({{site.RVTurl}}/)
focused on [creating a continuum of verification techniques and tools][Rust testing or verifying: why not both]
including fuzz-testing, concolic execution, symbolic execution, bounded model checking and abstract interpretation.

- [Performance and efficiency][Verifier performance]
  - QSYM: A practical concolic execution engine tailored for hybrid fuzzing [<a href="{{site.RWurl}}/papers/yun:usenix:2018/">yun:usenix:2018</a>]
  - Symbolic execution with SymCC: Don't interpret, compile! [<a href="{{site.RWurl}}/papers/poeplau:usenix:2020/">poeplau:usenix:2020</a>]
  - TracerX: Dynamic symbolic execution with interpolation [<a href="{{site.RWurl}}/papers/jaffar:arxiv:2020/">jaffar:arxiv:2020</a>]
  - Efficient state merging in symbolic execution [<a href="{{site.RWurl}}/papers/kuznetsov:pldi:2012/">kuznetsov:pldi:2012</a>]
  - Evaluating manual intervention to address the challenges of bug finding with KLEE [<a href="{{site.RWurl}}/papers/galea:arxiv:2018/">galea:arxiv:2018</a>]
  - Finding code that explodes under symbolic evaluation [<a href="{{site.RWurl}}/papers/bornholt:oopsla:2018/">bornholt:oopsla:2018</a>]
  - Chopped symbolic execution [<a href="{{site.RWurl}}/papers/trabish:icse:2018/">trabish:icse:2018</a>]
- [Hybrid fuzzing]
  - SAVIOR: Towards bug-driven hybrid testing [<a href="{{site.RWurl}}/papers/chen:sp:2020/">chen:sp:2020</a>]
- [Symbolic memory]
  - Rethinking pointer reasoning in symbolic execution [<a href="{{site.RWurl}}/papers/coppa:ase:2017/">coppa:ase:2017</a>]
  - A segmented memory model for symbolic execution [<a href="{{site.RWurl}}/papers/kapus:fse:2019/">kapus:fse:2019</a>]
- [Lazy initialization]
  - Generalized symbolic execution for model checking and testing [<a href="{{site.RWurl}}/papers/khurshid:tacas:2003/">khurshid:tacas:2003</a>]
  - Scalable error detection using boolean satisfiability [<a href="{{site.RWurl}}/papers/xie:popl:2005/">xie:popl:2005</a>]
  - Under-constrained symbolic execution: Correctness checking for real code [<a href="{{site.RWurl}}/papers/ramos:sec:2015/">ramos:sec:2015</a>]
  - Under-constrained execution: Making automatic code destruction easy and scalable [<a href="{{site.RWurl}}/papers/engler:issta:2007/">engler:issta:2007</a>]
  - Practical, low-effort equivalence verification of real code [<a href="{{site.RWurl}}/papers/ramos:cav:2011/">ramos:cav:2011</a>]
- [Swarming][Swarm verification]
  - Swarm verification techniques [<a href="{{site.RWurl}}/papers/holzmann:ieeetse:2011/">holzmann:ieeetse:2011</a>]
  - Swarm testing [<a href="{{site.RWurl}}/papers/groce:issta:2012/">groce:issta:2012</a>]
  - Scaling symbolic execution using ranged analysis [<a href="{{site.RWurl}}/papers/siddiqui:oopsla:2012/">siddiqui:oopsla:2012</a>]
  - A synergistic approach for distributed symbolic execution using test ranges [<a href="{{site.RWurl}}/papers/qiu:icse:2017/">qiu:icse:2017</a>]
- Vacuity checks
  - Sanity checks in formal verification [<a href="{{site.RWurl}}/papers/kupferman:concur:2006/">kupferman:concur:2006</a>]
- Counterexamples and test generation
  - Executable counterexamples in software model checking [<a href="{{site.RWurl}}/papers/gennari:vstte:2018/">gennari:vstte:2018</a>]
  - Formal specification and testing of QUIC [<a href="{{site.RWurl}}/papers/mcmillan:sigcomm:2019/">mcmillan:sigcomm:2019</a>]
- [Separation logic]
  - A local shape analysis based on separation logic [<a href="{{site.RWurl}}/papers/distefano:tacas:2006/">distefano:tacas:2006</a>]
  - Beyond reachability: Shape abstraction in the presence of pointer arithmetic [<a href="{{site.RWurl}}/papers/calcagno:sas:2006/">calcagno:sas:2006</a>]


## CPUs and security

- Microarchitecture
  - [Hardware faults]
    - Silent data corruptions at scale [<a href="{{site.RWurl}}/papers/dixit:arxiv:2021/">dixit:arxiv:2021</a>]
    - Cores that don't count [<a href="{{site.RWurl}}/papers/hochschild:hotos:2021/">hochschild:hotos:2021</a>]
  - [Power viruses][Power virus]
    - GeST: An automatic framework for generating CPU stress-tests [<a href="{{site.RWurl}}/papers/hadjilambrou:ispass:2019/">hadjilambrou:ispass:2019</a>]
  - [Side channels][Side channel]
    - Spectector: Principled detection of speculative information flows [<a href="{{site.RWurl}}/papers/guarnieri:sandp:2020/">guarnieri:sandp:2020</a>]
    - CacheQuery: Learning replacement policies from hardware caches [<a href="{{site.RWurl}}/papers/vila:pldi:2020/">vila:pldi:2020</a>]
- Security
  - CHERI concentrate: Practical compressed capabilities [<a href="{{site.RWurl}}/papers/woodruff:tocs:2019/">woodruff:tocs:2019</a>]
  - snmalloc: A message passing allocator [<a href="{{site.RWurl}}/papers/lietar:ismm:2019/">lietar:ismm:2019</a>]
  - PAC: Practical Accountability for CCF [<a href="{{site.RWurl}}/papers/shamis:arxiv:2021/">shamis:arxiv:2021</a>]
  - Toward confidential cloud computing: Extending hardware-enforced cryptographic protection to data while in use [<a href="{{site.RWurl}}/papers/russinovich:acmq:2021/">russinovich:acmq:2021</a>]
  

## [Neural networks / Machine learning][Neural network]

Since I work in a machine-learning part of Google, I have been reading about machine learning.

- Language and kernels
  - TensorFlow: Large-scale machine learning on heterogeneous distributed systems [<a href="{{site.RWurl}}/papers/abadi:arxiv:2016/">abadi:arxiv:2016</a>]
  - The tensor algebra compiler [<a href="{{site.RWurl}}/papers/kjolstad:oopsla:2017/">kjolstad:oopsla:2017</a>]
  - Sparse GPU kernels for deep learning [<a href="{{site.RWurl}}/papers/gale:arxiv:2020/">gale:arxiv:2020</a>]
- Hardware
  - In-datacenter performance analysis of a tensor processing unit [<a href="{{site.RWurl}}/papers/jouppi:isca:2017/">jouppi:isca:2017</a>]
  - SIGMA: A sparse and irregular GEMM accelerator with flexible interconnects for DNN training [<a href="/papers/qin:hpca:2020/">qin:hpca:2020</a>]
  - ExTensor: An accelerator for sparse tensor algebra [<a href="{{site.RWurl}}/papers/hedge:micro:2019/">hedge:micro:2019</a>]
- [Sparsity][Sparse model]
  - The state of sparsity in deep neural networks [<a href="{{site.RWurl}}/papers/gale:arxiv:2019/">gale:arxiv:2019</a>]
  - Fast sparse ConvNets [<a href="{{site.RWurl}}/papers/elsen:arxiv:2019/">elsen:arxiv:2019</a>]
- Scaling
  - Outrageously large neural networks: The sparsely-gated mixture-of-experts layer [<a href="{{site.RWurl}}/papers/shazeer:arxiv:2017/">shazeer:arxiv:2017</a>]
  - GShard: Scaling giant models with conditional computation and automatic sharding [<a href="{{site.RWurl}}/papers/lepikhin:arxiv:2020/">lepikhin:arxiv:2020</a>]
  - Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity [<a href="{{site.RWurl}}/papers/fedus:arxiv:2021/">fedus:arxiv:2021</a>]
  - Attention is all you need [<a href="{{site.RWurl}}/papers/vaswani:arxiv:2017/">vaswani:arxiv:2017</a>]

## [Information flow control]

- Noninterference for free [<a href="{{site.RWurl}}/papers/bowman:icfp:2015/">bowman:icfp:2015</a>]

## Programming languages

- The next 700 semantics: A research challenge [<a href="{{site.RWurl}}/papers/krishnamurthi:snapl:2019/">krishnamurthi:snapl:2019</a>]


## Miscellaneous

- Large teams have developed science and technology; small teams have disrupted it [<a href="{{site.RWurl}}/papers/wu:arxiv:2017/">wu:arxiv:2017</a>]
- As we may think [<a href="{{site.RWurl}}/papers/bush:atlantic:1945/">bush:atlantic:1945</a>]



[summary-2020]:               {% post_url 2020-10-04-a-year-of-papers %}
[Rust testing or verifying: why not both]: {% post_url 2020-09-03-why-not-both %}

[RelatedWork]:                {{site.RWurl}}
[bibfile]:                    {{site.RWurl}}/RelatedWork.bib
[papers]:                     {{site.RWurl}}/papers
[backlog]:                    {{site.RWurl}}/papers/#unsummarized
[notes]:                      {{site.RWurl}}/notes

[Hardware faults]:            {{site.RWurl}}/notes/hardware-faults/
[Hybrid fuzzing]:             {{site.RWurl}}/notes/hybrid-testing/
[Information flow control]:   {{site.RWurl}}/notes/information-flow/
[Lazy initialization]:        {{site.RWurl}}/notes/lazy-initialization/
[Neural network]:             {{site.RWurl}}/notes/neural-network/
[Power virus]:                {{site.RWurl}}/notes/power-virus/
[Phantom types]:              {{site.RWurl}}/notes/phantom-types/
[Rust language]:              {{site.RWurl}}/notes/rust-language/
[Rust unsafe code]:           {{site.RWurl}}/notes/rust-unsafe-code/
[Separation logic]:           {{site.RWurl}}/notes/separation-logic/
[Side channel]:               {{site.RWurl}}/notes/side-channel/
[Sparse model]:               {{site.RWurl}}/notes/sparse-model/
[Swarm verification]:         {{site.RWurl}}/notes/swarm-verification/
[Symbolic memory]:            {{site.RWurl}}/notes/symbolic-memory/
[Verifier performance]:       {{site.RWurl}}/notes/verifier-performance/

[the morning paper]:          https://blog.acolyer.org
[Zettelkasten]:               https://zettelkasten.de/posts/zettelkasten-improves-thinking-writing
