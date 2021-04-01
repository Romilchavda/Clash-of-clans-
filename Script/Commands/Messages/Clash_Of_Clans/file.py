from Script.import_functions import create_embed


async def file(ctx):
    embed = create_embed('Here is the file that resume all the data of the bot on Clash Of Clans', 'https://docs.google.com/spreadsheets/d/1K7P7Wi4zH76TDlVolaXpjGq20u_PnIc7mWUBYWSINaQ/edit?usp=drivesdk', ctx.guild.me.color, '', ctx.guild.me.avatar_url)
    await ctx.channel.send(embed=embed)
    return
