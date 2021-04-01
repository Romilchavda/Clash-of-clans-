from Script.import_functions import create_embed


async def direct_message_role(ctx, role, text):
    if ctx.author.guild_permissions.administrator:
        for member in role.members:
<<<<<<< HEAD
            if not member.bot:
                await member.send(f"{text}\n*Sent by {ctx.author} ({ctx.author.id}) from the server {ctx.guild.name} ({ctx.guild.id})*")
                embed = create_embed(member.name, "This member has received the message.", member.color, "", ctx.guild.me.avatar_url)
                await ctx.send(embed=embed)
            else:
                await ctx.send("You cannot send a direct message to a bot")
    else:
        await ctx.send("You cannot do this action\nYou are not allowed to send direct message to a role. You must be an administrator.")
=======
            await member.send(f"{text}\n*Sent by {ctx.author} ({ctx.author.id}) from the server {ctx.guild.name} ({ctx.guild.id})*")
            embed = create_embed(member.name, "This member has received the message.", member.color, "", ctx.guild.me.avatar_url)
            await ctx.channel.send(embed=embed)
    else:
        embed = create_embed("You cannot do this action", "You are not allowed to send direct message to a role. You must be an administrator.", 0xff8000, "", ctx.guild.me.avatar_url)
        await ctx.channel.send(embed=embed)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    return


async def direct_message_member(ctx, member, text):
    await member.send(f"{text}\n*Sent by {ctx.author} ({ctx.author.id}) from the server {ctx.guild.name} ({ctx.guild.id})*")
    embed = create_embed(member.name, "This member has received the message.", member.color, "", ctx.guild.me.avatar_url)
<<<<<<< HEAD
    await ctx.send(embed=embed)
=======
    await ctx.channel.send(embed=embed)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    return
