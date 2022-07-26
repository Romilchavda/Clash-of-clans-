import asyncio
import datetime
import json
import os
import shutil
import sqlite3
import threading
import time

import discord
import flask

from bot.emojis import Emojis
from bot.functions import create_embed
from data.config import Config
from data.secure_folder import Login
from data.useful import Ids


async def ready(self: discord.Client):
    if Config["main_bot"]:
        status_channel = self.get_channel(Ids["Status_channel"])
        await status_channel.send(f"{Emojis['Yes']} Connected `{datetime.datetime.now().replace(microsecond=0).isoformat(sep=' ')}`")

    await self.sync_commands()

    from bot.apis_clients.clash_of_clans import Clash_of_clans, login
    await Clash_of_clans.login(login["email"], login["password"])

    for guild in self.guilds:
        await guild.chunk()

    if Config["main_bot"]:
        status_channel = self.get_channel(Ids["Status_channel"])
        await status_channel.send(f"{Emojis['Yes']} Cache loaded `{datetime.datetime.now().replace(microsecond=0).isoformat(sep=' ')}`")

    support_server = self.get_guild(Ids["Support_server"])

    if self.id == 704688212832026724:  # TODO : The following code only works with Clash INFO for the moment (see also member_join.py)
        member_role = discord.utils.get(support_server.roles, name="Member")
        for member in support_server.members:
            if member_role not in member.roles and not member.bot:
                await member.add_roles(member_role)

    clash_info = self

    if Config["main_bot"]:
        discord_token = Login["discord"]["main"]
    else:
        discord_token = Login["discord"]["beta"]

    def thread_weekly_stats():
        while True:
            date = datetime.datetime.now()
            monday = datetime.date.today() + datetime.timedelta(days=(7 - date.weekday()))
            monday = datetime.datetime(monday.year, monday.month, monday.day)
            diff = monday - date
            time.sleep(diff.seconds + diff.days * 24 * 3600)
            print("Weekly Stats", datetime.datetime.now())

            # ===== WEEKLY STATS =====

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            class WeeklyStatsBot(discord.Client):
                def __init__(self):
                    super().__init__(intents=discord.Intents.default())

                async def on_ready(self):
                    channel = self.get_channel(Ids["Weekly_stats_channel"])
                    old_servers_count = 0
                    async for message in channel.history(limit=None):
                        if message.is_system():
                            await message.delete()
                        if message.pinned:
                            old_servers_count = int(message.content)
                            await message.delete()
                            break
                    msg = await channel.send(str(len(clash_info.guilds)))
                    await msg.pin()
                    diff_servers_count = len(clash_info.guilds) - old_servers_count
                    diff_servers_count = "%+d" % diff_servers_count
                    await channel.send(f"Evolution of number of servers this week: {diff_servers_count}")
                    await self.close()

            weekly_stats_bot = WeeklyStatsBot()
            try:
                loop.run_until_complete(weekly_stats_bot.start(discord_token))
            except KeyboardInterrupt:
                loop.run_until_complete(weekly_stats_bot.close())
            finally:
                loop.close()

    thread = threading.Thread(target=thread_weekly_stats)
    thread.start()

    def thread_monthly_users():
        while True:
            date = datetime.datetime.now()
            if date.month < 12:
                day1 = datetime.datetime(date.year, date.month + 1, 1)
            else:
                day1 = datetime.datetime(date.year + 1, 1, 1)
            diff = day1 - date
            time.sleep(diff.seconds + diff.days * 24 * 3600 + 3600)  # 1h00 instead of 0h00 to avoid conflicts with WeeklyStats
            print("Monthly Users Stats", datetime.datetime.now())

            # ===== MONTHLY USERS =====

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            class MonthlyUsersBot(discord.Client):

                def __init__(self):
                    super().__init__(intents=discord.Intents.default())

                async def on_ready(self):
                    connection = sqlite3.connect(Config["secure_folder_path"] + "secure.sqlite")
                    cursor = connection.cursor()
                    cursor.execute("SELECT COUNT(*) FROM bot_usage")
                    nb_monthly_users = cursor.fetchone()[0]
                    text = f"**Monthly users: {nb_monthly_users}\n\n**"
                    commands_stats = {}

                    cursor.execute("PRAGMA table_info(bot_usage)")
                    commands_names = []
                    for command in cursor.fetchall():
                        command_name = command[1]
                        if command_name != "user_id":
                            commands_names += [command_name]

                    for command_name in commands_names:
                        cursor.execute(f"SELECT COUNT(*) FROM bot_usage WHERE NOT {command_name} = 0")
                        commands_stats[command_name] = cursor.fetchone()[0]

                    for name, usages in {k: v for k, v in sorted(commands_stats.items(), key=lambda x: x[1], reverse=True)}.items():
                        text += f"{name}: {usages}\n"

                    channel = self.get_channel(Ids["Monthly_stats_channel"])
                    await channel.send(text)
                    cursor.execute("DELETE FROM bot_usage")
                    connection.commit()
                    await self.close()

            monthly_users_bot = MonthlyUsersBot()
            try:
                loop.run_until_complete(monthly_users_bot.start(discord_token))
            except KeyboardInterrupt:
                loop.run_until_complete(monthly_users_bot.close())
            finally:
                loop.close()

    thread = threading.Thread(target=thread_monthly_users)
    thread.start()

    def thread_backup_secure_folder():
        while True:
            date = datetime.datetime.now()
            monday = datetime.date.today() + datetime.timedelta(days=(7 - date.weekday()))
            monday = datetime.datetime(monday.year, monday.month, monday.day)
            diff = monday - date
            time.sleep(diff.seconds + diff.days * 24 * 3600)
            print("Save Secure Folder", datetime.datetime.now())

            # ===== BACKUP SECURE FOLDER =====

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            class BackupSecureFolderBot(discord.Client):

                def __init__(self):
                    super().__init__(intents=discord.Intents.default())

                async def on_ready(self):
                    shutil.make_archive("Secure Folder", 'zip', "../Secure Folder")
                    file = discord.File(fp="Secure Folder.zip", filename="Secure Folder.zip")
                    await self.get_channel(Ids["Secure_folder_backup_channel"]).send("Here is the Secure Folder backup !", file=file)
                    os.remove("Secure Folder.zip")
                    await self.close()

            secure_folder_backup_bot = BackupSecureFolderBot()
            try:
                loop.run_until_complete(secure_folder_backup_bot.start(discord_token))
            except KeyboardInterrupt:
                loop.run_until_complete(secure_folder_backup_bot.close())
            finally:
                loop.close()

    thread = threading.Thread(target=thread_backup_secure_folder)
    thread.start()

    def thread_webhooks_app():
        app = flask.Flask(__name__)

        @app.route("/topgg_webhook", methods=["post"])
        def topgg_webhook():
            if flask.request.remote_addr != "159.203.105.187" or "Authorization" not in list(flask.request.headers.keys()) or flask.request.headers["Authorization"] != Login["top_gg"]["authorization"]:
                authorization = None if "Authorization" not in list(flask.request.headers.keys()) else flask.request.headers["Authorization"]
                print(f"Unauthorized:\nIP = {flask.request.remote_addr}\nAuthorization = {authorization}")
                return flask.Response(status=401)

            def run_bot(voter_id: int):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

                class TopggWebhooksBot(discord.Client):
                    def __init__(self):
                        super().__init__(intents=discord.Intents.default())

                    async def on_ready(self):
                        from data.secure_folder import Votes

                        user = clash_info.get_user(voter_id)
                        votes_channel = self.get_channel(Ids["Votes_channel"])

                        if user.id not in list(Votes.keys()):
                            Votes[user.id] = 1
                        else:
                            Votes[user.id] += 1
                        json_text = json.dumps(Votes, sort_keys=True, indent=4)
                        def_votes = open(f"{Config['secure_folder_path']}votes.json", "w")
                        def_votes.write(json_text)
                        def_votes.close()
                        vote_copy = dict(Votes)
                        vote = {}
                        for member_id, member_votes in vote_copy.items():
                            member = clash_info.get_user(int(member_id))
                            vote[member.mention] = member_votes
                        vote = sorted(vote.items(), key=lambda t: t[1])
                        text = ""
                        for user_vote_tuple in vote:
                            text += f"{user_vote_tuple[0]} has voted {user_vote_tuple[1]} times\n"
                        embed = create_embed(f"{user} has voted for Clash INFO", text, votes_channel.guild.me.color, "", votes_channel.guild.me.display_avatar.url)
                        await votes_channel.send(embed=embed)
                        await self.close()

                topgg_webhooks_bot = TopggWebhooksBot()
                try:
                    loop.run_until_complete(topgg_webhooks_bot.start(discord_token))
                except KeyboardInterrupt:
                    loop.run_until_complete(topgg_webhooks_bot.close())
                finally:
                    loop.close()

            thread = threading.Thread(target=run_bot, kwargs={"voter_id": int(flask.request.get_json()["user"])})
            thread.start()
            return flask.Response(status=200)

        @app.route("/github_webhook", methods=["post"])
        def github_webhook():  # TODO : Finish it
            if flask.request.get_json()["repository"]["name"] != "Clash-Of-Clans-Discord-Bot":
                return 418

            print("GitHub Webhooks:", flask.request.headers["X-Github-Event"])
            print(flask.request.get_json())

            def run_bot(event_name: str, original_json: dict):
                lite_json = original_json
                for k, v in original_json["repository"].items():
                    lite_json.pop(k)
                lite_json.pop("repository")
                if "forkee" in list(original_json.keys()):
                    for k, v in original_json["forkee"].items():
                        lite_json.pop(k)
                    lite_json.pop("forkee")
                print(lite_json)
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

                class GitHubWebhooksBot(discord.Client):
                    def __init__(self):
                        super().__init__(intents=discord.Intents.default())

                    async def on_ready(self):
                        events_channel = self.get_channel(837339878869565460)  # TODO : Generalize it (with ids.json)
                        embed = create_embed(f"{event_name.capitalize()} from {lite_json['sender']['login']}", f"```json\n{json.dumps(lite_json, indent=2)}```", events_channel.guild.me.color, "", events_channel.guild.me.display_avatar.url)
                        await events_channel.send(f"{event_name.capitalize()} from {lite_json['sender']['login']}")
                        await events_channel.send(embed=embed)
                        await self.close()

                github_webhooks_bot = GitHubWebhooksBot()
                try:
                    loop.run_until_complete(github_webhooks_bot.start(discord_token))
                except KeyboardInterrupt:
                    loop.run_until_complete(github_webhooks_bot.close())
                finally:
                    loop.close()

            thread = threading.Thread(target=run_bot, kwargs={"event_name": flask.request.headers["X-Github-Event"], "original_json": flask.request.get_json()})
            thread.start()
            return flask.Response(status=200)

        app.run(host="0.0.0.0", port=8080)

    thread = threading.Thread(target=thread_webhooks_app, args=())
    thread.start()

    print("Connected")

    nb_guilds = len(self.guilds)
    act = discord.Activity(type=discord.ActivityType.watching, name=f"{nb_guilds: ,} servers")
    await self.change_presence(status=discord.Status.online, activity=act)
    return
