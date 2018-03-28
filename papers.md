---
layout: page
title: Papers, Talks and Patents
permalink: /papers/
---

* Table of contents
{:toc}

My [Google Scholar](https://scholar.google.co.uk/citations?hl=en&user=oT8RhJgAAAAJ),
[DBLP](http://dblp.uni-trier.de/pers/hd/r/Reid:Alastair_David) and
[Microsoft Academic](https://academic.microsoft.com/#/detail/2293162450)
pages.

## Papers

<table>
{% for paper in site.data.biblio %}
    <tr valign="top">
        <td align="right" class="bibtexnumber" style="padding: 10px;">
            <a class="papertitle" href="{{ site.baseurl }}/papers/{{ paper.ar_file }}">{{ paper.ar_shortname | replace:' ','&nbsp;'}}</a>
        </td>
        <td class="bibtexitem">
            {{ paper.ar_title }}
        </td>
    </tr>
{% endfor %}
</table>


## Talks

<h3>Creating Specifications of Real World Artifacts (provisional title)</h3>

_Creating formal specifications for real world systems is hard because there are
usually many existing implementations that it will not be practical to formally
verify against the formal specification you create.
This talk is about lessons learned when creating a formal specification of the Arm
Processor Architecture and how those lessons can be applied in other contexts._

  - [ACL2 Workshop](http://www.cs.utexas.edu/users/moore/acl2/workshop-2018/index.html)
    <br>
    Invited keynote talk,
    Austin, Texas, USA.
    5-6 November, 2018.

  - [Austrian Computer Science Day](https://arise.or.at/2018/01/austrian-computer-science-day-june-2018-salzburg/)
    <br>
    Invited talk,
    Salzburg, Austria.
    15 June, 2018.

  - [OAuth Security Workshop](https://st.fbk.eu/osw2018)
    <br>
    Invited keynote talk,
    Fondazione Bruno Kessler, Trento, Italy.
    14-16 March, 2018.
    [[pdf](/talks/real-world-artifacts-OSW-2018-03-15.pdf)]

<h3>Specifications: The Next Verification Bottleneck</h3>

_A talk about the importance and difficulty of creating trustworthy specifications of all
the software and protocols we will need to verify software and about the
techniques I used to create a trustworthy specification of the ARM processor
architecture._

  - [ENTROPY 2018: ENabling TRust through Os Proofs...and beYond](https://entropy2018.sciencesconf.org)
    <br>
    Invited talk,
    Villeneuve d'Ascq, France,
    25-26 January, 2018.
    [[pdf](/talks/specs-the-next-bottleneck-ENTROPY-2018-01-26.pdf)]

<h3>How can you trust formally verified software?</h3>

_A talk about practical things you can do with ARM's executable formal
specification with an emphasis on security research.
Despite having the same title, this is a completely different talk from the next one._
TUWAT!

  - [Chaos Communication Congress (34C3)](https://events.ccc.de/congress/2017/wiki/index.php/Main_Page)
    <br>
    [CCC](https://ccc.de/en/),
    Leipzig, Germany,
    27-30 December, 2017.
    [[video](https://media.ccc.de/v/34c3-8915-how_can_you_trust_formally_verified_software)]
    [[pdf](/talks/using-arm-specs-34C3-2017-12-27.pdf)]

<h3>How can you trust formally verified software?</h3>

_A gradually evolving series of talks about my work on creating
correct formal specifications (when there are multiple implementations
already in existence).
Reinforces the idea of having multiple users of a single specification and
includes a short version of the FMCAD16, CAV16 and OOPSLA17 talks._

  - High Performance Embedded and Distributed Systems (HiPEDS) seminar series
    <br>
    Invited talk,
    Imperial College London, UK,
    6th November, 2017.
    [[pdf](/talks/trusting-verified-software-ICL-2017-11-06.pdf)]

  - [Formal Aspects of Computing Science (British Computer Society)](https://www.bcs.org/content/ConWebDoc/58298)
    <br>
    Invited talk,
    London, UK,
    29th September, 2017.
    [[pdf](/talks/trusting-verified-software-BCS-2017-09-29.pdf)]

  - [Reliable, Secure and Scalable Software Systems (RS4) Workshop](https://www.sicsa.ac.uk/events/reliable-secure-scalable-software-systems-rs4-workshop/)
    <br>
    Invited talk,
    Glasgow, UK,
    1st September, 2017.
    [[pdf](/talks/trusting-verified-software-GLA-2017-09-01.pdf)]
    <br>
    (Completely rewritten from May version.)

  - Microsoft Research
    <br>
    Invited talk,
    Cambridge, UK,
    22nd May, 2017.

  - [Cambridge University Computer Laboratory](http://talks.cam.ac.uk/talk/index/72325)
    <br>
    Cambridge, UK,
    2nd May, 2017.
    [[pdf](/talks/trusting-verified-software-CUCL-2017-05-02.pdf)]

  - Queen Mary University
    <br>
    Invited talk,
    London, UK,
    30th November, 2016.
    [[pdf](/talks/trustworthy-specs-QMU-2016-11-30.pdf)]

<h3>Trusting Large Specifications: The Virtuous Cycle</h3>

_First talk emphasizing the importance of having multiple users of a single
specification._

  - [The 4th South of England Regional Programming Language Seminar (S-REPLS 4)](http://srepls4.doc.ic.ac.uk/abstracts/reid/)
    <br>
    Imperial College London, UK,
    27th September, 2016.
    [[pdf](/talks/srepls4-trustworthy.pdf)]


<h3>Trustworthy Specifications of ARM System Level Architecture</h3>

  - [First Deepspec Workshop](https://deepspec.org/events/workshop2016/index.html),
    Princeton, NJ, USA,
    7th June, 2016.

<h3>Backwards compatible formalization of the ARM Architecture</h3>

_First public talk about creating formal specifications of ARM processors._

  - Cambridge University Computer Laboratory
    <br>
    Cambridge, UK,
    February, 2012.
    [[pdf](/talks/bottom-up-formalization-CUCL-2012-02.pdf)]


## Patents

<table>
{% for paper in site.data.patents %}
    <tr valign="top">
        <td align="right" class="bibtexnumber" style="padding: 10px;">
            {% if paper.link %}
                <a class="papertitle" href="{{ paper.link }}">{{ paper.number | replace:' ','&nbsp;'}}</a>
            {% else %}
                {{ paper.number | replace:' ','&nbsp;'}}
            {% endif %}
        </td>
        <td class="bibtexitem">
            {{ paper.title }}
            <br>
            {{ paper.author }},
            {{ paper.location }}
            {{ paper.type }},
            {{ paper.month }}
            {{ paper.year }}
        </td>
    </tr>
{% endfor %}
</table>
