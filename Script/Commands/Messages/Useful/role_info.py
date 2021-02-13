from Script.import_functions import create_embed


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
        perms = "Any"
    embed = create_embed(role.name, f"**Role permissions :**\n{perms}", role.color, "", ctx.guild.me.avatar_url)
    await ctx.channel.send(embed=embed)
    return
