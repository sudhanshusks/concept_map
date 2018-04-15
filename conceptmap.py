'''
Automatic Concept Map Generator
Author: Pranav Khadpe
'''
import sys
import getopt
import requests
import urllib.parse
import json
import nltk


'''
Function to get the imoprtant concepts using the DBpedia spotlight web API
query = text
'''
def GetImportantConcept(text):
	query = text
	params = urllib.parse.urlencode({'text': query})
	url = "http://model.dbpedia-spotlight.org/en/spot?%s" % params
	request = requests.get(url, headers={"accept": "application/json"})
	pydict = json.loads(request.content)
	entities = list(pydict["annotation"]["surfaceForm"])
	dictionary = len(entities)
	word_list = []
	for i in range(0, dictionary):
		word_list.append(entities[i]['@name'])
	return word_list
'''
Accepts the text and returns a list of sentences that contain the important concepts.
'''
def GetSentences(word_list, text):
	sent_list = nltk.sent_tokenize(text)
	impsent_list = []
	num_sentences = len(sent_list)
	for i in range(0,num_sentences):
		if any(word in sent_list[i] for word in word_list):
			impsent_list.append(sent_list[i])
	return impsent_list

'''
def ExtractRelations(word_list, sentences):
'''

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print ('test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
	print ('Input file is ', inputfile)
	print ('Output file is ', outputfile)
	with open(inputfile, 'r') as in_file:
		text = in_file.read()
	word_list = GetImportantConcept(text)
	sentences = GetSentences(word_list, text)
	print(word_list)
	print(sentences)
	word_file = open('word_list.txt', 'w')
	for item in word_list:
		word_file.write("%s\n" % item)



if __name__ == "__main__":
	print("Usage:test.py -i <inputfile> -o <outputfile>")
	main(sys.argv[1:])





