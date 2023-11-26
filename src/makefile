DOCNAME=main
CV_BUILD=build

all: cv paperhtml

.PHONY: clean

cv:
	mkdir -p $(CV_BUILD)
	lualatex --output-directory=$(CV_BUILD) $(DOCNAME).tex
	biber --output-directory $(CV_BUILD) $(DOCNAME)
	lualatex --output-directory=$(CV_BUILD) $(DOCNAME).tex
	lualatex --output-directory=$(CV_BUILD) $(DOCNAME).tex
	mv $(CV_BUILD)/$(DOCNAME).pdf $(DOCNAME).pdf

view: cv
	open $(DOCNAME).pdf

bibtex2html:
	(cd bibtex2html-1.99 && ./configure)
	(cd bibtex2html-1.99 && make bibtex2html)

paperhtml: bibtex2html
	export TMPDIR=.
	bibtex2html-1.99/bibtex2html -nobibsource -d -r -nodoc -nokeywords papers.bib

clean:
	(cd bibtex2html-1.99 && make distclean)
	rm -rf $(CV_BUILD)
