from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def reaction_add_close_ticket(self, reaction, member):
    if (reaction.emoji in [Emojis["Yes"], Emojis["No"]]) and (reaction.message.embeds[0].title == "Close this ticket"):
        if reaction.emoji == Emojis['Yes']:
            if member.guild_permissions.manage_channels:
                await reaction.message.channel.delete()
            else:
                embed = create_embed("You cannot do this action", member.mention + ", you are not allowed to manage channels.", 0xff8000, "", member.guild.me.avatar_url)
                await reaction.message.channel.send(embed=embed)
        if reaction.emoji == Emojis['No']:
            if member.guild_permissions.manage_channels:
                await reaction.message.delete()
            else:
                embed = create_embed("You cannot do this action", member.mention + ", you are not allowed to manage channels.", 0xff8000, "", member.guild.me.avatar_url)
                await reaction.message.channel.send(embed=embed)
    return
