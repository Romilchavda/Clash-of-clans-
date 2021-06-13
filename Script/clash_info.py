# ----- PACKAGES : -----
import coc
import json
import asyncio


# ----- PROJECT FILES : -----
from Script.import_functions import *


# ----- COMMANDS : -----

# ON_READY
from Script.Commands.On_Ready.ready_loop import ready_loop

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

from Script.Commands.Messages.Useful.github import github
from Script.Commands.Messages.Useful.tickets import tickets, close_ticket
from Script.Commands.Messages.Useful.member_info import member_info
from Script.Commands.Messages.Useful.role_info import role_info
from Script.Commands.Messages.Useful.server_info import server_info
from Script.Commands.Messages.Useful.emoji_info import emoji_info
from Script.Commands.Messages.Useful.poll import poll
from Script.Commands.Messages.Useful.ping import ping
from Script.Commands.Messages.Useful.add_the_bot import add_the_bot_default
from Script.Commands.Messages.Useful.support_server import support_server
from Script.Commands.Messages.Useful.promote_the_bot import promote_the_bot
from Script.Commands.Messages.Useful.youtube import youtube

from Script.Commands.Messages.Moderation.delete_messages import delete_messages_number, delete_messages_time, delete_messages_all


# CONST VARIABLES
from Script.import_emojis import Emojis
from Data.Const_variables.import_const import Ids


# MODIFIABLE VARIABLES
from Data.Modifiable_variables.import_var import Prefix, Votes


# This allow us to use discord.message.Message and discord_slash.context.SlashContext with the same functions :
async def send(self, *args, **kwargs):
    only_discord_slash = ["hidden"]
    for kwarg in dict(kwargs):
        if kwarg in only_discord_slash:
            kwargs.pop(kwarg)
    return await self.channel.send(*args, **kwargs)
async def defer(self, *args, **kwargs):
    pass
setattr(discord.message.Message, "send", send)
setattr(discord.message.Message, "defer", defer)


