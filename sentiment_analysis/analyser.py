#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

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


def analizza_categoria(category_name):
	category_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"+category_name+"/"
	
	with open(category_folder+"tmp_file.txt") as tmp_pros_file:
		content = tmp_pros_file.read().splitlines()

	dictionary = {}

	for tupla in content:
		(section,polarity,tagged) = eval(tupla)

		if section not in dictionary.keys():
			dictionary[section]={}

		feature = trova_caratteristica(tagged)
		if feature is not None:
			feature = str(st.stem(feature))


		value = trova_valore(tagged)
		if value is not None:
			value = str(st.stem(value))
			if feature in dictionary[section].keys():
				if polarity in dictionary[section][feature].keys():
					dictionary[section][feature][polarity].append(value)
				else:
					dictionary[section][feature][polarity]=[value]
			else:
				dictionary[section][feature]={}
				dictionary[section][feature][polarity]=[value]

	#pprint(dictionary)
	with open (category_folder+"feature_indicator.json","w") as myfile:
			json.dump(dictionary, myfile)


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

	#category_name = list_folder[6]
	#print "In esecuzione analisi su: " + category_name
	#analizza_categoria(category_name)

	for category_name in list_folder:
		print "In esecuzione analisi su: " + category_name
		analizza_categoria(category_name)