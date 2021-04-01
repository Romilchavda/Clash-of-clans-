from Script.import_functions import create_embed
from Script.Clients.discord import Clash_info


async def servers_list(ctx):
    servs = {}
    for guild in Clash_info.guilds:
        ok = 0
        for member in guild.members:
            if not member.bot:
                ok += 1
        servs[guild] = ok
    msg = ""
    a = 0
    z = 0
    for k in sorted(servs, key=servs.get, reverse=True):
        a += 1
        msg += f"\n{a + z * 10}) The server `{k.name}` with **{servs.get(k)}** members (owner : *{k.owner.name}*)"
        if a == 10:
            embed = create_embed(f"The {z * 10 + 1} to {(z + 1) * 10} best servers (by human members) :", msg, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
            await ctx.send(embed=embed)
            a = 0
            z += 1
            msg = ""
    if msg != "":
        embed = create_embed(f"The {z * 10 + 1} to {(z + 1) * 10} best servers (by human members) :", msg, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)
    return
