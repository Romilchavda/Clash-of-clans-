import discord
from Script.import_emojis import Emojis


async def raw_reaction_remove_auto_roles(self, raw_reaction):
    if (raw_reaction.emoji in list(Emojis["Th_emojis"].keys())) or (raw_reaction.emoji in list(Emojis["Bh_emojis"].keys())) or (raw_reaction.emoji in list(Emojis["League_emojis"].keys())):
        if raw_reaction.message.embeds[0].title == "Click on the emojis to get the matching roles":
            guild = raw_reaction.message.guild
            if raw_reaction.emoji in list(Emojis["Th_emojis"].keys()):
                role = discord.utils.get(guild.roles, name=Emojis["Th_emojis"][raw_reaction.complete_emoji][0])
                await raw_reaction.member.remove_roles(role)
                return
            if raw_reaction.emoji in list(Emojis["Bh_emojis"].keys()):
                role = discord.utils.get(guild.roles, name=Emojis["Bh_emojis"][raw_reaction.complete_emoji][0])
                await raw_reaction.member.remove_roles(role)
                return
            if raw_reaction.emoji in list(Emojis["League_emojis"].keys()):
                role = discord.utils.get(guild.roles, name=Emojis["League_emojis"][raw_reaction.complete_emoji][0])
                await raw_reaction.member.remove_roles(role)
                return
    return
