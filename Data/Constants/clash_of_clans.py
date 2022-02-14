# Creates the Troops, BuilderBuildings and MainBuildings constants

import sqlite3

from Data.Constants.useful import Useful

connection = sqlite3.connect("Data/Constants/Clash_Of_Clans.sqlite")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

BuilderBuildings = {}
for lvl in range(1, Useful["max_bh_lvl"] + 1):
    BuilderBuildings.update({lvl: {}})
    for category in Useful["bh_buildings_categories"]:
        BuilderBuildings[lvl].update({category: {}})
        cursor.execute(f"SELECT name, BH{lvl} FROM BuilderBuildings WHERE category='{category}' AND BH{lvl}!=0")
        for building in cursor.fetchall():
            BuilderBuildings[lvl][category].update({building["name"]: building[f"BH{lvl}"]})

MainBuildings = {}
for lvl in range(1, Useful["max_th_lvl"] + 1):
    MainBuildings.update({lvl: {}})
    for category in Useful["th_buildings_categories"]:
        MainBuildings[lvl].update({category: {}})
        cursor.execute(f"SELECT name, TH{lvl} FROM MainBuildings WHERE category='{category}' AND TH{lvl}!=0")
        for building in cursor.fetchall():
            MainBuildings[lvl][category].update({building["name"]: building[f"TH{lvl}"]})
