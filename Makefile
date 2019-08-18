# Begin

PDFS = $(wildcard papers/*.pdf)
THUMBS = $(PDFS:.pdf=.png)

test:
	echo $(PDFS)
	echo $(THUMBS)

all: _data/biblio.json
all: _data/patents.json
all: thumbs

_data/biblio.json: _data/papers.json _data/biblio.bib
	mkdir -p _papers
	python3 _scripts/bib2papers.py $^ > $@

_data/patents.json: _data/papers.json _data/patents.bib
	perl -p -e 's/\@patent/\@misc/' _data/patents.bib > _data/patents2.bib
	python3 _scripts/bib2yml.py _data/papers.json _data/patents2.bib > $@

thumbs: $(THUMBS)

%.png: %.pdf
	convert -thumbnail x300 -flatten $^[0] $@

clean:
	$(RM) _data/biblio.json _data/patents.json
	$(RM) _data/patents2.bib
	$(RM) _papers/*.md
	$(RM) $(THUMBS)

# End
