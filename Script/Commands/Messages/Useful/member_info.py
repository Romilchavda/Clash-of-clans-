from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def member_info(ctx, member):
    perms = ""
    if member.guild_permissions.administrator:
        perms += "Administrator\n"
    if member.guild_permissions.ban_members:
        perms += "Ban members\n"
    if member.guild_permissions.kick_members:
        perms += "Kick off members\n"
    if member.guild_permissions.manage_roles:
        perms += "Manage roles\n"
    if member.guild_permissions.manage_permissions:
        perms += "Manage permissions\n"
    if member.guild_permissions.manage_guild:
        perms += "Manage server\n"
    if member.guild_permissions.manage_channels:
        perms += "Manage channel\n"
    if member.guild_permissions.manage_messages:
        perms += "Manage messages\n"
    if member.guild_permissions.manage_nicknames:
        perms += "Manage nicknames\n"
    if member.guild_permissions.mention_everyone:
        perms += "Mention everyone\n"
    if member.guild_permissions.view_audit_log:
        perms += "View logs\n"
    if perms == "":
        perms = "Any"
    embed = create_embed(member.name, f"*The date format is YYYY-MM-DD*\n{Emojis['Invite']} Server join : **{member.joined_at.date().isoformat()}**.\n{Emojis['Discord']} Discord account creation : **{member.created_at.date().isoformat()}**\n\n**Member permissions :**\n{perms}", member.color, "", ctx.guild.me.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.channel.send(embed=embed)
