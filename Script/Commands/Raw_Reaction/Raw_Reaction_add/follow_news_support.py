# Adds the clash-info-news channel's updates to the channel

from Data.Const_variables.import_const import Ids
from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def raw_reaction_add_follow_news_support(self, raw_reaction):
    if raw_reaction.emoji == Emojis["News"]:
        guild = raw_reaction.message.guild
        channel = raw_reaction.message.channel
        if channel.permissions_for(raw_reaction.member).manage_webhooks:
            if channel.permissions_for(guild.me).manage_webhooks:
                news = self.get_channel(Ids["News_channel"])
                await news.follow(destination=channel)
                return
            else:
                await channel.send("The bot cannot do this action !\nPlease give the permission \"Manage Webhooks\" to the bot")
                return
        else:
            embed = create_embed("You cannot do this action", "You are not allowed to manage webhooks.", 0xff8000, "", guild.me.avatar_url)
            await channel.send(embed=embed)
    return
