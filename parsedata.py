import time
import pickle
import json

file1 = open('data.txt', 'r')
Paras = [para for para in file1.read().split('\n\n')]
paradict = {}
counter = 0
for para in Paras:
    print(para,  "/n"ç)
    time.sleep(1)
    paradict[counter] = [para, 0]
    counter +=1 
print(paradict)

""" with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(paradict, f) """


file_path = 'data.json'

# Writing JSON data
with open(file_path, 'w') as f:
    json.dump(paradict, f)