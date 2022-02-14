# Called when the bot is ready to be used

import asyncio
import datetime
import sqlite3
import threading
import time

import discord
import flask

from Data.Constants.import_const import Login, Ids, Main_bot, Useful
from Script.import_emojis import Emojis

if Main_bot:
    discord_token = Login["discord"]["token"]
else:
    discord_token = Login["discord"]["beta"]


async def ready_loop(self):
    support_server = self.get_guild(Ids["Support_server"])
    member_role = discord.utils.get(support_server.roles, name="Member")
    for member in support_server.members:
        if (member_role not in member.roles) and (not member.bot):
            await member.add_roles(member_role)

    if Main_bot:
        status_channel = self.get_channel(Ids["Status_channel"])
        msg = await status_channel.send(f"{Emojis['Yes']} Connected")
        await msg.edit(content=f"{Emojis['Yes']} Connected `{msg.created_at.replace(microsecond=0).isoformat(sep=' ')}` UTC-0")

    clash_info = self

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
                    super().__init__()

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
                    await channel.send(f"Evolution of number of servers this week : {diff_servers_count}")
                    await self.logout()

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
                    super().__init__()

                async def on_ready(self):
                    connection = sqlite3.connect(Useful["secure_folder_path"] + "Modifiable.sqlite")
                    cursor = connection.cursor()
                    cursor.execute("SELECT COUNT(*) FROM BotUsage")
                    nb_monthly_users = cursor.fetchone()[0]
                    text = f"Monthly users : {nb_monthly_users}"
                    channel = self.get_channel(Ids["Monthly_stats_channel"])
                    await channel.send(text)
                    if len(str(date.month)) == 1:
                        month = f"0{date.month}"
                    else:
                        month = str(date.month)
                    w = f"""CREATE TABLE IF NOT EXISTS BotUsage_{date.year}_{month} AS SELECT * FROM BotUsage"""
                    cursor.execute(w)
                    cursor.execute("DELETE FROM BotUsage")
                    connection.commit()
                    await self.logout()

            monthly_users_bot = MonthlyUsersBot()
            try:
                loop.run_until_complete(monthly_users_bot.start(discord_token))
            except KeyboardInterrupt:
                loop.run_until_complete(monthly_users_bot.close())
            finally:
                loop.close()

    thread = threading.Thread(target=thread_monthly_users)
    thread.start()

    def thread_webhooks_app():
        app = flask.Flask(__name__)

        @app.route('/topgg_webhook', methods=['post'])
        def topgg_webhook():
            if (flask.request.remote_addr != "159.203.105.187") or ("Authorization" not in list(flask.request.headers.keys())) or (flask.request.headers["Authorization"] != Login["topgg"]["authorization"]):
                authorization = None if "Authorization" not in list(flask.request.headers.keys()) else flask.request.headers["Authorization"]
                print(f"Unauthorized :\nIP = {flask.request.remote_addr}\nAuthorization = {authorization}")
                return flask.Response(status=401)

            def run_bot(voter_id):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

                class WebhooksBot(discord.Client):
                    def __init__(self):
                        super().__init__()

                    async def on_ready(self):
                        import json
                        from Script.import_functions import create_embed
                        from Data.Constants.useful import Useful
                        from Data.Variables.import_var import Votes

                        user = clash_info.get_user(voter_id)
                        votes_channel = self.get_channel(Ids["Votes_channel"])

                        if user.id not in list(Votes.keys()):
                            Votes[user.id] = 1
                        else:
                            Votes[user.id] += 1
                        json_text = json.dumps(Votes, sort_keys=True, indent=4)
                        def_votes = open(f"{Useful['secure_folder_path']}votes.json", "w")
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
                        embed = create_embed(f"{user} has voted for Clash INFO", text, votes_channel.guild.me.color, "", votes_channel.guild.me.avatar_url)
                        await votes_channel.send(embed=embed)
                        await self.logout()

                webhooks_bot = WebhooksBot()
                try:
                    loop.run_until_complete(webhooks_bot.start(discord_token))
                except KeyboardInterrupt:
                    loop.run_until_complete(webhooks_bot.close())
                finally:
                    loop.close()

            import threading
            thread = threading.Thread(target=run_bot, kwargs={"voter_id": int(flask.request.get_json()["user"])})
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