class Bot(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.default_prefix = None
        self.id = None


    async def on_dbl_vote(self, data):
        print(data)
        print("clash_info.py")


    # READY
    async def on_ready(self):
        from Script.Clients.top_gg import Dbl_client
        Dbl_client.bot = self
        await ready_loop(self)


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
        used_emojis = [Emojis["Yes"], Emojis["Yes"], list(Emojis["Numbers"].values()), Emojis["End"], Emojis["Delete"], Emojis["Ticket"], list(Emojis["Languages_emojis"].values()), Emojis["Yes"], list(Emojis["Th_emojis"].keys()), list(Emojis["Bh_emojis"].keys()), list(Emojis["League_emojis"].keys())]
        go = False
        for obj in used_emojis:
            if (type(obj) is list) and (raw_reaction.emoji in obj):
                go = True
            elif (type(obj) is dict) and (raw_reaction.emoji in list(obj.keys())):
                go = True
            elif raw_reaction == obj:
                go = True
        if not go:
            return

        channel = self.get_channel(raw_reaction.channel_id)
        if not channel.permissions_for(channel.guild.me).read_message_history:
            if channel.permissions_for(channel.guild.me).send_messages:
                await channel.send("Sorry, I don't have the `read messages history` permission")
            else:
                pass
            return
        raw_reaction.message = None
        try:
            async for message in channel.history(limit=100):
                if message.id == raw_reaction.message_id:
                    raw_reaction.message = message
                    break
        except Exception as e:
            print("Error Raw Reaction ADD : ", e)
            return
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
        used_emojis = [Emojis["Yes"], Emojis["Yes"], list(Emojis["Numbers"].values()), Emojis["End"], Emojis["Delete"], Emojis["Ticket"], list(Emojis["Languages_emojis"].values()), Emojis["Yes"], list(Emojis["Th_emojis"].keys()), list(Emojis["Bh_emojis"].keys()), list(Emojis["League_emojis"].keys())]
        go = False
        for obj in used_emojis:
            if (type(obj) is list) and (raw_reaction.emoji in obj):
                go = True
            elif (type(obj) is dict) and (raw_reaction.emoji in list(obj.keys())):
                go = True
            elif raw_reaction == obj:
                go = True
        if not go:
            return

        channel = self.get_channel(raw_reaction.channel_id)
        if not channel.guild.me.guild_permissions.read_message_history:
            await channel.send("Sorry, I don't have the `read messages history` permission")
            return
        raw_reaction.message = None
        try:
            async for message in channel.history(limit=100):
                if message.id == raw_reaction.message_id:
                    raw_reaction.message = message
                    break
        except Exception as e:
            print("Error Raw Reaction REMOVE : ", e)
        raw_reaction.member = channel.guild.get_member(raw_reaction.user_id)
        if (raw_reaction.message is not None) and (raw_reaction.member is not None) and (not raw_reaction.member.bot) and (raw_reaction.message.guild is not None) and (raw_reaction.message.author.id == self.id) and (raw_reaction.message.embeds != []):
            raw_reaction.complete_emoji = self.get_emoji(raw_reaction.emoji.id)
            await raw_reaction_remove_auto_roles(self, raw_reaction)
            await raw_reaction_remove_check_rules(self, raw_reaction)
            await raw_reaction_remove_auto_roles_languages(self, raw_reaction)
            await raw_reaction_remove_feedback(self, raw_reaction)
        return


    # RECEIVED MESSAGE
    async def on_message(self, message):
        if message.author.bot and message.author.id != self.id:
            if message.channel.id == Ids["Votes"] and message.author.name == "Top.gg":
                member_id = int(message.embeds[0].description.split("ID : ")[1])
                member = self.get_user(member_id)
                vote = int(message.embeds[0].title.split(" ")[1])
                if member_id not in list(Votes.keys()):
                    Votes[member.id] = vote
                else:
                    Votes[member.id] += vote
                json_txt = json.dumps(Votes, sort_keys=True, indent=4)
                def_votes = open("Data/Modifiable_variables/votes.json", "w")
                def_votes.write(json_txt)
                def_votes.close()
                vote_copy = dict(Votes)
                vote = {}
                for member_id, member_votes in vote_copy.items():
                    member = self.get_user(int(member_id))
                    vote[member.mention] = member_votes
                vote = sorted(vote.items(), key=lambda t: t[1])
                txt = ""
                for tuple in vote:
                    txt += f"{tuple[0]} have voted {tuple[1]} times !\n"
                embed = create_embed("Votes for Clash INFO", txt, message.guild.me.color, "", message.guild.me.avatar_url)
                await message.channel.send(embed=embed)
                return
            else:
                return
        if str(message.channel.type) == "private":
            salon = self.get_channel(Ids["Dm_bot"])
            if message.author.id != self.id:
                await message.author.send("Hello !\nI am a bot, so I cannot answer for your question ! You can ask it in the support server :\nhttps://discord.gg/KQmstPw\n```Default help command : /help \n(you can see it with sending @Clash INFO#3976 on your server)```")
                await salon.send(f"`{message.content}` de :\n{message.author} (`{message.author.id}`)\nMessage_id : `{message.id}`")
            return
        else:
            bot = message.guild.me
        # def Prefix
        global prefix
        if message.guild.id in list(Prefix.keys()):
            prefix = Prefix[message.guild.id]
        else:
            prefix = self.default_prefix
        no_prefix = message.content[len(prefix):]
        # test
        if message.content == prefix and (message.author.id == 393317636160618496 or message.author.id in Ids["Creators"]) and (message.guild.id == Ids["Support_server"] or message.guild.id == 710237092931829893 or message.guild.id == 808814347224481863):
            for guild in self.guilds:
                for channel in guild.channels:
                    if channel.name == "tickets" and type(channel) == discord.TextChannel:
                        async for message in channel.history(limit=None):
                            if message.embeds:
                                if message.author == guild.me and message.embeds[0].title == "Ticket :":
                                    for reaction in message.reactions:
                                        await reaction.clear()
                                    await message.add_reaction(Emojis["Ticket"])
                                    print(message.embeds[0].description)
                                    print(message.embeds[0].description.startswith == "Click on " and "to create a ticket" in message.embeds[0].description)
                                    if message.embeds[0].description.startswith == "Click on " and "to create a ticket" in message.embeds[0].description:
                                        embed = message.embeds[0]
                                        embed.description = "Click on "+Emojis["Ticket"]+" to create a ticket"
                                        await message.edit(embed=embed)
            from Script.Clients.top_gg import Dbl_client
            print("GO")
            r = await Dbl_client.get_user_vote(message.author.id)
            print(r)
            r = await Dbl_client.get_bot_votes()
            print(r)
            print("FINISH")
            return
        try:
            if bot.nick is not None:
                if message.clean_content == ("@" + bot.nick):
                    embed = create_embed(f"The prefix is `{prefix}`", f"Put `{prefix}help` to get the list of commands.", bot.color, "", message.guild.me.avatar_url)
                    await message.channel.send(embed=embed)
            else:
                if message.clean_content == ("@" + bot.name):
                    embed = create_embed(f"The prefix is `{prefix}`", f"Put `{prefix}help` to get the list of commands.", bot.color, "", message.guild.me.avatar_url)
                    await message.channel.send(embed=embed)
            if message.content.startswith(prefix):

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
                            embed = create_embed("Syntax Error", "You did not enter the tag of the player after the command.\n> Example : `" + prefix + "player #PlayerTag`", 0xff0000, "", message.guild.me.avatar_url)
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
                            embed = create_embed("Syntax Error", "You did not enter the tag of the clan after the command.\n> Example : `" + prefix + "clan #ClanTag`", 0xff0000, "", message.guild.me.avatar_url)
                            await message.channel.send(embed=embed)
                            return
                        return
                    # search clan
                    if no_prefix.startswith("search clan"):
                        name1 = message.content.split(" ")[2:]
                        if not name1:
                            embed = create_embed("Syntax Error", "You did not enter the name of the clan after the command.\n> Example : `" + prefix + "search clan Clan Name 5`", 0xff0000, "", message.guild.me.avatar_url)
                            await message.channel.send(embed=embed)
                            return
                        name1 = name1[:len(name1) - 1]
                        name = ""
                        for part in name1:
                            name += part + " "
                        name = name[:len(name) - 1]
                        try:
                            if int(message.content.split(" ")[len(message.content.split(" ")) - 1]) <= 0:
                                embed = create_embed("Syntax Error", "You must enter a positive number of clans to show after the command.\n> Example : `" + prefix + "search clan Clan Name 5`", 0xff0000, "", message.guild.me.avatar_url)
                                await message.channel.send(embed=embed)
                                return
                            if int(message.content.split(" ")[len(message.content.split(" ")) - 1]) <= 10:
                                number = int(message.content.split(" ")[len(message.content.split(" ")) - 1])
                            else:
                                number = 10
                                await message.channel.send("I can only show 10 clans to avoid spam.")
                            await search_clan(message, name, number)
                        except ValueError:
                            embed = create_embed("Syntax Error", "You did not enter the number of clans to show after the command.\n> Example : `" + prefix + "search clan Clan Name 5`", 0xff0000, "", message.guild.me.avatar_url)
                            await message.channel.send(embed=embed)
                            return
                        return
                    # members list (from a clan)
                    if no_prefix.startswith("members"):
                        try:
                            tag = message.content.split(" ")[1]
                            await clan_members(message, tag)
                        except IndexError:
                            embed = create_embed("Syntax Error", "You did not enter the tag of the clan after the command.\n> Example : `" + prefix + "members #ClanTag`", 0xff0000, "", message.guild.me.avatar_url)
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
                            embed = create_embed("Syntax Error", "Please give a valid TH level. You can also enter just `" + prefix + "th` and click on the emoji which match with your TH level.\n> Example : `" + prefix + "th 13`", 0xff0000, "", message.guild.me.avatar_url)
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
                            embed = create_embed("Syntax Error", "Please give a valid BH level. You can also enter just `" + prefix + "bh` and click on the emoji which match with your BH level.\n> Example : `" + prefix + "bh 9`", 0xff0000, "", message.guild.me.avatar_url)
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
                                    embed = create_embed("Syntax Error", "You did not enter the number of messages, the word \"all\" or the word \"time\" with the wished time after the command.\n> Examples : `" + prefix + "delete 5` ; `" + prefix + "delete all` ; `" + prefix + "delete time 5`", 0xff0000, "", message.guild.me.avatar_url)
                                    await message.channel.send(embed=embed)
                                    return
                                if nb_msg <= -1:
                                    embed = create_embed("Error", "You cannot delete a negative number of messages", 0xff0000, "", message.guild.me.avatar_url)
                                    await message.channel.send(embed=embed)
                                    return
                                await delete_messages_number(message, nb_msg)
                    except IndexError:
                        embed = create_embed("Syntax Error", "You did not enter the number of messages, the word \"all\" or the word \"time\" with the wished time after the command.\n> Examples : `" + prefix + "delete 5` ; `" + prefix + "delete all` ; `" + prefix + "delete time 5`", 0xff0000, "", message.guild.me.avatar_url)
                        await message.channel.send(embed=embed)
                        return
                    return


                # USEFUL :

                EVERYONE = (
                    "add",
                    "embed",
                    "emoji info",
                    "github",
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
                            embed = create_embed("Syntax Error", f"You did not enter the emoji after the command.\n> Examples : `{prefix}emoji info `{Emojis['Emoji_ghost']}", 0xff0000, "", message.guild.me.avatar_url)
                            await message.channel.send(embed=embed)
                            return
                        await emoji_info(message, emoji)
                        return

                    if no_prefix.startswith("github"):
                        await github(message)
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
                        if not message.role_mentions:
                            embed = create_embed("Syntax Error", "You did not mention any role after the command.\n> Example : `" + prefix + "role info @Role`", 0xff0000, "", message.guild.me.avatar_url)
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
                        embed = create_embed("You cannot do this action", "You are not allowed to manage channels.", 0xff8000, "", message.guild.me.avatar_url)
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
                                embed = create_embed("Prefix changed", "The new prefix is : `" + new + "`", bot.color, "", message.guild.me.avatar_url)
                                await message.channel.send(embed=embed)
                                json_txt = json.dumps(Prefix, sort_keys=True, indent=4)
                                def_prefix = open("Data/Modifiable_variables/prefix.json", "w")
                                def_prefix.write(json_txt)
                                def_prefix.close()
                            except IndexError:
                                embed = create_embed("Syntax Error", "You did not enter the new prefix after the command.\n> Example : `" + prefix + "prefix /`", 0xff0000, "", message.guild.me.avatar_url)
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
                                    embed = create_embed("Error", "There is already a channel " + salon.mention, 0xff0000, "", message.guild.me.avatar_url)
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
                        embed = create_embed("You cannot do this action", "You are not allowed to do this action. Only administrators of this server can do this action.", 0xff8000, "", message.guild.me.avatar_url)
                        await message.channel.send(embed=embed)
                        return

                CREATORS = (
                    "answer",
                    "say"
                )
                if no_prefix.startswith(CREATORS):
                    await message.channel.trigger_typing()
                    if message.author.id in Ids["Creators"]:

                        if no_prefix.startswith("answer"):
                            channel = self.get_channel(message.reference.channel_id)
                            async for msg in channel.history(limit=100):
                                if msg.id == message.reference.message_id:
                                    user_id = int(msg.content.split("`")[len(msg.content.split("`")) - 4])
                                    msg_id = int(msg.content.split("`")[len(msg.content.split("`")) - 2])
                                    user = self.get_user(user_id)
                                    text = ""
                                    for part in message.content.split(" ")[1:]:
                                        text += part + " "
                                    dm = await user.create_dm()
                                    async for msg in dm.history(limit=100):
                                        if msg.id == msg_id:
                                            await msg.reply(text)
                                            return
                            await message.channel.send("Unknown message")
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

                if message.guild.id == Ids["Support_server"]:
                    # perms mute
                    if message.content.startswith(prefix + "upmute"):
                        await message.channel.trigger_typing()
                        mute = discord.utils.get(message.guild.roles, name="Muted")
                        overwrite = {mute: discord.PermissionOverwrite(send_messages=False)}
                        for channel in message.guild.channels:
                            x = channel.overwrites
                            x.update(overwrite)
                            await channel.edit(overwrites=x)
                        await message.channel.send("The permissions for " + mute.mention + " have been updated.")
                        return
                    # suggestion
                    if message.content.startswith(prefix + "sugg"):
                        await message.channel.trigger_typing()
                        channel = self.get_channel(Ids["Suggestion"])
                        msg = message.content.split(" ")[1:]
                        content = ""
                        for part in msg:
                            content += " " + part
                        embed = create_embed("Suggestion from " + message.author.name + " (" + str(message.author.id) + ")", content, message.author.color, "", message.guild.me.avatar_url)
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
                        embed = create_embed("Bug report by " + message.author.name + " (" + str(message.author.id) + ")", content, message.author.color, "", message.guild.me.avatar_url)
                        a = await channel.send(embed=embed)
                        await a.add_reaction(Emojis["Yes"])
                        await a.add_reaction(Emojis["No"])
                        await message.channel.send("Your bug report was sent")
                        return
                    # rules
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
                        guild = self.get_guild(Ids["Support_server"])
                        bot_creator = discord.utils.get(guild.roles, id=719538013859872880)
                        bot_staff = discord.utils.get(guild.roles, id=743796789769142354)
                        embed = create_embed("Welcome in the Support server for Clash INFO !",
                                             f"Welcome ! Here is the support server of the {bot.mention} bot.\n\n{Emojis['Yes']} You can : {Emojis['Yes']}\n- Take your roles : {auto_roles.mention}\n- Follow the channel {clash_info.mention} to inform all your server about bot updates\n- Ask a question about the bot : {support.mention}\n- Take a ticket to speak with us : {tickets_channel.mention}\n- Send us a suggestion : {sugg.mention}\n- Notify us of a bug : {bug.mention}\n- Test the bot : {test01.mention}, {test02.mention}, {test03.mention}\n- Put the bot on your server : {put_bot.mention}\n- Rate the BOT : {feedback.mention}\n\n⚠️ You must : ⚠️\n- Respect the Discord ToS (https://discord.com/new/terms) and the Discord Guidelines (https://discord.com/new/guidelines)\n- Respect the language of each channel (with the flag emoji in the channel name). Default = English ONLY\n\n{Emojis['No']} You cannot : {Emojis['No']}\n- Put `| Clash INFO` after your name or `[role]` before your name without authorization from an {bot_creator.mention}\n- Put the same profile picture or name as an {bot_staff.mention}\n\nClick on {Emojis['Yes']} to access the whole server.",
                                             0x00ff00, "", message.guild.me.avatar_url)
                        a = await message.channel.send(embed=embed)
                        await a.add_reaction(Emojis["Yes"])
                        return
                    # auto-roles
                    if message.content == prefix + "auto-roles languages" and message.author.id in Ids["Creators"]:
                        await message.channel.trigger_typing()
                        await message.delete()
                        msg = ""
                        for emoji, name in Emojis["Languages_emojis"].items():
                            language = discord.utils.get(message.guild.roles, name=name)
                            msg += str(emoji) + " if you speak " + language.mention + "\n"
                        embed = create_embed("Click on the emojis to get the matching roles", msg, bot.color, "", message.guild.me.avatar_url)
                        a = await message.channel.send(embed=embed)
                        for emoji in Emojis["Languages_emojis"].keys():
                            await a.add_reaction(emoji)
                        return
                    # feedback
                    if message.content.startswith(prefix + "feedback"):
                        await message.channel.trigger_typing()
                        embed = create_embed("How do you like this bot ? Put a mark from 1 to 10", "", bot.color, "", message.guild.me.avatar_url)
                        a = await message.channel.send(embed=embed)
                        await message.delete()
                        for emoji in Emojis["Numbers"].values():
                            await a.add_reaction(emoji)
                        return

                # mentions
                members_done = []
                if message.mention_everyone:
                    for member in message.guild.members:
                        if await self.mention(message, member) == -1:
                            return
                if message.mentions:
                    for member in message.mentions:
                        if not str(member) in members_done:
                            members_done.append(str(member))
                            if await self.mention(message, member) == -1:
                                return
                if message.role_mentions:
                    for role in message.role_mentions:
                        for member in role.members:
                            if not str(member) in members_done:
                                members_done.append(str(member))
                                if await self.mention(message, member) == -1:
                                    return

        except discord.errors.Forbidden:
            if message.channel.permissions_for(bot).send_messages and message.channel.permissions_for(bot).embed_links:
                embed = create_embed("The bot cannot do this action !", "Please check its permissions.", 0xff0000, "", message.guild.me.avatar_url)
                await message.channel.send(embed=embed)
                return
            elif message.channel.permissions_for(bot).send_messages and not message.channel.permissions_for(bot).embed_links:
                await message.channel.send("The bot cannot do this action !\nPlease give the permission \"Embed Links\" to the bot")
                return
            elif not message.channel.permissions_for(bot).send_messages:
                embed = create_embed("The bot cannot send messages in this channel !", "Please check its permissions.", 0xff0000, "", message.guild.me.avatar_url)
                await message.author.send(embed=embed)
                return
        except TimeoutError:
            embed = create_embed("Timeout Error", "Please try again later", 0xff0000, "", message.guild.me.avatar_url)
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
            # direct message
            if message.content.startswith(prefix + "dm"):
                await message.channel.trigger_typing()
                try:
                    if message.author.guild_permissions.administrator or (message.role_mentions == [] and message.mention_everyone == 0):
                        if not member.bot:
                            msg = message.content.split("|")[1]
                            if msg == "":
                                embed = create_embed("Syntax Error", "You did not enter the text after the |.\n> Example : `" + prefix + "dm @user |Text`", 0xff0000, "", message.guild.me.avatar_url)
                                await message.channel.send(embed=embed)
                                return
                            await member.send(msg + "\n*Sent by " + str(message.author) + " (" + str(message.author.id) + ")*")
                            embed = create_embed(member.name, "This member has received the message.", member.color, "", message.guild.me.avatar_url)
                            await message.channel.send(embed=embed)
                    else:
                        embed = create_embed("You cannot do this action", "You are not allowed to send direct message to @everyone or a role. You must be an administrator", 0xff8000, "", message.guild.me.avatar_url)
                        await message.channel.send(embed=embed)
                        return -1

                except discord.Forbidden:
                    embed = create_embed(member.name, "This member does not want to receive direct message from this server.", member.color, "", message.guild.me.avatar_url)
                    await message.channel.send(embed=embed)
                    return
                except IndexError:
                    embed = create_embed("Syntax Error", "You did not enter the | after the command.\n> Example : `" + prefix + "dm @user |Text`", 0xff0000, "", message.guild.me.avatar_url)
                    await message.channel.send(embed=embed)
                    return
                return

            if message.guild.id == Ids["Support_server"]:
                # mute
                if message.content.startswith(prefix + "mute"):
                    await message.channel.trigger_typing()
                    if message.author.guild_permissions.manage_roles or message.author.guild_permissions.manage_permissions:
                        muted = discord.utils.get(member.guild.roles, name="Muted")
                        await member.add_roles(muted)
                        embed = create_embed(member.name, "This member has been muted", member.color, "", message.guild.me.avatar_url)
                        await message.channel.send(embed=embed)
                    else:
                        embed = create_embed("You cannot do this action", "You are not allowed to mute a member.", 0xff8000, "", message.guild.me.avatar_url)
                        await message.channel.send(embed=embed)
                        return
                    return
                # unmute
                if message.content.startswith(prefix + "unmute"):
                    await message.channel.trigger_typing()
                    if message.author.guild_permissions.manage_roles or message.author.guild_permissions.manage_permissions:
                        muted = discord.utils.get(member.guild.roles, name="Muted")
                        await member.remove_roles(muted)
                        embed = create_embed(member.name, "This member has been unmuted", member.color, "", message.guild.me.avatar_url)
                        await message.channel.send(embed=embed)
                    else:
                        embed = create_embed("You cannot do this action", "You are not allowed to mute a member.", 0xff8000, "", message.guild.me.avatar_url)
                        await message.channel.send(embed=embed)
                        return
                    return
                # temp mute
                if message.content.startswith(prefix + "tempmute"):
                    await message.channel.trigger_typing()
                    x = message.content.split(" ")[2]
                    if message.author.guild_permissions.manage_roles or message.author.guild_permissions.manage_permissions:
                        muted = discord.utils.get(member.guild.roles, name="Muted")
                        await member.add_roles(muted)
                        embed = create_embed(member.name, "This member has been muted", member.color, "", message.guild.me.avatar_url)
                        await message.channel.send(embed=embed)
                        x = float(x) * 60
                        await asyncio.sleep(x)
                        await member.remove_roles(muted)
                        embed = create_embed(member.name, "This member has been unmuted", member.color, "", message.guild.me.avatar_url)
                        await message.channel.send(embed=embed)
                    else:
                        embed = create_embed("You cannot do this action", "You are not allowed to mute a member.", 0xff8000, "", message.guild.me.avatar_url)
                        await message.channel.send(embed=embed)
                        return
                    return

        except discord.errors.Forbidden:
            embed = create_embed("The bot cannot do this action !", "Please check its permissions.", 0xff0000, "", message.guild.me.avatar_url)
            await message.channel.send(embed=embed)
        return
