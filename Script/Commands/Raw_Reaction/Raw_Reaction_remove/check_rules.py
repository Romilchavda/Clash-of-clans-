# Removes the member role when the rules are unchecked

import discord

from Data.Constants.import_const import Ids
from Script.import_emojis import Emojis


async def raw_reaction_remove_check_rules(self, raw_reaction):
    if raw_reaction.channel_id == Ids["Rules_channel"] and raw_reaction.emoji == Emojis["Yes"]:
        member_role = discord.utils.get(raw_reaction.message.guild.roles, name="Member")
        await raw_reaction.member.remove_roles(member_role)
        rules_not_checked_role = discord.utils.get(raw_reaction.message.guild.roles, name="Rules not checked")
        await raw_reaction.member.add_roles(rules_not_checked_role)
    return
