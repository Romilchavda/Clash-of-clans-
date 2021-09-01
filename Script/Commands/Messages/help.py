# Sends the help message to use the bot

from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def help(ctx):
    embed = create_embed("Help : Slash commands list", "", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    embed.add_field(name="Clash Of Clans :", value="player_info\nclan_info\nsearch_clan\nclan_members\nbuildings_th\nbuildings_bh\nauto_roles [th|bh|leagues]\nfile", inline=True)
    embed.add_field(name="Useful :", value="bot_info\ntickets / close_ticket\npoll\ndirect_message [member|role]\nmember_info\nrole_info\nserver_info\nadd_the_bot\nsupport_server\npromote_the_bot", inline=True)
    embed.add_field(name="Moderation :", value="delete_messages [number_of_messages|for_x_minutes|all]", inline=True)
    embed.add_field(name="Links :", value=f"[{Emojis['Clash_info']} Add the bot](https://discord.com/oauth2/authorize?client_id=704688212832026724&scope=applications.commands+bot&permissions=805694544) | [{Emojis['Discord']} Support server](https://discord.gg/KQmstPw) | [{Emojis['Github']} GitHub](https://github.com/rreemmii-dev/Clash-Of-Clans-Discord-Bot)", inline=False)
    await ctx.send(embed=embed)
    return
