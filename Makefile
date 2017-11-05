# Begin

all: _data/biblio.json
all: _data/patents.json

_data/biblio.json: _data/papers.json _data/biblio.bib
	python3 _scripts/bib2papers.py $^ > $@

_data/patents.json: _data/papers.json _data/patents.bib
	perl -p -e 's/\@patent/\@misc/' _data/patents.bib > _data/patents2.bib
	python3 _scripts/bib2yml.py _data/papers.json _data/patents2.bib > $@

clean:
	$(RM) _data/biblio.json _data/patents.json
	$(RM) _data/patents2.bib

# End
