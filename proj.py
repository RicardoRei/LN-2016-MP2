# -*- coding: utf-8 -*-
import sys
import re
import os
import nltk
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
	from collections import defaultdict

	counts = defaultdict(int)
	for bigram in ngram_tokens:
		counts[bigram] += 1

	result = list()
	for bigram, count in counts.iteritems():
		result.append((count, bigram))

	result.sort(reverse=True)
	return result


#prints output according to professors' specification	
def writeToFile(countedNgram,filename):
	indexNr = filename.index('.')
	newFilename=filename[:indexNr]+"out.txt"
	
	if os.path.isfile(newFilename):
		os.remove(newFilename)
		
	os.mknod(newFilename)
	outputFile=open(newFilename,"w")
	for element in countedNgram:
		new=""
		for i in element[1]:
			new=new+i+" "
		outputFile.write(new +" "+str(element[0])+"\n")

cmdargs=sys.argv
fileIn = open(cmdargs[1], 'rU')
#fileIn = open('Corpora/test.txt', 'rU')
processed_text = processPunctuation(fileIn)
fileIn.close()
print (processed_text)
	
# split the texts into tokens
tokens = nltk.word_tokenize(processed_text)
tokens = [token.lower() for token in tokens if (len(token) > 1)] #same as unigrams
tri_tokens=nltk.trigrams(tokens)
bi_tokens = nltk.bigrams(tokens)
	
counted_bigram = countNgramFrequency(list(bi_tokens))
counted_trigram=countNgramFrequency(list(tri_tokens))

writeToFile(counted_bigram,cmdargs[1])
