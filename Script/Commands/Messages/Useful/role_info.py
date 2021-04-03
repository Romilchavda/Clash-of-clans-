from Script.import_emojis import Emojis
from Script.import_functions import create_embed, int_to_str


async def role_info(ctx, role):
    perms = ""
    if role.permissions.administrator:
        perms += "Administrator\n"
    if role.permissions.ban_members:
        perms += "Ban members\n"
    if role.permissions.kick_members:
        perms += "Kick off members\n"
    if role.permissions.manage_roles:
        perms += "Manage roles\n"
    if role.permissions.manage_permissions:
        perms += "Manage permissions\n"
    if role.permissions.manage_guild:
        perms += "Manage server\n"
    if role.permissions.manage_channels:
        perms += "Manage channel\n"
    if role.permissions.manage_messages:
        perms += "Manage messages\n"
    if role.permissions.manage_nicknames:
        perms += "Manage nicknames\n"
    if role.permissions.mention_everyone:
        perms += "Mention everyone\n"
    if role.permissions.view_audit_log:
        perms += "View logs\n"
    if perms == "":
        perms = "Any\n"
    nb_humans = 0
    for members in ctx.guild.members:
        if members.bot == 0:
            nb_humans += 1
    nb_bots = 0
    for members in ctx.guild.members:
        if members.bot == 1:
            nb_bots += 1
    embed = create_embed(role.name, f"{Emojis['Members']} Humans : {int_to_str(nb_humans)}\n{Emojis['Bot']} Bots : {int_to_str(nb_bots)}\n\n{Emojis['Settings']} **Role permissions :** \n{perms}", role.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
