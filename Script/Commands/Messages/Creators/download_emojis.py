import discord


async def download_emojis(ctx):
    file = discord.File(fp="Emojis.zip", filename="Emojis.zip")
    await ctx.channel.send("Here are the emojis !", file=file)
    return
