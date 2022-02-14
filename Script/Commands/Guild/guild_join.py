# Called when the bot joins a guild

import discord

from Data.components import Components
from Data.Constants.import_const import Ids
from Script.Clients.top_gg_client import Dbl_client
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def guild_join(self, guild):
    await Dbl_client.post_guild_count(len(self.guilds))
    users = 0
    bots = 0
    for member in guild.members:
        if member.bot:
            bots += 1
        else:
            users += 1
    if users >= 100:
        log = self.get_channel(Ids["Guilds_bot_log_channel"])
        await log.send(f"The bot has JOINED the server {guild.name},\n owned by {guild.owner},\n with {len(guild.members)} members ({users} users and {bots} bots)")
    if guild.me.guild_permissions.manage_channels:
        for channel in guild.text_channels:
            if "clash-info-news" in channel.name:
                break
        else:
            overwrite = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), guild.me: discord.PermissionOverwrite(add_reactions=True, embed_links=True, external_emojis=True, read_message_history=True, send_messages=True, view_channel=True)}
            channel = await guild.create_text_channel("clash-info-news", overwrites=overwrite)
        embed = create_embed("Thank you for using this bot on your server !", f"Hello\nIf you want to receive the list of the features for the bot, please check the reaction {Emojis['News']} bellow. If you want to delete this channel, please check the reaction {Emojis['Delete']} bellow. You can join the Clash INFO support server here : https://discord.gg/KQmstPw\n\nPlease grant the permissions `Use External Emoji` to `@everyone`, or the bot slash commands won't show emojis !", 0x00ffff, "joined_guild_message", guild.me.avatar_url)
        await channel.send(embed=embed, components=Components["joined_guild_message"])
        await channel.send("https://discord.gg/KQmstPw")
        nb_guilds = len(self.guilds)
        act = discord.Activity(type=discord.ActivityType.watching, name=f"{nb_guilds: ,} servers")
        await self.change_presence(status=discord.Status.online, activity=act)
    return
