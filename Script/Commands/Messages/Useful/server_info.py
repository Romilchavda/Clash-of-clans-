# Sends information about the server

from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def server_info(ctx):
    users = 0
    for members in ctx.guild.members:
        if members.bot == 0:
            users += 1
    bots = 0
    for members in ctx.guild.members:
        if members.bot == 1:
            bots += 1
    emojis = ""
    emojis_count = 0
    for emoji in ctx.guild.emojis:
        if emojis_count > 10:
            emojis += "..."
            break
        emojis += f"{emoji} "
        emojis_count += 1
    admins = ""
    admins_count = 0
    for member in ctx.guild.members:
        if admins_count > 10:
            admins += "..."
            break
        if member.guild_permissions.administrator:
            admins += f"{member.mention} "
            admins_count += 1
    embed = create_embed(ctx.guild.name, f"{Emojis['Owner']} Owner : {ctx.guild.owner.mention}\n{Emojis['Calendar']} Created at : {ctx.guild.created_at.date().isoformat()}\n{Emojis['Members']} Humans : {users:, }\n{Emojis['Bot']} Bots : {bots: ,}\n{Emojis['Pin']} Region : {ctx.guild.region}\n{Emojis['Boost']} Boost level : {ctx.guild.premium_tier}/3\n{Emojis['Boost']} Boost number : {ctx.guild.premium_subscription_count}\n{Emojis['Emoji_ghost']} emojis : {emojis}\nAdministrators : {admins}", ctx.guild.me.color, "", ctx.guild.icon_url)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
    return
