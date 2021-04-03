import coc
from Script.import_emojis import Emojis
from Script.import_functions import create_embed, int_to_str
from Script.Clients.clash_of_clans import Clash_of_clans


async def get_clan(ctx, tag):
    try:
        clan = await Clash_of_clans.get_clan(tag)
        if clan.location is not None:
            lieu = clan.location.name
        else:
            lieu = "International"
        leader = "None"
        for member in clan.members:
            if member.role == coc.Role.leader:
                leader = member
                break
        ties = clan.war_ties
        if ties is None:
            ties = "unknown"
        losses = clan.war_losses
        if losses is None:
            losses = "unknown"
        embed = create_embed(f"Clan : {clan.name} ({clan.tag})", f"{Emojis['Trophy']} Clan points : {int_to_str(clan.points)}\n{Emojis['Trophy']} Builder base clan points : {int_to_str(clan.versus_points)}\n{Emojis['Trophy']} League : {clan.war_league}\n{Emojis['Trophy']} Required trophies : {int_to_str(clan.required_trophies)}\n{Emojis['Owner']} Leader : {leader.name} ({leader.tag})\n{Emojis['Members']} Number of members : {clan.member_count}\n:crossed_swords: Wars : {clan.war_wins} wins, {ties} ties and {losses} losses\n{Emojis['Pin']} Location : {lieu}\n{Emojis['Invite']} Invitations type : {clan.type}\n{Emojis['Description']} Description : {clan.description}\n[Open in Clash Of Clans]({clan.share_link})", ctx.guild.me.color, "For more information on clan members, put /members [tag]", ctx.guild.me.avatar_url)
        embed.set_thumbnail(url=clan.badge.url)
        await ctx.send(embed=embed)
    except coc.errors.NotFound:
        await ctx.send(f"Clan not found\nThere is no clan with the tag `{tag}` (do not forget the # in front of the tag).", hidden=True)
    return
