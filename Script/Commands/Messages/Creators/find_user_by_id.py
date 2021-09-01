# Allows to find the user with the given ID if he has common guilds with the bot

from Script.Clients.discord_client import Clash_info


async def find_user_by_id(ctx, user_id):
    user = Clash_info.get_user(user_id)
    if user is not None:
        await ctx.send(f"{user.name}#{user.discriminator} {user.mention}")
    else:
        await ctx.send("This user has not common servers with Clash INFO.")
    return
