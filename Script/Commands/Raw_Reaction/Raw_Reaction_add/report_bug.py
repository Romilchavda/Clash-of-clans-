from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Ids


async def raw_reaction_add_report_bug(self, raw_reaction):
    channel = self.get_channel(raw_reaction.channel_id)
    member = raw_reaction.member
    if channel.id == Ids["Bug"] and member.guild_permissions.manage_messages:
        async for message in channel.history(limit=None):
            if message.id == raw_reaction.message_id and message.author.id == self.id:
                member = self.get_user(int(message.embeds[0].title.split("(")[1].split(")")[0]))
                if raw_reaction.emoji == Emojis["No"]:
                    await member.send("Your bug report was not a bug !\n`" + message.embeds[0].description + "`")
                    await message.delete()
                    return
                if raw_reaction.emoji == Emojis["Yes"]:
                    await member.send("Your bug was fixed !\n`" + message.embeds[0].description + "`")
                    await message.delete()
                    return
    return
