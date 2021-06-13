import discord
import os
import shutil
import requests
from Script.Clients.discord import Clash_info


async def download_emojis(ctx):
    if os.path.exists("Emojis_save"):
        shutil.rmtree("Emojis_save")
    os.mkdir("Emojis_save")
    emojis_servers_id = [714841480602320958, 716259214279966770, 696344010905747487, 761885092649762826, 836587468144509009, 719537805604290650, 779396058349568001, 836674086183895089]
    forbidden_characters = ["<", ">", ":", "“", "/", "\\", "|", "?", "*"]
    for guild_id in emojis_servers_id:
        guild = Clash_info.get_guild(guild_id)
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

    file = discord.File(fp="Emojis.zip", filename="Emojis.zip")
    await ctx.send("Here are the emojis !", file=file)
    return
