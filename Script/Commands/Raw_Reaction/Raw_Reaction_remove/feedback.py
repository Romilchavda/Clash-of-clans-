from Script.import_emojis import Emojis
from Data.Const_variables.import_const import Ids
from Script.import_functions import create_embed


async def raw_reaction_remove_feedback(self, raw_reaction):
    if raw_reaction.channel_id == Ids["Feedback"] or True:
        message = raw_reaction.message
        react = {}
        for reaction in message.reactions:
            if reaction.emoji in list(Emojis["Numbers"].values()):
                react[{v: k for k, v in Emojis["Numbers"].items()}[reaction.emoji]] = reaction.count - 1
        pts_total = 0
        coef_total = 0
        for pts, coef in react.items():
            pts_total += pts * coef
            coef_total += coef
        embed = create_embed(message.embeds[0].title, f"The average is {round(pts_total / coef_total, 1)}/10", message.embeds[0].color, "", message.channel.guild.me.avatar_url)
        await message.edit(embed=embed)
    return
