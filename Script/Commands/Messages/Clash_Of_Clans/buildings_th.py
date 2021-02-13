from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Th_buildings
from Script.import_functions import create_embed


async def buildings_th(ctx, lvl):
    if lvl > 13 or lvl < 0:
        embed = create_embed("Town Hall not found", f"Please give a valid TH level : there is no level `{lvl}` TH.", 0xff0000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
    elif lvl == 0:
        embed = create_embed("What is your TH level ?", "", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await ctx.channel.send(embed=embed)
        for emoji in Emojis["Th_emojis"].keys():
            await msg.add_reaction(emoji)
    elif 0 < lvl <= 13:
        th = f"__**TH {lvl} :\n**__"
        level_hdv = Th_buildings[lvl]
        msg = ""
        for k, v in level_hdv.items():
            msg += k + "\n"
            for ka, va in v.items():
                msg += f"{ka} level max : {va}\n"
        embed = create_embed(th, msg, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await ctx.channel.send(embed=embed)
        for emoji in Emojis["Th_emojis"].keys():
            await msg.add_reaction(emoji)
    return
