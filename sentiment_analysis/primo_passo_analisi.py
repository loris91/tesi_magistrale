#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

'''
la classe primo_passo_analisi.py (nome da cambiare) prende con input i file pros_cat.json e cons_cat.json,
ogni commento viene tokenizzato e se il commento è composto da meno di 5 token allora i tokens vengono taggati
tramite un pos_tag. i tag vengono salvati in un file temporaneo tmp_cat.txt.
'''

import os
import re
import json
import nltk
from pprint import pprint

category_name = ""

categories_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"

characteristics_folder = "/home/alakay/Scrivania/Ciao.co.uk/Characteristics/"

tmp_file = ""

def analizza_pros(pros_json,dictionary):
	for section in pros_json.keys():
		section = str(section)
		
		max_size = len(pros_json[section])
		i = 0
		
		for phrase in pros_json[section]:
			phrase = phrase.lower()
			i=i+1
			if (i%100==0):
				print category_name+":="+section+" mancano: "+str(max_size-i)
			tokens = nltk.word_tokenize(phrase)
			if len(tokens)<5:
				tagged = nltk.pos_tag(tokens)
				field = (section,"pros",tagged)
				tmp_file.write(str(field)+"\n")


def analizza_cons(cons_json,dictionary):
	for section in cons_json.keys():
		section = str(section)

		max_size = len(cons_json[section])
		i = 0

		for phrase in cons_json[section]:
			phrase = phrase.lower()
			i=i+1
			if (i%100==0):
				print category_name+":= "+section+" mancano: "+str(max_size-i)
			tokens = nltk.word_tokenize(phrase)
			if len(tokens)<6:
				tagged = nltk.pos_tag(tokens)
				field = (section,"cons",tagged)
				tmp_file.write(str(field)+"\n")


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

	dictionary = {}

	analizza_pros(pros_json,dictionary)
	analizza_cons(cons_json,dictionary)



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
	category_name = list_folder[6] := Percussion & Drum Machines_4MB
	category_name = list_folder[5] := DJ Equipment_3MB
	category_name = list_folder[2] := Fishing_2MB
	'''

	#category_name = list_folder[2]
	#print "In esecuzione analisi su: " + category_name
	#analizza_categoria(category_name)

	for category_name in list_folder:
		print "In esecuzione analisi su: " + category_name
		analizza_categoria(category_name)