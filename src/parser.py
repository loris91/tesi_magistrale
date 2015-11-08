import os
import json
from pprint import pprint

review_folder = "/home/alakay/Scrivania/cache/review"

def prova():
	data = {}
	data['Username'] = 'Utente_1'
	data['Category'] = 'Mobile'
	data['Name'] = 'Name_1'
	data['Advantages'] = 'a1 a2 a3,a4 a5 a6,a7 a8 a9 10'
	data['Disadvantages'] = 'd1 d2, d3 d4 d5 d6, d7 d8 d9'
	json_data = json.dumps(data)

	with open("/home/alakay/Scrivania/file_json.txt","a") as myfile:
			myfile.write(str(json_data))

def analizza_file(file_name):
	file = open(review_folder+"/"+file_name)
	data = json.load(file)

if __name__ == "__main__":	
	list_files = os.listdir(review_folder)
	#print list_files[0]
	#analizza_file(list_files[0])
	prova()
