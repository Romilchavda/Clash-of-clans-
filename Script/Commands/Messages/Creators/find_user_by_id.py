from Script.Clients.discord import Clash_info


async def find_user_by_id(ctx, id):
    user = Clash_info.get_user(id)
    if user is not None:
        await ctx.send(f"{user.name}#{user.discriminator} {user.mention}")
    else:
        await ctx.send("This user has not common servers with Clash INFO.")
    return
