import discord
from Script.import_emojis import Emojis
from Data.Const_variables.import_const import Ids
from Script.import_functions import create_embed
from Script.Clients.top_gg import Dbl_client


async def guild_join(self, guild):
    await Dbl_client.post_guild_count(len(self.guilds))
    bot = guild.me
    log = self.get_channel(Ids["Log_bot"])
    await log.send(f"The bot has JOINED the server {guild.name}, with {len(guild.members)} members")
    if bot.guild_permissions.manage_channels:
        for salon in guild.text_channels:
            if "clash-info-news" in salon.name:
                channel = salon
                break
        if "channel" not in locals():
            overwrite = {guild.default_role: discord.PermissionOverwrite(view_channel=True, send_messages=False), bot: discord.PermissionOverwrite(send_messages=True)}
            channel = await guild.create_text_channel("clash info news", overwrites=overwrite)
        embed = create_embed("Thank you for using this bot on your server !", f"Hello\nIf you want to receive the list of the features for the bot, please check the reaction {Emojis['News']} bellow. If you want to delete this channel, please check the reaction {Emojis['Delete']} bellow. You can join the Clash INFO support server here : https://discord.gg/KQmstPw\n\nPlease grant the permissions `Use External Emoji` to `@everyone`, or the bot slash commands won't show emojis !", 0x00ffff, "", guild.me.avatar_url)
        msg = await channel.send(embed=embed)
        await msg.add_reaction(Emojis["News"])
        await msg.add_reaction(Emojis["Delete"])
        await channel.send("https://discord.gg/KQmstPw")
    return
