import json

from Data.utils import Utils

Main_bot = 0

def_login = open(Utils["secure_folder_path"] + "login.json", "r")
Login = json.load(def_login)
def_login.close()

def_ids = open("Data/Const_variables/ids.json", "r")
Ids = json.load(def_ids)
def_ids.close()
