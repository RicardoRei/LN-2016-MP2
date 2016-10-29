# -*- coding: utf-8 -*-
import nltk
import nltk.tokenize
from nltk import bigrams
from nltk import trigrams
from text import processText

#--------------------------------------------------------------------------------------------------
#     module that Creates, Stores (in files) and Retrieves  (from files) the counted Ngrams
#--------------------------------------------------------------------------------------------------

import sys
import os

#@brief:
#	Function that receives a list of ngram_token and returns a list of pairs (count, (word1, word2))
#
#	ex: input = [('volta', 'ter'), ('porque', 'era'), ('volta', 'ter')]
#		output = [(2, ('volta', 'ter')), (1, ('porque', 'era'))]
def countNgramFrequency(ngram_tokens):

	def getKey(item):
		return item[1][0]

	from collections import defaultdict

	counts = defaultdict(int)
	for bigram in ngram_tokens:
		counts[bigram] += 1

	result = list()
	for bigram, count in counts.iteritems():
		result.append((count, bigram))

	return sorted(result, key=getKey)

#@brief: 
#	used to create different ngrams with the tokens from the nltk.
#
def createNgram(ngramType, tokens):
	if ngramType == "bigrams":
		return nltk.bigrams(tokens)
	if ngramType == "trigrams":
		return nltk.trigrams(tokens)

#@brief: 
#	This funtion will create a big ngram of the type specified on argument ngramType with all the 
# 	words presented in the texts inside the authors folder.
def createAuthorCountedNgram(author_directory, ngramType):
	authorText = ""
	for file in os.listdir(author_directory):
		if "grams" not in file and file.endswith(".txt"):
			f = open(author_directory+"/" + file, 'r')
			authorText += processText(f).decode('utf-8')
			f.close()

	tokens = nltk.word_tokenize(authorText)
	ngrams = createNgram(ngramType, tokens)	
	return countNgramFrequency(list(ngrams))

#@brief:
#	This funtion creates a Ngram for a Specific Text.
#	Note that the last funtion creates a Ngram with all the texts of an author! 
#	This one only considers one text and its mainly used for the test part
def createTextCountedNgram(textPath, textFilename, ngramType):
	f1 = open(textPath + textFilename, 'r')
	processed_text = processText(f1).decode('utf-8')
	f1.close()
	tokens = nltk.word_tokenize(processed_text)
	ngrams = createNgram(ngramType, tokens)
	return countNgramFrequency(list(ngrams))

#@brief:
#	this funtion will write to a file a counted ngram. 
#	The directortFolder argument is the folder where the new file is going to be saved.
#	The name argument is the name of the file.
def writeNgramTofile(directoryName, name, counted_ngram):
	cwd = os.getcwd()
	os.chdir(directoryName)

	if os.path.isfile(name):
		os.remove(name)
		
	outputFile = open(name, "a+")
	for element in counted_ngram:
		new = ""
		for i in element[1]:
			new = new + i + " "
		outputFile.write(new.encode('utf-8') + " " + str(element[0])+"\n")

	outputFile.close()
	os.chdir(cwd)

#@brief:
#	In order to compare the Ngrams its easier if they have the same format.
#	This function receives a counted ngram and creates an dictionary.
# ex: Input = [(2, ('volta', 'ter')), (1, ('porque', 'era'))]
#	  Output = { ('volta', 'ter'): 2, ('porque', 'era'): 1 }
def countedNgramToDictionary(ngram):
	result = dict()
	for e in ngram:
		result[(e[1][0].encode('utf-8'), e[1][1].encode('utf-8'))] = e[0]
	return result

#@brief:
#	receives a FilePointer that stores a counted ngram and return a dictionary for that ngram.
def countedNgramFileToDictionary(file):
	result = dict()
	for line in file:
		w1, w2, count = line.split()
		bigram = (w1, w2)
		result[bigram] = count
	return result