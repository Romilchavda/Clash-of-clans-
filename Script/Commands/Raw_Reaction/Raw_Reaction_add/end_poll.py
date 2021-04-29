from Script.import_emojis import Emojis
from Script.import_functions import create_embed


async def raw_reaction_add_end_poll(self, raw_reaction):
    if raw_reaction.emoji == Emojis["End"]:
        message = raw_reaction.message
        guild = message.guild
        if "Poll" in message.embeds[0].title:
            author_id = message.embeds[0].description.split("(")[len(message.content.split("("))]
            author_id = author_id.split(")")[0]
            if int(author_id) == raw_reaction.member.id:
                yes = 0
                no = 0
                for react in message.reactions:
                    if react.emoji == Emojis["Yes"]:
                        yes = react.count
                    if react.emoji == Emojis["No"]:
                        no = react.count
                if yes == no:
                    embed = create_embed(message.embeds[0].title, "Server members score is tied !", message.embeds[0].color, "", guild.me.avatar_url)
                elif yes > no:
                    embed = create_embed(message.embeds[0].title, f"Server members score is {Emojis['Yes']} !", message.embeds[0].color, "", guild.me.avatar_url)
                elif yes < no:
                    embed = create_embed(message.embeds[0].title, f"Server members score is {Emojis['No']} !", message.embeds[0].color, "", guild.me.avatar_url)
                await message.edit(embed=embed)
    return
