#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
import re
import json
import nltk
from pprint import pprint
from nltk.corpus import treebank
from nltk.grammar import DependencyGrammar
from nltk.parse import DependencyGraph
from nltk.parse import ProjectiveDependencyParser
from nltk.parse import NonprojectiveDependencyParser

category_name = "Guitars, Amplifiers & Effects"

category_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"+category_name+"/"
characteristics_folder = "/home/alakay/Scrivania/Ciao.co.uk/Characteristics/"

def genera_albero(phrase,dictionary):
	#print "Frase iniziale: " +str(phrase)

	tokens = nltk.word_tokenize(phrase)
	#print "Word Tonized: " + str(tokens)

	tagged = nltk.pos_tag(tokens)
	#print "Pos tagged: " + str(tagged)
	array = []
	for el in tagged:
		array.append(el[1])
	
	key = str(array)

	if key in dictionary.keys():
		dictionary[key]=dictionary[key]+1
	else:
		dictionary[key]=1

	#entities = nltk.chunk.ne_chunk(tagged)
	#print "Entities: " + str(entities)
	#print "\n##########################\n"

def start():
	with open(category_folder+"pros_cat.json") as json_file:
		pros_json = json.load(json_file)
		json_file.close()

	section = pros_json.keys()[0]
	dictionary={}

	#for i in range(0,1):
	#	phrase = pros_json[section][i]
	for phrase in pros_json[section]:
		tokens = nltk.word_tokenize(phrase)
		if len(tokens)<5:
			genera_albero(phrase,dictionary)
	pprint(dictionary)


if __name__ == "__main__":
	start()
