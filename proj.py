
import sys
import os
from ngram import *

#--------------------------------------------------------------------------------------------------
#       							Main module
#--------------------------------------------------------------------------------------------------

training_dir = "Corpora/treino/"
samples_dir = ["500Palavras", "1000Palavras"]

test_dir = "Corpora/teste/"
authors = ["AlmadaNegreiros", "CamiloCasteloBranco", "EcaDeQueiros", \
			"JoseRodriguesSantos", "JoseSaramago", "LuisaMarquesSilva"]


def identifyAuthor(dir, ngramType):
	sample_dir = test_dir + dir
	authorText=""
	for file in os.listdir(sample_dir):
		if file and file.endswith(".txt"):
			counted_ngram = createTextCountedNgram(textPath=sample_dir + "/", 
												   textFilename=file, 
												   ngramType=ngramType)
			compareWithAuthorsNgrams(ngram=countedNgramToDictionary(counted_ngram), ngramType=ngramType)

def compareWithAuthorsNgrams(ngram, ngramType):
	closest_author = ("Unkown", float("inf"))
	for author in authors:
		author_file = open(training_dir + author + "/" + ngramType + "Profile.txt", "r")
		author_ngram = countedNgramFileToDictionary(file=author_file)
		value = distanceBetweenProfiles(author_ngram, ngram, ngramType)
		author_file.close()

		print (author, value)
		if value > closest_author[1]:
			closest_author = (author, value)
	print "closest one:"
	print closest_author

def distanceBetweenProfiles(knownProfileFile, unknownProfileFile, ngramType):
	def F(bigram, dictionary):
		try:
			return dictionary[bigram]
		except KeyError:
			return 0
	SUM = 0
	for key in unknownProfileFile:
		aux1 = int(F(key, unknownProfileFile))
	return SUM

def main():
	cmdargs = sys.argv
	cmd = cmdargs[1]
	ngramType = cmdargs[2]
	
	if cmd == "train":
		for author in authors:
			counted_ngram = createAuthorCountedNgram(author= author, ngramType="bigrams") 
			writeNgramTofile(directoryName=training_dir + author, 
							  name = ngramType + author, 
							  counted_ngram=counted_ngram)

	if cmd == "test":
		for dir in samples_dir:
			identifyAuthor(dir=dir, ngramType="bigrams")

main()

 


