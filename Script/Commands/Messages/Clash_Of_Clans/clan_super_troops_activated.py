# Sends the list of the clan members with the selected super troop active

import coc

from Script.Clients.clash_of_clans_client import Clash_of_clans
from Script.import_functions import create_embed


async def clan_super_troops_activated(ctx, clan_tag, super_troop):
    try:
        clan = await Clash_of_clans.get_clan(clan_tag)
    except coc.errors.NotFound:
        await ctx.send(f"Clan not found\nThere is no clan with the tag `{clan_tag}` (do not forget the # in front of the tag).", hidden=True)
        return
    members_with_super_troop = []
    async for member in clan.get_detailed_members():
        for s_troop in member.super_troops:
            if s_troop.name == super_troop:
                max_level = s_troop.max_level
                if s_troop.is_active:
                    members_with_super_troop.append({"name": member.name, "tag": member.tag, "super_troop_level": "Unknown"})  # TODO : Add super_troop_level when the API will make it available
    text = ""
    for player in members_with_super_troop:
        text += f"- `{player['name']}` : {super_troop} level {player['super_troop_level']}/{max_level} {player['tag']}\n"
    if text == "":
        text = f"No player has the {super_troop} active in this clan"
    embed = create_embed(f"Members with the {super_troop} active in the clan {clan.name} ({clan.tag})", text, ctx.guild.me.color, "", icon_url=ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
