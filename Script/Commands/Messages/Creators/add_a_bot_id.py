import discord
from Script.import_functions import create_embed


async def add_a_bot_id(ctx, id):
    link = discord.utils.oauth_url(id, permissions=discord.Permissions(administrator=True))
    embed = create_embed(f"Add the bot with the ID {id} :", link, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
