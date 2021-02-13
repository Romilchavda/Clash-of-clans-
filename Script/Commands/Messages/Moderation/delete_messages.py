import datetime
from Script.import_functions import create_embed, int_to_str


async def delete_messages_number(ctx, number):
    if ctx.author.guild_permissions.manage_messages:
        if number <= 0:
            embed = create_embed("Error", "You cannot delete a negative number of messages", 0xff0000, "", ctx.guild.me.avatar_url)
            await ctx.channel.send(embed=embed)
            return
        nb_msg = 0
        async for msg in ctx.channel.history(limit=number):
            if not msg.pinned:
                nb_msg += 1
                await msg.delete()
        if nb_msg == 1:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} message deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        else:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} messages deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed, delete_after=5)
    else:
        embed = create_embed("You cannot do this action", "You are not allowed to delete messages.", 0xff8000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
    return


async def delete_messages_time(ctx, minutes):
    if ctx.author.guild_permissions.manage_messages:
        if minutes <= 0:
            embed = create_embed("Error", "You must choose a number of minutes strictly positive", 0xff0000, "", ctx.guild.me.avatar_url)
            await ctx.channel.send(embed=embed)
            return
        nb_msg = 0
        async for msg in ctx.channel.history(after=datetime.datetime.now() - datetime.timedelta(minutes=minutes), oldest_first=False):
            if not msg.pinned:
                nb_msg += 1
                await msg.delete()
        if nb_msg == 1:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} message deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        else:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} messages deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed, delete_after=5)
    else:
        embed = create_embed("You cannot do this action", "You are not allowed to delete messages.", 0xff8000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
    return


async def delete_messages_all(ctx):
    if ctx.author.guild_permissions.manage_messages:
        nb_msg = 0
        async for msg in ctx.channel.history(limit=None):
            if not msg.pinned:
                nb_msg += 1
                await msg.delete()
        if nb_msg == 1:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} message deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        else:
            embed = create_embed("Messages deleted", f"{int_to_str(nb_msg)} messages deleted", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed, delete_after=5)
    else:
        embed = create_embed("You cannot do this action", "You are not allowed to delete messages.", 0xff8000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
    return
