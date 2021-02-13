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
    roles = ""
    count = 0
    for role in ctx.guild.roles:
        if count > 10:
            roles += "..."
            break
        roles += f"{role.mention} "
        count += 1
    embed = create_embed(ctx.guild.name, f"{Emojis['Owner']} Owner : {ctx.guild.owner.mention}\n{Emojis['Calendar']} Created at (*YYYY-MM-DD*) : {ctx.guild.created_at.date().isoformat()}\n{Emojis['Members']} Humans : {int_to_str(nb_humans)}\n{Emojis['Bot']} Bots : {int_to_str(nb_bots)}\n{Emojis['Pin']} Region : {ctx.guild.region}\n{Emojis['Boost']} Boost level : {ctx.guild.premium_tier}/3\n{Emojis['Boost']} Boost number : {ctx.guild.premium_subscription_count}\n{Emojis['Emoji_ghost']} emojis : {emojis}\nRoles : {roles}", ctx.guild.me.color, "", ctx.guild.icon_url)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.channel.send(embed=embed)
    return
