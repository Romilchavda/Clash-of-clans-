from Script.import_emojis import Emojis
from Script.Commands.Messages.Clash_Of_Clans.get_player import player_info, player_troops


async def reaction_add_change_player_stats_page(self, reaction, member):
    if (reaction.emoji in [Emojis["Barbarian_king"], Emojis["Battle_machine"], Emojis["Exp"], Emojis["Troop"]]) and ("Player : " in reaction.message.embeds[0].title):
        tag = "#" + reaction.message.embeds[0].title.split("#")[len(reaction.message.embeds[0].title.split("#")) - 1].split("(")[0]
        if reaction.emoji == Emojis["Barbarian_king"]:
            embed = await player_info(member, tag, "main")
        if reaction.emoji == Emojis["Battle_machine"]:
            embed = await player_info(member, tag, "builder_base")
        if reaction.emoji == Emojis["Troop"]:
            embed = await player_troops(member, tag)
        if reaction.emoji == Emojis["Exp"]:
            embed = await player_info(member, tag, "success")
        await reaction.message.edit(embed=embed)
        await reaction.remove(member)
    return
