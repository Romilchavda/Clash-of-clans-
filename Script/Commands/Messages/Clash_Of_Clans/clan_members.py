# Sends the list of the clan members 20 by 20, with several information about the member

import coc

from Script.Clients.clash_of_clans_client import Clash_of_clans
from Script.import_emojis import Emojis
from Script.import_functions import create_embed, trophies_to_league


async def clan_members(ctx, tag):
    try:
        clan = await Clash_of_clans.get_clan(tag)
    except coc.errors.NotFound:
        await ctx.send(f"Clan not found\nThere is no clan with the tag `{tag}` (do not forget the # in front of the tag).", hidden=True)
        return
    text = ""
    x = 0
    rank = 0
    async for member in clan.get_detailed_members():
        rank += 1
        lvl_to_emoji = {v[1]: k for k, v in tuple(Emojis["Th_emojis"].items())}
        text += f"- {rank} `{member.name}` : {trophies_to_league(member.trophies)} (best : {trophies_to_league(member.best_trophies)}) {lvl_to_emoji[member.town_hall]} {member.tag}\n"
        x += 1
        if x == 20:
            embed = create_embed(f"Clan members {clan.name} ({clan.tag})", f"Members list : \n{text}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
            await ctx.send(embed=embed)
            text = ""
            x = 0
    if x != 0:
        embed = create_embed(f"Clan members {clan.name} ({clan.tag})", f"Members list : \n{text}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)
    return
