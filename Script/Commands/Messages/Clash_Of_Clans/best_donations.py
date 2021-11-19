# Sends the ratio of donations for each clan member

import coc

from Script.Clients.clash_of_clans_client import Clash_of_clans
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def best_donations(ctx, tag):
    try:
        clan = await Clash_of_clans.get_clan(tag)
    except coc.errors.NotFound:
        await ctx.send(f"Clan not found\nThere is no clan with the tag `{tag}` (do not forget the # in front of the tag).", hidden=True)
        return
    donations = {}
    for member in clan.members:
        if member.received == 0:
            ratio = member.donations
        else:
            ratio = round(member.donations/member.received, 2)
        donations.update({member.tag: [ratio, member.donations, member.received]})
    print(donations)
    # embed = create_embed(f"Clan : {clan.name} ({clan.tag})", f"{Emojis['Trophy']} Clan points : {clan.points: ,}\n{Emojis['Trophy']} Builder base clan points : {clan.versus_points: ,}\n{Emojis['Trophy']} League : {clan.war_league}\n{Emojis['Trophy']} Required trophies : {clan.required_trophies: ,}\n{Emojis['Owner']} Leader : {leader.name} ({leader.tag})\n{Emojis['Members']} Number of members : {clan.member_count}\n:crossed_swords: Wars : {clan.war_wins} wins, {ties} ties and {losses} losses\n{Emojis['Pin']} Location : {location}\n{Emojis['Language']} Language : {clan.chat_language}\n{Emojis['Invite']} Invitations type : {clan.type}\n{Emojis['Description']} Description : {clan.description}\n[Open in Clash Of Clans]({clan.share_link})", ctx.guild.me.color, "For more information on clan members, send /members [tag]", ctx.guild.me.avatar_url)
    # embed.set_thumbnail(url=clan.badge.url)
    # await ctx.send(embed=embed)
    # TODO : Finish it
    return
