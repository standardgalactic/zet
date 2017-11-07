---
layout: page
title: Papers and Patents
permalink: /papers/
---

* Table of contents
{:toc}

My [Google Scholar](http://scholar.google.co.uk/citations?hl=en&user=oT8RhJgAAAAJ)
and
[DBLP](http://dblp.uni-trier.de/pers/hd/r/Reid:Alastair_David)
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

### How can you trust formally verified software?

A gradually evolving series of talks about my work on creating
correct formal specifications (when there are multiple implementations
already in existence).
Reinforces the idea of having multiple users of a single specification and
includes a short version of the FMCAD16, CAV16 and OOPSLA17 talks.

  - High Performance Embedded and Distributed Systems (HiPEDS) seminar series
    <br>
    Invited talk,
    Imperial College London, UK,
    6th November, 2017.
    [[pdf](/papers/trusting-verified-software-ICL-2017-11-06.pdf)]

  - [Formal Aspects of Computing Science (British Computer Society)](https://www.bcs.org/content/ConWebDoc/58298)
    <br>
    Invited talk,
    London, UK,
    29th September, 2017.
    [[pdf](/papers/trusting-verified-software-BCS-2017-09-29.pdf)]

  - [Reliable, Secure and Scalable Software Systems (RS4) Workshop](https://www.sicsa.ac.uk/events/reliable-secure-scalable-software-systems-rs4-workshop/)
    <br>
    Invited talk,
    Glasgow, UK,
    1st September, 2017.
    [[pdf](/papers/trusting-verified-software-GLA-2017-09-01.pdf)]
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
    [[pdf](/papers/trusting-verified-software-CUCL-2017-05-02.pdf)]

  - Queen Mary University
    <br>
    Invited talk,
    London, UK,
    30th November, 2016.
    [[pdf](/papers/trustworthy-specs-QMU-2016-11-30.pdf)]

### Trusting Large Specifications: The Virtuous Cycle

First talk emphasizing the importance of having multiple users of a single
specification.

  - [The 4th South of England Regional Programming Language Seminar (S-REPLS 4)](http://srepls4.doc.ic.ac.uk/abstracts/reid/)
    <br>
    Imperial College London, UK,
    27th September, 2016.
    [[pdf](/papers/srepls4-trustworthy.pdf)]


### Trustworthy Specifications of ARM System Level Architecture

  - [First Deepspec Workshop](https://deepspec.org/events/workshop2016/index.html),
    Princeton, NJ, USA,
    7th June, 2016.


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
