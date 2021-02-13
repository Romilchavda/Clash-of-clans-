import discord
from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Ids


async def raw_reaction_add_check_rules(self, raw_reaction):
    if (raw_reaction.emoji == Emojis["Yes"]) and (raw_reaction.channel_id == Ids["Rules"]):
        channel = raw_reaction.message.channel
        member = discord.utils.get(channel.guild.roles, name="Member")
        await member.add_roles(member)
        rules = discord.utils.get(channel.guild.roles, name="Rules not checked")
        await member.remove_roles(rules)
    return
