# Sends a message with the maximum level of each builder base building for the given BH level

from Data.clash_of_clans import BuilderBuildings
from Data.components import Components
from Data.utils import Utils
from Script.import_functions import create_embed


async def buildings_bh_embed(ctx, lvl):
    level_bh = BuilderBuildings[lvl]
    text_bh = ""
    for category, buildings in level_bh.items():
        text_bh += "\n__" + category + " :__\n"
        for building_name, building_max_level in buildings.items():
            text_bh += f"{building_name} level max : {building_max_level}\n"
    embed = create_embed(f"__**BH {lvl} :\n**__", text_bh, ctx.guild.me.color, "Buildings Builder Hall", ctx.guild.me.avatar_url)
    return embed


async def buildings_bh(ctx, lvl):
    if lvl > Utils["max_bh_lvl"] or lvl < 0:
        await ctx.send(f"Builder Hall not found\nPlease give a valid BH level : there is no level `{lvl}` BH.", hidden=True)
        return

    elif lvl == 0:
        embed = create_embed("What is your BH level ?", "", ctx.guild.me.color, "Buildings Builder Hall", ctx.guild.me.avatar_url)
        await ctx.send(components=Components["buildings_bh"], embed=embed)

    elif 0 < lvl <= Utils["max_bh_lvl"]:
        embed = await buildings_bh_embed(ctx, lvl)
        await ctx.send(components=Components["buildings_bh"], embed=embed)
    return
