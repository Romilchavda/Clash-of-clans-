import json

Main_bot = 1

def_login = open("Data/Const_variables/login.json", "r")
Login = json.load(def_login)
def_login.close()

def_ids = open("Data/Const_variables/ids.json", "r")
Ids = json.load(def_ids)
def_ids.close()
