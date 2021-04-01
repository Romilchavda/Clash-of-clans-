import discord
from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Ids


async def raw_reaction_remove_check_rules(self, raw_reaction):
    if raw_reaction.channel_id == Ids["Rules"] and raw_reaction.emoji == Emojis["Yes"]:
<<<<<<< HEAD
        member_role = discord.utils.get(raw_reaction.message.guild.roles, name="Member")
        await raw_reaction.member.remove_roles(member_role)
=======
        member = discord.utils.get(raw_reaction.message.guild.roles, name="Member")
        await member.remove_roles(member)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    return
