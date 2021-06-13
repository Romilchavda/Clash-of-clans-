import coc
from Script.import_emojis import Emojis
from Data.Const_variables.import_const import Troops
from Script.import_functions import create_embed, trophies_to_league
from Script.Clients.clash_of_clans import Clash_of_clans


async def player_info(ctx, tag, information):
    player = await Clash_of_clans.get_player(tag)
    lvl_bk = 0
    lvl_aq = 0
    lvl_gw = 0
    lvl_rc = 0
    lvl_bm = 0
    for hero in player.heroes:
        if hero.name == "Battle Machine":
            lvl_bm = hero.level
        if hero.name == "Barbarian King":
            lvl_bk = hero.level
        if hero.name == "Archer Queen":
            lvl_aq = hero.level
        if hero.name == "Grand Warden":
            lvl_gw = hero.level
        if hero.name == "Royal Champion":
            lvl_rc = hero.level
    if information == "main":
        for th, value in Emojis["Th_emojis"].items():
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
        embed = create_embed(f"Player : {player.name} ({player.tag}) (Main information)", f"{trophies_to_league(player.trophies)} Number of trophies : {player.trophies}\n{trophies_to_league(player.best_trophies)} Best trophies : {player.best_trophies}\n{th} Town Hall level : {player.town_hall} {weapon}\n{Emojis['Exp']} Experience level : {player.exp_level}\n{Emojis['Members']} Clan : {clan}\n{Emojis['Star']} War stars earned : {player.war_stars}\n{Emojis['Barbarian_king']} Heros level : {Emojis['Barbarian_king']} {lvl_bk} / {Emojis['Archer_queen']} {lvl_aq} / {Emojis['Grand_warden']} {lvl_gw} / {Emojis['Royal_champion']} {lvl_rc}\n{Emojis['Donations']} Troops donated : {player.donations}\n{Emojis['Received']} Troops received : {player.received}\n:crossed_swords: Attacks won : {player.attack_wins}\n:shield: Defenses won : {player.defense_wins}\n[Open in Clash Of Clans]({player.share_link})", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    elif information == "builder_base":
        if player.builder_hall:
            for bh, value in Emojis["Bh_emojis"].items():
                if value[1] == player.builder_hall:
                    break
            embed = create_embed(f"Player : {player.name} ({player.tag}) (Builder base)", f"{Emojis['Trophy']} Number of trophies : {player.versus_trophies}\n{Emojis['Trophy']} Best trophies : {player.best_versus_trophies}\n{bh} Builder Hall level : {player.builder_hall}\n{Emojis['Battle_machine']} Hero level : {Emojis['Battle_machine']} {lvl_bm}\n:crossed_swords: Versus battle won : {player.versus_attack_wins}\n[Open in Clash Of Clans]({player.share_link})", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        else:
            embed = create_embed(f"Player : {player.name} ({player.tag}) (Builder base)", f"This player has not yet unlocked the builder base !\n[Open in Clash Of Clans]({player.share_link})", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    elif information == "success":
        achievements = "*name : stars | % for next star*"
        Emojis['Star'] = ":star:"
        for achievement in player.achievements:
            achievements += f"\n{achievement.name} : {achievement.stars} {Emojis['Star']} | {int(achievement.value/achievement.target*100)}%"
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
    msg = "*level | max level (TH) | max level (all the game)*"

    for troop in Troops.values():
        if not type(troop) == str:
            emoji = Emojis["Troops_emojis"][troop["name"]]
            if troop["name"] == "Barbarian":
                msg += "\n\n__Troops :__\n"
                a = 0
            if troop["name"] == "Minion":
                msg += "\n\n__Dark troops :__\n"
                a = 0
            if troop["name"] == "Lightning Spell":
                msg += "\n\n__Spells :__\n"
                a = 0
            if troop["name"] == "Poison Spell":
                msg += "\n\n__Dark spells__ :\n"
                a = 0
            if troop["name"] == "Wall Wrecker":
                msg += "\n\n__Siege machines__ :\n"
                a = 0
            if troop["name"] == "L.A.S.S.I":
                msg += "\n\n__Pets__ :\n"
                a = 0
            if a == 4:
                a = 0
                msg += "\n"
            a += 1
            emoji = f"<:{emoji.name}:{emoji.id}>"
            msg += f"{emoji} : {troop['player']} | {troop['TH' + lvl]} | {troop['max']} "
    embed = create_embed(f"Player : {player.name} ({player.tag}) (Troops)", msg, ctx.guild.me.color, "", ctx.guild.me.avatar_url)
    return embed


async def get_player(ctx, tag, information):
    try:
        await Clash_of_clans.get_player(tag)
    except coc.errors.NotFound:
        await ctx.send(f"Player not found\nThere is no player with the tag `{tag}` (do not forget the # in front of the tag).", hidden=True)
    if information == "troops":
        embed = await player_troops(ctx, tag)
    else:
        embed = await player_info(ctx, tag, information)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction(Emojis["Barbarian_king"])
    await msg.add_reaction(Emojis["Battle_machine"])
    await msg.add_reaction(Emojis["Troop"])
    await msg.add_reaction(Emojis["Exp"])
    return
