import json


def_login = open("Data/Const_variables/login.json", "r")
Login = json.load(def_login)
def_login.close()

def_troops = open("Data/Const_variables/troops.json", "r")
Troops = json.load(def_troops)
def_troops.close()

def_th = open("Data/Const_variables/th_buildings.json", "r")
th_buildings = json.load(def_th)
def_th.close()
Th_buildings = {}
for th_lvl, dict in th_buildings.items():
    if th_lvl != "Last Update":
        Th_buildings[int(th_lvl)] = dict

def_bh = open("Data/Const_variables/bh_buildings.json", "r")
bh_buildings = json.load(def_bh)
def_bh.close()
Bh_buildings = {}
for bh_lvl, dict in bh_buildings.items():
    if bh_lvl != "Last Update":
        Bh_buildings[int(bh_lvl)] = dict

def_ids = open("Data/Const_variables/ids.json", "r")
Ids = json.load(def_ids)
def_ids.close()
