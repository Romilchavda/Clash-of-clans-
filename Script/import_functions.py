import discord
from Script.import_emojis import Emojis


def int_to_str(number):
    nb = " "
    number = str(number)
    a = -1
    for i in range(len(number)):
        a += 1
        if a == 3:
            nb = "," + nb
            a = 0
        j = len(number) - i - 1
        nb = number[j] + nb
    return nb


def create_embed_img(title, description, colour, footer, icon_url, img):
    embed = discord.Embed()
    embed.title = title
    embed.description = description
    embed.colour = colour
    embed.set_footer(text=footer + "\nHelp command : /help (slash command)", icon_url=icon_url)
    embed.set_image(url=img)
    return embed
def create_embed(title, description, colour, footer, icon_url):
    embed = discord.Embed()
    embed.title = title
    embed.description = description
    embed.colour = colour
    embed.set_footer(text=footer + "\nHelp command : /help (slash command)", icon_url=icon_url)
    return embed


def trophies_to_league(trophies):
    league_emojis_list = sorted(Emojis["League_emojis"].items(), key=lambda t: t[1][1], reverse=True)
    for tuple in league_emojis_list:
        if trophies >= tuple[1][1]:
            return tuple[0]
