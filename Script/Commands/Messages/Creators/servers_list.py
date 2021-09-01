# Sends the list of servers that have the bot
# TODO : Send a .txt file instead of embeds

from Script.Clients.discord_client import Clash_info
from Script.import_functions import create_embed


async def servers_list(ctx):
    guilds = {}
    for guild in Clash_info.guilds:
        users = 0
        for member in guild.members:
            if not member.bot:
                users += 1
        guilds[guild] = users
    text = ""
    ones = 0
    tens = 0
    for guild in sorted(guilds, key=guilds.get, reverse=True):
        ones += 1
        text += f"\n{ones + tens * 10}) The server `{guild.name}` with **{guilds[guild]}** members (owner : *{guild.owner.name}*)"
        if ones == 10:
            embed = create_embed(f"The {tens * 10 + 1} to {(tens + 1) * 10} best servers (by human members) :", text, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
            await ctx.send(embed=embed)
            ones = 0
            tens += 1
            text = ""
    if text != "":
        embed = create_embed(f"The {tens * 10 + 1} to {(tens + 1) * 10} best servers (by human members) :", text, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)
    return
