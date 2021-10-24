# Sends uptime and api latency

import requests

from Data.Const_variables.import_const import Login
from Script.import_functions import create_embed


async def ping(ctx, latency=None):
    if latency is not None:
        api = int(round(latency, 3) * 1000)
    else:
        api = "*unknown*"
    url = "https://api.watchbot.app/bot/704688212832026724"
    headers = {"AUTH-TOKEN": Login["watchbot"]["token"]}
    uptime_dict = requests.get(url, headers=headers).json()
    uptime_90d = uptime_dict["90d"]
    uptime_30d = uptime_dict["30d"]
    uptime_7d = uptime_dict["7d"]
    embed = create_embed("The bot is OK !", f"ping API : `{api}ms`\n\n**[Uptime :](https://status.watchbot.app/bot/704688212832026724)**\nUptime (last 90 days) : `{uptime_90d}%`\nUptime (last 30 days) : `{uptime_30d}%`\nUptime (last 7 days) : `{uptime_7d}%`", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
