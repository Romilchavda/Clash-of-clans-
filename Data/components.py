# Assembles the used components in the constant Components

from discord_slash.utils import manage_components

from Data.Constants.useful import Useful
from Script.import_emojis import Emojis


options = []
for bh_level, emoji in Emojis["Bh_emojis"].items():
    options.append(manage_components.create_select_option(f"Builder Hall {bh_level}", value=str(bh_level), emoji=emoji))
select = manage_components.create_select(options=options, placeholder="Select your builder hall level", min_values=1, max_values=Useful["max_bh_lvl"])
auto_roles__bh = [manage_components.create_actionrow(select)]

options = []
for league, emoji in Emojis["League_emojis"].items():
    options.append(manage_components.create_select_option(league, value=league, emoji=emoji))
select = manage_components.create_select(options=options, placeholder="Select your league", min_values=1, max_values=len(Useful["league_trophies"].keys()))
auto_roles__league = [manage_components.create_actionrow(select)]

options = []
for th_level, emoji in Emojis["Th_emojis"].items():
    options.append(manage_components.create_select_option(f"Town Hall {th_level}", value=str(th_level), emoji=emoji))
select = manage_components.create_select(options=options, placeholder="Select your town hall level", min_values=1, max_values=Useful["max_th_lvl"])
auto_roles__th = [manage_components.create_actionrow(select)]


options = []
for bh_level, emoji in Emojis["Bh_emojis"].items():
    options += [manage_components.create_select_option(f"BH {bh_level}", value=str(bh_level), emoji=emoji)]
select = manage_components.create_select(options=options, placeholder="Select your Builder Hall level", min_values=1, max_values=1)
buildings_bh = [manage_components.create_actionrow(select)]

options = []
for th_level, emoji in Emojis["Th_emojis"].items():
    options += [manage_components.create_select_option(f"TH {th_level}", value=str(th_level), emoji=emoji)]
select = manage_components.create_select(options=options, placeholder="Select your Town Hall level", min_values=1, max_values=1)
buildings_th = [manage_components.create_actionrow(select)]


options = [
    manage_components.create_select_option("Main", value="main", emoji=Emojis["Barbarian_king"]),
    manage_components.create_select_option("Troops", value="troops", emoji=Emojis["Troop"]),
    manage_components.create_select_option("Success", value="success", emoji=Emojis["Exp"])
]
select = manage_components.create_select(options=options, placeholder="Select the type of stats that you want to see", min_values=1, max_values=1)
player_info = [manage_components.create_actionrow(select)]


button_follow = manage_components.create_button(style=2, label="Follow the support server news channel", emoji=Emojis["News"], custom_id="follow")
button_delete = manage_components.create_button(style=4, label="Delete this channel", emoji=Emojis["Delete_grey"], custom_id="delete")
joined_guild_message = [manage_components.create_actionrow(button_follow, button_delete)]

Components = {
    "auto_roles__bh": auto_roles__bh,
    "auto_roles__league": auto_roles__league,
    "auto_roles__th": auto_roles__th,
    "buildings_bh": buildings_bh,
    "buildings_th": buildings_th,
    "joined_guild_message": joined_guild_message,
    "player_info": player_info
}
