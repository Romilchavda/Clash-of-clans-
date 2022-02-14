# Edits the message with the maximum level of each main base building for the given TH level

from Script.Commands.Messages.buildings_th import buildings_th_embed


async def change_th_lvl(ctx):
    if "buildings_th" in ctx.origin_message.embeds[0].footer.text:
        if ctx.author.id == int(ctx.origin_message.embeds[0].footer.text.split("|")[1]):
            await ctx.defer(edit_origin=True)
            embed = await buildings_th_embed(ctx, int(ctx.selected_options[0]))
            await ctx.edit_origin(embed=embed)
        else:
            await ctx.defer(hidden=True)
            await ctx.send("You can only use select menu of slash commands sent by you")
    return
