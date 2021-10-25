# Edits the message with the maximum level of each main base building for the given BH level

from Script.Commands.Messages.Clash_Of_Clans.buildings_th import buildings_th_embed


async def change_th_lvl(ctx):
    if "Buildings Town Hall" in ctx.origin_message.embeds[0].footer.text:
        embed = await buildings_th_embed(ctx, int(ctx.selected_options[0]))
        await ctx.edit_origin(embed=embed)
    return
