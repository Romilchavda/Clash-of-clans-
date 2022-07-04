import sqlite3

import discord

from bot.functions import create_embed
from data.config import Config


async def stats(interaction: discord.Interaction):
    connection = sqlite3.connect(Config["secure_folder_path"] + "secure.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM bot_usage")
    nb_monthly_users = cursor.fetchone()[0]
    text = f"Monthly users: {nb_monthly_users}\n"

    cursor.execute("PRAGMA table_info(bot_usage)")
    commands_names = []
    for command_name in cursor.fetchall():
        if command_name[1] != "user_id":
            commands_names += [command_name[1]]

    for command in commands_names:
        cursor.execute(f"SELECT COUNT(*) FROM bot_usage WHERE NOT {command} = 0")
        text += f"{command}: {cursor.fetchone()[0]}\n"

    embed = create_embed("Stats:", text, interaction.guild.me.color, "", interaction.guild.me.avatar.url)
    await interaction.response.send_message(embed=embed)
    return
