import discord
from Script.import_emojis import Emojis
from Data.Const_variables.import_const import Ids


async def raw_reaction_remove_check_rules(self, raw_reaction):
    if raw_reaction.channel_id == Ids["Rules"] and raw_reaction.emoji == Emojis["Yes"]:
        member_role = discord.utils.get(raw_reaction.message.guild.roles, name="Member")
        await raw_reaction.member.remove_roles(member_role)
    return
