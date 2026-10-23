.PHONY: generate check paper submission
PYTHON ?= python3
generate:
	$(PYTHON) tools/evidence.py generate
check:
	$(PYTHON) tools/evidence.py check
	$(PYTHON) -m unittest discover -s tests -v
paper: check
	cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
submission: paper
	mkdir -p build/submission/generated
	cp paper/main.tex build/submission/
	cp paper/generated/*.tex build/submission/generated/
	cd build/submission && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
	pdftotext paper/main.pdf build/reviewed.txt
	pdftotext build/submission/main.pdf build/submission.txt
	diff -u build/reviewed.txt build/submission.txt
	tar -czf build/arxiv-source-candidate.tar.gz -C build/submission main.tex generated/macros_results.tex generated/comparison_table.tex
