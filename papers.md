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

{% for paper in site.data.talks %}
  <div class="biblio">
    <a class="papertitle" href="{{ site.baseurl }}/papers/{{ paper.slides }}">{{ paper.title }}</a>
    <br>
    {% if paper.link %}
        <a href="{{ paper.link }}">{{ paper.venue }}</a>
    {% else %}
        {{ paper.venue }},
    {% endif %}
    <br>
    {{ paper.city }},
    {{ paper.day }} {{ paper.month }}, {{ paper.year }}.
    <br>
    <br>
  </div>
{% endfor %}


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
