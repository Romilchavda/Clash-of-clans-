# Sends the link of the Google Sheet file with data for buildings/troops max level

from Script.import_functions import create_embed


async def coc_file(ctx):
    embed = create_embed('Here is the file that resume all the data of the bot on Clash Of Clans', 'https://docs.google.com/spreadsheets/d/1xKWA0o9GN3g8O5gShHZs3uKF9olu9YuOvn8MAgIANO4/edit?usp=sharing', ctx.guild.me.color, '', ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
