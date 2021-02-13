import json
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def tickets(ctx, text, ticket_channel, support, Support):
    if ctx.author.guild_permissions.administrator:
        if support is not None:
            Support.update({str(ctx.guild.id): support.id})
            embed = create_embed("Support role changed", f"The new support role for tickets in this server is : {support.mention}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
            await ctx.channel.send(embed=embed)
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
            embed = create_embed("Support role", f"The support role for tickets in this server is always : {support} (no change)", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
            await ctx.channel.send(embed=embed)

        embed = create_embed("Ticket :", text, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await ticket_channel.send(embed=embed)
        await msg.add_reaction(Emojis["Ticket"])
    else:
        embed = create_embed("You cannot do this action", "You are not allowed to create a ticket channel. You must be an administrator", 0xff8000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
    return


async def close_ticket(ctx, channel):
    if ctx.author.guild_permissions.manage_channels:
        embed = create_embed("Close this ticket", f":warning: It will delete the channel {channel.mention} !", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction(Emojis["Yes"])
        await msg.add_reaction(Emojis["No"])
    else:
        embed = create_embed("You cannot do this action", "You are not allowed to manage channels.", 0xff8000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
    return
