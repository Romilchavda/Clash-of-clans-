# Sends the list of the clan members with the selected super troop active

import coc

from Script.Clients.clash_of_clans_client import Clash_of_clans
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def clan_super_troops(ctx, clan_tag, super_troop):
    try:
        clan = await Clash_of_clans.get_clan(clan_tag)
    except coc.errors.NotFound:
        await ctx.send(f"Clan not found\nThere is no clan with the tag `{clan_tag}` (do not forget the # in front of the tag).", hidden=True)
        return
    members_with_super_troop = []
    async for member in clan.get_detailed_members():
        for s_troop in member.super_troops:
            if s_troop.name == super_troop and s_troop.is_active:
                members_with_super_troop.append(member.name)
    await ctx.send()  # TODO : Add the text to return
    return
