# -*- coding: utf-8 -*-
import sys
import re
import os
import nltk
import nltk.tokenize
import types
from nltk import bigrams
from nltk import trigrams


#@brief:
#	Function that receives a file and reads every line adding a space at right and left of every 
#	punctuation.
def processPunctuation(file):
	text = ""
	for line in file:
		result = re.sub(r'((\.\.\.)|[:,!?;.])', r' \1 ', line)
		text = text + result
	return text

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


def createAuthorProfile():
	cmdargs=sys.argv
	authorText=""
	for file in os.listdir(cmdargs[1]):
		if "grams" not in file and file.endswith(".txt"):
			f = open(cmdargs[1]+"/" + file, 'r')
			authorText += processPunctuation(f).decode('utf-8')
			f.close()

	authorPath = cmdargs[1].split("/")
	authorName = authorPath[2]
	tokens = nltk.word_tokenize(authorText)

	#cmdargs[2] is the the ngram type we want (ex. if we want to create a bigram cmdargs[2] = 'bigramas')
	ngrams = createNgram(cmdargs[2], tokens)	
	counted_ngram = countNgramFrequency(list(ngrams))
	writeAuthorProfile(counted_ngram, authorName, cmdargs[2])
	#tokens = [token.lower() for token in tokens if (len(token) > 1)] #same as unigrams

#writes .txt according to professors' specification	
def writeAuthorProfile(countedNgram, authorName, ngramType):
	directoryName = "Corpora/treino/"+authorName+"/"
	newFilename = ngramType+"Profile.txt"
	
	cwd = os.getcwd()
	
	os.chdir(directoryName)
	if os.path.isfile(newFilename):
		os.remove(newFilename)
		
	outputFile = open(newFilename, "a+")
	for element in countedNgram:
		new = ""
		for i in element[1]:
			new = new + i + " "

		outputFile.write(new.encode('utf-8') + " " + str(element[0])+"\n")
	outputFile.close()
	os.chdir(cwd)

#so far, we have all texts from a specific author in variable authorText
def createNgram(ngramType, tokens):
	if ngramType == "bigrams":
		return nltk.bigrams(tokens)
	if ngramType == "trigrams":
		return nltk.trigrams(tokens)		


def createTextProfile(textPath, ngramType, textFilename):
	f1 = open(textPath, 'r')
	processed_text = processPunctuation(f1).decode('utf-8')
	f1.close()

	tokens = nltk.word_tokenize(processed_text)
	ngrams = createNgram(ngramType, tokens)
	profile = countNgramFrequency(list(ngrams))
	print textFilename
	writeTextProfile(profile, textFilename, textPath)

def identifyAuthor(args):
	cmdargs=sys.argv
	authorText=""
	for file in os.listdir(cmdargs[1]):
		if "profile" not in file and file.endswith(".txt"):
			createTextProfile(cmdargs[1]+"/"+file, cmdargs[2], file)
			compareWithAuthors(cmdargs[1]+"/profile_"+file, cmdargs[2])

def compareWithAuthors(textProfile, ngramType):
	text_profile = open(textProfile, "r")
	trainDirectory= "Corpora/treino/"
	authors = ["AlmadaNegreiros", "CamiloCasteloBranco", "EcaDeQueiros", \
			   "JoseRodriguesSantos", "JoseSaramago", "LuisaMarquesSilva"]

	closest_author = ("Unkown", float("inf"))
	for author in authors:
		author_profile = open(trainDirectory + author+ "/" + ngramType + "Profile.txt", "r")
		value = distanceBetweenProfiles(author_profile, text_profile, ngramType)
		print (author, value)
		if value > closest_author[1]:
			closest_author = (author, value)
	print "closest one:"
	print closest_author

def writeTextProfile(countedNgram, filename, textPath):
	directoryName = "Corpora/teste/1000Palavras"
	if "500" in textPath:
		directoryName = "Corpora/teste/500Palavras" 
	newFilename = "profile_"+filename
	
	cwd = os.getcwd()
	os.chdir(directoryName)
	if os.path.isfile(newFilename):
		os.remove(newFilename)
		
	outputFile=open(newFilename,"a+")
	for element in countedNgram:
		new = ""
		for i in element[1]:
			new = new + i + " "
		outputFile.write(new.encode('utf-8') + " " + str(element[0]) + "\n")

	outputFile.close()
	os.chdir(cwd)

def profileToDictionary(file):
	result = dict()
	for line in file:
		w1, w2, count = line.split()
		bigram = (w1, w2)
		result[bigram] = count
	return result

def distanceBetweenProfiles(knownProfileFile, unknownProfileFile, ngramType):

	def F(bigram, dictionary):
		try:
			return dictionary[bigram]
		except KeyError:
			return 0

	d_known = profileToDictionary(knownProfileFile)
	d_unknown =  profileToDictionary(unknownProfileFile)

	SUM = 0
	for key in d_unknown:
		aux1 = int(F(key, d_known))

	return SUM

#ex: python proj.py Corpora/treino/Einstein bigramas
def main():
	cmdargs = sys.argv
	dirs = cmdargs[1].split('/')
	
	if dirs[1] == "treino":
		createAuthorProfile()
	if dirs[1] == "teste":
		identifyAuthor(cmdargs)

main()

 


