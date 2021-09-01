# Sends links to add the bot

import discord

from Script.import_emojis import Emojis
from Script.import_functions import create_embed_img


async def add_the_bot_default(ctx):
    perms = discord.Permissions(manage_roles=True, manage_channels=True, view_channel=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True, read_message_history=True, add_reactions=True, use_external_emojis=True, manage_webhooks=True)
    url = "attachment://Add_the_bot_default.png"
    link = discord.utils.oauth_url(ctx.guild.me.id, permissions=perms, scopes=["applications.commands", "bot"])
    qrcode = discord.File("Pictures/Add_the_bot_default.png", filename="Add_the_bot_default.png")
    embed = create_embed_img("The link to invite the bot", f"{Emojis['Browser']} Enter this link in a browser to add the bot to your server or scan this QR Code.\n{link}", ctx.guild.me.color, "If you like the bot, do not forget to share it !", ctx.guild.me.avatar_url, url)
    await ctx.send(embed=embed, file=qrcode)
    return


async def add_the_bot_administrator(ctx):
    perms = discord.Permissions(administrator=True)
    url = "attachment://Add_the_bot_administrator.png"
    link = discord.utils.oauth_url(ctx.guild.me.id, permissions=perms, scopes=["applications.commands", "bot"])
    qrcode = discord.File("Pictures/Add_the_bot_administrator.png", filename="Add_the_bot_administrator.png")
    embed = create_embed_img("The link to invite the bot", f"{Emojis['Browser']} Enter this link in a browser to add the bot to your server or scan this QR Code.\n{link}", ctx.guild.me.color, "If you like the bot, do not forget to share it !", ctx.guild.me.avatar_url, url)
    await ctx.send(embed=embed, file=qrcode)
    return
