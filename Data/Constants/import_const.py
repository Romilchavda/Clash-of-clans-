# Creates the Login and Ids constants

import json

from Data.Constants.useful import Useful

Main_bot = 1

login_file = open(f"{Useful['secure_folder_path']}login.json", "r")
Login = json.load(login_file)
login_file.close()

ids_file = open("Data/Constants/ids.json", "r")
Ids = json.load(ids_file)
ids_file.close()
