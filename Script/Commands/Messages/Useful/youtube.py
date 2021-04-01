from Script.import_functions import create_embed


async def youtube(ctx):
    embed = create_embed("The YouTube channel dedicated to the bot :", "[Clash FAMILY YouTube Channel](https://www.youtube.com/channel/UC5jAaxdA0uWJCOfghYORWjA)", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
