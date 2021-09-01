# Sends information about the player with the given tag

import coc

from Data.clash_of_clans import Troops
from Script.Clients.clash_of_clans_client import Clash_of_clans
from Script.import_emojis import Emojis
from Script.import_functions import create_embed, trophies_to_league


async def player_infos(ctx, tag, information):
    player = await Clash_of_clans.get_player(tag)
    lvl_barbarian_king = 0
    lvl_archer_queen = 0
    lvl_grand_warden = 0
    lvl_royal_champion = 0
    lvl_battle_machine = 0
    for hero in player.heroes:
        if hero.name == "Battle Machine":
            lvl_battle_machine = hero.level
        if hero.name == "Barbarian King":
            lvl_barbarian_king = hero.level
        if hero.name == "Archer Queen":
            lvl_archer_queen = hero.level
        if hero.name == "Grand Warden":
            lvl_grand_warden = hero.level
        if hero.name == "Royal Champion":
            lvl_royal_champion = hero.level

    if information == "main":
        for th_lvl, value in Emojis["Th_emojis"].items():
            if value[1] == player.town_hall:
                break
        if player.town_hall_weapon:
            weapon = f"({player.town_hall_weapon} {Emojis['Star']})"
        else:
            weapon = ""
        if player.clan:
            clan = f"{player.clan.name} ({player.clan.tag})"
        else:
            clan = "None"

        bh_lvl = None
        for bh_emoji, value in Emojis["Bh_emojis"].items():
            if bh_lvl is None:
                bh_lvl = bh_emoji
            if value[1] == player.builder_hall:
                bh_lvl = bh_emoji
                break
        if player.builder_hall:
            player__versus_trophies = player.versus_trophies
            player__best_versus_trophies = player.best_versus_trophies
        else:
            player__versus_trophies = 0
            player__best_versus_trophies = 0
        embed = create_embed(f"Player : {player.name} ({player.tag}) (Main information)",
                             f"===== Main Base =====\n{th_lvl} {weapon} | {trophies_to_league(player.trophies)} {player.trophies} | {trophies_to_league(player.best_trophies)} Best : {player.best_trophies} | {Emojis['Exp']} {player.exp_level}\n{Emojis['Barbarian_king']} {lvl_barbarian_king} | {Emojis['Archer_queen']} {lvl_archer_queen} | {Emojis['Grand_warden']} {lvl_grand_warden} | {Emojis['Royal_champion']} {lvl_royal_champion}\n{Emojis['Members']} Clan : {clan}\n{Emojis['Star']} War stars earned : {player.war_stars}\n{Emojis['Donations']} Troops donated : {player.donations}\n{Emojis['Received']} Troops received : {player.received}\n:crossed_swords: Attacks won : {player.attack_wins}\n:shield: Defenses won : {player.defense_wins}\n\n===== Builder Base =====\n{bh_lvl} | {Emojis['Versus_trophy']} {player__versus_trophies} | {Emojis['Versus_trophy']} Best : {player__best_versus_trophies} | {Emojis['Battle_machine']} {lvl_battle_machine}\n:crossed_swords: Versus battle won : {player.versus_attack_wins}\n\n[Open in Clash Of Clans]({player.share_link})",
                             ctx.guild.me.color, "", ctx.guild.me.avatar_url)

    elif information == "success":
        achievements = "*name : stars | % for next star*"
        for achievement in player.achievements:
            achievements += f"\n{achievement.name} : {achievement.stars} {Emojis['Star_success']} | {int(achievement.value / achievement.target * 100)}%"
        embed = create_embed(f"Player : {player.name} ({player.tag}) (Achievements)", f"{achievements}\n[Open in Clash Of Clans]({player.share_link})", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    return embed


async def player_troops(ctx, tag):
    player = await Clash_of_clans.get_player(tag)
    lvl = str(player.town_hall)
    for troop in player.home_troops:
        if troop.name in list(Troops.keys()):
            Troops[troop.name].update({"player": troop.level})
    for troop in player.spells:
        Troops[troop.name].update({"player": troop.level})
    for troop in player.siege_machines:
        Troops[troop.name].update({"player": troop.level})
    for troop in player.hero_pets:
        Troops[troop.name].update({"player": troop.level})
    text = "*level | max level (TH) | max level (all the game)*"

    for troop in Troops.values():
        if not type(troop) == str:
            emoji = Emojis["Troops_emojis"][troop["name"]]
            if troop["name"] == "Barbarian":
                text += "\n\n__Troops :__\n"
                a = 0
            if troop["name"] == "Minion":
                text += "\n\n__Dark troops :__\n"
                a = 0
            if troop["name"] == "Lightning Spell":
                text += "\n\n__Spells :__\n"
                a = 0
            if troop["name"] == "Poison Spell":
                text += "\n\n__Dark spells__ :\n"
                a = 0
            if troop["name"] == "Wall Wrecker":
                text += "\n\n__Siege machines__ :\n"
                a = 0
            if troop["name"] == "L.A.S.S.I":
                text += "\n\n__Pets__ :\n"
                a = 0
            if a == 4:
                a = 0
                text += "\n"
            a += 1
            emoji = f"<:{emoji.name}:{emoji.id}>"
            text += f"{emoji} : {troop['player']} | {troop['TH' + lvl]} | {troop['max']} "
    embed = create_embed(f"Player : {player.name} ({player.tag}) (Troops)", text, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    return embed


async def player_info(ctx, tag, information):
    try:
        await Clash_of_clans.get_player(tag)
    except coc.errors.NotFound:
        await ctx.send(f"Player not found\nThere is no player with the tag `{tag}` (do not forget the # in front of the tag).", hidden=True)
        return
    if information == "troops":
        embed = await player_troops(ctx, tag)
    else:
        embed = await player_infos(ctx, tag, information)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(Emojis["Barbarian_king"])
    await msg.add_reaction(Emojis["Troop"])
    await msg.add_reaction(Emojis["Exp"])
    return
