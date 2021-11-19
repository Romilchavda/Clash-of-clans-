# Called when the bot leaves a guild

from Data.Constants.import_const import Ids
from Script.Clients.top_gg_client import Dbl_client


async def guild_remove(self, guild):
    await Dbl_client.post_guild_count(len(self.guilds))
    users = 0
    bots = 0
    for member in guild.members:
        if member.bot:
            bots += 1
        else:
            users += 1
    log = self.get_channel(Ids["Guilds_bot_log_channel"])
    await log.send(f"The bot has LEFT the server {guild.name},\n owned by {guild.owner},\n with {len(guild.members)} members ({users} users and {bots} bots)")
    return
