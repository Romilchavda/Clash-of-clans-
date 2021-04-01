import discord


Intents = discord.Intents.default()
Intents.members = True
from Script.clash_info import Bot
Clash_info = Bot(intents=Intents)

from Script.Const_variables.import_const import Login
which_bot = 0
if which_bot == 0:
    Token = Login["discord"]["token"]
<<<<<<< HEAD
    Clash_info.default_prefix = "/"
    Clash_info.id = 704688212832026724
if which_bot == 1:
    Token = Login["discord"]["beta"]
    Clash_info.default_prefix = ","
=======
    Clash_info.Prefix_default = "/"
    Clash_info.id = 704688212832026724
if which_bot == 1:
    Token = Login["discord"]["beta"]
    Clash_info.Prefix_default = ","
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    Clash_info.id = 710119855348645888
