import pandas as pd
import time
import pickle
import csv
import re
import json
from progress.bar import Bar
from collections import Counter


# Load the dictionary
""" with open('saved_dictionary_iterate_sicut.pkl', 'rb') as f:
    para_dict = pickle.load(f) """
with open('data25edit.json') as json_file:
    para_dict = json.load(json_file)

newdict = {}         
for key, value in para_dict.items():
    # Normalize the full text by removing extra whitespace
    #print(key)
    OldKey = key
    LatinText = value[0]
    idlist = value[1]
    def normalize(sublist):
        return [elem.replace(":", "").replace(" ", "") for elem in sublist]

    # Use a set to store normalized sublists and avoid duplicates
    seen = set()
    unique_lists = []
    for sublist in idlist:
        normalized_sublist = tuple(normalize(sublist))
        if normalized_sublist not in seen:
            seen.add(normalized_sublist)
            unique_lists.append(sublist)  # Add the original list (not normalized)

    # Print the result
    #print(unique_lists)

    def normalize_string(s):
        return s.replace(":", "").replace(" ", "")

    # Extract first and second elements from each sublist and normalize
    normalized_pairs = [(sublist[0], normalize_string(sublist[1])) for sublist in unique_lists]

    # Count occurrences of the second element in the normalized pairs
    second_elements = [pair[1] for pair in normalized_pairs]
    occurrences = Counter(second_elements)

    # Create a dictionary with the unique (first, second) pair as key and its occurrence count
    unique_dict = {}
    for sublist in unique_lists:
        normalized_second = normalize_string(sublist[1])
        if (sublist[0], sublist[1]) not in unique_dict:
            unique_dict[(sublist[0], sublist[1])] = occurrences[normalized_second]

    # Sort the dictionary by occurrence count in descending order
    sorted_dict = dict(sorted(unique_dict.items(), key=lambda x: x[1], reverse=True))

    #save first items of sorted_dict into a variable
    besthit = 0
    result = []
    alternate = []
    for key, value in sorted_dict.items():
        if value == besthit:
           # print("tie")
            alternate.append(key)
        if value > besthit:
            besthit = value
            result = key
            alternate = []
        
        #print(key)
        break
    #print(result, besthit, alternate)
    
    newdict[OldKey] = [LatinText, result]
    # Print the resulting dictionary
    #print(sorted_dict)
        
for key, value in newdict.items():
    print(key)
    



json_file_path = 'data_result.json' 

# Writing JSON data
with open(json_file_path, 'w') as f:
        json.dump(newdict, f)  
           

  

