import discord
from Script.import_emojis import Emojis
from Script.import_functions import create_embed_img


<<<<<<< HEAD
async def add_the_bot_default(ctx):
    perms = discord.Permissions(manage_roles=True, manage_channels=True, view_channel=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True, read_message_history=True, add_reactions=True, use_external_emojis=True, manage_webhooks=True)
    link = f"https://discord.com/oauth2/authorize?client_id={ctx.guild.me.id}&permissions={perms.value}&scope=applications.commands%20bot"
    url = "attachment://Add_the_bot_default.png"
    file = discord.File("Pictures/Add_the_bot_default.png", filename="Add_the_bot_default.png")
    embed = create_embed_img("The link to invite the bot", f"{Emojis['Browser']} Enter this link in a browser to add the bot to your server or scan this QR Code.\n{link}", ctx.guild.me.color, "If you like the bot, do not forget to share it !", ctx.guild.me.avatar_url, url)
    await ctx.send(embed=embed, file=file)
    return


async def add_the_bot_administrator(ctx):
    perms = discord.Permissions(administrator=True)
    link = f"https://discord.com/oauth2/authorize?client_id={ctx.guild.me.id}&permissions={perms.value}&scope=applications.commands%20bot"
    url = "attachment://Add_the_bot_administrator.png"
    file = discord.File("Pictures/Add_the_bot_administrator.png", filename="Add_the_bot_administrator.png")
    embed = create_embed_img("The link to invite the bot", f"{Emojis['Browser']} Enter this link in a browser to add the bot to your server or scan this QR Code.\n{link}", ctx.guild.me.color, "If you like the bot, do not forget to share it !", ctx.guild.me.avatar_url, url)
    await ctx.send(embed=embed, file=file)
    return
=======
async def add_the_bot(ctx):
    perms = discord.Permissions(manage_roles=True, manage_channels=True, create_instant_invite=True, view_channel=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True, read_message_history=True, mention_everyone=True, add_reactions=True, use_external_emojis=True, view_audit_log=True, manage_webhooks=True)
    link = f"https://discord.com/oauth2/authorize?client_id={ctx.guild.me.id}&permissions={perms.value}&scope=applications.commands%20bot"
    url = "attachment://add_clash_info.png"
    file = discord.File("../Pictures/add_clash_info.png", filename="add_clash_info.png")
    embed = create_embed_img("The link to invite the bot", f"{Emojis['Browser']} Enter this link in a browser to add the bot to your server or scan this QR Code.\n{link}", ctx.guild.me.color, "If you like the bot, do not forget to share it !", ctx.guild.me.avatar_url, url)
    await ctx.channel.send(embed=embed, file=file)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
