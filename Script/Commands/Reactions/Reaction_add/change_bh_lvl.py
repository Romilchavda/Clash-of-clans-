from Script.import_emojis import Emojis
from Data.Const_variables.import_const import Bh_buildings
from Script.import_functions import create_embed


async def reaction_add_change_bh_lvl(self, reaction, member):
    if (reaction.emoji in Emojis["Bh_emojis"].keys()) and ("BH" in reaction.message.embeds[0].title):
        lvl = Emojis["Bh_emojis"][reaction.emoji][1]
        bh = f"__**BH {lvl} :\n**__"
        level_bh = Bh_buildings[lvl]
        msg = ""
        for k, v in level_bh.items():
            msg += k + "\n"
            for ka, va in v.items():
                msg += f"{ka} level max : {va}\n"
        embed = create_embed(bh, msg, member.guild.me.color, "", member.guild.me.avatar_url)
        await reaction.message.edit(embed=embed)
        await reaction.remove(member)
    return
