import discord


Intents = discord.Intents.default()
Intents.members = True
from Script.clash_info import Bot
Clash_info = Bot(intents=Intents)

from Script.Const_variables.import_const import Login
which_bot = 0
if which_bot == 0:
    Token = Login["discord"]["token"]
    Clash_info.default_prefix = "/"
    Clash_info.id = 704688212832026724
if which_bot == 1:
    Token = Login["discord"]["beta"]
    Clash_info.default_prefix = ","
    Clash_info.id = 710119855348645888
