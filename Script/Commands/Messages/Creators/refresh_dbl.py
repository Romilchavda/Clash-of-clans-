from Script.import_emojis import Emojis
from Script.Clients.top_gg import Dbl_client
from Script.Clients.discord import Clash_info


async def refresh_dbl(ctx):
    await Dbl_client.post_guild_count(len(Clash_info.guilds))
    await ctx.send(str(Emojis["Yes"]) + " (https://top.gg/bot/704688212832026724)")
    return
