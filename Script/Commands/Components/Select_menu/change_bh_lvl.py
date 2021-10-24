# Edits the message with the maximum level of each builder base building for the given BH level

from Script.Commands.Messages.Clash_Of_Clans.buildings_bh import buildings_bh_embed


async def change_bh_lvl(ctx):
    if "Buildings Builder Hall" in ctx.origin_message.embeds[0].description:
        embed = buildings_bh_embed(ctx, int(ctx.selected_options[0]))
        await ctx.edit_origin(embed=embed)
    return
