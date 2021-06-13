import discord
import asyncio
from Script.import_emojis import Emojis
from Script.import_functions import int_to_str


async def ready_loop(self):
    if self.id == 704688212832026724:
        status_channel = self.get_channel(733089353634545684)
        msg = await status_channel.send(f"{Emojis['Yes']} Connected")
        await msg.edit(content=f"{Emojis['Yes']} Connected `{msg.created_at.replace(microsecond=0).isoformat(sep=' ')}` UTC-0")

    print("Connected")

    while True:
        nb_guilds = len(self.guilds)
        act = discord.Activity(type=discord.ActivityType.watching, name=int_to_str(nb_guilds) + " servers")
        await self.change_presence(status=discord.Status.online, activity=act)
        await asyncio.sleep(10)
        act = discord.Activity(type=discord.ActivityType.watching, name="/help")
        await self.change_presence(status=discord.Status.online, activity=act)
        await asyncio.sleep(50)
