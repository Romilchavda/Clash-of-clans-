import coc
from Script.import_emojis import Emojis
from Script.import_functions import create_embed
from Script.Clients.clash_of_clans import Clash_of_clans


async def clan_members(ctx, tag):
    try:
        clan = await Clash_of_clans.get_clan(tag)
        msg = ""
        x = 0
        async for member in clan.get_detailed_members():
            msg += f"- {member.name} : {member.trophies} {Emojis['Trophy']} (best : {member.best_trophies}) **TH {member.town_hall}** {member.tag}\n"
            x += 1
            if x == 10:
                embed = create_embed(f"Clan members {clan.name} ({clan.tag})", f"Members list : \n{msg}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
                await ctx.channel.send(embed=embed)
                msg = ""
                x = 0
        embed = create_embed(f"Clan members {clan.name} ({clan.tag})", f"Members list : \n{msg}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
    except coc.errors.NotFound:
        embed = create_embed("Not Found", f"There is no clan with the tag `{tag}` (do not forget the # in front of the tag).", 0xff0000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
    return
