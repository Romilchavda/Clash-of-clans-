import discord
from Script.import_emojis import Emojis
from Script.import_functions import create_embed
from Script.Clients.discord import Clash_info


async def bot_info(ctx):
    permission_now = ctx.guild.me.guild_permissions
    perms_required = discord.Permissions(manage_roles=True, manage_channels=True, create_instant_invite=True, view_channel=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True, read_message_history=True, mention_everyone=True, add_reactions=True, use_external_emojis=True, view_audit_log=True, manage_webhooks=True)
    msg_perm = ":warning: The bot needs the permissions : "
    perms_bot = []
    for perm in permission_now:
        if perm[1]:
            perms_bot.append(perm[0])
    for perm in perms_required:
        if perm[1] and not perm[0] in perms_bot:
            msg_perm += "\n" + perm[0]
    msg_perm += "\nSo please grant it to the bot."
    if msg_perm == ":warning: The bot needs the permissions : " + "\nSo please grant it to the bot.":
        msg_perm = f"{Emojis['Yes']} The bot has all required permissions !"
    msg_serv = f"{Emojis['Discord']} The bot is on {len(Clash_info.guilds)} servers !"
    msg_created = f"{Emojis['Calendar']} The bot was created the 28/04/2020, and certified the 23/09/2020."
    embed = create_embed("Clash INFO", f"{msg_perm}\n{msg_serv}\n{msg_created}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
