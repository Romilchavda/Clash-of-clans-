import discord

from Data.Constants.useful import Useful
from Script.import_emojis import Emojis


def create_embed_img(title, description, colour, footer, icon_url, img):
    embed = discord.Embed()
    embed.title = title
    embed.description = description
    embed.colour = colour
    embed.set_footer(text=footer, icon_url=icon_url)
    embed.set_image(url=img)
    return embed


def create_embed(title, description, colour, footer, icon_url):
    embed = discord.Embed()
    embed.title = title
    embed.description = description
    embed.colour = colour
    embed.set_footer(text=footer, icon_url=icon_url)
    return embed


def trophies_to_league(trophies):
    league_to_trophies = Useful["league_trophies"]
    for league in sorted(league_to_trophies, key=league_to_trophies.get, reverse=True):
        if trophies >= league_to_trophies[league]:
            return Emojis["League_emojis"][league]
