from Script.import_emojis import Emojis
from Data.Const_variables.import_const import Th_buildings
from Script.import_functions import create_embed


async def reaction_add_change_th_lvl(self, reaction, member):
    if (reaction.emoji in Emojis["Th_emojis"].keys()) and ("TH" in reaction.message.embeds[0].title):
        lvl = Emojis["Th_emojis"][reaction.emoji][1]
        th = f"__**TH {lvl} :\n**__"
        level_th = Th_buildings[lvl]
        msg = ""
        for k, v in level_th.items():
            msg += k + "\n"
            for ka, va in v.items():
                msg += f"{ka} level max : {va}\n"
        embed = create_embed(th, msg, member.guild.me.color, "", member.guild.me.avatar_url)
        await reaction.message.edit(embed=embed)
        await reaction.remove(member)
    return
