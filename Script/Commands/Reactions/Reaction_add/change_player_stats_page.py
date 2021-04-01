from Script.import_emojis import Emojis
<<<<<<< HEAD
from Script.Commands.Messages.Clash_Of_Clans.get_player import player_info, player_troops
=======
from Script.Const_variables.import_const import Troops
from Script.import_functions import create_embed, trophies_to_league
from Script.Clients.clash_of_clans import Clash_of_clans


async def player(tag, information, member):
    player = await Clash_of_clans.get_player(tag)
    lvl_rdb = 0
    lvl_aq = 0
    lvl_gg = 0
    lvl_ch = 0
    lvl_bm = 0
    for hero in player.heroes:
        if hero.name == "Battle Machine":
            lvl_bm = hero.level
        if hero.name == "Barbarian King":
            lvl_rdb = hero.level
        if hero.name == "Archer Queen":
            lvl_aq = hero.level
        if hero.name == "Grand Warden":
            lvl_gg = hero.level
        if hero.name == "Royal Champion":
            lvl_ch = hero.level
    if information == "main":
        for th, value in Emojis["Th_emojis"].items():
            if value[1] == player.town_hall:
                break
        embed_main = create_embed(f"Player : {player.name} ({player.tag}) (Main information)", f"{trophies_to_league(player.trophies)} Number of trophies : {player.trophies}\n{trophies_to_league(player.best_trophies)} Best trophies : {player.best_trophies}\n{th} Town Hall level : {player.town_hall}\n{th} Town Hall weapon level : {player.town_hall_weapon}\n{Emojis['Exp']} Experience level : {player.exp_level}\n{Emojis['Star_emoji']} War stars earned : {player.war_stars}\n{Emojis['Barbarian_king']} Heros level : {Emojis['Barbarian_king']} {lvl_rdb} / {Emojis['Archer_queen']} {lvl_aq} / {Emojis['Grand_warden']} {lvl_gg} / {Emojis['Royal_champion']} {lvl_ch}\n{Emojis['Donations']} Troops donated : {player.donations}\n{Emojis['Received']} Troops received : {player.received}\n:crossed_swords: Attacks won : {player.attack_wins}\n:shield: Defenses won : {player.defense_wins}\n[Open in Clash Of Clans]({player.share_link})", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        embed = embed_main
    elif information == "builder_base":
        for bh, value in Emojis["Bh_emojis"].items():
            if value[1] == player.builder_hall:
                break
        embed_builder = create_embed(f"Player : {player.name} ({player.tag}) (Builder base)", f"{Emojis['Trophy']} Number of trophies : {player.versus_trophies}\n{Emojis['Trophy']} Best trophies : {player.best_versus_trophies}\n{bh} Builder Hall level : {player.builder_hall}\n{Emojis['Battle_machine']} Hero level : {Emojis['Battle_machine']} {lvl_bm}\n:crossed_swords: Versus battle won : {player.versus_attack_wins}\n[Open in Clash Of Clans]({player.share_link})", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        embed = embed_builder
    elif information == "success":
        achievements = "*name | stars | score (target description)*"
        for achievement in player.achievements:
            achievements += f"\n{achievement.stars} | {achievement.value} ({achievement.info})"
        embed_success = create_embed(f"Player : {player.name} ({player.tag}) (Achievements)", f"{achievements}\n[Open in Clash Of Clans]({player.share_link})", member.guild.me.color, "", member.guild.me.avatar_url)
        embed = embed_success
    return embed


async def troops(tag, member):
    player = await Clash_of_clans.get_player(tag)
    th = str(player.town_hall)
    for troop in player.home_troops:
        try:
            Troops[troop.name]["player"] = troop.level
        except KeyError:
            pass
    for troop in player.spells:
        Troops[troop.name]["player"] = troop.level
    for troop in player.siege_machines:
        Troops[troop.name]["player"] = troop.level
    msg = "*level | max level (TH) | max level (all the game)*"
    for dico in Troops.values():
        emoji = Emojis["Troops_emojis"][dico["emoji"]]
        if dico.get("name") == "Barbarian":
            msg += "\n\n__Troops :__\n"
            a = 0
        if dico.get("name") == "Minion":
            msg += "\n\n__Dark troops :__\n"
            a = 0
        if dico.get("name") == "Lightning Spell":
            msg += "\n\n__Spells :__\n"
            a = 0
        if dico.get("name") == "Poison Spell":
            msg += "\n\n__Dark spells__ :\n"
            a = 0
        if dico.get("name") == "Wall Wrecker":
            msg += "\n\n__Siege machines__ :\n"
            a = 0
        if a == 4:
            a = 0
            msg += "\n"
        a += 1
        msg += f"{emoji} : {troop['player']} {troop['TH' + th]} | {troop['max']} "
    embed = create_embed(f"Player : {player.name} ({player.tag}) (Troops)", msg, member.guild.me.color, "")
    return embed
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9


async def reaction_add_change_player_stats_page(self, reaction, member):
    if (reaction.emoji in [Emojis["Barbarian_king"], Emojis["Battle_machine"], Emojis["Exp"], Emojis["Troop"]]) and ("Player : " in reaction.message.embeds[0].title):
        tag = "#" + reaction.message.embeds[0].title.split("#")[len(reaction.message.embeds[0].title.split("#")) - 1].split("(")[0]
        if reaction.emoji == Emojis["Barbarian_king"]:
<<<<<<< HEAD
            embed = await player_info(member, tag, "main")
        if reaction.emoji == Emojis["Battle_machine"]:
            embed = await player_info(member, tag, "builder_base")
        if reaction.emoji == Emojis["Troop"]:
            embed = await player_troops(member, tag)
        if reaction.emoji == Emojis["Exp"]:
            embed = await player_info(member, tag, "success")
=======
            embed = await player("main", tag, member)
        if reaction.emoji == Emojis["Battle_machine"]:
            embed = await player("builder_base", tag)
        if reaction.emoji == Emojis["Troop"]:
            embed = await troops(tag, member, member)
        if reaction.emoji == Emojis["Exp"]:
            embed = await player("success", tag, member)
>>>>>>> 2c5eeb557ba56deaebc5d7b35352d13b7f7ff1c9
        await reaction.message.edit(embed=embed)
        await reaction.remove(member)
    return
