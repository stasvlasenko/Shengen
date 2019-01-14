import os
import requests
import json
from pprint import pprint

with open("windows-1251.json", "r") as file:
     load_info = json.load(file)

#print(load_info)
memory = load_info['TextBody']

print(memory)

memory = memory.lower()
memory = memory.replace(',', '')
memory = memory.replace('.', '')
memory = memory.replace('/', '')
memory = memory.replace('!', '')
memory = memory.split()

my_dict = {}
for i in memory:
    if len(i) > 2:
        my_dict[i] = memory.count(i)

my_dict = sorted(my_dict.items(), key = lambda x: x[1], reverse= True)

for i, o in my_dict:
    if o > 1:
        print('%s - %s' % (i, o))


directory = os.getcwd()
print(directory)
os.chdir('../')
print(os.getcwd())