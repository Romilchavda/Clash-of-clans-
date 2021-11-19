# Creates the Useful constant

import json

useful_file = open("Data/Constants/useful.json", "r")
Useful = json.load(useful_file)
useful_file.close()
