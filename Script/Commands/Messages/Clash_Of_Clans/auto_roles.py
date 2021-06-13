import discord
import discord_slash
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def auto_roles_th(ctx, channel):
    if ctx.author.guild_permissions.administrator:
        msg = ""
        for emoji, value in Emojis["Th_emojis"].items():
            role = discord.utils.get(ctx.guild.roles, name=value[0])
            if role is None:
                role = await ctx.guild.create_role(name=value[0])
            msg += f"{emoji} to be {role.mention}\n"
        embed = create_embed("Click on the emojis to get the matching roles", msg, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await channel.send(embed=embed)
        if type(ctx) == discord_slash.context.SlashContext:
            await ctx.send("Done", hidden=True)
        for emoji in Emojis["Th_emojis"].keys():
            await msg.add_reaction(emoji)
    else:
        await ctx.send("You are not allowed to create an auto-roles system. You must be an administrator", hidden=True)
    return


async def auto_roles_bh(ctx, channel):
    if ctx.author.guild_permissions.administrator:
        msg = ""
        for emoji, value in Emojis["Bh_emojis"].items():
            role = discord.utils.get(ctx.guild.roles, name=value[0])
            if role is None:
                role = await ctx.guild.create_role(name=value[0])
            msg += f"{emoji} to be {role.mention}\n"
        embed = create_embed("Click on the emojis to get the matching roles", msg, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await channel.send(embed=embed)
        if type(ctx) == discord_slash.context.SlashContext:
            await ctx.send("Done", hidden=True)
        for emoji in Emojis["Bh_emojis"].keys():
            await msg.add_reaction(emoji)
    else:
        await ctx.send("You are not allowed to create an auto-roles system. You must be an administrator", hidden=True)
    return


async def auto_roles_leagues(ctx, channel):
    if ctx.author.guild_permissions.administrator:
        msg = ""
        for emoji, value in Emojis["League_emojis"].items():
            role = discord.utils.get(ctx.guild.roles, name=value[0])
            if role is None:
                role = await ctx.guild.create_role(name=value[0])
            msg += f"{emoji} to be {role.mention}\n"
        embed = create_embed("Click on the emojis to get the matching roles", msg, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        msg = await channel.send(embed=embed)
        if type(ctx) == discord_slash.context.SlashContext:
            await ctx.send("Done", hidden=True)
        for emoji in Emojis["League_emojis"].keys():
            await msg.add_reaction(emoji)
    else:
        await ctx.send("You are not allowed to create an auto-roles system. You must be an administrator", hidden=True)
    return
