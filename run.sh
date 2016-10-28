#!/bin/bash
# renames.sh
# basic file renamer



names=(
	Corpora/treino/Tolkien Corpora/treino/EcaDeQueiros 
	#Corpora/test2.txt para adicionar mais filenames
	#devem estar separados por espacos
	)
for i in ${names[*]}; 
do
	python proj.py $i bigramas
done