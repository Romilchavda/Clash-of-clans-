from discord.message import Message


class Msg(Message):
    def __init__(self, message):
        __slots__ = ('_edited_timestamp', 'tts', 'content', 'channel', 'webhook_id',
                     'mention_everyone', 'embeds', 'id', 'mentions', 'author',
                     '_cs_channel_mentions', '_cs_raw_mentions', 'attachments',
                     '_cs_clean_content', '_cs_raw_channel_mentions', 'nonce', 'pinned',
                     'role_mentions', '_cs_raw_role_mentions', 'type', 'call', 'flags',
                     '_cs_system_content', '_cs_guild', '_state', 'reactions', 'reference',
                     'application', 'activity', 'stickers')
        __replace__ = {
            "_edited_timestamp": "edited_timestamp"
        }
        data = {}
        # print("Undefined : ", end="")
        for attr in __slots__:
            if attr in list(__replace__.keys()):
                name = __replace__[attr]
            else:
                name = attr
            # print(name, attr)
            try:
                getattr(message, attr)
            except AttributeError:
                pass
                # print(attr, end=", ")
            data.update({name: getattr(message, attr, None)})
        # print()
        data["author"] = {"id": data["author"].id}
        # print(data)
        super().__init__(state=message._state, channel=message.channel, data=data)

    async def send(self, *args, **kwargs):
        # print("*args", args)
        # print("**kwargs", kwargs)
        if "hidden" in list(kwargs.keys()):
            kwargs.pop("hidden")
        # print("**kwargs", kwargs)
        msg = await self.channel.send(*args, **kwargs)
        return msg


# ----- LIBRARIES : -----
import coc
import json
import datetime
from matplotlib import dates as mdates
from matplotlib import pyplot
import asyncio
from PIL import Image, ImageFont, ImageDraw


# ----- PROJECT FILES : -----
from Script.import_functions import *
from Script.Clients.top_gg import Dbl_client
from Script.Clients.clash_of_clans import Clash_of_clans
from Script.Const_variables.import_const import Login


# ----- COMMANDS : -----

# ON_READY
from Script.Commands.On_Ready.loop import loop

# GUILD
from Script.Commands.Guild.guild_join import guild_join
from Script.Commands.Guild.guild_remove import guild_remove

# MEMBER
from Script.Commands.Member.member_join import member_join
from Script.Commands.Member.member_remove import member_remove

# REACTION add
from Script.Commands.Reactions.Reaction_add.help import reaction_add_help
from Script.Commands.Reactions.Reaction_add.close_ticket import reaction_add_close_ticket
from Script.Commands.Reactions.Reaction_add.change_th_lvl import reaction_add_change_th_lvl
from Script.Commands.Reactions.Reaction_add.change_bh_lvl import reaction_add_change_bh_lvl
from Script.Commands.Reactions.Reaction_add.show_link_vote import reaction_add_show_link_vote
from Script.Commands.Reactions.Reaction_add.change_player_stats_page import reaction_add_change_player_stats_page
# REACTION remove


# RAW_REACTION add
from Script.Commands.Raw_Reaction.Raw_Reaction_add.follow_news_support import raw_reaction_add_follow_news_support
from Script.Commands.Raw_Reaction.Raw_Reaction_add.auto_roles import raw_reaction_add_auto_roles
from Script.Commands.Raw_Reaction.Raw_Reaction_add.check_rules import raw_reaction_add_check_rules
from Script.Commands.Raw_Reaction.Raw_Reaction_add.auto_roles_languages import raw_reaction_add_auto_roles_languages
from Script.Commands.Raw_Reaction.Raw_Reaction_add.create_ticket import raw_reaction_add_create_ticket
from Script.Commands.Raw_Reaction.Raw_Reaction_add.delete_ticket import raw_reaction_add_delete_ticket
from Script.Commands.Raw_Reaction.Raw_Reaction_add.end_poll import raw_reaction_add_end_poll
from Script.Commands.Raw_Reaction.Raw_Reaction_add.feedback import raw_reaction_add_feedback
from Script.Commands.Raw_Reaction.Raw_Reaction_add.report_bug import raw_reaction_add_report_bug
# RAW_REACTION remove
from Script.Commands.Raw_Reaction.Raw_Reaction_remove.auto_roles import raw_reaction_remove_auto_roles
from Script.Commands.Raw_Reaction.Raw_Reaction_remove.check_rules import raw_reaction_remove_check_rules
from Script.Commands.Raw_Reaction.Raw_Reaction_remove.auto_roles_languages import raw_reaction_remove_auto_roles_languages
from Script.Commands.Raw_Reaction.Raw_Reaction_remove.feedback import raw_reaction_remove_feedback

# MESSAGES
from Script.Commands.Messages.help import help

from Script.Commands.Messages.Clash_Of_Clans.get_player import get_player
from Script.Commands.Messages.Clash_Of_Clans.get_clan import get_clan
from Script.Commands.Messages.Clash_Of_Clans.search_clan import search_clan
from Script.Commands.Messages.Clash_Of_Clans.clan_members import clan_members
from Script.Commands.Messages.Clash_Of_Clans.buildings_th import buildings_th
from Script.Commands.Messages.Clash_Of_Clans.buildings_bh import buildings_bh
from Script.Commands.Messages.Clash_Of_Clans.auto_roles import auto_roles_th, auto_roles_bh, auto_roles_leagues
from Script.Commands.Messages.Clash_Of_Clans.coc_file import coc_file

