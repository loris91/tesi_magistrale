#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
La classe characteristics_extractor.py ha lo scopo di estrarre le il "nome" delle caratteristiche e non loro valore.
'''

import os
import re
import json
import nltk
from pprint import pprint

category_name = "Software"

review_folder = "/home/alakay/Scrivania/cache/"+category_name+"/product"

def estrai():
	with open(review_folder+"/"+file_name) as json_file:
		json_data = json.load(json_file)
		json_file.close()

if __name__ == "__main__":
	list_files = os.listdir(review_folder)

	print len(list_files)
