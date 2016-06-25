#!/usr/bin/env python

import json
import sys

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogeneize_latex_encoding
from bibtexparser.customization import convert_to_unicode

extra = sys.argv[1]
bib   = sys.argv[2]

with open(extra) as data_file:
    extra = json.load(data_file)
    with open(bib) as bibtex_file:
        parser = BibTexParser()
        # parser.customization = homogeneize_latex_encoding
        parser.customization = convert_to_unicode
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

        papers = bib_database.entries

        # Apply minor cleanups to the data: removing {}, newline, adding a file
        for paper in papers:
            for key, value in paper.iteritems():
                paper[key] = value.replace("{", "").replace("}", "").replace("\n", " ")
            paper['author'] = paper['author'].replace(" and ", ", ")
            if paper['ID'] in extra:
                info = extra[paper['ID']]
                paper['file'] = info['file']

        # print(papers)
        print(json.dumps(papers))
