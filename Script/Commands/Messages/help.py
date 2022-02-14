# Sends the help message to use the bot

from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def help(ctx):
    embed = create_embed("Help : Slash commands list", "", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    embed.add_field(name="Clash Of Clans :", value="member_info\nbot_info\nplayer_info\nclan_info\nsearch_clan\nclan_members\nclan_super_troops_activated\nbuildings_th\nbuildings_bh\nauto_roles [th|bh|leagues]", inline=True)
    embed.add_field(name="Links :", value=f"[{Emojis['Clash_info']} Add the bot](https://discord.com/oauth2/authorize?client_id=704688212832026724&scope=applications.commands+bot&permissions=805694544) | [{Emojis['Discord']} Support server](https://discord.gg/KQmstPw) | [{Emojis['Github']} GitHub](https://github.com/rreemmii-dev/Clash-Of-Clans-Discord-Bot)", inline=False)
    await ctx.send(embed=embed)
    return