from Script.Commands.Messages.Useful.tickets import tickets, close_ticket
from Script.Commands.Messages.Useful.member_info import member_info
from Script.Commands.Messages.Useful.role_info import role_info
from Script.Commands.Messages.Useful.server_info import server_info
from Script.Commands.Messages.Useful.emoji_info import emoji_info
from Script.Commands.Messages.Useful.direct_message import direct_message_member, direct_message_role
from Script.Commands.Messages.Useful.poll import poll
from Script.Commands.Messages.Creators.add_a_bot_id import add_a_bot_id
from Script.Commands.Messages.Useful.ping import ping
# from Script.Commands.Messages.Useful.bot_info import bot_info
from Script.Commands.Messages.Useful.add_the_bot import add_the_bot_default, add_the_bot_administrator
from Script.Commands.Messages.Useful.support_server import support_server
from Script.Commands.Messages.Useful.promote_the_bot import promote_the_bot
from Script.Commands.Messages.Useful.youtube import youtube

from Script.Commands.Messages.Moderation.delete_messages import delete_messages_number, delete_messages_time, delete_messages_all


# CONST VARIABLES
from Script.import_emojis import Emojis
from Script.Const_variables.import_const import Th_buildings, Bh_buildings, Troops, Ids


# MODIFIABLE VARIABLES
from Script.Modifiable_variables.import_var import Prefix, History, Votes, Support


