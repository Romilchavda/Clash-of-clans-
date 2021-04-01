from Script.import_emojis import Emojis
from Script.import_functions import create_embed
from Script.Clients.clash_of_clans import Clash_of_clans


async def search_clan(ctx, name, number):
    if number <= 0:
<<<<<<< HEAD
        await ctx.send("Syntax Error\nYou must enter a positive number of clans to show after the command.", hidden=True)
        return
    elif number > 10:
        number = 10
        await ctx.send("I can only show 10 clans to avoid spam.")
=======
        embed = create_embed("Syntax Error", "You must enter a positive number of clans to show after the command.", 0xff0000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
        return
    elif number > 10:
        number = 10
        await ctx.channel.send("I can only show 10 clans to avoid spam.")

>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    clans = await Clash_of_clans.search_clans(name=name, limit=number)
    a = 0
    for clan in clans:
        a += 1
        if clan.location is not None:
            lieu = clan.location.name
        else:
            lieu = "International"
        embed = create_embed(f"Clan : {clan.name} ({clan.tag})", f"{Emojis['Trophy']} Clan points : {clan.points}\n{Emojis['Trophy']} Builder base clan points : {clan.versus_points}\n{Emojis['Members']} Number of members : {clan.member_count}\n{Emojis['Pin']} Location : {lieu}\n[Open in Clash Of Clans]({clan.share_link})", ctx.guild.me.color, "For more information on clan members, put /clan_members [tag]", ctx.guild.me.avatar_url)
        embed.set_thumbnail(url=clan.badge.url)
<<<<<<< HEAD
        await ctx.send(embed=embed)
    await ctx.send(f"I showed {len(clans)} clans with the name `{name}`")
=======
        await ctx.channel.send(embed=embed)
    await ctx.channel.send(f"I showed {len(clans)} clans with the name `{name}`")
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    return
