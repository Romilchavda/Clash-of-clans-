from Script.import_emojis import Emojis
from Script.import_functions import create_embed, int_to_str


async def server_info(ctx):
    nb_humans = 0
    for members in ctx.guild.members:
        if members.bot == 0:
            nb_humans += 1
    nb_bots = 0
    for members in ctx.guild.members:
        if members.bot == 1:
            nb_bots += 1
    emojis = ""
    count = 0
    for emoji in ctx.guild.emojis:
        if count > 10:
            emojis += "..."
            break
        emojis += f"{emoji} "
        count += 1
    admins = ""
    count = 0
    for member in ctx.guild.members:
        if count > 10:
            admins += "..."
            break
        if member.guild_permissions.administrator:
            admins += f"{member.mention} "
            count += 1
    embed = create_embed(ctx.guild.name, f"{Emojis['Owner']} Owner : {ctx.guild.owner.mention}\n{Emojis['Calendar']} Created at : {ctx.guild.created_at.date().isoformat()}\n{Emojis['Members']} Humans : {int_to_str(nb_humans)}\n{Emojis['Bot']} Bots : {int_to_str(nb_bots)}\n{Emojis['Pin']} Region : {ctx.guild.region}\n{Emojis['Boost']} Boost level : {ctx.guild.premium_tier}/3\n{Emojis['Boost']} Boost number : {ctx.guild.premium_subscription_count}\n{Emojis['Emoji_ghost']} emojis : {emojis}\nAdministrators : {admins}", ctx.guild.me.color, "", ctx.guild.icon_url)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
    return
