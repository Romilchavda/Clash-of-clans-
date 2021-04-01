import discord
from Script.import_functions import create_embed_img


async def support_server(ctx):
    url = "attachment://support_server.png"
<<<<<<< HEAD
    file = discord.File("Pictures/support_server.png", filename="support_server.png")
    embed = create_embed_img("Our support server :", "Join our support server if you have questions or suggestions. https://discord.gg/KQmstPw", ctx.guild.me.color, "", ctx.guild.me.avatar_url, url)
    await ctx.send(embed=embed, file=file)
=======
    file = discord.File("../Pictures/support_server.png", filename="support_server.png")
    embed = create_embed_img("Our support server :", "Join our support server if you have questions or suggestions. https://discord.gg/KQmstPw", ctx.guild.me.color, "", ctx.guild.me.avatar_url, url)
    await ctx.channel.send(embed=embed, file=file)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    return
