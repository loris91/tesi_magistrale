#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
La classe characteristics_find.py ha lo scopo di verificare se in un commento Pros o Cons esiste una caratteristica
gia presente in elenco
'''

import os
import re
import json
import nltk
from pprint import pprint

category_name = "Guitars, Amplifiers & Effects"

category_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"+category_name+"/"
characteristics_folder = "/home/alakay/Scrivania/Ciao.co.uk/Characteristics/"

def get_bigram(parole):
	bigram =[]
	for i in range(1,len(parole)):
		tmp = str(parole[i-1]) +" " + str(parole[i])
		bigram.append(tmp)
	return bigram

def get_trigram(parole):
	trigram = []
	for i in range(2,len(parole)):
		tmp = str(parole[i-2])+" "+str(parole[i-1])+" "+str(parole[i])
		trigram.append(tmp)
	return trigram

def verifica_1gram(stringa,char):
	parole = stringa.split(" ")
	for p in parole:
		if p in char:
			return p

def verifica_2gram(stringa,char):
	parole = stringa.split(" ")
	parole = get_bigram(parole)
	for p in parole:
		if p in char:
			return p

def verifica_3gram(stringa,char):
	parole = stringa.split( )
	parole = get_trigram(parole)
	for p in parole:
		if p in char:
			return p

if __name__ == "__main__":
	#Apro il file pros_cat.json contenenti i commenti pros divisi per sezione
	with open(category_folder+"pros_cat.json") as json_file:
		pros_json = json.load(json_file)
		json_file.close()

	#Apro il file contenente le caratteristiche, della categoria, divise per sezione
	with open(characteristics_folder+category_name+".json") as json_file:
		charact_json = json.load(json_file)
		json_file.close()

	
	#print  pros_json.keys()
	#print charact_json[category_name].keys()

	#lista_caratteristiche charact_json[category_name]['Bass Guitars']


	for section in pros_json.keys():
		lista_characts = charact_json[category_name][section]
		print section
		print lista_characts
		for phrase in pros_json[section]:
			find = verifica_1gram(phrase,lista_characts)
			if find is None:
				find = verifica_2gram(phrase,lista_characts)
				if find is None:
					find = verifica_3gram(phrase,lista_characts)
			if find is not None:
				print "Caratteristica trovata: " + find
		print "\n########################################################################################"

	'''
	for key in json_data.keys():
		section =  key.encode('utf-8')
		print json_data[key]

	section = pros_json.keys()[0]
	print section.encode('utf-8')

	print charact_json[section]

	print pros_json[key]
	for phrase in pros_json[key]:
		print phrase
	'''