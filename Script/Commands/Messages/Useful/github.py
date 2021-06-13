import discord
from Script.import_emojis import Emojis
from Script.import_functions import create_embed_img


async def github(ctx):
    url = "attachment://github.png"
    file = discord.File("Pictures/Github.png", filename="github.png")
    embed = create_embed_img("Our Github :", f"{Emojis['Browser']} Enter this link in a browser to access to our GitHub or scan this QR Code.\nhttps://github.com/rreemmii-dev/Clash-Of-Clans-Discord-Bot", ctx.guild.me.color, "", ctx.guild.me.avatar_url, url)
    await ctx.send(embed=embed, file=file)
    return
