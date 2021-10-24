# Edits information about the player with the given tag

from Data.components import Components
from Script.Commands.Messages.Clash_Of_Clans.player_info import player_info_embed


async def change_player_stats_page(ctx):
    if "Player Information" == ctx.origin_message.embeds[0].description:
        tag = "#" + ctx.origin_message.embeds[0].title.split("#")[len(ctx.origin_message.embeds[0].title.split("#")) - 1].split("(")[0]
        if ctx.selected_options[0] == "main":
            embed = await player_info_embed(ctx, tag, "main")
        if ctx.selected_options[0] == "troops":
            embed = await player_info_embed(ctx, tag, "troops")
        if ctx.selected_options[0] == "success":
            embed = await player_info_embed(ctx, tag, "success")
        await ctx.send(components=Components["player_info"], embed=embed)
    return
