#!/bin/bash

echo "OWASP Markdown Conversion Tool"
echo ""

function command_exists () {
    command -v $1 >/dev/null 2>&1;
}

if ! command_exists pandoc; then
    echo "Error: Please install pandoc. Cannot continue"
    exit;
fi

generate_docx() {
    pandoc -s -f gfm --reference-doc=../templates/reference.docx --columns 10000 --toc -t docx -o "../docs_$1/OWASP CBAS SAP Security Maturity Model $2-$1.docx" *.md
	# After this process, move the Table of Contents and change the style
	# of the first Heading 1 so it is on the first page
}

# generate_html() {
#     pandoc -s -f markdown_github -t html5 -o "../OWASP Application Security Verification Standard 4.0-$1.html" *.md
# }

lang="en"
vers="0.8.1"

if [ -z "$1" ]
then
	  lang="en"
else
      lang=$1
fi

if [ -z "$2" ]
then
      vers="0.8"
else
      vers=$2
fi

echo -n "Generating OWASP SAP Security Verification Standard $vers ($lang)..."
if [ -d "$lang" ];
then
	cd "Controls_${lang}"
	generate_docx $lang $vers
	# generate_html $lang
	cd ..
	echo " done."
else
	echo " No OWASP CBAS found in directory $lang"
fi


echo
echo "Generated OWASP CBAS SAP Security Maturity Model $vers"
