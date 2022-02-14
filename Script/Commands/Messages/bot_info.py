# Sends information about the bot

from Data.Constants.useful import Useful
from Script.Clients.discord_client import Clash_info
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def bot_info(ctx):
    actual_permissions = ctx.guild.me.guild_permissions
    required_permissions = Useful["required_permissions"]
    text_permissions = ":warning: The bot needs the permissions : "
    perms_bot = []
    for perm in actual_permissions:
        if perm[1]:
            perms_bot.append(perm[0])
    for perm in required_permissions:
        if perm[1] and not perm[0] in perms_bot:
            text_permissions += "\n" + perm[0]
    text_permissions += "\nSo please grant it to the bot."
    if text_permissions == ":warning: The bot needs the permissions : " + "\nSo please grant it to the bot.":
        text_permissions = f"{Emojis['Yes']} The bot has all required permissions !"
    text_servers_number = f"{Emojis['Discord']} The bot is on {len(Clash_info.guilds)} servers !"
    text_created = f"{Emojis['Calendar']} The bot was created the 2020-04-28, and certified the 2020-09-23."
    embed = create_embed("Clash INFO", f"{text_permissions}\n{text_servers_number}\n{text_created}", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
