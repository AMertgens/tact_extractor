import pandas as pd
import time
import pickle
import csv
import re
import json

# Specify the file path of the CSV file (parsed list of quotes)
file_path = 'nostri-parsed_data.csv'
# Load the dictionary
with open('saved_dictionary_iterate.pkl', 'rb') as f:
    para_dict = pickle.load(f)

# Load the CSV file into a DataFrame
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    textfound= 0
    for row in csv_reader:
        # for each row in the CSV file, check if the snippet is found in the full text
        textfoundlocal = 0
        snippet =  normalized_string = re.sub(r'\s+', ' ', row[3])
        print("Snippet: ", snippet)
        idString = [row[0], row[1], row[2]]
        for key, value in para_dict.items():
            # Normalize the full text by removing extra whitespace
            fulltext =  normalized_string = re.sub(r'\s+', ' ', value[0])
            if snippet in fulltext :
                # If the snippet is found in the full text, increment the counter
                textfound += 1
                textfoundlocal += 1
                # Add the identifier to the list of identifiers for the snippet
                value[1].append(idString)
                #print(textfound,textfoundlocal)
                """ print("Found",snippet, key)
                time.sleep(1) """
            if textfoundlocal > 1:
                # If the snippet is found in more than one full text, print a warning
                print("Warning",snippet, key)
                time.sleep(1)
                break
    print(textfound)

# Save the dictionary
    with open('saved_dictionary_iterate2.pkl', 'wb') as f:
        pickle.dump(para_dict, f)     
    json_file_path = 'data3.json'

# Writing JSON data
    with open(json_file_path, 'w') as f:
        json.dump(para_dict, f)   
           

  

