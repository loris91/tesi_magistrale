#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

'''
La classe pros_cons_word_cout analizza i file generati dalla classe pros_cons_extractor.
Per ogni file si dividono i commenti in base al numero di parole di cui il commento è formato, si conta 
di quante parole sono composti i commenti e se ne calcola la media. Tutte le informazioni vengono salvate in un file
json statistiche.json

'''
import os
import re
import json
import nltk
from pprint import pprint

categories_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"

def pros_work(category_folder):
	with open(category_folder+"pros.json") as json_file:
		json_data = json.load(json_file)
		json_file.close()

	json_stat = {}
	json_stat['Tipo'] = "Commenti PROS"


	numero_commenti = len(json_data['opinion'])
	somma =0

	for opinion  in json_data['opinion']:
		tokens = nltk.word_tokenize(opinion)
		somma = somma + len(tokens)
		key = str(len(tokens)) if (len(tokens)<8) else '>7'
		if json_stat.has_key(key):
			json_stat[key]=json_stat[key]+1
		else:
			json_stat[key]=1

	media = float(somma)/float(numero_commenti)
	media = str(media)
	media = re.sub(r"\.",",",media)

	json_stat['Numero_Commenti'] = str(numero_commenti)
	json_stat['Media'] = str(media)

	with open (category_folder+"statistiche.json","a") as myfile:
			json.dump(json_stat, myfile)


def cons_work(category_folder):
	with open(category_folder+"cons.json") as json_file:
		json_data = json.load(json_file)
		json_file.close()

	numero_commenti = len(json_data['opinion'])
	somma =0

	json_stat = {}
	json_stat['Tipo'] = "Commenti CONS"

	for opinion  in json_data['opinion']:
		tokens = nltk.word_tokenize(opinion)
		somma = somma + len(tokens)
		key = str(len(tokens)) if (len(tokens)<8) else '>7'
		if json_stat.has_key(key):
			json_stat[key]=json_stat[key]+1
		else:
			json_stat[key]=1

	media = float(somma)/float(numero_commenti)
	media = str(media)
	media = re.sub(r"\.",",",media)

	json_stat['Numero_Commenti'] = str(numero_commenti)
	json_stat['Media'] = str(media)
	with open (category_folder+"statistiche.json","a") as myfile:
			json.dump(json_stat, myfile)


if __name__ == "__main__":
	list_folder = os.listdir(categories_folder)

	for category_name in list_folder:
		#print category_name
		category_folder = categories_folder+category_name+"/"
		pros_work(category_folder)
		cons_work(category_folder)