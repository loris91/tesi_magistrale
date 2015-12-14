#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
import re
import json
import nltk
from pprint import pprint

categories_folder = "/home/alakay/Scrivania/Ciao.co.uk/Category/"

def conta_righe_file_tmp():
	list_folder = os.listdir(categories_folder)

	for category_name in list_folder:
		category_folder = categories_folder+category_name+"/"

		with open(category_folder+"tmp_file.txt") as tmp_pros_file:
			content = tmp_pros_file.read().splitlines()

		pros_count=0
		cons_coutn=0
		count=0

		for tupla in content:
			(section,polarity,tagged) = eval(tupla)
			if "pros" == polarity:
				pros_count = pros_count+1
			if "cons" == polarity:
				cons_coutn = cons_coutn+1
			count = count+1

		print str(category_name) + "\t" + str(pros_count) + "\t" + str(cons_coutn) + "\t" + str(count)

if __name__ == "__main__":
	conta_righe_file_tmp()