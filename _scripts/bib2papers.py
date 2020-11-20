#!/usr/bin/env python3

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.customization import homogenize_latex_encoding
from bibtexparser.customization import convert_to_unicode

import json
from yaml import dump
from yaml import Dumper

import sys

def toString(e):
    writer = BibTexWriter()
    writer.indent = '    '     # indent entries with 4 spaces instead of one
    writer.comma_first = True  # place the comma at the beginning of the line

    return writer._entry_to_bibtex(e)

def parseEntry(s):
    # normalize unicode by reparsing
    parser = BibTexParser()
    parser.customization = convert_to_unicode
    db1 = bibtexparser.loads(s, parser=parser)
    es = db1.entries
    return es[0]

extra = sys.argv[1]
with open(extra) as data_file:
    extra = json.load(data_file)

bib = sys.argv[2]
with open(bib) as bibtex_file:
    parser = BibTexParser()
    parser.customization = homogenize_latex_encoding
    db = bibtexparser.load(bibtex_file, parser=parser)

for e in db.entries:
    if 'url' in e: e['link'] = e['url'] # default link

    if e['ID'] in extra:
        info = extra[e['ID']]
        link = info['file'] if 'file' in info else info['slides']
        e['file'] = link
        e['png'] = link.replace(".pdf", ".png")
        if 'slides' in info: e['slides'] = info['slides']
        if 'video' in info: e['video'] = info['video']

    name = e['ar_shortname']
    filename = name.replace(' ','_').replace('-','_')
    e['ar_file'] = filename
    filename = '_papers/' + filename + '.md'

    s = toString(e)
    s = s.replace("\\textquotesingle ", "'")
    s = s.replace("\\textasciigrave ", "`")
    # print(s)
    e2 = parseEntry(s)
    e2['bibtex'] = s

    v = e2['title']
    v = v.replace('\n',' ')
    v = v.replace("{", "").replace("}", "")
    v = v.replace("' ", "'")
    # print(v)
    e['ar_title'] = v
    v = v.replace(": ", " - ")
    e2['title'] = v

    # print(toString(e2))
    # print(dump(e, Dumper=Dumper))
    with open(filename, 'w') as file:
        file.write("---\n")
        file.write("layout: paper\n")
        for k,v in e2.items():
            if k == 'author': v = v.replace('\n',' ').replace(' and ', ', ')
            if k == 'editor': v = v.replace('\n',' ').replace(' and ', ', ')
            if k == 'abstract' or k == 'bibtex':
                v = v.rstrip().split('\n\n')
                v = '\n<p>\n'.join(v)
                v = v.split('\n')
                v = '|\n    ' + ('\n    '.join(v))
            elif 'http' in v: # don't mess with : in urls
                v = v.replace('~ ','~')
                pass
            else:
                v = v.replace('\n',' ')
                v = v.replace("{", "").replace("}", "")
                v = v.replace(":", "")
            file.write(k + ": " + v +"\n")
        file.write("---\n")

print(json.dumps(db.entries, indent=4))

# with open('normalized.bib', 'w') as bibfile:
#     bibfile.write(writer.write(db))
