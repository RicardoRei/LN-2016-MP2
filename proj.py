# -*- coding: utf-8 -*-
import sys
import os
from ngram import *

#--------------------------------------------------------------------------------------------------
#       							Main module
#--------------------------------------------------------------------------------------------------

training_dir = "Corpora/treino/"
test_dir = "Corpora/teste/"

samples_dir = ["500Palavras", "1000Palavras"]
authors = ["AlmadaNegreiros", "CamiloCasteloBranco", "EcaDeQueiros", \
			"JoseRodriguesSantos", "JoseSaramago", "LuisaMarquesSilva"]

#@brief:
#	Function that receives the path of the tests directory and the type of the ngrams we are using.
#	For every file in that directory creates the dictionary with the counted ngrams and compares 
#	that dictionary with the Authors.

#	Prints for the terminal the result of the best author for every test in the test Directory
def identifyAuthor(directoryPath, ngramsType):
	tests = test_dir + directoryPath

	for file in os.listdir(tests):
		if file and file.endswith(".txt"):
			counted_ngrams = createTextCountedNgrams(tests + "/", file, ngramsType)
			result = compareWithAuthorsNgrams(countedNgramsToDictionary(counted_ngrams), ngramsType)

			print 'result for file: ' + file + ' ' + str(result)

#@brief:
#	Funtion that receives a dictonary with the counted ngrams from a text (argument ngrams), and 
#	compares that ngrams with the Authors ngrams (calculates in train). Returns the value and name
#	of the closest author.

#	The closest Author is the one with the MAX value obtained in the funtion normalizedFrequenciesValue
def compareWithAuthorsNgrams(ngrams, ngramsType):
	closest_author = ("Unkown", float("-inf"))
	for author in authors:
		author_file = open(training_dir + author + "/" + ngramsType + author + ".txt", "r")
		author_ngrams = countedNgramsFileToDictionary(author_file)
		author_file.close()
		value = normalizedFrequenciesValue(author_ngrams, ngrams)
		print 'value: ' + str(value) + ' for author '+ author

		if value > closest_author[1]:
			closest_author = (author, value)

	return closest_author

#@brief:
#	Function that receives a well known Author counted Ngrams (argument knownAuthorsNgram) and the
#	counted ngrams of a text.
#	Return a value that expresses the similarity between the Known Author and the author of the text.

#	The value returned is based on the SUM of the frequencies, of the ngrams in the text, in the Authors
#	corpora dividing by the number of ngrams in the authors corpora.
def normalizedFrequenciesValue(knownAuthorNgrams, unknownTextNgrams):
	def getCount(ngram, dictionary):
		try:
			return dictionary[ngram]
		except KeyError:
			return 0

	SUM = 0
	for key in unknownTextNgrams:
		if key != "Ngrams_Info":
			SUM = SUM + int(getCount(key, knownAuthorNgrams))

	return SUM / float(knownAuthorNgrams["Ngrams_Info"][0])

#@brief:
#	Main funtion.
#	To train (for bigrams) run: python proj.py train bigrams
#	To test  (for bigrams) run: python proj.py test bigrams
def main():
	cmdargs = sys.argv
	cmd = cmdargs[1]
	ngramsType = cmdargs[2]
	
	# In the train it's going to create for each author the Counted Ngrams and write them in a file.
	if cmd == "train":
		for author in authors:
			counted_ngrams = createAuthorCountedNgrams(training_dir + author, ngramsType) 
			writeNgramsTofile(training_dir + author, ngramsType + author + ".txt", counted_ngrams)

	# In the test it's going to run the diferent folders for text samples (ex: 500Palavras) and
	# 	try to identify the author of the texts presented on that folders.
	if cmd == "test":
		for dir in samples_dir:
			identifyAuthor(dir, ngramsType)

main()

 


