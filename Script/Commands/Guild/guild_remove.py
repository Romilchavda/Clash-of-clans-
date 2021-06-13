from Data.Const_variables.import_const import Ids
from Script.Clients.top_gg import Dbl_client


async def guild_remove(self, guild):
    await Dbl_client.post_guild_count(len(self.guilds))
    log = self.get_channel(Ids["Log_bot"])
    await log.send(f"The bot has LEFT the server {guild.name}, with {len(guild.members)} members")
    return
