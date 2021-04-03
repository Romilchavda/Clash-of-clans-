import discord
from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Ids


async def raw_reaction_remove_auto_roles_languages(self, raw_reaction):
    if (raw_reaction.emoji in list(Emojis["Languages_emojis"].keys())) and (raw_reaction.channel_id == Ids["Auto_roles"]):
        role = discord.utils.get(raw_reaction.message.guild.roles, name=Emojis["Languages_emojis"][raw_reaction.emoji])
        await raw_reaction.member.remove_roles(role)
        return
    return
