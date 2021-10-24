# Called when the bot is ready to be used

import asyncio
import datetime
import sqlite3
import threading
import time

import discord

from Data.Const_variables.import_const import Login, Ids
from Script.import_emojis import Emojis
from Script.import_functions import int_to_str


async def ready_loop(self):
    if self.id == 704688212832026724:
        status_channel = self.get_channel(733089353634545684)
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
                weekly_bot_connected = asyncio.Event()

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
                    diff_servers_count = "%+d" % (diff_servers_count)
                    await channel.send(f"Evolution of number of servers this week : {diff_servers_count}")
                    await self.logout()

                async def on_disconnect(self):
                    self.weekly_bot_connected.set()

            weekly_stats_bot = WeeklyStatsBot()

            async def login():
                await weekly_stats_bot.login(Login["discord"]["beta"])

            loop.run_until_complete(login())

            async def wrapped_connect():
                try:
                    await weekly_stats_bot.connect()
                except Exception as e:
                    print("Weekly, ", e)
                    await weekly_stats_bot.close()
                    weekly_stats_bot.weekly_bot_connected.set()

            loop.create_task(wrapped_connect())

            async def check_close():
                futures = [weekly_stats_bot.weekly_bot_connected.wait()]
                await asyncio.wait(futures)

            loop.run_until_complete(check_close())
            loop.close()

    thread = threading.Thread(target=thread_weekly_stats, args=())
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
                monthly_bot_connected = asyncio.Event()

                def __init__(self):
                    super().__init__()

                async def on_ready(self):
                    connection = sqlite3.connect("Data/Modifiable_variables.sqlite")
                    cursor = connection.cursor()
                    cursor.execute("SELECT COUNT(*) FROM BotUsage")
                    nb_monthly_users = cursor.fetchone()[0]
                    text = f"Monthly users : {nb_monthly_users}"
                    channel = self.get_channel(Ids["Monthly_stats_channel"])
                    await channel.send(text)
                    if len(str(date.month)) == 1:
                        month = "0" + str(date.month)
                    else:
                        month = str(date.month)
                    w = f"""CREATE TABLE IF NOT EXISTS BotUsage_{date.year}_{month} AS SELECT * FROM BotUsage"""
                    cursor.execute(w)
                    cursor.execute("DELETE FROM BotUsage")
                    connection.commit()
                    await self.logout()

                async def on_disconnect(self):
                    self.monthly_bot_connected.set()

            monthly_users_bot = MonthlyUsersBot()

            async def login():
                await monthly_users_bot.login(Login["discord"]["beta"])

            loop.run_until_complete(login())

            async def wrapped_connect():
                try:
                    await monthly_users_bot.connect()
                except Exception as e:
                    print("Monthly, ", e)
                    await monthly_users_bot.close()
                    monthly_users_bot.monthly_bot_connected.set()

            loop.create_task(wrapped_connect())

            async def check_close():
                futures = [monthly_users_bot.monthly_bot_connected.wait()]
                await asyncio.wait(futures)

            loop.run_until_complete(check_close())
            loop.close()

    thread = threading.Thread(target=thread_monthly_users, args=())
    thread.start()

    print("Connected")

    while True:
        nb_guilds = len(self.guilds)
        act = discord.Activity(type=discord.ActivityType.watching, name=int_to_str(nb_guilds) + " servers")
        await self.change_presence(status=discord.Status.online, activity=act)
        await asyncio.sleep(60)
