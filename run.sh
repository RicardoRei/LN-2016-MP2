#!/bin/bash
# renames.sh
# basic file renamer


tests=(
	Corpora/teste/500Palavras
	Corpora/teste/1000Palavras
	)

for i in ${tests[*]}; 
do
	python proj.py $i bigrams
done
