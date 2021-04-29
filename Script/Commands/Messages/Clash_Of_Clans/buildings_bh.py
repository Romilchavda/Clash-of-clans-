from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Bh_buildings
from Script.import_functions import create_embed


async def buildings_bh(ctx, lvl):
    if lvl > 9 or lvl < 0:
        await ctx.send(f"Builder Hall not found\nPlease give a valid BH level : there is no level `{lvl}` BH.", hidden=True)
        return
    elif lvl == 0:
        embed = create_embed("What is your BH level ?", "", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await ctx.send(embed=embed)
        for emoji in Emojis["Bh_emojis"].keys():
            await msg.add_reaction(emoji)
    elif 0 < lvl <= 9:
        level_bh = Bh_buildings.get(lvl)
        msg_bh = ""
        for category, buildings in level_bh.items():
            msg_bh += category + "\n"
            for building_name, building_max_level in buildings.items():
                msg_bh += f"{building_name} level max : {building_max_level}\n"
        embed = create_embed(f"__**BH {lvl} :\n**__", msg_bh, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await ctx.send(embed=embed)
        for emoji in Emojis["Bh_emojis"].keys():
            await msg.add_reaction(emoji)
    return
