from Script.Const_variables.import_const import Ids


async def raw_reaction_remove_feedback(self, raw_reaction):
    if raw_reaction.message.channel.id == Ids["Feedback"]:
        a = 0
        react = {}
        for reaction in raw_reaction.message.reactions:
            react[a] = reaction.count - 1
            a += 1
        pts_total = 0
        coef_total = 0
        for pts, coef in react.items():
            pts_total += pts * coef
            coef_total += coef
        embed = self.create_embed(raw_reaction.message.embeds[0].title, f"The average is {round(pts_total / coef_total, 1)}/9", raw_reaction.message.embeds[0].color, "")
        await raw_reaction.message.edit(embed=embed)
    return
