countries_dict = [
    {"names" : "Russia"},
    {"names" : "USA"},
    {"names" : "Italy"}
]

with open("list_country.json", "w") as list:
    json.dump(countries_dict, list_country)