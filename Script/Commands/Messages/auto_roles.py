# Sends a message allowing users to add a reaction to get the matching role
import discord
import discord_slash

from Data.components import Components
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def auto_roles__th(ctx, channel):
    text = ""
    for th_level, emoji in Emojis["Th_emojis"].items():
        role = discord.utils.get(ctx.guild.roles, name=f"Town Hall {th_level}")
        if role is None:
            role = await ctx.guild.create_role(name=f"Town Hall {th_level}")
        text += f"{emoji} to be {role.mention}\n"
    embed = create_embed("Select your town hall level to get the matching role", text, ctx.guild.me.color, "auto_roles th", ctx.guild.me.avatar_url)
    if ctx.channel == channel:
        await ctx.send(embed=embed, components=Components["auto_roles__th"])
    else:
        await channel.send(embed=embed)
        if type(ctx) == discord_slash.context.SlashContext:
            await ctx.send("Done", hidden=True)
    return


async def auto_roles__bh(ctx, channel):
    text = ""
    for bh_level, emoji in Emojis["Bh_emojis"].items():
        role = discord.utils.get(ctx.guild.roles, name=f"Builder Hall {bh_level}")
        if role is None:
            role = await ctx.guild.create_role(name=f"Builder Hall {bh_level}")
        text += f"{emoji} to be {role.mention}\n"
    embed = create_embed("Select your builder hall level to get the matching role", text, ctx.guild.me.color, "auto_roles bh", ctx.guild.me.avatar_url)
    if ctx.channel == channel:
        await ctx.send(embed=embed, components=Components["auto_roles__bh"])
    else:
        await channel.send(embed=embed)
        if type(ctx) == discord_slash.context.SlashContext:
            await ctx.send("Done", hidden=True)
    return


async def auto_roles__leagues(ctx, channel):
    text = ""
    for league, emoji in Emojis["League_emojis"].items():
        role = discord.utils.get(ctx.guild.roles, name=league)
        if role is None:
            role = await ctx.guild.create_role(name=league)
        text += f"{emoji} to be {role.mention}\n"
    embed = create_embed("Select your league to get the matching role", text, ctx.guild.me.color, "auto_roles league", ctx.guild.me.avatar_url)
    if ctx.channel == channel:
        await ctx.send(embed=embed, components=Components["auto_roles__league"])
    else:
        await channel.send(embed=embed)
        if type(ctx) == discord_slash.context.SlashContext:
            await ctx.send("Done", hidden=True)
    return
