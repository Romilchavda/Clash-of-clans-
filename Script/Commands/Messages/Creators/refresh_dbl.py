# Refreshes the top.gg guilds count

from Script.Clients.discord_client import Clash_info
from Script.Clients.top_gg_client import Dbl_client
from Script.import_emojis import Emojis


async def refresh_dbl(ctx):
    await Dbl_client.post_guild_count(len(Clash_info.guilds))
    await ctx.send(f"{Emojis['Yes']}) (https://top.gg/bot/704688212832026724)")
    return
