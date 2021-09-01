# Processes the ticket deletion confirmation

from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def raw_reaction_add_delete_ticket(self, raw_reaction):
    if raw_reaction.emoji == Emojis["Delete"]:
        channel = raw_reaction.message.channel
        if raw_reaction.member.guild_permissions.manage_channels:
            await channel.delete()
        else:
            embed = create_embed("You cannot do this action", "You are not allowed to manage channels.", 0xff8000, "", channel.guild.me.avatar_url)
            await channel.send(embed=embed)
    return
