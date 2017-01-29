# Begin

all: _data/biblio.json
all: _data/patents.json

_data/biblio.json: _data/papers.json _data/biblio.bib
	python3 _scripts/bib2yml.py $^ > $@

_data/patents.json: _data/papers.json _data/patents.bib
	python3 _scripts/bib2yml.py $^ > $@


clean:
	$(RM) _data/biblio.json _data/patents.json

# End
