import sqlite3

from Data.utils import Utils

connection = sqlite3.connect("Data/Clash_Of_Clans.sqlite")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("SELECT * FROM Troops")
Troops = {}
for troop in cursor.fetchall():
    d = dict(troop)
    d.update({"player": "-"})
    Troops[d["name"]] = d

BuilderBuildings = {}
for lvl in range(1, Utils["max_bh_lvl"] + 1):
    BuilderBuildings.update({lvl: {}})
    for category in Utils["bh_buildings_categories"]:
        BuilderBuildings[lvl].update({category: {}})
        cursor.execute(f"SELECT name, BH{lvl} FROM BuilderBuildings WHERE category='{category}' AND BH{lvl}!=0")
        for building in cursor.fetchall():
            BuilderBuildings[lvl][category].update({building["name"]: building["BH" + str(lvl)]})

MainBuildings = {}
for lvl in range(1, Utils["max_th_lvl"] + 1):
    MainBuildings.update({lvl: {}})
    for category in Utils["th_buildings_categories"]:
        MainBuildings[lvl].update({category: {}})
        cursor.execute(f"SELECT name, TH{lvl} FROM MainBuildings WHERE category='{category}' AND TH{lvl}!=0")
        for building in cursor.fetchall():
            MainBuildings[lvl][category].update({building["name"]: building["TH" + str(lvl)]})
