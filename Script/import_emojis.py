import asyncio

import discord

from Data.Constants.import_const import Login, Ids, Main_bot
from Data.Constants.useful import Useful

Emojis = {}


class EmojisBot(discord.Client):
    emojis = {}
    emoji_connected = asyncio.Event()

    def __init__(self):
        super().__init__()

    async def on_ready(self):
        emojis = {}

        # COC Th-Bh-Leagues
        guild = self.get_guild(Ids["Emojis_coc_th_bh_leagues_server"])
        th_emojis = {}
        for i in range(1, Useful["max_th_lvl"] + 1):
            th_emojis[i] = discord.utils.get(guild.emojis, name=f"TH_{i:02d}")  # Name from TH_01 to TH_14
        emojis["Th_emojis"] = th_emojis

        bh_emojis = {}
        for i in range(1, Useful["max_bh_lvl"] + 1):
            bh_emojis[i] = discord.utils.get(guild.emojis, name=f"BH_{i:02d}")  # Name from BH_01 to BH_09
        emojis["Bh_emojis"] = bh_emojis

        league_emojis = {}
        for league in Useful["league_trophies"].keys():
            emoji = discord.utils.get(guild.emojis, name=league.replace(" ", "_").lower())
            league_emojis[league] = emoji
        emojis["League_emojis"] = league_emojis

        emojis["Barbarian_king"] = discord.utils.get(guild.emojis, name="barbarian_king")
        emojis["Archer_queen"] = discord.utils.get(guild.emojis, name="archer_queen")
        emojis["Grand_warden"] = discord.utils.get(guild.emojis, name="grand_warden")
        emojis["Royal_champion"] = discord.utils.get(guild.emojis, name="royal_champion")
        emojis["Battle_machine"] = discord.utils.get(guild.emojis, name="battle_machine")

        # COC Troops-Spell
        guild = self.get_guild(Ids["Emojis_coc_troops_spells_server"])
        emojis["Troop"] = discord.utils.get(guild.emojis, name="TE1")
        troops_emojis = {}
        emoji_to_name = {"TE1": "Barbarian", "TE2": "Archer", "TE3": "Giant", "TE4": "Goblin", "TE5": "Wall Breaker", "TE6": "Balloon", "TE7": "Wizard", "TE8": "Healer", "TE9": "Dragon", "TE10": "P.E.K.K.A", "TE11": "Baby Dragon", "TE12": "Miner", "TE13": "Electro Dragon", "TE14": "Yeti", "TE15": "Dragon Rider", "TD1": "Minion", "TD2": "Hog Rider", "TD3": "Valkyrie", "TD4": "Golem", "TD5": "Witch", "TD6": "Lava Hound", "TD7": "Bowler", "TD8": "Ice Golem", "TD9": "Headhunter", "SE1": "Lightning Spell", "SE2": "Healing Spell", "SE3": "Rage Spell", "SE4": "Jump Spell", "SE5": "Freeze Spell", "SE6": "Clone Spell", "SE7": "Invisibility Spell", "SD1": "Poison Spell", "SD2": "Earthquake Spell", "SD3": "Haste Spell", "SD4": "Skeleton Spell", "SD5": "Bat Spell", "M1": "Wall Wrecker", "M2": "Battle Blimp", "M3": "Stone Slammer", "M4": "Siege Barracks", "M5": "Log Launcher", "M6": "Flame Flinger", "P1": "L.A.S.S.I", "P2": "Electro Owl", "P3": "Mighty Yak", "P4": "Unicorn"}
        for emoji in guild.emojis:
            troops_emojis.update({emoji_to_name[emoji.name]: emoji})
        emojis["Troops_emojis"] = troops_emojis

        # COC War Leagues
        guild = self.get_guild(Ids["Emojis_coc_war_leagues"])
        war_leagues_emojis = {}
        name_to_emoji_name = {"Unranked": "unranked", "Bronze League III": "bronze_league_III", "Bronze League II": "bronze_league_II", "Bronze League I": "bronze_league_I", "Silver League III": "silver_league_III", "Silver League II": "silver_league_II", "Silver League I": "silver_league_I", "Gold League III": "gold_league_III", "Gold League II": "gold_league_II", "Gold League I": "gold_league_I", "Crystal League III": "crystal_league_III", "Crystal League II": "crystal_league_II", "Crystal League I": "crystal_league_I", "Master League III": "master_league_III", "Master League II": "master_league_II", "Master League I": "master_league_I", "Champion League III": "champion_league_III", "Champion League II": "champion_league_II", "Champion League I": "champion_league_I"}
        for name, emoji_name in name_to_emoji_name.items():
            war_leagues_emojis[name] = discord.utils.get(guild.emojis, name=emoji_name)
        emojis["War_leagues"] = war_leagues_emojis

        # COC Main
        guild = self.get_guild(Ids["Emojis_coc_main_server"])
        emojis["Trophy"] = discord.utils.get(guild.emojis, name="trophy")
        emojis["Versus_trophy"] = discord.utils.get(guild.emojis, name="versus_trophy")
        emojis["Star"] = discord.utils.get(guild.emojis, name="star")
        emojis["Star_empty"] = discord.utils.get(guild.emojis, name="star_empty")
        emojis["Star_old"] = discord.utils.get(guild.emojis, name="star_old")
        emojis["Star_success"] = discord.utils.get(guild.emojis, name="star_success")

        # Support
        guild = self.get_guild(Ids["Support_server"])
        emojis["Bot"] = discord.utils.get(guild.emojis, name="bot")
        emojis["Bot_certified"] = discord.utils.get(guild.emojis, name="bot_certified")
        emojis["Clash_esport"] = discord.utils.get(guild.emojis, name="ClashESPORT")
        emojis["Clash_info"] = discord.utils.get(guild.emojis, name="ClashINFO")
        emojis["Github"] = discord.utils.get(guild.emojis, name="github")
        emojis["Yes"] = discord.utils.get(guild.emojis, name="yes")
        emojis["No"] = discord.utils.get(guild.emojis, name="no")

        # Discord Main
        guild = self.get_guild(Ids["Emojis_discord_main_server"])
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
        guild = self.get_guild(Ids["Emojis_discord_badges_server"])
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
        guild = self.get_guild(Ids["Emojis_discord_general_icons_server"])
        emojis["Browser"] = discord.utils.get(guild.emojis, name="browser")
        emojis["Calendar"] = discord.utils.get(guild.emojis, name="calendar")
        emojis["Delete"] = discord.utils.get(guild.emojis, name="delete")
        emojis["Delete_grey"] = discord.utils.get(guild.emojis, name="delete_grey")
        emojis["Description"] = discord.utils.get(guild.emojis, name="description")
        emojis["Id"] = discord.utils.get(guild.emojis, name="id")
        emojis["Language"] = discord.utils.get(guild.emojis, name="language")
        emojis["Name"] = discord.utils.get(guild.emojis, name="name")
        emojis["Ticket"] = discord.utils.get(guild.emojis, name="ticket")

        # Spam
        guild = self.get_guild(Ids["Emojis_spam_server"])
        fr_emoji = discord.utils.get(guild.emojis, name="fr")
        us_uk_emoji = discord.utils.get(guild.emojis, name="us_uk")
        emojis["Languages_emojis"] = {"English": us_uk_emoji, "French": fr_emoji}

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
    if Main_bot:
        discord_token = Login["discord"]["token"]
    else:
        discord_token = Login["discord"]["beta"]
    await client.login(discord_token)
loop.run_until_complete(login())


async def wrapped_connect():
    await client.connect()
    global Emojis
    Emojis = client.emojis
loop.create_task(wrapped_connect())


async def check_close():
    futures = [client.emoji_connected.wait()]
    await asyncio.wait(futures)
loop.run_until_complete(check_close())
