# Edits information about the player with the given tag

from Data.components import Components
from Script.Commands.Messages.player_info import player_info_embed


async def change_player_stats_page(ctx):
    if "player_info" in ctx.origin_message.embeds[0].footer.text:
        if ctx.author.id == int(ctx.origin_message.embeds[0].footer.text.split("|")[1]):
            await ctx.defer(edit_origin=True)
            tag = f"#{ctx.origin_message.embeds[0].title.split('#')[len(ctx.origin_message.embeds[0].title.split('#')) - 1].split('(')[0]}"
            if ctx.selected_options[0] == "main":
                embed = await player_info_embed(ctx, tag, "main")
            if ctx.selected_options[0] == "troops":
                embed = await player_info_embed(ctx, tag, "troops")
            if ctx.selected_options[0] == "success":
                embed = await player_info_embed(ctx, tag, "success")
            await ctx.send(embed=embed, components=Components["player_info"])
        else:
            await ctx.defer(hidden=True)
            await ctx.send("You can only use select menu of slash commands sent by you")
    return
