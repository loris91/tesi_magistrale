#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
La classe ha lo scopo di aggiungere ai file prodotto il campo categoria 
che è presente nel file revie relativo al prodotto in analisi.
Per ogni file prodotto va a cercare il relativo file review, da esso estrare la categoria e la aggiunge al file prodotto.





COSE DA FARE: 
Quando viene recuperata la categoria dal file review e viene aggiunta al file product cambiare il nome di quest'ultimo
eliminando lo spazio prima dell'estensione
'''

import os
import re
import json
import nltk
from pprint import pprint

review_folder = "/home/alakay/Scrivania/cache/"

def verifica_esistenza_review(category,filename):
	review_path = "/home/alakay/Scrivania/cache/"+category+"/review/"+re.sub(r" .json",".json",filename)
	try:
		open(review_path)
		return True
	except Exception, e:
		return False

def rinomina_file(category,filename):
	old_file_path = "/home/alakay/Scrivania/cache/"+category+"/product/"+filename
	new_file_path = "/home/alakay/Scrivania/cache/"+category+"/product/"+re.sub(r" .json",".json",filename)

	with open(old_file_path) as json_file:
		product_json = json.load(json_file)
		json_file.close()

	with open (new_file_path,"w") as myfile:
		json.dump(product_json, myfile)



def cancella_file(category,filename):
	if (" .json" in filename):
		file_path = "/home/alakay/Scrivania/cache/"+category+"/product/"+filename
		os.remove(file_path)

def elimina_spazio():
	list_folder = os.listdir(review_folder)

	for folder in list_folder:
		print folder
		folder_path = review_folder+folder+"/product"
		list_files = os.listdir(folder_path)
		for filename in list_files:
			if (verifica_esistenza_review(folder,filename)):
				rinomina_file(folder,filename)
			cancella_file(folder,filename)


def aggiungi_categoria():
	list_folder = os.listdir(review_folder)

	for folder in list_folder:
		print folder
		folder_path = review_folder+folder+"/product"
		list_files = os.listdir(folder_path)
		for filename in list_files:
			print filename
	

if __name__ == "__main__":
	list_folder = os.listdir(review_folder)
	folder = list_folder[0]

	folder_path = review_folder+folder+"/product"
	list_files = os.listdir(folder_path)

	for i in range(1,11):
		print list_files[i]
			
	
