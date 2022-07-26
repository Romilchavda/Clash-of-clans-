import discord

from bot.core.slash_commands.player_info import player_info_embed


async def change_player_stats_page(interaction: discord.Interaction):
    tag = f"#{interaction.message.embeds[0].title.split('#')[-1].split('(')[0].split(')')[0]}"
    if interaction.data["values"][0] == "main":
        embed = await player_info_embed(interaction, tag, "main")
    elif interaction.data["values"][0] == "troops":
        embed = await player_info_embed(interaction, tag, "troops")
    elif interaction.data["values"][0] == "success":
        embed = await player_info_embed(interaction, tag, "success")
    await interaction.response.edit_message(embed=embed)
    return
