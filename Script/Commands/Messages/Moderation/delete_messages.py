import discord
import datetime
from Script.import_functions import create_embed, int_to_str


async def delete_messages_number(ctx, number):
    if ctx.author.guild_permissions.manage_messages:
        if number <= 0:
            await ctx.send("Error\nYou cannot delete a negative number of messages", hidden=True)
            return
        nb_msg = 0
        async for msg in ctx.channel.history(limit=number+1):
            if not msg.pinned:
                nb_msg += 1
                await msg.delete()
        nb_msg -= 1
        if nb_msg == 1:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} message deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        else:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} messages deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        try:
            await ctx.send(embed=embed)
        except discord.errors.NotFound:
            await ctx.channel.send(embed=embed)
    else:
        await ctx.send("You cannot do this action\nYou are not allowed to delete messages.", hidden=True)
    return


async def delete_messages_time(ctx, minutes):
    if ctx.author.guild_permissions.manage_messages:
        if minutes <= 0:
            await ctx.send("Error\nYou must choose a number of minutes strictly positive", hidden=True)
            return
        nb_msg = 0
        async for msg in ctx.channel.history(after=(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=minutes)).replace(tzinfo=None), oldest_first=False):
            if not msg.pinned:
                nb_msg += 1
                await msg.delete()
        nb_msg -= 1
        if nb_msg == 1:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} message deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        else:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} messages deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        try:
            await ctx.send(embed=embed)
        except discord.errors.NotFound:
            await ctx.channel.send(embed=embed)
    else:
        await ctx.send("You cannot do this action\nYou are not allowed to delete messages.", hidden=True)
    return


async def delete_messages_all(ctx):
    if ctx.author.guild_permissions.manage_messages:
        nb_msg = 0
        async for msg in ctx.channel.history(limit=100):
            if not msg.pinned:
                nb_msg += 1
                await msg.delete()
        nb_msg -= 1
        if nb_msg == 1:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} message deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        else:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} messages deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        try:
            await ctx.send(embed=embed)
        except discord.errors.NotFound:
            await ctx.channel.send(embed=embed)
    else:
        await ctx.send("You cannot do this action\nYou are not allowed to delete messages.", hidden=True)
    return
