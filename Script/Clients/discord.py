import discord
from Script.clash_info import Bot
from Data.Const_variables.import_const import Login


intents = discord.Intents.default()
intents.members = True
Clash_info = Bot(intents=intents)

main_bot = 1
if main_bot:
    Token = Login["discord"]["token"]
    Clash_info.default_prefix = "/"
    Clash_info.id = 704688212832026724
else:
    Token = Login["discord"]["beta"]
    Clash_info.default_prefix = ","
    Clash_info.id = 710119855348645888
