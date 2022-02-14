# Edits the message with the information about the selected clan

from Script.Commands.Messages.clan_info import clan_info_embed


async def change_search_clan(ctx):
    if "search_clan" in ctx.origin_message.embeds[0].footer.text:
        if ctx.author.id == int(ctx.origin_message.embeds[0].footer.text.split("|")[1]):
            await ctx.defer(edit_origin=True)
            embed = await clan_info_embed(ctx, ctx.selected_options[0])
            embed.set_footer(text=f"search_clan|{ctx.author.id}")
            await ctx.edit_origin(embed=embed)
        else:
            await ctx.defer(hidden=True)
            await ctx.send("You can only use select menu of slash commands sent by you")
    return
