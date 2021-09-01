# Sends direct message to users / users with a given role
# TODO : Allow users to refuse DM

from Script.import_functions import create_embed


async def direct_message_role(ctx, role, text):
    for member in role.members:
        if not member.bot:
            await member.send(f"{text}\n*Sent by {ctx.author} ({ctx.author.id}) from the server {ctx.guild.name} ({ctx.guild.id})*")
            embed = create_embed(member.name, "This member has received the message.", member.color, "", ctx.guild.me.avatar_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("You cannot send a direct message to a bot")
    return


async def direct_message_member(ctx, member, text):
    await member.send(f"{text}\n*Sent by {ctx.author} ({ctx.author.id}) from the server {ctx.guild.name} ({ctx.guild.id})*")
    embed = create_embed(member.name, "This member has received the message.", member.color, "", ctx.guild.me.avatar_url)
    await ctx.send(embed=embed)
    return
