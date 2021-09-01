# Deletes messages

import datetime

import discord

from Script.import_functions import create_embed, int_to_str


async def delete_messages_number(ctx, number):
    if number <= 0:
        await ctx.send("Error\nYou cannot delete a negative number of messages", hidden=True)
        return
    message_numbers = 0
    async for message in ctx.channel.history(limit=number + 1):
        if not message.pinned:
            message_numbers += 1
            await message.delete()
    message_numbers -= 1
    if message_numbers == 1:
        embed = create_embed("Messages deleted", f"{int_to_str(message_numbers)} message deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    else:
        embed = create_embed("Messages deleted", f"{int_to_str(message_numbers)} messages deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    try:
        await ctx.send(embed=embed)
    except discord.errors.NotFound:
        await ctx.channel.send(embed=embed)
    return


async def delete_messages_time(ctx, minutes):
    if minutes <= 0:
        await ctx.send("Error\nYou must choose a number of minutes strictly positive", hidden=True)
        return
    message_numbers = 0
    async for message in ctx.channel.history(after=(datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=minutes)).replace(tzinfo=None), oldest_first=False):
        if not message.pinned:
            message_numbers += 1
            await message.delete()
    message_numbers -= 1
    if message_numbers == 1:
        embed = create_embed("Messages deleted", f"{int_to_str(message_numbers)} message deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    else:
        embed = create_embed("Messages deleted", f"{int_to_str(message_numbers)} messages deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    try:
        await ctx.send(embed=embed)
    except discord.errors.NotFound:
        await ctx.channel.send(embed=embed)
    return


async def delete_messages_all(ctx):
    message_numbers = 0
    async for message in ctx.channel.history(limit=None):
        if not message.pinned:
            message_numbers += 1
            await message.delete()
    message_numbers -= 1
    if message_numbers == 1:
        embed = create_embed("Messages deleted", f"{int_to_str(message_numbers)} message deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    else:
        embed = create_embed("Messages deleted", f"{int_to_str(message_numbers)} messages deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    try:
        await ctx.send(embed=embed)
    except discord.errors.NotFound:
        await ctx.channel.send(embed=embed)
    return
