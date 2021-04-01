import discord
import asyncio
from Script.import_functions import int_to_str


async def loop(self):
    while True:
        nb_guilds = len(self.guilds)
        act = discord.Activity(type=discord.ActivityType.watching, name=int_to_str(nb_guilds) + " servers")
        await self.change_presence(status=discord.Status.online, activity=act)
        await asyncio.sleep(10)
        act = discord.Activity(type=discord.ActivityType.watching, name="/help")
        await self.change_presence(status=discord.Status.online, activity=act)
        await asyncio.sleep(50)
