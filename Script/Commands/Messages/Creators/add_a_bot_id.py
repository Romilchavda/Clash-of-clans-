# Sends a link to add the bot with the given ID

import discord

from Script.import_functions import create_embed


async def add_a_bot_id(ctx, bot_id):
    link = discord.utils.oauth_url(bot_id, permissions=discord.Permissions(administrator=True))
    embed = create_embed(f"Add the bot with the ID {bot_id} :", link, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
