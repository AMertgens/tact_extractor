import pandas as pd
import time
import pickle
import csv
import re
import json

# Specify the file path
file_path = 'nostri-parsed_data.csv'
with open('saved_dictionary_iterate.pkl', 'rb') as f:
    para_dict = pickle.load(f)

# Load the CSV file into a DataFrame
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    textfound= 0
    for row in csv_reader:
        textfoundlocal = 0
        snippet =  normalized_string = re.sub(r'\s+', ' ', row[3])
        print("Snippet: ", snippet)
        idString = [row[0], row[1], row[2]]
        for key, value in para_dict.items():
            fulltext =  normalized_string = re.sub(r'\s+', ' ', value[0])
            if snippet in fulltext :
                textfound += 1
                textfoundlocal += 1
                value[1].append(idString)
                #print(textfound,textfoundlocal)
                """ print("Found",snippet, key)
                time.sleep(1) """
            if textfoundlocal > 1:
                print("Warning",snippet, key)
                time.sleep(1)
                break
    print(textfound)
    with open('saved_dictionary_iterate2.pkl', 'wb') as f:
        pickle.dump(para_dict, f)     
    json_file_path = 'data3.json'

# Writing JSON data
    with open(json_file_path, 'w') as f:
        json.dump(para_dict, f)   
           

  

