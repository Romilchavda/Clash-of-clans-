import discord_slash.utils.manage_components as manage_components

from Script.import_emojis import Emojis

options = []
for emoji, name_value in Emojis["Bh_emojis"].items():
    options += [manage_components.create_select_option(name_value[0], value=str(name_value[1]), emoji=emoji)]
select = manage_components.create_select(options=options, placeholder="Select your Builder Hall level", min_values=1, max_values=1)
buildings_bh = [manage_components.create_actionrow(select)]

options = []
for emoji, name_value in Emojis["Th_emojis"].items():
    options += [manage_components.create_select_option(name_value[0], value=str(name_value[1]), emoji=emoji)]
select = manage_components.create_select(options=options, placeholder="Select your Town Hall level", min_values=1, max_values=1)
buildings_th = [manage_components.create_actionrow(select)]

options = [
    manage_components.create_select_option("Main", value="main", emoji=Emojis["Barbarian_king"]),
    manage_components.create_select_option("Troops", value="troops", emoji=Emojis["Troop"]),
    manage_components.create_select_option("Success", value="success", emoji=Emojis["Exp"])
]
select = manage_components.create_select(options=options, placeholder="Select the type of stats that you want to see", min_values=1, max_values=1)
player_info = [manage_components.create_actionrow(select)]

Components = {
    "buildings_bh": buildings_bh,
    "buildings_th": buildings_th,
    "player_info": player_info
}
