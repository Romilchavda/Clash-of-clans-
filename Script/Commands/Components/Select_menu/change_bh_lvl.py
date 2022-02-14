# Edits the message with the maximum level of each builder base building for the given BH level

from Script.Commands.Messages.buildings_bh import buildings_bh_embed


async def change_bh_lvl(ctx):
    if "buildings_bh" in ctx.origin_message.embeds[0].footer.text:
        if ctx.author.id == int(ctx.origin_message.embeds[0].footer.text.split("|")[1]):
            await ctx.defer(edit_origin=True)
            embed = await buildings_bh_embed(ctx, int(ctx.selected_options[0]))
            await ctx.edit_origin(embed=embed)
        else:
            await ctx.defer(hidden=True)
            await ctx.send("You can only use select menu of slash commands sent by you")
    return
