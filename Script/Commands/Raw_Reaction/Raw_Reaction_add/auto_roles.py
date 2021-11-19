# Adds the role matching with the clicked emoji

import discord

from Script.import_emojis import Emojis


async def raw_reaction_add_auto_roles(self, raw_reaction):
    if (raw_reaction.emoji in list(Emojis["Th_emojis"].keys())) or (raw_reaction.emoji in list(Emojis["Bh_emojis"].keys())) or (raw_reaction.emoji in list(Emojis["League_emojis"].keys())):
        message = raw_reaction.message
        guild = message.guild
        member = raw_reaction.member
        if message.embeds[0].title == "Click on the emojis to get the matching roles":
            role = None
            if raw_reaction.emoji in list(Emojis["Th_emojis"].keys()):
                role = discord.utils.get(guild.roles, name=Emojis["Th_emojis"][raw_reaction.whole_emoji][0])
            if raw_reaction.emoji in list(Emojis["Bh_emojis"].keys()):
                role = discord.utils.get(guild.roles, name=Emojis["Bh_emojis"][raw_reaction.whole_emoji][0])
            if raw_reaction.emoji in list(Emojis["League_emojis"].keys()):
                role = discord.utils.get(guild.roles, name=Emojis["League_emojis"][raw_reaction.whole_emoji][0])
            if role and (guild.me.top_role.position > role.position):
                await member.add_roles(role)
    return
