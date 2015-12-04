#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
La classe pros_cons_extractor si occupa di estrarre i commenti PROS e CONS dai file json della cartella review
della categoria scelta. Per ogni review i commenti vengono puliti (eliminati caratteri specili), e le frasi
vengono separate in base ai caratteri [,.!?;] trovati in essa. Infine vengono generati 2 file json contenenti 
i commenti lavorati.

'''

import os
import re
import json
import nltk
from pprint import pprint

categories_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"


#Funzione che pulisce una frase da caratteri indesiderati
def pulisci(phrase):
	phrase = re.sub(r"\\xa0", " ", phrase)
	phrase = re.sub(r"&[^;]*;"," ",phrase) #Elimino i caratteri speciali

	phrase = re.sub(r"\{[^}]*\}","",phrase) #Elimino le parentesi {} e il loro contenuto
	phrase = re.sub(r"\[[^\]]*\]","",phrase) #Elimino le parentesi [] e il loro contenuto
	phrase = re.sub(r"\([^)]*\)","",phrase) #Elimino le parentesi () e il loro contenuto

	phrase = re.sub(r" +"," ",phrase) #Elimino gli spazi ripetuti
	return phrase

#Funzione che splitta una frase secondo la punteggiatura considerata
def split_phrase(phrase,data,key):
	phrase = re.sub(r"[,.!?;]",".",phrase)
	phrase = phrase.split(".")
	
	for opinion in phrase:
		if nltk.word_tokenize(opinion) != []:
			data[key].append(opinion)

	return data

#Funzione che splitta una frase secondo la punteggiatura 

#Funzione che analizza un file di una review e ne estrae i commenti Pros e Cons
def analizza_file(file_name,data_pros,data_pros_cat,data_cons,data_cons_cat):
	with open(review_folder+file_name) as json_file:
		json_data = json.load(json_file)
		json_file.close()

	for element in json_data['reviews']:
		section =  pulisci(element['Section'].encode('utf-8'))

		if section not in data_pros_cat.keys():
			data_pros_cat[section] = []
			data_cons_cat[section] = []

		
		pros = pulisci(element["Advantages"])
		split_phrase(pros,data_pros,'opinion')
		split_phrase(pros,data_pros_cat,section)

		cons = pulisci(element["Disadvantages"])
		split_phrase(cons,data_cons,'opinion')
		split_phrase(cons,data_cons_cat,section)

def funzione(review_folder,category_folder):
	list_files = os.listdir(review_folder)

	data_pros = {}
	data_pros['opinion'] = []

	data_pros_cat = {}

	data_cons = {}
	data_cons['opinion'] = []

	data_cons_cat = {}
	
	
	for product in list_files:
		analizza_file(product,data_pros,data_pros_cat,data_cons,data_cons_cat)

	print len (data_pros['opinion'])
	print len (data_cons['opinion'])

	with open (category_folder+"pros.json","w") as myfile:
			json.dump(data_pros, myfile)

	with open (category_folder+"cons.json","w") as myfile:
			json.dump(data_cons, myfile)

	with open (category_folder+"pros_cat.json","w") as myfile:
			json.dump(data_pros_cat, myfile)

	with open (category_folder+"cons_cat.json","w") as myfile:
			json.dump(data_cons_cat, myfile)





if __name__ == "__main__":
	list_folder = os.listdir(categories_folder)

	for category_name in list_folder:
		print category_name
		category_folder = categories_folder+category_name+"/"
		review_folder = category_folder+"review/"
		list_files = os.listdir(review_folder)
		funzione(review_folder,category_folder)
