#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

'''
La classe prove_analyser.py prende in input i file temporanei tmp_cat.txt generati dalla classe filter.py.
Lo scopo della classe è analizzare possibili "qualcosa" che permetta di estrarre contenuti prima scartati.
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

def get_phrase(tagged):
	stringa = ""
	for (word,pos_tag) in tagged:
		stringa = stringa + str(word) + " "	
	return stringa


def stemma(phrase):
	string = ""
	for word in phrase.split():
		string = string + str(st.stem(word)) + " "

	return string

def analizza_categoria(array):
	new_array = []
	print len(array)
	for tagged in array:
		feature = trova_caratteristica(tagged)

		value = trova_valore(tagged)
		if value is not None:
			new_array.append((tagged,feature,value))
	print len(new_array)
	for a in new_array:
		print a


def analizza(array):
	new_array = []
	for frase in array:
		phrase = stemma(frase)
		tokens = nltk.word_tokenize(phrase)
		tagged = nltk.pos_tag(tokens)
		new_array.append(tagged)
	analizza_categoria(new_array)



def scartati(category_name):
	category_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"+category_name+"/"
		
	with open(category_folder+"tmp_file.txt") as tmp_pros_file:
		content = tmp_pros_file.read().splitlines()

	array = []

	for tupla in content:
		(section,polarity,tagged) = eval(tupla)

		feature = trova_caratteristica(tagged)
		if feature is not None:
			feature = str(st.stem(feature))


		value = trova_valore(tagged)
		if value is None:
			array.append(get_phrase(tagged))

	print len(array)

	analizza(array)




if __name__ == "__main__":
	list_folder = os.listdir(categories_folder)
	'''
	category_name = list_folder[0] := Cameras_286MB
	category_name = list_folder[8] := Computers_196MB
	category_name = list_folder[7] := Small Kitchen Appliances_99MB
	category_name = list_folder[1] := TVs_65_MB	
	category_name = list_folder[3] := Large Kitchen Appliances_64MB	
	category_name = list_folder[9] := Software_32MB
	category_name = list_folder[4] := Guitars, Amplifiers & Effects_26MB
	category_name = list_folder[10] := Car Accessories_16MB
	###category_name = list_folder[6] := Percussion & Drum Machines_4MB
	###category_name = list_folder[5] := DJ Equipment_3MB
	###category_name = list_folder[2] := Fishing_2MB
	'''

	category_name = list_folder[5]
	print "In esecuzione analisi su: " + category_name
	scartati(category_name)


	'''
	for category_name in list_folder:
		print "In esecuzione analisi su: " + category_name
		scartati(category_name)
	'''

