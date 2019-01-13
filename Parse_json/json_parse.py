import requests
import json
from pprint import pprint

with open("windows-1251.json", "r") as file:
     load_info = json.load(file)

pprint(load_info)

#resopnse = requests.get("https://jsonplaceholder.typicode.com/todos")
#todos = json.loads(resopnse.text)

#print(type(todos))
#pprint(todos)

