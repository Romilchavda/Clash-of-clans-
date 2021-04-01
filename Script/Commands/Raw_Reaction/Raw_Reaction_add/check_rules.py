import discord
from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Ids


async def raw_reaction_add_check_rules(self, raw_reaction):
    if (raw_reaction.emoji == Emojis["Yes"]) and (raw_reaction.channel_id == Ids["Rules"]):
        channel = raw_reaction.message.channel
<<<<<<< HEAD
        member_role = discord.utils.get(channel.guild.roles, name="Member")
        await raw_reaction.member.add_roles(member_role)
        rules = discord.utils.get(channel.guild.roles, name="Rules not checked")
        await raw_reaction.member.remove_roles(rules)
=======
        member = discord.utils.get(channel.guild.roles, name="Member")
        await member.add_roles(member)
        rules = discord.utils.get(channel.guild.roles, name="Rules not checked")
        await member.remove_roles(rules)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    return
