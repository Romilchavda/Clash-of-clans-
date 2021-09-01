# Sends information about the role

from Script.import_emojis import Emojis
from Script.import_functions import create_embed, int_to_str


async def role_info(ctx, role):
    role_permissions = ""
    if role.permissions.administrator:
        role_permissions += "Administrator\n"
    if role.permissions.ban_members:
        role_permissions += "Ban members\n"
    if role.permissions.kick_members:
        role_permissions += "Kick off members\n"
    if role.permissions.manage_roles:
        role_permissions += "Manage roles\n"
    if role.permissions.manage_permissions:
        role_permissions += "Manage permissions\n"
    if role.permissions.manage_guild:
        role_permissions += "Manage server\n"
    if role.permissions.manage_channels:
        role_permissions += "Manage channel\n"
    if role.permissions.manage_messages:
        role_permissions += "Manage messages\n"
    if role.permissions.manage_nicknames:
        role_permissions += "Manage nicknames\n"
    if role.permissions.mention_everyone:
        role_permissions += "Mention everyone\n"
    if role.permissions.view_audit_log:
        role_permissions += "View logs\n"
    if role_permissions == "":
        role_permissions = "Any\n"
    users = 0
    for members in role.members:
        if members.bot == 0:
            users += 1
    bots = 0
    for members in role.members:
        if members.bot == 1:
            bots += 1
    embed = create_embed(role.name, f"{Emojis['Members']} Humans : {int_to_str(users)}\n{Emojis['Bot']} Bots : {int_to_str(bots)}\n\n{Emojis['Settings']} **Role permissions :** \n{role_permissions}", role.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
