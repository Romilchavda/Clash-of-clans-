# Edits the message with the maximum level of each builder base building for the given BH level

from Data.clash_of_clans import BuilderBuildings
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def reaction_add_change_bh_lvl(self, reaction, member):
    if (reaction.emoji in Emojis["Bh_emojis"].keys()) and ("BH" in reaction.message.embeds[0].title):
        lvl = Emojis["Bh_emojis"][reaction.emoji][1]
        bh = f"__**BH {lvl} :\n**__"
        level_bh = BuilderBuildings[lvl]
        text = ""
        for k, v in level_bh.items():
            text += "\n__" + k + " :__\n"
            for ka, va in v.items():
                text += f"{ka} level max : {va}\n"
        embed = create_embed(bh, text, member.guild.me.color, "", member.guild.me.avatar_url)
        await reaction.message.edit(embed=embed)
        await reaction.remove(member)
    return
