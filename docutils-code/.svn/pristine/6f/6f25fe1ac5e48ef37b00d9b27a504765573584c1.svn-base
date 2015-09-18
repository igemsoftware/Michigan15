<<<<<<< HEAD
all: document.pdf

document.xml: document.rst
	rst2xml.py --no-doctype --no-doc-title --trim-footnote-reference-space document.rst |rstxml2xml.py  > document.xml


document_docbook.xml: document.xml
	xsltproc rst_docbook.xsl document.xml > document_docbook.xml

document_docbook.fo: document_docbook.xml docbook_fo.xsl
	xsltproc docbook_fo.xsl document_docbook.xml > document_docbook.fo


document.pdf: document_docbook.fo
	fop -fo document_docbook.fo -pdf document.pdf

clean: 
	rm -f document.xml document_docbook.xml document_docbook.fo document.pdf *~
=======
all: document.pdf

document.xml: document.rst
	rst2xml.py --no-doctype --no-doc-title --trim-footnote-reference-space document.rst |rstxml2xml.py  > document.xml


document_docbook.xml: document.xml
	xsltproc rst_docbook.xsl document.xml > document_docbook.xml

document_docbook.fo: document_docbook.xml docbook_fo.xsl
	xsltproc docbook_fo.xsl document_docbook.xml > document_docbook.fo


document.pdf: document_docbook.fo
	fop -fo document_docbook.fo -pdf document.pdf

clean: 
	rm -f document.xml document_docbook.xml document_docbook.fo document.pdf *~
>>>>>>> 30665a03f9af0025ac7f44d3b46a3b6df1db009f