class Bot(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)


    # temp
    def create_embed(self, title, description, colour, footer):
        icon_url = "https://cdn.discordapp.com/avatars/704688212832026724/810c7d7d98bbcb5294444742b01c9e04.webp?size=1024"
        embed=create_embed(title, description, colour, footer, icon_url)
        return embed
    def create_embed_img(self, title, description, colour, footer, img):
        icon_url = "https://cdn.discordapp.com/avatars/704688212832026724/810c7d7d98bbcb5294444742b01c9e04.webp?size=1024"
        embed=create_embed_img(title, description, colour, footer, icon_url, img)
        return embed


    # READY
    async def on_ready(self):
        print("Connected")
        if self.id == 704688212832026724:
            status_channel = self.get_channel(733089353634545684)
            msg = await status_channel.send(f"{Emojis['Yes']} Connected")
            await msg.edit(content=f"{Emojis['Yes']} Connected `{msg.created_at.replace(microsecond=0).isoformat(sep=' ')}` UTC-0")
        await loop(self)


    # GUILD
    async def on_guild_join(self, guild):
        await guild_join(self, guild)
        return

    async def on_guild_remove(self, guild):
        await guild_remove(self, guild)
        return


    # MEMBER
    async def on_member_join(self, member):
        await member_join(self, member)
        return

    async def on_member_remove(self, member):
        await member_remove(self, member)
        return


    # REACTION
    async def on_reaction_add(self, reaction, member):
        if (not member.bot) and (reaction.message.guild is not None) and (reaction.message.author.id == self.id) and (reaction.message.embeds != []):
            await reaction_add_help(self, reaction, member)
            await reaction_add_close_ticket(self, reaction, member)
            await reaction_add_change_th_lvl(self, reaction, member)
            await reaction_add_change_bh_lvl(self, reaction, member)
            await reaction_add_show_link_vote(self, reaction, member)
            await reaction_add_change_player_stats_page(self, reaction, member)
        return


    # RAW REACTION
    async def on_raw_reaction_add(self, raw_reaction):
        channel = self.get_channel(raw_reaction.channel_id)
        raw_reaction.message = None
        if channel.guild.me.guild_permissions.read_message_history:
            async for message in channel.history(limit=None):
                if message.id == raw_reaction.message_id:
                    raw_reaction.message = message
                    break
        if (raw_reaction.message is not None) and (not raw_reaction.member.bot) and (raw_reaction.message.guild is not None) and (raw_reaction.message.author.id == self.id) and (raw_reaction.message.embeds != []):
            raw_reaction.complete_emoji = self.get_emoji(raw_reaction.emoji.id)
            await raw_reaction_add_follow_news_support(self, raw_reaction)
            await raw_reaction_add_auto_roles(self, raw_reaction)
            await raw_reaction_add_check_rules(self, raw_reaction)
            await raw_reaction_add_auto_roles_languages(self, raw_reaction)
            await raw_reaction_add_create_ticket(self, raw_reaction)
            await raw_reaction_add_delete_ticket(self, raw_reaction)
            await raw_reaction_add_end_poll(self, raw_reaction)
            await raw_reaction_add_feedback(self, raw_reaction)
            await raw_reaction_add_report_bug(self, raw_reaction)
        return

    async def on_raw_reaction_remove(self, raw_reaction):
        channel = self.get_channel(raw_reaction.channel_id)
        raw_reaction.message = None
        if channel.guild.me.guild_permissions.read_message_history:
            async for message in channel.history(limit=None):
                if message.id == raw_reaction.message_id:
                    raw_reaction.message = message
                    break
        raw_reaction.member = channel.guild.get_member(raw_reaction.user_id)
        if (raw_reaction.message is not None) and (not raw_reaction.member.bot) and (raw_reaction.message.guild is not None) and (raw_reaction.message.author.id == self.id) and (raw_reaction.message.embeds != []):
            raw_reaction.complete_emoji = self.get_emoji(raw_reaction.emoji.id)
            await raw_reaction_remove_auto_roles(self, raw_reaction)
            await raw_reaction_remove_check_rules(self, raw_reaction)
            await raw_reaction_remove_auto_roles_languages(self, raw_reaction)
            await raw_reaction_remove_feedback(self, raw_reaction)
        return


    # MESSAGE RECU
    async def on_message(self, message):
        if message.author.bot and not message.author.id == self.id:
            if message.channel.id == Ids["Votes"] and message.author.name == "Top.gg":
                member_id = int(message.embeds[0].description.split("ID : ")[1])
                member = message.guild.get_member(member_id)
                vote = int(message.embeds[0].title.split(" ")[1])
                if str(Votes[member_id]) == "None":
                    Votes[member.id] = vote
                else:
                    Votes[member.id] = Votes[member.id] + vote
                json_txt = json.dumps(Votes, sort_keys=True, indent=4)
                def_votes = open("Script/Modifiable_variables/def_votes.json", "w")
                def_votes.write(json_txt)
                def_votes.close()
                await message.channel.send("/show votes")
                return
            else:
                return
        if str(message.channel.type) == "private":
            salon = self.get_channel(Ids["Dm_bot"])
            if message.author.id != self.id:
                await message.author.send("Hello !\nI am a bot, so I cannot answer for your question ! You can ask it in the support server :\nhttps://discord.gg/KQmstPw\n```Default help command : /help \n(you can see it with sending @Clash INFO#3976 on your server)```")
                await salon.send("`" + message.content + "` de :\n" + str(message.author) + " (`" + str(message.author.id) + "`)\nMessage_id : `" + str(message.id) + "`")
            return
        else:
            bot = message.guild.me
        # def Prefix
        global prefix
        try:
            prefix = Prefix[message.guild.id]
        except KeyError:
            prefix = self.default_prefix
        no_prefix = message.content[len(prefix):]
        # test
        if message.content == prefix and (message.author.id == 393317636160618496 or message.author.id in Ids["Creators"]) and (message.guild.id == Ids["Support"] or message.guild.id == 710237092931829893 or message.guild.id == 808814347224481863):
            return
            await member_join(self, message.author)
            await asyncio.sleep(5)
            await member_remove(self, message.author)
            return
            if 0 == 0:
                channel = self.get_channel(Ids["Log_bot"])
                a = 0
                moins = 0
                plus = 0
                reste = 0
                dict = {}
                servs = 76
                async for msg in channel.history(limit=None, oldest_first=True):
                    if msg.content.startswith("The bot has LEFT"):
                        moins += 1
                        servs -= 1
                    elif msg.content.startswith("The bot has JOINED "):
                        plus += 1
                        servs += 1
                    else:
                        reste += 1
                    mydate = msg.created_at
                    monday = mydate - datetime.timedelta(days=mydate.weekday())
                    monday = datetime.date(year=monday.year, month=monday.month, day=monday.day)
                    dict[monday.date().isoformat()] = servs
                    a += 1

                print(servs)
                dates = []
                serv = []
                mois = []
                for date, s in dict.items():
                    date = datetime.date.fromisoformat(date)
                    dates += [date]
                    serv += [s]
                    if not datetime.date(year=date.year, month=date.month, day=1) in mois:
                        mois += [datetime.date(year=date.year, month=date.month, day=1)]
                print(serv)
                json_txt = json.dumps(dict, sort_keys=True, indent=4)
                print(json_txt)
                file = open("Modifiable_variables/def_history.json", "w")
                file.write(json_txt)
                file.close()

                ax = pyplot.gca()
                ax.set_xticks(mois)
                pyplot.title("Servers number evolution")
                xfmt = mdates.DateFormatter("%Y-%m")
                ax.xaxis.set_major_formatter(xfmt)
                pyplot.plot(dates, serv, "r")
                pyplot.xlabel("Date")
                pyplot.ylabel("Nombre de serveurs")
                pyplot.savefig("../Pictures/stats.png")
                file = discord.File("../Pictures/stats.png", filename="stats.png")
                url = "attachment://stats.png"
                embed = self.create_embed_img("titre", "description", message.author.color, "", url)
                await message.channel.send(embed=embed, file=file)
                return
                g = self.get_guild(786225914253934602)
                parts = message.content.split(" ")[1:]
                txt = ""
                for part in parts:
                    txt += part + "    "
                msg = ""
                for i in range(len(txt)):
                    emj = str(discord.utils.get(g.emojis, name=txt[i] + "_"))
                    print(str(emj))
                    if str(emj) != "None":
                        msg += str(emj)
                    else:
                        msg += txt[i]
                print(len(msg))
                await message.channel.send(msg)
                return
        try:
            if bot.nick is not None:
                if message.clean_content == ("@" + bot.nick):
                    embed = self.create_embed("The prefix is `" + prefix + "`", "Put `" + prefix + "help` to get the list of commands.", bot.color, "")
                    await message.channel.send(embed=embed)
            else:
                if message.clean_content == ("@" + bot.name):
                    embed = self.create_embed("The prefix is `" + prefix + "`", "Put `" + prefix + "help` to get the list of commands.", bot.color, "")
                    await message.channel.send(embed=embed)
            if message.content.startswith(prefix):
                message = Msg(message)
                global list_ok
                list_ok = []

                # TEMP
                if no_prefix.startswith("ency"):
                    txt = "Make your researches faster with https://ency.live/"
                    await message.channel.send(txt)
                    return

                # AIDE
                if no_prefix.startswith("help"):
                    await help(message)
                    return

                # CLASH OF CLANS :
                try:
                    # bases
                    if no_prefix.startswith("base"):
                        await message.channel.trigger_typing()
                        await message.channel.send("This command is not yet available")
                        return
                    # player
                    if no_prefix.startswith("player"):
                        try:
                            tag = message.content.split(" ")[1]
                            information = "main"
                            await get_player(message, tag, information)
                        except IndexError:
                            embed = self.create_embed("Syntax Error", "You did not enter the tag of the player after the command.\n> Example : `" + prefix + "player #PlayerTag`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        return
                    # search player
                    if no_prefix.startswith("search player"):
                        await message.channel.trigger_typing()
                        await message.channel.send("This command is unavailable because the API does not allow it, but maybe later !")
                        return
                    # clan
                    if no_prefix.startswith("clan"):
                        try:
                            tag = message.content.split(" ")[1]
                            await get_clan(message, tag)
                        except IndexError:
                            embed = self.create_embed("Syntax Error", "You did not enter the tag of the clan after the command.\n> Example : `" + prefix + "clan #ClanTag`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        return
                    # search clan
                    if no_prefix.startswith("search clan"):
                        name1 = message.content.split(" ")[2:]
                        if name1 == []:
                            embed = self.create_embed("Syntax Error", "You did not enter the name of the clan after the command.\n> Example : `" + prefix + "search clan Clan Name 5`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        name1 = name1[:len(name1) - 1]
                        name = ""
                        for part in name1:
                            name += part + " "
                        name = name[:len(name) - 1]
                        try:
                            if int(message.content.split(" ")[len(message.content.split(" ")) - 1]) <= 0:
                                embed = self.create_embed("Syntax Error", "You must enter a positive number of clans to show after the command.\n> Example : `" + prefix + "search clan Clan Name 5`", 0xff0000, "")
                                await message.channel.send(embed=embed)
                                return
                            if int(message.content.split(" ")[len(message.content.split(" ")) - 1]) <= 10:
                                number = int(message.content.split(" ")[len(message.content.split(" ")) - 1])
                            else:
                                number = 10
                                await message.channel.send("I can only show 10 clans to avoid spam.")
                            await search_clan(message, name, number)
                        except ValueError:
                            embed = self.create_embed("Syntax Error", "You did not enter the number of clans to show after the command.\n> Example : `" + prefix + "search clan Clan Name 5`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        return
                    # members list (from a clan)
                    if no_prefix.startswith("members"):
                        try:
                            tag = message.content.split(" ")[1]
                            await clan_members(message, tag)
                        except IndexError:
                            embed = self.create_embed("Syntax Error", "You did not enter the tag of the clan after the command.\n> Example : `" + prefix + "members #ClanTag`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        return
                    # th
                    if no_prefix.startswith("th"):
                        try:
                            level = int(message.content.split(" ")[1])
                        except IndexError:
                            level = 0
                        except ValueError:
                            embed = self.create_embed("Syntax Error", "Please give a valid TH level. You can also enter just `" + prefix + "th` and click on the emoji which match with your TH level.\n> Example : `" + prefix + "th 13`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        await buildings_th(message, level)
                        return
                    # bh
                    if no_prefix.startswith("bh"):
                        try:
                            level = int(message.content.split(" ")[1])
                        except IndexError:
                            level = 0
                        except ValueError:
                            embed = self.create_embed("Syntax Error", "Please give a valid BH level. You can also enter just `" + prefix + "bh` and click on the emoji which match with your BH level.\n> Example : `" + prefix + "bh 9`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        await buildings_bh(message, level)
                        return
                    # coc
                    if no_prefix.startswith("coc"):
                        await coc_file(message)
                        return
                except coc.errors.Maintenance:
                    await message.channel.send("Service Unavailable : API is currently in maintenance, please come back later !")
                    return

                # MODERATION :
                # vide
                if no_prefix.startswith("delete"):
                    try:
                        which = str(message.content.split(" ")[1])
                        if which == "all":
                            await delete_messages_all(message)
                        else:
                            if which == "time":
                                minutes = int(message.content.split(" ")[2])
                                await delete_messages_time(message, minutes)
                            else:
                                try:
                                    nb_msg = int(message.content.split(" ")[1])
                                except ValueError:
                                    embed = self.create_embed("Syntax Error", "You did not enter the number of messages, the word \"all\" or the word \"time\" with the wished time after the command.\n> Examples : `" + prefix + "delete 5` ; `" + prefix + "delete all` ; `" + prefix + "delete time 5`", 0xff0000, "")
                                    await message.channel.send(embed=embed)
                                    return
                                if nb_msg <= -1:
                                    embed = self.create_embed("Error", "You cannot delete a negative number of messages", 0xff0000, "")
                                    await message.channel.send(embed=embed)
                                    return
                                await delete_messages_number(message, nb_msg)
                    except IndexError:
                        embed = self.create_embed("Syntax Error", "You did not enter the number of messages, the word \"all\" or the word \"time\" with the wished time after the command.\n> Examples : `" + prefix + "delete 5` ; `" + prefix + "delete all` ; `" + prefix + "delete time 5`", 0xff0000, "")
                        await message.channel.send(embed=embed)
                        return
                    return


                # UTILITAIRE :

                EVERYONE = (
                    "add",
                    "embed",
                    "emoji info",
                    "invite",
                    "ping",
                    "poll",
                    "promote",
                    "role info",
                    "server info",
                    "support",
                    "yt"
                )
                if no_prefix.startswith(EVERYONE):
                    await message.channel.trigger_typing()

                    if no_prefix.startswith("add") or message.content.startswith(prefix + "invite"):
                        await add_the_bot_default(message)
                        return

                    if no_prefix.startswith("embed"):
                        embed = discord.Embed()
                        embed.title = "title"
                        embed.description = "description"
                        embed.colour = 0x00ffff
                        embed.set_footer(text="footer\n\nDefault help command : /help", icon_url=message.author.avatar_url)
                        embed.set_image(url=message.author.avatar_url)
                        embed.set_thumbnail(url=message.author.avatar_url)
                        embed.set_author(name="author", icon_url=message.author.avatar_url)
                        await message.channel.send(embed=embed)
                        return

                    if no_prefix.startswith("emoji info"):
                        try:
                            emoji = message.content.split(":")[1]
                        except IndexError:
                            embed = self.create_embed("Syntax Error", f"You did not enter the emoji after the command.\n> Examples : `{prefix}emoji info `{Emojis['Emoji_ghost']}", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        await emoji_info(message, emoji)
                        return

                    if no_prefix.startswith("ping"):
                        await ping(message, self.latency)
                        return

                    if no_prefix.startswith("poll"):
                        name = message.content.split(" ")[1:]
                        title = ""
                        for part in name:
                            title += part + " "
                        await poll(message, title)
                        return

                    if no_prefix.startswith("promote"):
                        await promote_the_bot(message)
                        return

                    if no_prefix.startswith("role info"):
                        if message.role_mentions == []:
                            embed = self.create_embed("Syntax Error", "You did not mention any role after the command.\n> Example : `" + prefix + "role info @Role`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        else:
                            for role in message.role_mentions:
                                await role_info(message, role)
                        return

                    if no_prefix.startswith("server info"):
                        await server_info(message)
                        return

                    if no_prefix.startswith("support"):
                        await support_server(message)
                        return

                    if no_prefix.startswith("yt"):
                        await youtube(message)
                        return


                MANAGE_CHANNEL = (
                    "close"
                )
                if no_prefix.startswith(MANAGE_CHANNEL):
                    await message.channel.trigger_typing()
                    if message.author.guild_permissions.manage_channels:

                        if no_prefix.startswith("close"):
                            await close_ticket(message, message.channel)
                            return

                    else:
                        embed = self.create_embed("You cannot do this action", "You are not allowed to manage channels.", 0xff8000, "")
                        await message.channel.send(embed=embed)
                        return

                ADMIN = (
                    "prefix",
                    "roles TH",
                    "roles BH",
                    "roles league",
                    "ticket"
                )
                if no_prefix.startswith(ADMIN):
                    await message.channel.trigger_typing()
                    if message.author.guild_permissions.administrator:

                        if no_prefix.startswith("prefix"):
                            try:
                                new = message.content.split(" ")[1]
                                while new.startswith(" "):
                                    new = new[1:]
                                Prefix[message.author.guild.id] = new
                                embed = self.create_embed("Prefix changed", "The new prefix is : `" + new + "`", bot.color, "")
                                await message.channel.send(embed=embed)
                                json_txt = json.dumps(Prefix, sort_keys=True, indent=4)
                                def_prefix = open("Script/Modifiable_variables/def_prefix.json", "w")
                                def_prefix.write(json_txt)
                                def_prefix.close()
                            except IndexError:
                                embed = self.create_embed("Syntax Error", "You did not enter the new prefix after the command.\n> Example : `" + prefix + "prefix /`", 0xff0000, "")
                                await message.channel.send(embed=embed)
                                return
                            return

                        if no_prefix.startswith("roles TH"):
                            await auto_roles_th(message, message.channel)
                            return

                        if no_prefix.startswith("roles BH"):
                            await auto_roles_bh(message, message.channel)
                            return

                        if no_prefix.startswith("roles league"):
                            await auto_roles_leagues(message, message.channel)
                            return

                        if no_prefix.startswith("ticket"):
                            for salon in message.guild.text_channels:
                                if salon.name == "tickets":
                                    embed = self.create_embed("Error", "There is already a channel " + salon.mention, 0xff0000, "")
                                    await message.channel.send(embed=embed)
                                    return
                            bout = message.content.split("|")[0]
                            bout = bout.split(" ")[1:]
                            msg = ""
                            for part in bout:
                                msg += part + " "
                            if msg == "":
                                msg = "Click on " + str(Emojis["Ticket"]) + " to create a ticket"
                            await tickets(message, msg, message.channel, None)
                            return

                    else:
                        embed = self.create_embed("You cannot do this action", "You are not allowed to do this action. Only administrators of this server can do this action.", 0xff8000, "")
                        await message.channel.send(embed=embed)
                        return

                CREATORS = (
                    "answer",
                    "refresh History",
                    "say",
                    "show votes"
                )
                if no_prefix.startswith(CREATORS):
                    await message.channel.trigger_typing()
                    if message.author.id in Ids["Creators"]:

                        if no_prefix.startswith("answer"):
                            channel = self.get_channel(message.reference.channel_id)
                            async for msg in channel.history(limit=None):
                                if msg.id == message.reference.message_id:
                                    user_id = int(msg.content.split("`")[len(msg.content.split("`")) - 4])
                                    msg_id = int(msg.content.split("`")[len(msg.content.split("`")) - 2])
                                    user = self.get_user(user_id)
                                    text = "ok"
                                    dm = await user.create_dm()
                                    async for msg in dm.history(limit=None):
                                        if msg.id == msg_id:
                                            await msg.reply(text)
                                            return
                            await message.channel.send("Unknown message")
                            return

                        if no_prefix.startswith("refresh History"):
                            channel = self.get_channel(Ids["Log_bot"])
                            a = 0
                            moins = 0
                            plus = 0
                            reste = 0
                            dict = {}
                            servs = 76
                            async for msg in channel.history(limit=None, oldest_first=True):
                                if msg.content.startswith("The bot has LEFT"):
                                    moins += 1
                                    servs -= 1
                                elif msg.content.startswith("The bot has JOINED "):
                                    plus += 1
                                    servs += 1
                                else:
                                    reste += 1
                                monday = msg.created_at - datetime.timedelta(days=msg.created_at.weekday())
                                monday = datetime.date(year=monday.year, month=monday.month, day=monday.day)
                                if not monday.isoformat() in list(dict.keys()):
                                    dict[monday.isoformat()] = servs
                                a += 1
                            global History
                            History = dict
                            json_txt = json.dumps(History, sort_keys=True, indent=4)
                            await message.channel.send(json_txt)
                            months = []
                            servers = []
                            dates = []
                            for date, servers_nb in History.items():
                                date = datetime.date.fromisoformat(date)
                                date_month = datetime.date(year=date.year, month=date.month, day=1)
                                if not date_month in months:
                                    months += [date_month]
                                dates += [date]
                                servers += [servers_nb]
                            ax = pyplot.gca()
                            ax.set_xticks(months)
                            pyplot.title("Servers number evolution")
                            xfmt = mdates.DateFormatter("%Y-%m")
                            ax.xaxis.set_major_formatter(xfmt)
                            pyplot.plot(dates, servers, "r")
                            pyplot.xlabel("Date")
                            pyplot.ylabel("Servers number")
                            pyplot.savefig("../Pictures/stats.png")
                            file = discord.File("../Pictures/stats.png", filename="stats.png")
                            url = "attachment://stats.png"
                            embed = self.create_embed_img("Clash INFO", "Clash INFO Stats", bot.color, "", url)
                            await message.channel.send(embed=embed, file=file)
                            return

                        if no_prefix.startswith("say"):
                            bout = message.content
                            bout = bout.split(" ")[1:]
                            msg = ""
                            for part in bout:
                                msg += part + " "
                            await message.channel.send(msg)
                            await message.delete()
                            return

                        if no_prefix.startswith("show votes"):
                            vote_copy = Votes
                            vote = {}
                            txt = "```\n{\n"
                            for k, v in vote_copy.items():
                                member = self.get_user(int(k))
                                vote[member.name + "#" + member.discriminator + " (" + k + ")"] = v
                            vote = sorted(vote.items(), key=lambda t: t[1])
                            for tuple in vote:
                                txt += f"\t{tuple[0]} : {tuple[1]},\n"
                            txt += "}\n```"
                            await message.channel.send(txt)
                            return

                if message.guild.id == Ids["Support"]:
                    # perms mute
                    if message.content.startswith(prefix + "upmute"):
                        await message.channel.trigger_typing()
                        mute = discord.utils.get(message.guild.roles, name="Muted")
                        overwrite = {mute: discord.PermissionOverwrite(send_messages=False)}
                        for channel in message.guild.channels:
                            x = channel.overwrites
                            x.update(overwrite)
                            await channel.edit(overwrites=x)
                        await message.channel.send("Les permissions du rôle " + mute.mention + " ont été mises à jour.")
                        return
                    # suggestion
                    if message.content.startswith(prefix + "sugg"):
                        await message.channel.trigger_typing()
                        channel = self.get_channel(Ids["Suggestion"])
                        msg = message.content.split(" ")[1:]
                        content = ""
                        for part in msg:
                            content += " " + part
                        embed = self.create_embed("Suggestion from " + message.author.name + " (" + str(message.author.id) + ")", content, message.author.color, "")
                        a = await channel.send(embed=embed)
                        await a.add_reaction(Emojis["Yes"])
                        await a.add_reaction(Emojis["No"])
                        await message.channel.send("Your suggestion was sent")
                        return
                    # bug
                    if message.content.startswith(prefix + "bug"):
                        await message.channel.trigger_typing()
                        channel = self.get_channel(Ids["Bug"])
                        msg = message.content.split(" ")[1:]
                        content = ""
                        for part in msg:
                            content += " " + part
                        embed = self.create_embed("Bug report by " + message.author.name + " (" + str(message.author.id) + ")", content, message.author.color, "")
                        a = await channel.send(embed=embed)
                        await a.add_reaction(Emojis["Yes"])
                        await a.add_reaction(Emojis["No"])
                        await message.channel.send("Your bug report was sent")
                        return
                    # reglement
                    if message.content.startswith(prefix + "rules"):
                        await message.channel.trigger_typing()
                        sugg = self.get_channel(Ids["Suggestion_chat"])
                        bug = self.get_channel(Ids["Bug_chat"])
                        test01 = self.get_channel(Ids["Test_channel_1"])
                        test02 = self.get_channel(Ids["Test_channel_2"])
                        test03 = self.get_channel(Ids["Test_channel_3"])
                        auto_roles = self.get_channel(722020813259276378)
                        clash_info = self.get_channel(741278417130881024)
                        support = self.get_channel(719826409987768392)
                        tickets_channel = self.get_channel(767418391559929906)
                        put_bot = self.get_channel(722025320202633323)
                        feedback = self.get_channel(719827869295050812)
                        guild = self.get_guild(Ids["Support"])
                        bot_creator = discord.utils.get(guild.roles, id=719538013859872880)
                        bot_staff = discord.utils.get(guild.roles, id=743796789769142354)
                        embed = self.create_embed("Welcome in the Support server for Clash INFO !",
                                                  f"Welcome ! Here is the support server of the {bot.mention} bot.\n\n{Emojis['Yes']} You can : {Emojis['Yes']}\n- Take your roles : {auto_roles.mention}\n- Follow the channel {clash_info.mention} to informe all your server about bot updates\n- Ask a question about the bot : {support.mention}\n- Take a ticket to speak with us : {tickets_channel.mention}\n- Send us a suggestion : {sugg.mention}\n- Notify us of a bug : {bug.mention}\n- Test the bot : {test01.mention}, {test02.mention}, {test03.mention}\n- Put the bot on your server : {put_bot.mention}\n- Rate the BOT : {feedback.mention}\n\n⚠️ You must : ⚠️\n- Respect the Discord ToS (https://discord.com/new/terms) and the Discord Guidelines (https://discord.com/new/guidelines)\n- Respect the language of each channel (with the flag emoji in the channel name). Default = English ONLY\n\n{Emojis['No']} You cannot : {Emojis['No']}\n- Put `| Clash INFO` after your name or `[role]` before your name without authorization from an {bot_creator.mention}\n- Put the same profile picture or name as an {bot_staff.mention}\n\nClick on {Emojis['Yes']} to access the whole server.",
                                                  0x00ff00, "")
                        a = await message.channel.send(embed=embed)
                        await a.add_reaction(Emojis["Yes"])
                        return
                    # auto-roles
                    if message.content == prefix + "auto-roles langues" and message.author.id in Ids["Creators"]:
                        await message.channel.trigger_typing()
                        await message.delete()
                        msg = ""
                        for emoji, name in Emojis["Languages_emojis"].items():
                            langue = discord.utils.get(message.guild.roles, name=name)
                            msg += str(emoji) + " if you speak " + langue.mention + "\n"
                        embed = self.create_embed("Click on the emojis to get the matching roles", msg, bot.color, "")
                        a = await message.channel.send(embed=embed)
                        for emoji in Emojis["Languages_emojis"].keys():
                            await a.add_reaction(emoji)
                        return
                    # noter
                    if message.content.startswith(prefix + "note"):
                        await message.channel.trigger_typing()
                        embed = self.create_embed("How do you like this bot ? Put a mark from 0 to 9 (0 is the worst and 9 is the best).", "", bot.color, "")
                        a = await message.channel.send(embed=embed)
                        await message.delete()
                        await a.add_reaction("0️⃣")
                        await a.add_reaction("1️⃣")
                        await a.add_reaction("2️⃣")
                        await a.add_reaction("3️⃣")
                        await a.add_reaction("4️⃣")
                        await a.add_reaction("5️⃣")
                        await a.add_reaction("6️⃣")
                        await a.add_reaction("7️⃣")
                        await a.add_reaction("8️⃣")
                        await a.add_reaction("9️⃣")
                        return

                # mentions
                if message.mention_everyone:
                    for member in message.guild.members:
                        if await self.mention(message, member) == -1:
                            return
                if message.mentions:
                    for member in message.mentions:
                        if not str(member) in list_ok:
                            list_ok.append(str(member))
                            if await self.mention(message, member) == -1:
                                return
                if message.role_mentions:
                    for role in message.role_mentions:
                        for member in role.members:
                            if not str(member) in list_ok:
                                list_ok.append(str(member))
                                if await self.mention(message, member) == -1:
                                    return

        except discord.errors.Forbidden:
            if message.channel.permissions_for(bot).send_messages and message.channel.permissions_for(bot).embed_links:
                embed = self.create_embed("The bot cannot do this action !", "Please check its permissions.", 0xff0000, "")
                await message.channel.send(embed=embed)
                return
            elif message.channel.permissions_for(bot).send_messages and not message.channel.permissions_for(bot).embed_links:
                await message.channel.send("The bot cannot do this action !\nPlease give the permission \"Embed Links\" to the bot")
                return
            elif not message.channel.permissions_for(bot).send_messages:
                embed = self.create_embed("The bot cannot send messages in this channel !", "Please check its permissions.", 0xff0000, "")
                await message.author.send(embed=embed)
                return
        except TimeoutError:
            embed = self.create_embed("Timeout Error", "Please try again later", 0xff0000, "")
            await message.channel.send(embed=embed)
            print("timeout error", message.created_at)
            return
        return

    # MENTIONS
    async def mention(self, message, member):
        try:
            # CLASH OF CLANS

            # MODERATION

            # USEFUL
            # member info
            if message.content.startswith(prefix + "member info"):
                await member_info(message, member)
                return
            # message privé
            if message.content.startswith(prefix + "dm"):
                await message.channel.trigger_typing()
                try:
                    if message.author.guild_permissions.administrator or (message.role_mentions == [] and message.mention_everyone == 0):
                        if not member.bot:
                            msg = message.content.split("|")[1]
                            if msg == "":
                                embed = self.create_embed("Syntax Error", "You did not enter the text after the |.\n> Example : `" + prefix + "dm @user |Text`", 0xff0000, "")
                                await message.channel.send(embed=embed)
                                return
                            await member.send(msg + "\n*Sent by " + str(message.author) + " (" + str(message.author.id) + ")*")
                            embed = self.create_embed(member.name, "This member has received the message.", member.color, "")
                            await message.channel.send(embed=embed)
                    else:
                        embed = self.create_embed("You cannot do this action", "You are not allowed to send direct message to @everyone or a role. You must be an administrator", 0xff8000, "")
                        await message.channel.send(embed=embed)
                        return -1

                except discord.Forbidden:
                    embed = self.create_embed(member.name, "This member do not want to receive direct message from this server.", member.color, "")
                    await message.channel.send(embed=embed)
                    return
                except IndexError:
                    embed = self.create_embed("Syntax Error", "You did not enter the | after the command.\n> Example : `" + prefix + "dm @user |Text`", 0xff0000, "")
                    await message.channel.send(embed=embed)
                    return
                return

            if message.guild.id == Ids["Support"]:
                # muet
                if message.content.startswith(prefix + "mute"):
                    await message.channel.trigger_typing()
                    if message.author.guild_permissions.manage_roles or message.author.guild_permissions.manage_permissions:
                        muted = discord.utils.get(member.guild.roles, name="Muted")
                        await member.add_roles(muted)
                        embed = self.create_embed(member.name, "This member has been muted", member.color, "")
                        await message.channel.send(embed=embed)
                    else:
                        embed = self.create_embed("You cannot do this action", "You are not allowed to mute a member.", 0xff8000, "")
                        await message.channel.send(embed=embed)
                        return
                    return
                # muet enlever
                if message.content.startswith(prefix + "unmute"):
                    await message.channel.trigger_typing()
                    if message.author.guild_permissions.manage_roles or message.author.guild_permissions.manage_permissions:
                        muted = discord.utils.get(member.guild.roles, name="Muted")
                        await member.remove_roles(muted)
                        embed = self.create_embed(member.name, "This member has been unmuted", member.color, "")
                        await message.channel.send(embed=embed)
                    else:
                        embed = self.create_embed("You cannot do this action", "You are not allowed to mute a member.", 0xff8000, "")
                        await message.channel.send(embed=embed)
                        return
                    return
                # muet temporaire
                if message.content.startswith(prefix + "tempmute"):
                    await message.channel.trigger_typing()
                    x = message.content.split(" ")[2]
                    if message.author.guild_permissions.manage_roles or message.author.guild_permissions.manage_permissions:
                        muted = discord.utils.get(member.guild.roles, name="Muted")
                        await member.add_roles(muted)
                        embed = self.create_embed(member.name, "This member has been muted", member.color, "")
                        await message.channel.send(embed=embed)
                        x = float(x) * 60
                        await asyncio.sleep(x)
                        await member.remove_roles(muted)
                        embed = self.create_embed(member.name, "This member has been unmuted", member.color, "")
                        await message.channel.send(embed=embed)
                    else:
                        embed = self.create_embed("You cannot do this action", "You are not allowed to mute a member.", 0xff8000, "")
                        await message.channel.send(embed=embed)
                        return
                    return

        except discord.errors.Forbidden:
            embed = self.create_embed("The bot cannot do this action !", "Please check its permissions.", 0xff0000, "")
            await message.channel.send(embed=embed)
        return


async def ascii(image):
    # --lettres_taux_noir--
    IMAGE_WIDTH = 60
    IMAGE_HEIGHT = 100
    font = ImageFont.truetype("../ttf/JetBrainsMono-Regular.ttf", 100)
    characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    char = {}
    for i in characters:
        im = Image.new("L", (IMAGE_WIDTH, IMAGE_HEIGHT), (0))
        draw = ImageDraw.Draw(im)
        text_width, text_height = draw.textsize(i, font=font)
        x = (IMAGE_WIDTH - text_width) // 2
        y = (IMAGE_HEIGHT - text_height) // 2 - 10
        draw.text((x, y), i, fill=(255), font=font)
        white = 0
        black = 0
        for px in list(im.getdata()):
            if px < 128:
                black += 1
            if px >= 128:
                white += 1
        coef = 2
        char[i] = coef * white / (white + black)
    char = sorted(char.items(), key=lambda t: t[1])
    print(char)
    width = 180
    height = 30
    image = image.resize((width, height))
    img = ImageDraw.Draw(image)

    position = 0
    final = []
    for y in range(height):
        final.append([])
        for x in range(width):
            final[y].append([])
    for px in list(image.getdata()):
        x = position % image.width
        y = position // image.width
        grey = int(px[0] * 299 / 1000 + px[1] * 587 / 1000 + px[2] * 114 / 1000)
        final[y][x] = (grey, grey, grey)
        position += 1
    msg = ""
    for line in final:
        for px in line:
            for letter in char:
                if (px[0] / 255) <= letter[1]:
                    msg += letter[0]
                    break
                if (px[0] / 255) > char[len(char) - 1][1]:
                    msg += char[len(char) - 1][0]
                    break
        msg += "\n"
    print(msg)
