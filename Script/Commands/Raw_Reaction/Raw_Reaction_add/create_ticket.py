# Creates a ticket when the emoji is clicked

import discord

from Data.Variables.import_var import Support
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def raw_reaction_add_create_ticket(self, raw_reaction):
    if raw_reaction.emoji == Emojis["Ticket"]:
        channel = raw_reaction.message.channel
        guild = channel.guild
        member = raw_reaction.member
        await raw_reaction.message.remove_reaction(Emojis["Ticket"], member)
        for c in guild.text_channels:
            if c.topic == str(member.id):
                embed = create_embed("You cannot do this action", f"You are not allowed to create 2 ticket at the same time. You have already a ticket : {c.mention}", 0xff8000, "", guild.me.avatar_url)
                await channel.send(embed=embed, delete_after=5)
                return
        overwrite = {member.guild.default_role: discord.PermissionOverwrite(view_channel=False), member: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True, attach_files=True), self.user: discord.PermissionOverwrite(view_channel=True, send_messages=True, manage_channels=True, add_reactions=True, external_emojis=True)}
        if guild.id in list(Support.keys()):
            support = guild.get_role(Support[guild.id])
            overwrite.update({support: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)})
        ticket_category = channel.category
        text_channel = await member.guild.create_text_channel(f"Ticket {member.name}", category=ticket_category, overwrites=overwrite, topic=str(raw_reaction.user_id))
        await text_channel.send(f"{member.mention} this is your ticket !")
        return
    return
