# Removes the role matching with the clicked emoji

import discord

from Data.Constants.import_const import Ids
from Script.import_emojis import Emojis


async def raw_reaction_remove_auto_roles_languages(self, raw_reaction):
    if (raw_reaction.emoji in list(Emojis["Languages_emojis"].values())) and (raw_reaction.channel_id == Ids["Auto_roles_channel"]):
        role = discord.utils.get(raw_reaction.message.guild.roles, name=list(Emojis["Languages_emojis"].keys())[list(Emojis["Languages_emojis"].values()).index(raw_reaction.emoji)])
        await raw_reaction.member.remove_roles(role)
        return
    return
