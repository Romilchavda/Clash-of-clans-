import json
from Script.import_emojis import Emojis
from Script.import_functions import create_embed
<<<<<<< HEAD
from Script.Modifiable_variables.import_var import Support


async def tickets(ctx, text, ticket_channel, support):
    if ctx.author.guild_permissions.administrator:
        await ticket_channel.edit(name="tickets")
        if support is not None:
            Support.update({str(ctx.guild.id): support.id})
            embed = create_embed("Support role changed", f"The new support role for tickets in this server is : {support.mention}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
            await ctx.send(embed=embed)
=======


async def tickets(ctx, text, ticket_channel, support, Support):
    if ctx.author.guild_permissions.administrator:
        if support is not None:
            Support.update({str(ctx.guild.id): support.id})
            embed = create_embed("Support role changed", f"The new support role for tickets in this server is : {support.mention}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
            await ctx.channel.send(embed=embed)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
            json_txt = json.dumps(Support, sort_keys=True, indent=4)
            def_support = open("Modifiable_variables/def_support_tickets.json", "w")
            def_support.write(json_txt)
            def_support.close()
        else:
            try:
                support = ctx.guild.get_role(Support[str(ctx.guild.id)])
            except KeyError:
                support = None
            if support is None:
                support = "`not set : only administrators`"
            else:
                support = support.mention
<<<<<<< HEAD
            embed = create_embed("Support role", f"The support role for tickets in this server stay : {support})", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
            await ctx.send(embed=embed)
=======
            embed = create_embed("Support role", f"The support role for tickets in this server is always : {support} (no change)", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
            await ctx.channel.send(embed=embed)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9

        embed = create_embed("Ticket :", text, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await ticket_channel.send(embed=embed)
        await msg.add_reaction(Emojis["Ticket"])
    else:
<<<<<<< HEAD
        await ctx.send("You cannot do this action\nYou are not allowed to create a ticket channel. You must be an administrator", hidden=True)
=======
        embed = create_embed("You cannot do this action", "You are not allowed to create a ticket channel. You must be an administrator", 0xff8000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    return


async def close_ticket(ctx, channel):
    if ctx.author.guild_permissions.manage_channels:
        embed = create_embed("Close this ticket", f":warning: It will delete the channel {channel.mention} !", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
<<<<<<< HEAD
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(Emojis["Yes"])
        await msg.add_reaction(Emojis["No"])
    else:
        await ctx.send("You cannot do this action\nYou are not allowed to manage channels.", hidden=True)
=======
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction(Emojis["Yes"])
        await msg.add_reaction(Emojis["No"])
    else:
        embed = create_embed("You cannot do this action", "You are not allowed to manage channels.", 0xff8000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    return
