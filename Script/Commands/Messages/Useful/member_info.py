# Sends information about a user

from Data.Modifiable_variables.import_var import Linked_accounts
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def member_info(ctx, member):
    accounts_linked = ""
    if member.id in list(Linked_accounts.keys()):
        for k, v in Linked_accounts[member.id].items():
            accounts_linked += f"{k} : {v}"
    else:
        accounts_linked = "None"
    member_permissions = ""
    if member.guild_permissions.administrator:
        member_permissions += "Administrator\n"
    if member.guild_permissions.ban_members:
        member_permissions += "Ban members\n"
    if member.guild_permissions.kick_members:
        member_permissions += "Kick off members\n"
    if member.guild_permissions.manage_roles:
        member_permissions += "Manage roles\n"
    if member.guild_permissions.manage_permissions:
        member_permissions += "Manage permissions\n"
    if member.guild_permissions.manage_guild:
        member_permissions += "Manage server\n"
    if member.guild_permissions.manage_channels:
        member_permissions += "Manage channel\n"
    if member.guild_permissions.manage_messages:
        member_permissions += "Manage messages\n"
    if member.guild_permissions.manage_nicknames:
        member_permissions += "Manage nicknames\n"
    if member.guild_permissions.mention_everyone:
        member_permissions += "Mention everyone\n"
    if member.guild_permissions.view_audit_log:
        member_permissions += "View logs\n"
    if member_permissions == "":
        member_permissions = "Any"
    embed = create_embed(member.name, f"{Emojis['Invite']} Server join : **{member.joined_at.date().isoformat()}**.\n{Emojis['Discord']} Discord account creation : **{member.created_at.date().isoformat()}**\n\n{Emojis['Member']} **Accounts linked :**\n{accounts_linked}\n\n{Emojis['Settings']} **Member permissions :**\n{member_permissions}", member.color, "", ctx.guild.me.avatar_url)
    embed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=embed)
