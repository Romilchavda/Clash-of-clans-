# Initialize the Top.gg client : Dbl_client

import discord
import topgg

from Data.Const_variables.import_const import Login

Dbl_client = topgg.DBLClient(discord.Client(), Login["topgg"]["token"])
