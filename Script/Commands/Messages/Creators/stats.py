# Sends stats with monthly users

import sqlite3

from Script.import_functions import create_embed


async def stats(ctx):
    conn = sqlite3.connect("Data/Modifiable_variables.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM BotUsage")
    _monthly_users = cursor.fetchone()[0]
    text = f"Monthly users : {_monthly_users}"
    embed = create_embed("Stats :", text, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
