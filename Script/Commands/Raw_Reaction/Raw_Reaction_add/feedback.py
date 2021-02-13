from Script.Const_variables.import_const import Ids
from Script.import_functions import create_embed


async def raw_reaction_add_feedback(self, raw_reaction):
    if raw_reaction.channel_id == Ids["Feedback"]:
        message = raw_reaction.message
        channel = message.channel
        a = 0
        react = {}
        for reaction in message.reactions:
            react[a] = reaction.count - 1
            a += 1
        pts_total = 0
        coef_total = 0
        for pts, coef in react.items():
            pts_total += pts * coef
            coef_total += coef
        embed = create_embed(message.embeds[0].title, f"The average is {round(pts_total / coef_total, 1)}/9", message.embeds[0].color, "", channel.guild.me.avatar_url)
        await message.edit(embed=embed)
    return
