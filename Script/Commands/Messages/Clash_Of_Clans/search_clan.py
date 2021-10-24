# Searches clans with the given name

from Script.Clients.clash_of_clans_client import Clash_of_clans
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def search_clan(ctx, name, number):
    if number <= 0:
        await ctx.send("Syntax Error\nYou must enter a positive number of clans to show after the command.", hidden=True)
        return
    elif number > 10:
        number = 10
        await ctx.send("I can only show 10 clans to avoid spam.")
    clans = await Clash_of_clans.search_clans(name=name, limit=number)
    n = 0
    for clan in clans:
        n += 1
        if clan.location is not None:
            location = clan.location.name
        else:
            location = "International"
        embed = create_embed(f"Clan : {clan.name} ({clan.tag})", f"{Emojis['Trophy']} Clan points : {clan.points}\n{Emojis['Trophy']} Builder base clan points : {clan.versus_points}\n{Emojis['Members']} Number of members : {clan.member_count}\n{Emojis['Pin']} Location : {location}\n[Open in Clash Of Clans]({clan.share_link})", ctx.guild.me.color, "For more information on clan members, put /clan_members [tag]", ctx.guild.me.avatar_url)
        embed.set_thumbnail(url=clan.badge.url)
        await ctx.send(embed=embed)
    await ctx.send(f"I sent {len(clans)} clans with the name `{name}`")
    return
