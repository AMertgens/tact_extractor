import time
import pickle
import json
import re

file1 = open('data.txt', 'r')
content = file1.read()
Paras = re.split(r'\n\s*\n\s*\n+', content)
paradict = {}
counter = 0
for para in Paras:
    """ print(para)
    time.sleep(1)  """
    paradict[counter] = [para.replace("\n", " "), []]
    counter +=1 
print(paradict)

with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(paradict, f)


file_path = 'data.json'

# Writing JSON data
with open(file_path, 'w') as f:
    json.dump(paradict, f)