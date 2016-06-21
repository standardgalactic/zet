#!/usr/bin/env python

import json

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogeneize_latex_encoding
from bibtexparser.customization import convert_to_unicode

with open('_data/papers.json') as data_file:
    extra = json.load(data_file)
    with open('_data/biblio.bib') as bibtex_file:
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
