import asyncio

import discord

from Data.Const_variables.import_const import Login

Emojis = {}

Emojis_coc_th_bh_leagues_id = 696344010905747487
Emojis_coc_troops_spells_id = 716259214279966770
Emojis_coc_main_id = 870305165180305408
Emojis_discord_badges_id = 761885092649762826
Emojis_discord_general_icons_id = 836587468144509009
Emojis_discord_main_id = 714841480602320958
Support_id = 719537805604290650
Emojis_spam_id = 779396058349568001


class EmojisBot(discord.Client):
    emojis = {}
    emoji_connected = asyncio.Event()

    def __init__(self):
        super().__init__()

    async def on_ready(self):
        emojis = {}

        # COC Th-Bh-Leagues
        guild = self.get_guild(Emojis_coc_th_bh_leagues_id)
        th_emojis = {}
        th_emojis_dict = {"TH_01": ("TH 1", 1), "TH_02": ("TH 2", 2), "TH_03": ("TH 3", 3), "TH_04": ("TH 4", 4), "TH_05": ("TH 5", 5), "TH_06": ("TH 6", 6), "TH_07": ("TH 7", 7), "TH_08": ("TH 8", 8), "TH_09": ("TH 9", 9), "TH_10": ("TH 10", 10), "TH_11": ("TH 11", 11), "TH_12": ("TH 12", 12), "TH_13": ("TH 13", 13), "TH_14": ("TH 14", 14)}
        for emoji_name, emoji_dict in th_emojis_dict.items():
            emoji = discord.utils.get(guild.emojis, name=emoji_name)
            th_emojis[emoji] = th_emojis_dict[emoji_name]
        emojis["Th_emojis"] = th_emojis

        bh_emojis = {}
        bh_emojis_dict = {"BH_01": ("BH 1", 1), "BH_02": ("BH 2", 2), "BH_03": ("BH 3", 3), "BH_04": ("BH 4", 4), "BH_05": ("BH 5", 5), "BH_06": ("BH 6", 6), "BH_07": ("BH 7", 7), "BH_08": ("BH 8", 8), "BH_09": ("BH 9", 9)}
        for emoji_name, emoji_dict in bh_emojis_dict.items():
            emoji = discord.utils.get(guild.emojis, name=emoji_name)
            bh_emojis[emoji] = bh_emojis_dict[emoji_name]
        emojis["Bh_emojis"] = bh_emojis

        league_emojis = {}
        league_emojis_dict = {"unranked_league": ("unranked league", 0), "bronze_league": ("bronze league", 400), "silver_league": ("silver league", 800), "gold_league": ("gold league", 1400), "crystal_league": ("crystal league", 2000), "master_league": ("master league", 2600), "champion_league": ("champion league", 3200), "titan_league": ("titan league", 4100), "legend_league": ("legend league", 5000)}
        for emoji_name, emoji_dict in league_emojis_dict.items():
            emoji = discord.utils.get(guild.emojis, name=emoji_name)
            league_emojis[emoji] = league_emojis_dict[emoji_name]
        emojis["League_emojis"] = league_emojis

        emojis["Barbarian_king"] = discord.utils.get(guild.emojis, name="barbarian_king")
        emojis["Archer_queen"] = discord.utils.get(guild.emojis, name="archer_queen")
        emojis["Grand_warden"] = discord.utils.get(guild.emojis, name="grand_warden")
        emojis["Royal_champion"] = discord.utils.get(guild.emojis, name="royal_champion")
        emojis["Battle_machine"] = discord.utils.get(guild.emojis, name="battle_machine")

        # COC Troops-Spell
        guild = self.get_guild(Emojis_coc_troops_spells_id)
        emojis["Troop"] = discord.utils.get(guild.emojis, name="TE1")
        troops_emojis = {}
        emoji_to_name = {"TE1": "Barbarian", "TE2": "Archer", "TE3": "Giant", "TE4": "Goblin", "TE5": "Wall Breaker", "TE6": "Balloon", "TE7": "Wizard", "TE8": "Healer", "TE9": "Dragon", "TE10": "P.E.K.K.A", "TE11": "Baby Dragon", "TE12": "Miner", "TE13": "Electro Dragon", "TE14": "Yeti", "TE15": "Dragon Rider", "TD1": "Minion", "TD2": "Hog Rider", "TD3": "Valkyrie", "TD4": "Golem", "TD5": "Witch", "TD6": "Lava Hound", "TD7": "Bowler", "TD8": "Ice Golem", "TD9": "Headhunter", "SE1": "Lightning Spell", "SE2": "Healing Spell", "SE3": "Rage Spell", "SE4": "Jump Spell", "SE5": "Freeze Spell", "SE6": "Clone Spell", "SE7": "Invisibility Spell", "SD1": "Poison Spell", "SD2": "Earthquake Spell", "SD3": "Haste Spell", "SD4": "Skeleton Spell", "SD5": "Bat Spell", "M1": "Wall Wrecker", "M2": "Battle Blimp", "M3": "Stone Slammer", "M4": "Siege Barracks", "M5": "Log Launcher", "P1": "L.A.S.S.I", "P2": "Electro Owl", "P3": "Mighty Yak", "P4": "Unicorn"}
        for emoji in guild.emojis:
            troops_emojis.update({emoji_to_name[emoji.name]: emoji})
        emojis["Troops_emojis"] = troops_emojis

        # COC Main
        guild = self.get_guild(Emojis_coc_main_id)
        emojis["Trophy"] = discord.utils.get(guild.emojis, name="trophy")
        emojis["Versus_trophy"] = discord.utils.get(guild.emojis, name="versus_trophy")
        emojis["Star"] = discord.utils.get(guild.emojis, name="star")
        emojis["Star_empty"] = discord.utils.get(guild.emojis, name="star_empty")
        emojis["Star_old"] = discord.utils.get(guild.emojis, name="star_old")
        emojis["Star_success"] = discord.utils.get(guild.emojis, name="star_success")

        # Support
        guild = self.get_guild(Support_id)
        emojis["Bot"] = discord.utils.get(guild.emojis, name="bot")
        emojis["Bot_certified"] = discord.utils.get(guild.emojis, name="bot_certified")
        emojis["Clash_esport"] = discord.utils.get(guild.emojis, name="ClashESPORT")
        emojis["Clash_info"] = discord.utils.get(guild.emojis, name="ClashINFO")
        emojis["Github"] = discord.utils.get(guild.emojis, name="github")
        emojis["Yes"] = discord.utils.get(guild.emojis, name="yes")
        emojis["No"] = discord.utils.get(guild.emojis, name="no")

        # Discord Main
        guild = self.get_guild(Emojis_discord_main_id)
        emojis["Add_reaction"] = discord.utils.get(guild.emojis, name="add_reaction")
        emojis["Channel"] = discord.utils.get(guild.emojis, name="channel")
        emojis["Channel_locked"] = discord.utils.get(guild.emojis, name="channel_locked")
        emojis["Channel_nsfw"] = discord.utils.get(guild.emojis, name="channel_nsfw")
        emojis["Cursor"] = discord.utils.get(guild.emojis, name="cursor")
        emojis["Deafened"] = discord.utils.get(guild.emojis, name="deafened")
        emojis["Discord"] = discord.utils.get(guild.emojis, name="discord")
        emojis["Emoji_ghost"] = discord.utils.get(guild.emojis, name="emoji_ghost")
        emojis["Invite"] = discord.utils.get(guild.emojis, name="invite")
        emojis["Member"] = discord.utils.get(guild.emojis, name="member")
        emojis["Members"] = discord.utils.get(guild.emojis, name="members")
        emojis["Mention"] = discord.utils.get(guild.emojis, name="mention")
        emojis["Muted"] = discord.utils.get(guild.emojis, name="muted")
        emojis["News"] = discord.utils.get(guild.emojis, name="news")
        emojis["Nitro"] = discord.utils.get(guild.emojis, name="nitro")
        emojis["Pin"] = discord.utils.get(guild.emojis, name="pin")
        emojis["Pin_unread"] = discord.utils.get(guild.emojis, name="pin_unread")
        emojis["Settings"] = discord.utils.get(guild.emojis, name="settings")
        emojis["Slowmode"] = discord.utils.get(guild.emojis, name="slowmode")
        emojis["Stream"] = discord.utils.get(guild.emojis, name="stream")
        emojis["Store_tag"] = discord.utils.get(guild.emojis, name="store_tag")
        emojis["Typing"] = discord.utils.get(guild.emojis, name="typing")
        emojis["Typing_status"] = discord.utils.get(guild.emojis, name="typing_status")
        emojis["Undeafened"] = discord.utils.get(guild.emojis, name="undeafened")
        emojis["Unmuted"] = discord.utils.get(guild.emojis, name="unmuted")
        emojis["Update"] = discord.utils.get(guild.emojis, name="update")
        emojis["Updating"] = discord.utils.get(guild.emojis, name="updating")
        emojis["Voice"] = discord.utils.get(guild.emojis, name="voice")
        emojis["Voice_locked"] = discord.utils.get(guild.emojis, name="voice_locked")

        # Discord Badges
        guild = self.get_guild(Emojis_discord_badges_id)
        emojis["Balance"] = discord.utils.get(guild.emojis, name="balance")
        emojis["Boost"] = discord.utils.get(guild.emojis, name="boost")
        emojis["Bravery"] = discord.utils.get(guild.emojis, name="bravery")
        emojis["Brilliance"] = discord.utils.get(guild.emojis, name="brilliance")
        emojis["Bug_hunter_lvl1"] = discord.utils.get(guild.emojis, name="bug_hunter_lvl_1")
        emojis["Bug_hunter_lvl_2"] = discord.utils.get(guild.emojis, name="bug_hunter_lvl_2")
        emojis["Developer"] = discord.utils.get(guild.emojis, name="developer")
        emojis["Do_not_disturb"] = discord.utils.get(guild.emojis, name="do_not_disturb")
        emojis["Early_supporter"] = discord.utils.get(guild.emojis, name="early_supporter")
        emojis["Idle"] = discord.utils.get(guild.emojis, name="idle")
        emojis["Hypesquad"] = discord.utils.get(guild.emojis, name="hypesquad")
        emojis["Hypesquad_events"] = discord.utils.get(guild.emojis, name="hypesquad_events")
        emojis["Info"] = discord.utils.get(guild.emojis, name="info")
        emojis["Offline"] = discord.utils.get(guild.emojis, name="offline")
        emojis["Online"] = discord.utils.get(guild.emojis, name="online")
        emojis["Owner"] = discord.utils.get(guild.emojis, name="owner")
        emojis["Partner"] = discord.utils.get(guild.emojis, name="partner")
        emojis["Streaming"] = discord.utils.get(guild.emojis, name="streaming")

        # Discord Icons
        guild = self.get_guild(Emojis_discord_general_icons_id)
        emojis["Browser"] = discord.utils.get(guild.emojis, name="browser")
        emojis["Calendar"] = discord.utils.get(guild.emojis, name="calendar")
        emojis["Delete"] = discord.utils.get(guild.emojis, name="delete")
        emojis["Description"] = discord.utils.get(guild.emojis, name="description")
        emojis["Id"] = discord.utils.get(guild.emojis, name="id")
        emojis["Language"] = discord.utils.get(guild.emojis, name="language")
        emojis["Name"] = discord.utils.get(guild.emojis, name="name")
        emojis["Ticket"] = discord.utils.get(guild.emojis, name="ticket")

        # Spam
        guild = self.get_guild(Emojis_spam_id)
        fr_emoji = discord.utils.get(guild.emojis, name="fr")
        us_uk_emoji = discord.utils.get(guild.emojis, name="us_uk")
        emojis["Languages_emojis"] = {"English": us_uk_emoji, "French": fr_emoji}

        emojis["Numbers"] = {}
        numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}
        for number, name in numbers.items():
            emojis["Numbers"][number] = discord.utils.get(guild.emojis, name=name)

        emojis["Banned1"] = discord.utils.get(guild.emojis, name="banned1")
        emojis["Banned2"] = discord.utils.get(guild.emojis, name="banned2")
        emojis["Banned3"] = discord.utils.get(guild.emojis, name="banned3")
        emojis["Dg"] = discord.utils.get(guild.emojis, name="dg")
        emojis["Donations"] = discord.utils.get(guild.emojis, name="donations")
        emojis["End"] = discord.utils.get(guild.emojis, name="end")
        emojis["Exp"] = discord.utils.get(guild.emojis, name="exp")
        emojis["Link"] = discord.utils.get(guild.emojis, name="link")
        emojis["Python"] = discord.utils.get(guild.emojis, name="python")
        emojis["Received"] = discord.utils.get(guild.emojis, name="received")
        emojis["Think"] = discord.utils.get(guild.emojis, name="think")

        self.emojis = emojis
        await self.logout()

    async def on_disconnect(self):
        self.emoji_connected.set()


client = EmojisBot()
loop = asyncio.get_event_loop()


async def login():
    await client.login(Login["discord"]["beta"])
loop.run_until_complete(login())


async def wrapped_connect():
    try:
        await client.connect()
        global Emojis
        Emojis = client.emojis
    except Exception as e:
        print("Error (import_emojis)", e)
        await client.close()
        client.emoji_connected.set()
loop.create_task(wrapped_connect())


async def check_close():
    futures = [client.emoji_connected.wait()]
    await asyncio.wait(futures)
loop.run_until_complete(check_close())
