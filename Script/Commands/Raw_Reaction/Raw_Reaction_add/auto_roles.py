import discord
from Script.import_emojis import Emojis


async def raw_reaction_add_auto_roles(self, raw_reaction):
<<<<<<< HEAD
    if (raw_reaction.emoji in list(Emojis["Th_emojis"].keys())) or (raw_reaction.emoji in list(Emojis["Bh_emojis"].keys())) or (raw_reaction.emoji in list(Emojis["League_emojis"].keys())):
=======
    if (raw_reaction.emoji in Emojis["Th_emojis"].keys()) or (raw_reaction.emoji in Emojis["Bh_emojis"].keys()) or (raw_reaction.emoji in Emojis["League_emojis"].keys()):
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
        message = raw_reaction.message
        guild = message.guild
        member = raw_reaction.member
        if message.embeds[0].title == "Click on the emojis to get the matching roles":
<<<<<<< HEAD
            if raw_reaction.emoji in list(Emojis["Th_emojis"].keys()):
                a = discord.utils.get(guild.roles, name=Emojis["Th_emojis"][raw_reaction.complete_emoji][0])
                await member.add_roles(a)
                return
            if raw_reaction.emoji in list(Emojis["Bh_emojis"].keys()):
                a = discord.utils.get(guild.roles, name=Emojis["Bh_emojis"][raw_reaction.complete_emoji][0])
                await member.add_roles(a)
                return
            if raw_reaction.emoji in list(Emojis["League_emojis"].keys()):
                a = discord.utils.get(guild.roles, name=Emojis["League_emojis"][raw_reaction.complete_emoji][0])
=======
            if raw_reaction.emoji in Emojis["Th_emojis"].keys():
                a = discord.utils.get(guild.roles, name=Emojis["Th_emojis"][raw_reaction.emoji[0]])
                await member.add_roles(a)
                return
            if raw_reaction.emoji in Emojis["Bh_emojis"].keys():
                a = discord.utils.get(guild.roles, name=Emojis["Bh_emojis"][raw_reaction.emoji[0]])
                await member.add_roles(a)
                return
            if raw_reaction.emoji in Emojis["League_emojis"].keys():
                a = discord.utils.get(guild.roles, name=Emojis["League_emojis"][raw_reaction.emoji[0]])
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
                await member.add_roles(a)
                return
    return
