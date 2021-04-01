from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Bh_buildings
from Script.import_functions import create_embed


async def buildings_bh(ctx, lvl):
    if lvl > 9 or lvl < 0:
<<<<<<< HEAD
        await ctx.send(f"Builder Hall not found\nPlease give a valid BH level : there is no level `{lvl}` BH.", hidden=True)
        return
    elif lvl == 0:
        embed = create_embed("What is your BH level ?", "", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await ctx.send(embed=embed)
=======
        embed = create_embed("Town Hall not found", f"Please give a valid BH level : there is no level `{lvl}` BH.", 0xff0000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
    elif lvl == 0:
        embed = create_embed("What is your BH level ?", "", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await ctx.channel.send(embed=embed)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
        for emoji in Emojis["Bh_emojis"].keys():
            await msg.add_reaction(emoji)
    elif 0 < lvl <= 9:
        bh = f"__**BH {lvl} :\n**__"
        level_bh = Bh_buildings.get(lvl)
        msg_bh = ""
        for kk, vv in level_bh.items():
            msg_bh += kk + "\n"
            for kka, vva in vv.items():
                msg_bh += f"{kka} level max : {vva}\n"
        embed = create_embed(bh, msg_bh, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
<<<<<<< HEAD
        msg = await ctx.send(embed=embed)
=======
        msg = await ctx.channel.send(embed)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
        for emoji in Emojis["Bh_emojis"].keys():
            await msg.add_reaction(emoji)
    return
