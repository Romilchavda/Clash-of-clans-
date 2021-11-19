# Sends information about the bot

import discord

from Script.Clients.discord_client import Clash_info
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def bot_info(ctx):
    permission_now = ctx.guild.me.guild_permissions
    perms_required = discord.Permissions(manage_roles=True, manage_channels=True, create_instant_invite=True, view_channel=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True, read_message_history=True, mention_everyone=True, add_reactions=True, use_external_emojis=True, view_audit_log=True, manage_webhooks=True)
    text_permissions = ":warning: The bot needs the permissions : "
    perms_bot = []
    for perm in permission_now:
        if perm[1]:
            perms_bot.append(perm[0])
    for perm in perms_required:
        if perm[1] and not perm[0] in perms_bot:
            text_permissions += f"\n{perm[0]}"
    text_permissions += "\nSo please grant it to the bot."
    if text_permissions == ":warning: The bot needs the permissions : " + "\nSo please grant it to the bot.":
        text_permissions = f"{Emojis['Yes']} The bot has all required permissions !"
    text_servers_number = f"{Emojis['Discord']} The bot is on {len(Clash_info.guilds)} servers !"
    text_created = f"{Emojis['Calendar']} The bot was created the 2020-04-28, and certified the 2020-09-23."
    embed = create_embed("Clash INFO", f"{text_permissions}\n{text_servers_number}\n{text_created}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
