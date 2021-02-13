import discord
from Script.import_emojis import Emojis
from Script.Modifiable_variables.import_var import Support
from Script.import_functions import create_embed


async def raw_reaction_add_create_ticket(self, raw_reaction):
    if raw_reaction.emoji == Emojis["Ticket"]:
        channel = raw_reaction.message.channel
        guild = channel.guild
        member = raw_reaction.member
        await raw_reaction.message.remove_reaction(Emojis["Ticket"], member)
        for salon in guild.channels:
            if str(salon.type) == "text":
                if salon.topic == str(member.id):
                    embed = create_embed("You cannot do this action", "You are not allowed to create 2 ticket at the same time. You have already a ticket : " + salon.mention, 0xff8000, "", guild.me.avatar_url)
                    await channel.send(embed=embed, delete_after=5)
                    return
        overwrite = {member.guild.default_role: discord.PermissionOverwrite(view_channel=False), member: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True), self.user: discord.PermissionOverwrite(view_channel=True, send_messages=True, manage_channels=True, add_reactions=True, external_emojis=True)}
        try:
            support = Support[guild.id]
            overwrite.update({support: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)})
        except KeyError:
            pass
        ticket_cat = channel.category
        text_channel = await member.guild.create_text_channel("Ticket " + member.name, category=ticket_cat, overwrites=overwrite, topic=raw_reaction.user_id)
        await text_channel.send(member.mention + " this is your ticket !")
        return
    return
