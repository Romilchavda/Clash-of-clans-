import discord
from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Ids


async def raw_reaction_remove_auto_roles_languages(self, raw_reaction):
<<<<<<< HEAD
    if (raw_reaction.emoji in list(Emojis["Languages_emojis"].keys())) and (raw_reaction.channel_id == Ids["Auto_roles"]):
        role = discord.utils.get(raw_reaction.message.guild.roles, name=Emojis["Languages_emojis"][raw_reaction.emoji])
=======
    if (raw_reaction.emoji in Emojis["Languages_emoji"].keys()) and (raw_reaction.channel_id == Ids["Auto_roles"]):
        role = discord.utils.get(raw_reaction.message.guild.roles, name=Emojis["Languages_emoji"][raw_reaction.emoji])
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
        await raw_reaction.member.remove_roles(role)
        return
    return
