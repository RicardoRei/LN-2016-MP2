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


#writes .txt according to professors' specification	
def writeToFile(countedNgram,filename):
	newFilename=str(filename)+"out.txt"
	
	if os.path.isfile(newFilename):
		os.remove(newFilename)
		
	os.mknod(newFilename)
	outputFile=open(newFilename,"w")
	for element in countedNgram:
		new=""
		for i in element[1]:
			new=new+i+" "
		outputFile.write(new +" "+str(element[0])+"\n")
		
#ngram is the number corresponding to n-gram, EX: if we want to calculate probabilities over bigrams, ngram should be 2		
def probabilities(filename,ngram):
	f=open(filename,'r')

			
	
	
def main():
	cmdargs=sys.argv
	authorText=""
	for file in os.listdir(cmdargs[1]):
		f=open(cmdargs[1]+"/"+file,'r')
		processed_text = processPunctuation(f)
		authorText+=processed_text+"\n"
		print file
		
		
	# split the texts into tokens
	#tokens = nltk.word_tokenize(authorText)
	#tokens = [token.lower() for token in tokens if (len(token) > 1)] #same as unigrams
	#tri_tokens=nltk.trigrams(tokens)
	#bi_tokens = nltk.bigrams(tokens)
		
	#counted_bigram = countNgramFrequency(list(bi_tokens))
	#counted_trigram=countNgramFrequency(list(tri_tokens))
	
	authorPath=cmdargs[1].split("/")
	authorName=authorPath[2]
	
	#writeToFile(counted_trigram,authorName)
	
	
main()
