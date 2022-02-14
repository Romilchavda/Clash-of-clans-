# Follow the support server news channel / delete the created channel

from Data.Constants.import_const import Ids


async def joined_guild_message(ctx):
    if "joined_guild_message" in ctx.origin_message.embeds[0].footer.text:

        if ctx.custom_id == "follow":
            channel = ctx.origin_message.channel
            if channel.permissions_for(ctx.author).manage_webhooks:
                if channel.permissions_for(ctx.guild.me).manage_webhooks:
                    news = ctx.bot.get_channel(Ids["News_channel"])
                    await news.follow(destination=channel)
                    await ctx.defer(ignore=True)
                    return
                else:
                    await ctx.defer(hidden=True)
                    await channel.send("The bot cannot do this action !\nPlease give the permission \"Manage Webhooks\" to the bot")
                    return
            else:
                await ctx.defer(hidden=True)
                await channel.send("You cannot do this action !\nYou are not allowed to manage webhooks.")
                return

        elif ctx.custom_id == "delete":
            channel = ctx.origin_message.channel
            if channel.permissions_for(ctx.author).manage_channels:
                if channel.permissions_for(ctx.guild.me).manage_channels:
                    await channel.delete()
                    await ctx.defer(ignore=True)
                    return
                else:
                    await ctx.defer(hidden=True)
                    await channel.send("The bot cannot do this action !\nPlease give the permission \"Manage Channels\" to the bot")
            else:
                await ctx.defer(hidden=True)
                await channel.send("You cannot do this action !\nYou are not allowed to manage channels.")
                return
