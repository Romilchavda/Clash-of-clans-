# Adds the role when the rules are checked

import discord

from Data.Const_variables.import_const import Ids
from Script.import_emojis import Emojis


async def raw_reaction_add_check_rules(self, raw_reaction):
    if (raw_reaction.emoji == Emojis["Yes"]) and (raw_reaction.channel_id == Ids["Rules_channel"]):
        channel = raw_reaction.message.channel
        member_role = discord.utils.get(channel.guild.roles, name="Member")
        await raw_reaction.member.add_roles(member_role)
        rules_not_checked_role = discord.utils.get(channel.guild.roles, name="Rules not checked")
        await raw_reaction.member.remove_roles(rules_not_checked_role)
    return
