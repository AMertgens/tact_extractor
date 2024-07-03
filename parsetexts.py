import pandas as pd
import time
import pickle
import csv
import re

# Specify the file path
file_path = 'parsed_data.csv'
with open('saved_dictionary.pkl', 'rb') as f:
    para_dict = pickle.load(f)

# Load the CSV file into a DataFrame
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    textfound= 0
    for row in csv_reader:
        textfoundlocal = 0
        snippet =  normalized_string = re.sub(r'\s+', ' ', row[3])
        
        for key, value in para_dict.items():
            fulltext =  normalized_string = re.sub(r'\s+', ' ', value[0])
            if snippet in fulltext :
                textfound += 1
                textfoundlocal += 1
                print(textfound,textfoundlocal)
                print("Found", snippet, key, fulltext)
            if textfoundlocal > 1:
                print("Warning", snippet, key, fulltext)
                time.sleep(10)
                break
    print(textfound)
                
          
           

  

