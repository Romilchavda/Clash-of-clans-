# Edits the message with the maximum level of each main base building for the given BH level

from Data.clash_of_clans import MainBuildings
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def reaction_add_change_th_lvl(self, reaction, member):
    if (reaction.emoji in Emojis["Th_emojis"].keys()) and ("TH" in reaction.message.embeds[0].title):
        lvl = Emojis["Th_emojis"][reaction.emoji][1]
        th = f"__**TH {lvl} :\n**__"
        level_th = MainBuildings[lvl]
        text = ""
        for k, v in level_th.items():
            text += "\n__" + k + " :__\n"
            for ka, va in v.items():
                text += f"{ka} level max : {va}\n"
        embed = create_embed(th, text, member.guild.me.color, "", member.guild.me.avatar_url)
        await reaction.message.edit(embed=embed)
        await reaction.remove(member)
    return
