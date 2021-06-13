from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def poll(ctx, question):
    embed_title = f"Poll : {question}"
    if len(embed_title) > 256:
        await ctx.send("The embed title cannot have more than 249 characters.", hidden=True)
    else:
        embed = create_embed(embed_title, f"This poll is requested by :\n{ctx.author.name}#{ctx.author.discriminator} ({ctx.author.id})", ctx.author.color, "", ctx.guild.me.avatar_url)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(Emojis["Yes"])
        await msg.add_reaction(Emojis["No"])
        await msg.add_reaction(Emojis["Think"])
        await msg.add_reaction(Emojis["End"])
    return
