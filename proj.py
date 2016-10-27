# -*- coding: utf-8 -*-
import sys
import re
import os
import nltk
import nltk.tokenize
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
def writeToFileTreino(countedNgram,authorName,ngramas):
	directoryName = "Corpora/treino/"+authorName+"/"
	newFilename = ngramas+authorName+".txt"
	
	cwd = os.getcwd()
	
	os.chdir(directoryName)
	if os.path.isfile(newFilename):
		os.remove(newFilename)
		
	os.mknod(newFilename)
	outputFile=open(newFilename,"w")
	for element in countedNgram:
		new=""
		for i in element[1]:
			new=new+i+" "
		outputFile.write(new +" "+str(element[0])+"\n")
	outputFile.close()
	os.chdir(cwd)
		
#ngram is the number corresponding to n-gram, EX: if we want to calculate probabilities over bigrams, ngram should be bi		
def probabilities(filename,ngram):
	fileIn=open(filename,'r')
	for line in f:
		print "bla"



			
	
#so far, we have all texts from a specific author in variable authorText

def createNgram(ngramName,tokens):
	if ngramName == "bigramas":
		return nltk.bigrams(tokens)
	if ngramName == "trigramas":
		return nltk.trigrams(tokens)	
	
def treino():
	cmdargs=sys.argv
	authorText=""
	for file in os.listdir(cmdargs[1]):
		if "gramas" not in str(file):
			f = open(cmdargs[1]+"/"+file,'r')
			processed_text = processPunctuation(f)
			authorText+= processed_text+"\n"
			f.close()
			print "read from :"+str(file)
	
	authorPath = cmdargs[1].split("/")
	authorName = authorPath[2]
	
	tokens = nltk.word_tokenize(authorText)
	ngramasName = cmdargs[2]
	ngrams = createNgram(ngramasName,tokens)	
	counted_ngram = countNgramFrequency(list(ngrams))
	writeToFileTreino(counted_ngram,authorName,ngramasName)
	#tokens = [token.lower() for token in tokens if (len(token) > 1)] #same as unigrams

def identifyAuthor(args):	
	
	f1 = open(args[1],'r')
	processed_text=processPunctuation(f1)
	f1.close()
	
	tokens = nltk.word_tokenize(processed_text)
	ngramasName = args[2]
	ngrams = createNgram(ngramasName,tokens)	
	ngramOfUnknownAuthor = countNgramFrequency(list(ngrams))
	
	dictionary=dict()
	for author in ["Einstein","Tolkien"]:
		dictionary[author] = likelihood(ngramOfUnknownAuthor,author)
		
	print dictionary
	
def writeToFileTeste(countedNgram,ngramas):
	directoryName = "Corpora/teste/"
	newFilename = ngramas+".txt"
	
	cwd = os.getcwd()
	os.chdir(directoryName)
	if os.path.isfile(newFilename):
		os.remove(newFilename)
		
	os.mknod(newFilename)
	outputFile=open(newFilename,"w")
	for element in countedNgram:
		new=""
		for i in element[1]:
			new=new+i+" "
		outputFile.write(new +" "+str(element[0])+"\n")
	outputFile.close()
	os.chdir(cwd)
	
#receives ngram and author, and returns the number of ngrams in the test that match the ones inside the authors directory
def likelihood(ngram,authorName):
	grama = len(ngram[0][1])
	
	if grama == 2:
		grama="bigramas"
		fTreino=open("Corpora/treino/"+authorName+"/bigramas"+authorName+".txt",'r')
	if grama == 3:
		grama="trigramas"
		fTreino=open("Corpora/treino/"+authorName+"/trigramas"+authorName+".txt",'r')
	
	writeToFileTeste(ngram,grama)	
	
	#Go get both afiles and compare
	"""for line in fTreino:
		for elem in ngram:
			field = re.search("to run  1", line)
			if field is None:	
				print ("hey")
			else:
				p1 = field.group(0)
				p2 = field.group(2)	
			
				if p1 == elem[1][1] and p2 == elem[1][0]:
					print IGUAIS"""
			
	return 0
	
#ex: python proj.py Corpora/treino/Einstein bigramas
def main():
	cmdargs = sys.argv
	dirs = cmdargs[1].split('/')
	
	if dirs[1] == "treino":
		treino()
	if dirs[1] == "teste":
		identifyAuthor(cmdargs)


main()