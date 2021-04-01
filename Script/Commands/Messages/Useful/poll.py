from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def poll(ctx, question):
    embed = create_embed(f"Poll : {question}", f"This poll is requested by :\n{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})", ctx.author.color, "", ctx.guild.me.avatar_url)
<<<<<<< HEAD
    msg = await ctx.send(embed=embed)
=======
    msg = await ctx.channel.send(embed=embed)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
    await msg.add_reaction(Emojis["Yes"])
    await msg.add_reaction(Emojis["No"])
    await msg.add_reaction(Emojis["Think"])
    await msg.add_reaction(Emojis["End"])
    return
