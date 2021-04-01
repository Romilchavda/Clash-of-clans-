import discord
import dbl
from discord.ext import commands
from Script.Const_variables.import_const import Login


class TopGG(commands.Cog, dbl.DBLClient):
    def __init__(self):
        self.bot = discord.Client()
        self.token = Login["dbl"]["token"]
        self.dblpy = dbl.DBLClient(self.bot, self.token)
        self.http = self.dblpy

    async def update_stats(self, server_count):
        await self.bot.wait_until_ready()
        try:
            await self.dblpy.post_guild_count(server_count)
        except Exception as e:
            print("Failed to post server count\n{}: {}".format(type(e).__name__, e))


Dbl_client = TopGG()
