import discord
import topgg
from Data.Const_variables.import_const import Login


class DblClient(topgg.DBLClient):
    async def on_dbl_vote(self, data):
        print(data)
        print("top_gg.py")


Dbl_client = DblClient(discord.Client(), Login["topgg"]["token"], autopost=True)
