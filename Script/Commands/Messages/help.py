from Script.import_emojis import Emojis
from Script.import_functions import create_embed
"""
Emojis
Const
Var
Funct
Ids
Client
"""


async def help(ctx):
    embed = create_embed("Help : Slash commands list", "", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    embed.add_field(name="Clash Of Clans :", value="get_player\nget_clan\nsearch_clan\nclan_members\nbuildings_th\nbuildings_bh\nauto_roles [th|bh|leagues]\nfile", inline=True)
    embed.add_field(name="Useful :", value="bot_info\ntickets / close_ticket\npoll\ndirect_message [member|role]\nmember_info\nrole_info\nserver_info\nadd_the_bot\nsupport_server\npromote_the_bot", inline=True)
    embed.add_field(name="Moderation :", value="delete_messages [number_of_messages|for_x_minutes|all]", inline=True)
<<<<<<< HEAD
    msg = await ctx.send(embed=embed)
=======
    msg = await ctx.channel.send(embed=embed)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")
    await msg.add_reaction("3️⃣")
    await msg.add_reaction(Emojis["Info"])
    await msg.add_reaction(Emojis["Yes"])
    return
