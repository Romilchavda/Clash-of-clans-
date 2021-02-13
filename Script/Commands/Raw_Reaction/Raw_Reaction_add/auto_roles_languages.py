import discord
from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Ids


async def raw_reaction_add_auto_roles_languages(self, raw_reaction):
    if (raw_reaction.emoji in Emojis["Languages_emoji"].keys()) and (raw_reaction.channel_id == Ids["Auto_roles"]):
        role = discord.utils.get(raw_reaction.message.guild.roles, name=Emojis["Languages_emoji"][raw_reaction.emoji])
        await raw_reaction.member.add_roles(role)
    return
