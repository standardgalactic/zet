---
layout: page
title: Publications
permalink: /papers/
---

(my [Google Scholar](http://scholar.google.co.uk/citations?hl=en&user=oT8RhJgAAAAJ)
and
[DBLP](http://dblp.uni-trier.de/pers/hd/r/Reid:Alastair_David)
pages)

{% for paper in site.data.biblio %}
  <div class="biblio">
    <a href="{{ site.baseurl }}/papers/{{ paper.file }}">{{ paper.title }}</a>
    <br>
    {{ paper.author }},
    <br>
    {% if paper.booktitle %} In <i>{{ paper.booktitle }}</i>, {% endif %}
    {% if paper.acceptance %} {{ paper.acceptance }}% acceptance rate, {% endif %}
    {% if paper.journal %} {{ paper.journal }}, {% endif %}
    {% if paper.number %} {{ paper.number }}, {% endif %}
    {% if paper.publisher %} {{ paper.publisher }}, {% endif %}
    {% if paper.pages %} pp. {{ paper.pages }}, {% endif %}
    {{ paper.year }}.
    {% if paper.doi %} doi: <a href="{{ paper.link }}">{{ paper.doi }}</a>
    {% elsif paper.link %} url: <a href="{{ paper.link }}">{{ paper.link }}</a>
    {% endif %}
    <br>
    <br>
  </div>
{% endfor %}

Lock inference for systems software
Proceedings of the Second AOSD Workshop on Aspects, Components, and Patterns
for Infrastructure Software (ACP4IS), 2003
Authors:  John Regehr, Alastair Reid

The Hugs Graphics Library
2002
Authors: Alastair Reid

Aspect Weaving as Component Knitting: Separating Concerns with Knit
Workshop on Advanced Separation of Concerns in Software Engineering, 2001
Authors: Alastair Reid

Handling Exceptions in Haskell
1999
Authors: Alastair Reid

Adding Records to Haskell
1998
Authors: Alastair Reid, John Peterson

Green Card: a foreign-language interface for Haskell
Proceedings of the Haskell Workshop, Amsterdam, June 1997, January 1997
Authors: Alastair Reid, Thomas Nordin, Simon Peyton Jones

Malloc Pointers and Stable Pointers: Improving Haskell's Foreign Language
Interface
Proceedings of Glasgow Functional Programming Workshop, 1994
Authors: Alastair Reid

Implementing Fudgets with Standard Widget Sets
Proceedings of Glasgow Functional Programming Workshop, 1993
Authors: Alastair Reid, Satnam Singh

