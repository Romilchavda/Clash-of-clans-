from Script.import_functions import create_embed
from Script.Clients.discord import Clash_info


async def servers_list(ctx):
    servers = {}
    for guild in Clash_info.guilds:
        human_members = 0
        for member in guild.members:
            if not member.bot:
                human_members += 1
        servers[guild] = human_members
    msg = ""
    a = 0
    z = 0
    for guild in sorted(servers, key=servers.get, reverse=True):
        a += 1
        msg += f"\n{a + z * 10}) The server `{guild.name}` with **{servers[guild]}** members (owner : *{guild.owner.name}*)"
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
