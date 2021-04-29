import discord
import asyncio
import os
import shutil
import requests
from Script.import_emojis import Emojis
from Script.import_functions import int_to_str


async def ready_loop(self):
    if self.id == 704688212832026724:
        status_channel = self.get_channel(733089353634545684)
        msg = await status_channel.send(f"{Emojis['Yes']} Connected")
        await msg.edit(content=f"{Emojis['Yes']} Connected `{msg.created_at.replace(microsecond=0).isoformat(sep=' ')}` UTC-0")

    if os.path.exists("Emojis_save"):
        shutil.rmtree("Emojis_save")
    os.mkdir("Emojis_save")
    emojis_servers_id = [714841480602320958, 716259214279966770, 696344010905747487, 761885092649762826, 836587468144509009, 719537805604290650, 779396058349568001, 836674086183895089]
    forbidden_characters = ["<", ">", ":", "“", "/", "\\", "|", "?", "*"]
    for guild_id in emojis_servers_id:
        guild = self.get_guild(guild_id)
        guild_name = guild.name
        for char in forbidden_characters:
            guild_name = guild_name.replace(char, "_")
        os.mkdir(f"Emojis_save/{guild_name}")
        for emoji in guild.emojis:
            r = requests.get(emoji.url, allow_redirects=True)
            extension = r.headers["Content-type"].split("/")[1]
            open(f"Emojis_save/{guild_name}/{emoji.name}.{extension}", "wb").write(r.content)
    shutil.make_archive("Emojis", 'zip', "Emojis_save")
    shutil.rmtree("Emojis_save")

    print("Connected")

    while True:
        nb_guilds = len(self.guilds)
        act = discord.Activity(type=discord.ActivityType.watching, name=int_to_str(nb_guilds) + " servers")
        await self.change_presence(status=discord.Status.online, activity=act)
        await asyncio.sleep(10)
        act = discord.Activity(type=discord.ActivityType.watching, name="/help")
        await self.change_presence(status=discord.Status.online, activity=act)
        await asyncio.sleep(50)
