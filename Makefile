# Begin

all: _data/biblio.json
all: _data/patents.json

_data/biblio.json: _data/papers.json _data/biblio.bib
	_scripts/bib2yml.py $^ > $@

_data/patents.json: _data/papers.json _data/patents.bib
	_scripts/bib2yml.py $^ > $@


clean:
	$(RM) _data/biblio.json _data/patents.json

# End
