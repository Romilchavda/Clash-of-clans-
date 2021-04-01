from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def promote_the_bot(ctx):
    embed = create_embed("Links to promote the bot :", f"[Top.gg](https://top.gg/bot/704688212832026724)\n[Discord.Bots.gg](https://discord.bots.gg/bots/704688212832026724)\n[Arcane-Center.xyz](https://arcane-center.xyz/bot/704688212832026724)\n[WonderBotList.com](https://wonderbotlist.com/en/bot/704688212832026724)\n\nYou can click on {Emojis['Link']} to see the URL.", ctx.guild.me.color, "Thanks you for your support !", ctx.guild.me.avatar_url)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(Emojis['Link'])
    return
