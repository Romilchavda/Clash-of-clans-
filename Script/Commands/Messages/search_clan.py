# Searches clans with the given name

from discord_slash.utils import manage_components

from Script.Clients.clash_of_clans_client import Clash_of_clans
from Script.Commands.Messages.clan_info import clan_info_embed


async def search_clan(ctx, name):
    if len(name) < 3:
        await ctx.send(f"Clan name has to be at least 3 characters long, not `{name}`")
        return
    clans = await Clash_of_clans.search_clans(name=name, limit=25)
    if not clans:
        await ctx.send(f"There is no clan with the name `{name}`")
        return

    first_embed_defined = False
    components_options = []
    for clan in clans:
        if not first_embed_defined:
            embed = await clan_info_embed(ctx, clan.tag)
            embed.set_footer(text=f"search_clan|{ctx.author.id}")
            first_embed_defined = True
        components_options += [manage_components.create_select_option(f"{clan.name} ({clan.tag}) - Level {clan.level}", value=clan.tag)]

    select = manage_components.create_select(options=components_options, placeholder="Select your clan", min_values=1, max_values=1)
    components = [manage_components.create_actionrow(select)]
    await ctx.send(embed=embed, components=components)
    return
