# Initialize the Discord client : Clash_info

import discord

from Data.Const_variables.import_const import Login, Main_bot
from Script.clash_info import Bot

intents = discord.Intents.default()
intents.members = True
Clash_info = Bot(intents=intents)

if Main_bot:
    Token = Login["discord"]["token"]
    Clash_info.default_prefix = "/"
    Clash_info.id = 704688212832026724
else:
    Token = Login["discord"]["beta"]
    Clash_info.default_prefix = ","
    Clash_info.id = 710119855348645888
