from Script.Clients.discord import Clash_info


async def add_reaction_with_id(ctx, channel_id, message_id, emoji_id):
    channel = Clash_info.get_channel(channel_id)
    async for message in channel.history(limit=None):
        if message.id == message_id:
            emoji = Clash_info.get_emoji(emoji_id)
            await message.add_reaction(emoji)
            await ctx.send(f"Done\nhttps://discord.com/channels/{channel.guild.id}/{channel_id}/{message_id}")
            return
    return
