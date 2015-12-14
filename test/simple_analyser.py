#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

'''
La classe analyser.py prende in input i file temporanei tmp_cat.txt generati dalla classe filter.py e 
ne analizza il contenuto andato ad estrarre feature e feature_indicator da ogni singolo commento.
In questo passo una feature è una sequenza di parole consecutive non vuota di ["NN","NNS","NNP","NNPS"]
cioè nomi e nomi propri, mentre
un feature_indicator è una sequenza di parole consecutive non vuota di ["JJ","JJR","JJS","RB","RBR","RBS"],
cioè aggettivi o avverbi.
Vengono salvati tutti quei commenti in cui è presente almeno il feature_indicator.
Per ogni categoria viene generato un file json in cui si memorizza
	dictionary_json[section][feature][polarity]=list[value]
'''

import os
import re
import json
import nltk
from pprint import pprint
from nltk.stem.snowball import SnowballStemmer

categories_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"

characteristics_folder = "/home/alakay/Scrivania/Ciao.co.uk/Characteristics/"

feature_pos_tag = ["NN","NNS","NNP","NNPS"]
value_pos_tag = ["JJ","JJR","JJS","RB","RBR","RBS"]
st = SnowballStemmer("english")


def trova_caratteristica(tagged):
	for i in range(0,len(tagged)):
		element = tagged[i]
		if element[1] in feature_pos_tag:
			if len(tagged)>i+1 :
				if tagged[i+1][1] in feature_pos_tag:
					return str(element[0])+" "+str(tagged[i+1][0])
			return str(element[0])

def trova_valore(tagged):
	for i in range(0,len(tagged)):
		element = tagged[i]
		if element[1] in value_pos_tag:
			if len(tagged)>i+1 :
				if tagged[i+1][1] in value_pos_tag:
					return str(element[0])+" "+str(tagged[i+1][0])
			return str(element[0])


def analizza_tupla(tupla,phrase):
	(section,polarity,tagged) = tupla

	feature = trova_caratteristica(tagged)
	if feature is not None:
		feature_stem = str(st.stem(feature))

	value = trova_valore(tagged)
	if value is not None:
		value_stem = str(st.stem(value))
	if value is not None and feature is not None:
		print phrase
		print (feature_stem,value_stem)
		print ""


def analizza_pros(pros_json):
	for section in pros_json.keys():
		section = str(section)

		for i in range (0,11):
			phrase = pros_json[section][i]
		#for phrase in cons_json[section]:
			phrase = phrase.lower()
			tokens = nltk.word_tokenize(phrase)
			if len(tokens)<8:
				tagged = nltk.pos_tag(tokens)
				field = (section,"pros",tagged)
				analizza_tupla(field,phrase)


def analizza_cons(cons_json):
	for section in cons_json.keys():
		section = str(section)

		for i in range (0,11):
			phrase = cons_json[section][i]
		#for phrase in cons_json[section]:
			phrase = phrase.lower()
			tokens = nltk.word_tokenize(phrase)
			if len(tokens)<8:
				tagged = nltk.pos_tag(tokens)
				field = (section,"cons",tagged)
				analizza_tupla(field,phrase)


def analizza_categoria(category_name):
	category_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"+category_name+"/"
	
	global tmp_file
	tmp_file = open(category_folder+"tmp_file.txt","w")

	with open(category_folder+"pros_cat.json") as json_file:
		pros_json = json.load(json_file)
		json_file.close()

	with open(category_folder+"cons_cat.json") as json_file:
		cons_json = json.load(json_file)
		json_file.close()

	analizza_pros(pros_json)
	analizza_cons(cons_json)




if __name__ == "__main__":
	list_folder = os.listdir(categories_folder)

	category_name = "Computers"
	analizza_categoria(category_name)