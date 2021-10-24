# Sends stats with monthly users

import sqlite3

from Data.utils import Utils
from Script.import_functions import create_embed


async def stats(ctx):
    connection = sqlite3.connect(Utils["secure_folder_path"] + "Modifiable.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM BotUsage")
    _monthly_users = cursor.fetchone()[0]
    text = f"Monthly users : {_monthly_users}"
    embed = create_embed("Stats :", text, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
