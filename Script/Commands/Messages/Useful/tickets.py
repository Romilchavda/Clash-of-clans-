# Sends a message with a reaction to create a ticket channel

import json

from Data.Modifiable_variables.import_var import Support
from Data.utils import Utils
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def tickets(ctx, text, ticket_channel, support):
    await ticket_channel.edit(name="tickets")
    if support is not None:
        Support.update({str(ctx.guild.id): support.id})
        embed = create_embed("Support role changed", f"The new support role for tickets in this server is : {support.mention}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)
        json_text = json.dumps(Support, sort_keys=True, indent=4)
        def_support = open(Utils["secure_folder_path"] + "support_for_tickets.json", "w")
        def_support.write(json_text)
        def_support.close()
    else:
        if ctx.guild.id in list(Support.keys()):
            support = ctx.guild.get_role(Support[ctx.guild.id])
        else:
            support = None
        if support is None:
            support = "`not set : only administrators by default`"
        else:
            support = support.mention
        embed = create_embed("Support role", f"The support role for tickets in this server stay : {support})", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)

    embed = create_embed("Ticket :", text, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    message = await ticket_channel.send(embed=embed)
    await message.add_reaction(Emojis["Ticket"])
    return


async def close_ticket(ctx, channel):
    embed = create_embed("Close this ticket", f":warning: It will delete the channel {channel.mention} !", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    message = await ctx.send(embed=embed)
    await message.add_reaction(Emojis["Yes"])
    await message.add_reaction(Emojis["No"])
    return
