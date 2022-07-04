from typing import Union

import discord

from bot.emojis import Emojis
from data.useful import Useful


def create_embed(title: str, description: str, colour: Union[hex, discord.Colour], footer: str, icon_url: str, img: str = "") -> discord.Embed:
    embed = discord.Embed()
    embed.title = title
    embed.description = description
    embed.colour = colour
    embed.set_footer(text=footer, icon_url=icon_url)
    if img:
        embed.set_image(url=img)
    return embed


def escape_markdown(text: str) -> str:
    text = text.replace("\\", "\\\\")
    text = text.replace("*", "\*")
    text = text.replace("_", "\_")
    text = text.replace("~", "\~")
    text = text.replace(">", "\>")
    text = text.replace("|", "\|")
    text = text.replace("`", "\`")
    return text


def trophies_to_league(trophies: int) -> discord.Emoji:
    league_to_trophies = Useful["league_trophies"]
    for league in sorted(league_to_trophies, key=league_to_trophies.get, reverse=True):
        if trophies >= league_to_trophies[league]:
            return Emojis["League_emojis"][league]
