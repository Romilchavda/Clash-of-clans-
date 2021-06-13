import discord
from Script.import_emojis import Emojis
from Data.Const_variables.import_const import Ids


async def raw_reaction_add_auto_roles_languages(self, raw_reaction):
    if (raw_reaction.emoji in list(Emojis["Languages_emojis"].values())) and (raw_reaction.channel_id == Ids["Auto_roles"]):
        role = discord.utils.get(raw_reaction.message.guild.roles, name=list(Emojis["Languages_emojis"].keys())[list(Emojis["Languages_emojis"].values()).index(raw_reaction.emoji)])
        await raw_reaction.member.add_roles(role)
    return
