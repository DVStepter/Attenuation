manuscript = report
latexopt = -file-line-error -halt-on-error

# Build the PDF of the lab report from the source files
$(manuscript).pdf: $(manuscript).tex text/*.tex references.bib images/*.png
	pdflatex $(latexopt) $(manuscript).tex
	bibtex $(manuscript).aux
	bibtex $(manuscript).aux
	pdflatex $(latexopt) $(manuscript).tex
	pdflatex $(latexopt) $(manuscript).tex

# Get/download necessary data
data :
	curl -L -o responses.csv "https://www.dropbox.com/s/rm8gwngq8e8xqet/responses.csv?dl=0"

# Automate running the analysis code
analysis :
	python code/euclidean.py

clean :
	rm -f *.aux *.log *.bbl *.lof *.lot *.blg *.out *.toc *.run.xml *.bcf *.csv
	rm -f text/*.aux
	rm $(manuscript).pdf

# Make keyword for commands that don't have dependencies
.PHONY : test data validate analysis clean
