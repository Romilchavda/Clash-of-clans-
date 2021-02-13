# ----- LIBRARIES : -----
import coc
import json
import datetime
from matplotlib import dates as mdates
from matplotlib import pyplot
import io
import asyncio
from PIL import Image, ImageFont, ImageDraw


# ----- PROJECT FILES : -----
from Script.import_functions import *
from Script.Clients.top_gg import Dbl_client
from Script.Clients.clash_of_clans import Clash_of_clans


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
from Script.Commands.Messages.Clash_Of_Clans.file import file

from Script.Commands.Messages.Useful.tickets import tickets, close_ticket
from Script.Commands.Messages.Useful.member_info import member_info
from Script.Commands.Messages.Useful.role_info import role_info
from Script.Commands.Messages.Useful.server_info import server_info
from Script.Commands.Messages.Useful.emoji_info import emoji_info
from Script.Commands.Messages.Useful.direct_message import direct_message_member, direct_message_role
from Script.Commands.Messages.Useful.poll import poll
from Script.Commands.Messages.Useful.bot_info import bot_info
from Script.Commands.Messages.Useful.add_the_bot import add_the_bot
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

    #temp
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

        act = discord.Activity(type=discord.ActivityType.watching, name="/help")
        await self.change_presence(status=discord.Status.online, activity=act)
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
        async for message in channel.history(limit=None):
            if message.id == raw_reaction.message_id:
                raw_reaction.message = message
                break
        if raw_reaction.message is None:
            return
        if (not raw_reaction.member.bot) and (raw_reaction.message.guild is not None) and (raw_reaction.message.author.id == self.id) and (raw_reaction.message.embeds != []):
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
        async for message in channel.history(limit=None):
            if message.id == raw_reaction.message_id:
                raw_reaction.message = message
                break
        if raw_reaction.message is None:
            return
        raw_reaction.member = channel.guild.get_member(raw_reaction.user_id)
        if (not raw_reaction.member.bot) and (raw_reaction.message.guild is not None) and (raw_reaction.message.author.id == self.id) and (raw_reaction.message.embeds != []):
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
                def_votes = open("Modifiable_variables/def_votes.json", "w")
                def_votes.write(json_txt)
                def_votes.close()
                await message.channel.send("/show votes")
                return
            else:
                return
        if str(message.channel.type) == "private":
            salon = self.get_channel(748509142578233364)
            if message.author.id != self.id:
                await message.author.send("Hello !\nI am a bot, so I cannot answer for your question ! You can ask it in the support server :\nhttps://discord.gg/KQmstPw\n```Default help command : /help \n(you can see it with sending @Clash INFO#3976 on your server)```")
                await salon.send("`" + message.content + "` de :\n" + str(message.author) + " (`" + str(message.author.id) + "`)\nMessage_id : `" + str(message.id) + "`")
            return
        else:
            bot = message.guild.me
        # def Prefix
        global prefix
        try:
            global Prefix
            prefix = Prefix[message.guild.id]
        except KeyError:
            prefix = self.Prefix_default
        no_prefix = message.content[len(prefix):]
        # test
        if message.content == prefix and (message.author.id == 393317636160618496 or message.author.id in Ids["Creators"]) and (message.guild.id == Ids["Support"] or message.guild.id == 767745074096111656):
            await member_join(self, message.author)
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
                user_mention = message.mentions
                role_mention = message.role_mentions
                everyone = message.mention_everyone
                global liste_ok
                liste_ok = []

                # AIDE
                if message.content.startswith(prefix + "help"):
                    await message.channel.trigger_typing()
                    d1 = f"**{prefix}th [Level]** : Show the max level for your buildings at your Town Hall level.\n**{prefix}bh [Level]** : Show the max level for your buildings at your Builder Hall level.\n**{prefix}player [Tag CoC]** : Show data about the player (with the troops players on the 3rd page).\n**{prefix}clan [Tag CoC]** : Show data about the clan.\n**{prefix}members [Tag CoC]** : Show the clan members list.\n**{prefix}search clan [Name] [Number of Clans]** : Search clans by name.\n**{prefix}roles TH** : Create an auto-roles system to give the roles (created by the bot if they did not exist) with reactions\n**{prefix}roles BH** : Create an auto-roles system to give the roles (created by the bot if they did not exist) with reactions\n**{prefix}roles league** : Create an auto-roles system to give the roles (created by the bot if they did not exist) with reactions\n**{prefix}bases [TH level]** : Show bases for your TH level *(Not yet available)*\n**{prefix}coc** : Give link for Clash Of Clans data sheet."
                    embed1 = self.create_embed("▬▬▬ Clash Of Clans Commands ▬▬▬", d1, 0x00ffff, "Click on 1, 2 or 3 to change page. Click on (i) to get bot information. Click on ✅ to close the help.\nHelp page 1/3")
                    a = await message.channel.send(embed=embed1)
                    await a.add_reaction("1️⃣")
                    await a.add_reaction("2️⃣")
                    await a.add_reaction("3️⃣")
                    await a.add_reaction(Emojis["Info"])
                    await a.add_reaction(Emojis["Yes"])
                    return
                if message.content.startswith(prefix + "aide"):
                    await message.channel.trigger_typing()
                    d1 = f"**{prefix}th [Level]** : Affiche le niveau maximum des bâtiments pour le niveau d'Hôtel De Ville. \n**{prefix}player [Tag CoC]** : Affiche des informations sur le joueur (informations générales, troupes).\n**{prefix}clan [Tag CoC]** : Affiche des informations à propos du clan.\n**{prefix}members [Tag CoC]** : Affiche la liste des membres du clan.\n**{prefix}search clan [Name] [Number of Clans]** : Cherche des clans selon leur noms.\n**{prefix}roles TH** : Crée un système d'auto-rôle donnant les rôles d'HDV (créés par le bot s'ils n'existent pas) avec des réactions.\n**{prefix}roles BH** : Crée un système d'auto-rôle donnant les rôles de MDO (créés par le bot s'ils n'existent pas) avec des réactions.\n**{prefix}roles league** : Crée un système d'auto-rôle donnant les rôles de ligue (créés par le bot s'ils n'existent pas) avec des réactions.\n**{prefix}bases [TH level]** : Affiche des bases pour le niveau d'HDV *(Pas encore disponible)*.\n**{prefix}coc** : Donne le lien d'un tableur regroupant certaines informations."
                    fr_embed1 = self.create_embed("▬▬▬ Clash Of Clans Commands (FR) ▬▬▬", d1, 0x00ffff, "Click on 1, 2 or 3 to change page. Click on (i) to get bot information. Click on ✅ to close the help.\nHelp page 1/3")
                    a = await message.channel.send(embed=fr_embed1)
                    await a.add_reaction("1️⃣")
                    await a.add_reaction("2️⃣")
                    await a.add_reaction("3️⃣")
                    await a.add_reaction(Emojis["Info"])
                    await a.add_reaction(Emojis["Yes"])
                    return

                # CLASH OF CLANS :
                try:
                    # bases
                    if message.content.startswith(prefix + "base"):
                        await message.channel.trigger_typing()
                        await message.channel.send("This command is not yet available")
                        return
                    # player
                    if message.content.startswith(prefix + "player"):
                        await message.channel.trigger_typing()
                        try:
                            tag = message.content.split(" ")[1]
                            embed = await self.joueur("principal", tag)
                            a = await message.channel.send(embed=embed)
                            await a.add_reaction(Emojis["Barbarian_king"])
                            await a.add_reaction(Emojis["Battle_machine"])
                            guild = self.get_guild(Ids["Emojis_troops_spells_id"])
                            barbare = discord.utils.get(guild.emojis, name="barb")
                            await a.add_reaction(barbare)
                            await a.add_reaction(Emojis["Exp"])
                        except IndexError:
                            embed = self.create_embed("Syntax Error", "You did not enter the tag of the clan after the command.\n> Example : `" + prefix + "player #PlayerTag`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        except coc.errors.NotFound:
                            embed = self.create_embed("Error", "There is no player with the tag `" + tag + "` (do not forget the # in front of the tag).", bot.color, "")
                            await message.channel.send(embed=embed)
                            return
                        return
                    # search player
                    if message.content.startswith(prefix + "search player"):
                        await message.channel.trigger_typing()
                        await message.channel.send("This command is unavailable because the API does not allow it, but maybe later !")
                        return
                    # clan
                    if message.content.startswith(prefix + "clan"):
                        await message.channel.trigger_typing()
                        try:
                            tag = message.content.split(" ")[1]
                            if tag == "":
                                embed = self.create_embed("Syntax Error", "You must enter only 1 space between the command and the tag of the clan.\n> Example : `" + prefix + "clan #ClanTag`", 0xff0000, "")
                                await message.channel.send(embed=embed)
                                return
                            clan = await Clash_of_clans.get_clan(tag)
                            if clan.location != None:
                                lieu = clan.location.name
                            else:
                                lieu = "International"
                            leader = coc.utils.get(clan.members, role=coc.Role.leader)
                            ties = clan.war_ties
                            if ties == None:
                                ties = "unkown"
                            losses = clan.war_losses
                            if losses == None:
                                losses = "unknown"
                            embed = self.create_embed("Clan : " + clan.name + " (" + clan.tag + ")", f"{Emojis['Trophy']} Clan points : {int_to_str(clan.points)}\n{Emojis['Trophy']} Builder base clan points : {int_to_str(clan.versus_points)}\n{Emojis['Trophy']} League : {clan.war_league}\n{Emojis['Trophy']} Required trophies : {int_to_str(clan.required_trophies)}\n{Emojis['Owner']} Leader : {leader.name} ({leader.tag})\n{Emojis['Members']} Number of members : {clan.member_count}\n:crossed_swords: Wars : {clan.war_wins} wins, {ties} ties and {losses} losses\n{Emojis['Pin']} Location : {lieu}\n{Emojis['Invite']} Invitations type : {clan.type}\n{Emojis['Description']} Description : {clan.description}\n[Open in Clash Of Clans]({clan.share_link})", bot.color, "For more information on clan members, put " + prefix + "members [tag]")
                            embed.set_thumbnail(url=clan.badge.url)
                            await message.channel.send(embed=embed)
                        except IndexError:
                            embed = self.create_embed("Syntax Error", "You did not enter the tag of the clan after the command.\n> Example : `" + prefix + "clan #ClanTag`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        except coc.errors.NotFound:
                            embed = self.create_embed("Not Found", "There is no clan with the tag `" + tag + "` (do not forget the # in front of the tag).", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        return
                    # search clan
                    if message.content.startswith(prefix + "search clan"):
                        await message.channel.trigger_typing()
                        nom = message.content.split(" ")[2:]
                        if nom == []:
                            embed = self.create_embed("Syntax Error", "You did not enter the name of the clan after the command.\n> Example : `" + prefix + "search clan Clan Name 5`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        nom = nom[:len(nom) - 1]
                        name = ""
                        for part in nom:
                            name += part + " "
                        try:
                            if int(message.content.split(" ")[len(message.content.split(" ")) - 1]) <= 0:
                                embed = self.create_embed("Syntax Error", "You must enter a positive number of clans to show after the command.\n> Example : `" + prefix + "search clan Clan Name 5`", 0xff0000, "")
                                await message.channel.send(embed=embed)
                                return
                            if int(message.content.split(" ")[len(message.content.split(" ")) - 1]) <= 10:
                                limite = int(message.content.split(" ")[len(message.content.split(" ")) - 1])
                            else:
                                limite = 10
                                await message.channel.send("I can only show 10 clans to avoid spam.")
                        except ValueError:
                            embed = self.create_embed("Syntax Error", "You did not enter the number of clans to show after the command.\n> Example : `" + prefix + "search clan Clan Name 5`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        clans = await Clash_of_clans.search_clans(name=name, limit=limite)
                        a = 0
                        for clan in clans:
                            a += 1
                            if clan.location != None:
                                lieu = clan.location.name
                            else:
                                lieu = "International"
                            embed = self.create_embed("Clan : " + clan.name + " (" + clan.tag + ")", str(Emojis["Trophy"]) + " Clan points : " + str(clan.points) + "\n" + str(Emojis["Trophy"]) + " Builder base clan points : " + str(clan.versus_points) + "\n" + str(Emojis["Members"]) + " Number of members : " + str(clan.member_count) + "\n" + str(Emojis["Pin"]) + " Location : " + lieu + "\n[Open in Clash Of Clans](" + clan.share_link + ")", bot.color, "For more information on clan members, put " + prefix + "members [tag]")
                            embed.set_thumbnail(url=clan.badge.url)
                            await message.channel.send(embed=embed)
                        await message.channel.send("I showed " + str(len(clans)) + " clans with the name " + name)
                        return
                    # members list (from a clan)
                    if message.content.startswith(prefix + "members"):
                        await message.channel.trigger_typing()
                        try:
                            tag = message.content.split(" ")[1]
                            if tag == "":
                                embed = self.create_embed("Syntax Error", "You must enter only 1 space between the command and the tag of the clan.\n> Example : `" + prefix + "members #ClanTag`", 0xff0000, "")
                                await message.channel.send(embed=embed)
                                return
                            clan = await Clash_of_clans.get_clan(tag)
                            msg = ""
                            async for member in clan.get_detailed_members():
                                msg += f"- {member.name} : {member.trophies} {Emojis['Trophy']} (best : {member.best_trophies}) **TH {member.town_hall}** {member.tag}\n"
                            embed = self.create_embed("Clan members " + clan.name + " (" + clan.tag + ")", "Members list : \n" + msg, message.author.color, "")
                            await message.channel.send(embed=embed)
                        except discord.errors.HTTPException:
                            await message.channel.send("This clan has too many members, and Discord refuse to show all of them... But no problem : I will send the message in several parts !", delete_after=30)
                            msg = ""
                            x = 0
                            async for member in clan.get_detailed_members():
                                msg += f"- {member.name} : {member.trophies} {Emojis['Trophy']} (best : {member.best_trophies}) **TH {member.town_hall}** {member.tag}\n"
                                x += 1
                                if x >= clan.member_count / 4:
                                    embed = self.create_embed("Clan members " + clan.name + " (" + clan.tag + ")", "Members list : \n" + msg, message.author.color, "")
                                    await message.channel.send(embed=embed)
                                    msg = ""
                                    x = 0
                            embed = self.create_embed("Clan members " + clan.name + " (" + clan.tag + ")", "Members list : \n" + msg, message.author.color, "")
                            await message.channel.send(embed=embed)
                        except IndexError:
                            embed = self.create_embed("Syntax Error", "You did not enter the tag of the clan after the command.\n> Example : `" + prefix + "members #ClanTag`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        except coc.errors.NotFound:
                            embed = self.create_embed("Error", "There is no clan with the tag `" + tag + "` (do not forget the # in front of the tag).", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        return
                    # th
                    if message.content.startswith(prefix + "th") and not message.content.startswith(prefix + "thank"):
                        await message.channel.trigger_typing()
                        try:
                            lvl = message.content.split(" ")[1]
                            embed = self.hdv(lvl, message)
                            await message.channel.send(embed=embed)
                        except AttributeError:
                            embed = self.create_embed("Syntax Error", "Please give a valid TH level. You can also enter just `" + prefix + "th` and click on the emoji which match with your TH level.\n> Example : `" + prefix + "th 13`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        except IndexError:
                            embed = self.create_embed("What is your TH level ?", "", bot.color, "")
                            z = await message.channel.send(embed=embed)
                            for emoji in Emojis["Th_emojis"].keys():
                                await z.add_reaction(emoji)
                            return
                        return
                    # bh
                    if message.content.startswith(prefix + "bh"):
                        await message.channel.trigger_typing()
                        try:
                            lvl_mdo = message.content.split(" ")[1]
                            embed = self.mdo(lvl_mdo, message)
                            await message.channel.send(embed=embed)
                        except AttributeError:
                            embed = self.create_embed("Syntax Error", "Please give a valid BH level. You can also enter just `" + prefix + "bh` and click on the emoji which match with your BH level.\n> Example : `" + prefix + "bh 9`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        except IndexError:
                            guild = self.get_guild(Ids["Emojis_th_bh_leagues"])
                            if guild.id == Ids["Emojis_th_bh_leagues"]:
                                embed = self.create_embed("What is your BH level ?", "", bot.color, "")
                                zmdo = await message.channel.send(embed=embed)
                                for emoji in Emojis["Bh_emojis"].keys():
                                    await zmdo.add_reaction(emoji)
                            return
                        return
                    # coc
                    if message.content.startswith(prefix + "coc"):
                        await message.channel.trigger_typing()
                        embed = self.create_embed("Here is the file that resume all the data of the bot on Clash Of Clans", "https://docs.google.com/spreadsheets/d/1K7P7Wi4zH76TDlVolaXpjGq20u_PnIc7mWUBYWSINaQ/edit?usp=drivesdk", message.author.color, "")
                        await message.channel.send(embed=embed)
                        return
                except coc.errors.Maintenance:
                    await message.channel.send("Service Unavailable : API is currently in maintenance, please come back later !")
                    return

                # MODERATION :
                # vide
                if message.content.startswith(prefix + "delete"):
                    await message.channel.trigger_typing()
                    if message.author.guild_permissions.manage_messages:
                        try:
                            nb_msg = 0
                            quoi = str(message.content.split(" ")[1])
                            if quoi == "all":
                                async for msg in message.channel.history(limit=None):
                                    if not msg.pinned:
                                        nb_msg += 1
                                        await msg.delete()
                            else:
                                if quoi == "time":
                                    combien = int(message.content.split(" ")[2])
                                    async for msg in message.channel.history(after=(message.created_at) - datetime.timedelta(minutes=combien), oldest_first=False):
                                        if not msg.pinned:
                                            nb_msg += 1
                                            await msg.delete()
                                else:
                                    try:
                                        combien = int(message.content.split(" ")[1])
                                    except ValueError:
                                        embed = self.create_embed("Syntax Error", "You did not enter the number of messages, the word \"all\" or the word \"time\" with the wished time after the command.\n> Examples : `" + prefix + "delete 5` ; `" + prefix + "delete all` ; `" + prefix + "delete time 5`", 0xff0000, "")
                                        await message.channel.send(embed=embed)
                                        return
                                    if combien <= -1:
                                        embed = self.create_embed("Error", "You cannot delete a negative number of messages", 0xff0000, "")
                                        await message.channel.send(embed=embed)
                                        return
                                    async for msg in message.channel.history(limit=combien + 1):
                                        if not msg.pinned:
                                            nb_msg += 1
                                            await msg.delete()
                            if nb_msg == 1 or nb_msg == 2:
                                embed = self.create_embed("Messages deleted", int_to_str(nb_msg - 1) + " message deleted", bot.color, "")
                            else:
                                embed = self.create_embed("Messages deleted", int_to_str(nb_msg - 1) + " messages deleted", bot.color, "")
                            await message.channel.send(embed=embed, delete_after=5)
                        except IndexError:
                            embed = self.create_embed("Syntax Error", "You did not enter the number of messages, the word \"all\" or the word \"time\" with the wished time after the command.\n> Examples : `" + prefix + "delete 5` ; `" + prefix + "delete all` ; `" + prefix + "delete time 5`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                    else:
                        embed = self.create_embed("You cannot do this action", "You are not allowed to delete messages.", 0xff8000, "")
                        await message.channel.send(embed=embed)
                        return
                    return

                # UTILITAIRE :

                EVERYONE = (
                    "add",
                    "age",
                    "bot info",
                    "embed",
                    "emoji info",
                    "invite",
                    "ping",
                    "poll",
                    "promote",
                    "role info",
                    "server info",
                    "support",
                    "thank"
                )
                if no_prefix.startswith(EVERYONE):
                    await message.channel.trigger_typing()

                    if no_prefix.startswith("add") or message.content.startswith(prefix + "invite"):
                        perms = discord.Permissions(manage_roles=True, manage_channels=True, kick_members=True, ban_members=True, create_instant_invite=True, view_channel=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True, read_message_history=True, mention_everyone=True, add_reactions=True, use_external_emojis=True, view_audit_log=True, manage_webhooks=True)
                        lien = "https://discord.com/oauth2/authorize?client_id=" + str(self.id) + "&permissions=" + str(perms.value) + "&scope=applications.commands%20bot"
                        url = "attachment://add_clash_info.png"
                        file = discord.File("../Pictures/add_clash_info.png", filename="add_clash_info.png")
                        embed = self.create_embed_img("The link to invite the bot", str(Emojis["Browser"]) + " Enter this link in a browser to add the bot at your server.\n" + lien, message.author.color, "If you like the bot, do not forget to share it !", url)
                        await message.channel.send(embed=embed, file=file)
                        return

                    if no_prefix.startswith("age"):
                        try:
                            annee = int(message.content.split(" ")[3])
                            mois = int(message.content.split(" ")[2])
                            jour = int(message.content.split(" ")[1])
                        except (IndexError, ValueError):
                            embed = self.create_embed("Syntax Error", "You did not enter your birth year/month/day after the command.\n> Example : `" + prefix + "age 28 04 2020`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        try:
                            heure = int(message.content.split(" ")[4])
                            try:
                                minute = int(message.content.split(" ")[5])
                                try:
                                    seconde = int(message.content.split(" ")[6])
                                except (IndexError, ValueError):
                                    seconde = 0
                            except (IndexError, ValueError):
                                minute = 0
                                seconde = 0
                        except (IndexError, ValueError):
                            heure = 0
                            minute = 0
                            seconde = 0
                        now = message.created_at
                        try:
                            ne = datetime.datetime(year=annee, month=mois, day=jour, hour=heure, minute=minute, second=seconde)
                        except ValueError:
                            embed = self.create_embed("Error", f"This day ({jour}/{mois}/{annee}; with *day/month/year*) does not exist !", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        diff = now - ne
                        s = datetime.timedelta.total_seconds(diff)
                        embed = self.create_embed("If you was born the " + str(ne) + " (UTC-0), you are :", int_to_str(diff.days) + " days old\n" + int_to_str(int(s)) + " seconds old", message.author.color, "")
                        await message.channel.send(embed=embed)
                        return

                    if no_prefix.startswith("bot info"):
                        perms_bot_d = bot.guild_permissions
                        perms_r = discord.Permissions(manage_roles=True, manage_channels=True, kick_members=True, ban_members=True, create_instant_invite=True, view_channel=True, send_messages=True, manage_messages=True, embed_links=True, attach_files=True, read_message_history=True, mention_everyone=True, add_reactions=True, use_external_emojis=True, view_audit_log=True, manage_webhooks=True)
                        msg_perm = ":warning: The bot needs the permissions : "
                        perms_bot = []
                        for perm in perms_bot_d:
                            if perm[1]:
                                perms_bot.append(perm[0])
                        for perm in perms_r:
                            if perm[1] and not perm[0] in perms_bot:
                                msg_perm += "\n" + perm[0]
                        msg_perm += "\nSo please grant it to the bot."
                        if msg_perm == ":warning: The bot needs the permissions : " + "\nSo please grant it to the bot.":
                            msg_perm = str(Emojis["Yes"]) + " The bot have all required permissions !"
                        nb_guilde = len(self.guilds)
                        msg_serv = str(Emojis["Discord"]) + " The bot is on " + int_to_str(nb_guilde) + " servers !"
                        msg_crea = str(Emojis["Calendar"]) + " The bot was created the 28/04/2020, and certified the 23/09/2020."
                        file = discord.File("../Pictures/stats.png", filename="stats.png")
                        url = "attachment://stats.png"
                        embed = self.create_embed_img("Clash INFO", msg_perm + "\n" + msg_serv + "\n" + msg_crea, bot.color, "", url)
                        await message.channel.send(embed=embed, file=file)
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
                        guild = self.get_guild(message.guild.id)
                        emoji = discord.utils.get(guild.emojis, name=message.content.split(":")[1])
                        embed = self.create_embed(emoji.name, f"{Emojis['Name']} Name : `{emoji.name}`\n{Emojis['Id']} ID : `{emoji.id}`\nAnimated : {emoji.animated}\nTry it : {emoji}", 0x00ffff, "")
                        embed.set_thumbnail(url=emoji.url)
                        await message.channel.send(embed=embed)
                        return

                    if no_prefix.startswith("ping"):
                        bout = [char for char in str(self.latency)]
                        bout = bout[2:5]
                        api = ""
                        for part in bout:
                            api += part
                        embed = self.create_embed("The bot is OK !", "ping API : " + api + "ms", bot.color, "")
                        await message.channel.send(embed=embed)
                        return

                    if no_prefix.startswith("poll"):
                        nom = message.content.split(" ")[1:]
                        titre = ""
                        for part in nom:
                            titre += part + " "
                        embed = self.create_embed("Poll : " + titre, "This poll is requested by :\n" + message.author.name + "#" + str(message.author.discriminator) + " (" + str(message.author.id) + ")", message.author.color, "")
                        a = await message.channel.send(embed=embed)
                        await a.add_reaction(Emojis["Yes"])
                        await a.add_reaction(Emojis["No"])
                        await a.add_reaction(Emojis["Think"])
                        await a.add_reaction(Emojis["End"])
                        await message.delete()
                        return

                    if no_prefix.startswith("promote"):
                        embed = self.create_embed("Links to promote the bot :", "[Top.gg](https://top.gg/bot/704688212832026724)\n[Discord.Bots.gg](https://discord.bots.gg/bots/704688212832026724)\n[Arcane-Center.xyz](https://arcane-center.xyz/bot/704688212832026724)\n[WonderBotList.com](https://wonderbotlist.com/en/bot/704688212832026724)\n\nYou can click on " + str(Emojis["Link"]) + " to see the URL.", message.author.color, "Thanks you for your support !")
                        a = await message.channel.send(embed=embed)
                        await a.add_reaction(Emojis["Link"])
                        return

                    if no_prefix.startswith("role info"):
                        if role_mention == []:
                            embed = self.create_embed("Syntax Error", "You did not mention any role after the command.\n> Example : `" + prefix + "role info @Role`", 0xff0000, "")
                            await message.channel.send(embed=embed)
                            return
                        for role in role_mention:
                            perms = ""
                            if role.permissions.administrator:
                                perms += "Administrator\n"
                            if role.permissions.ban_members:
                                perms += "Ban members\n"
                            if role.permissions.kick_members:
                                perms += "Kick off members\n"
                            if role.permissions.manage_roles:
                                perms += "Manage roles\n"
                            if role.permissions.manage_permissions:
                                perms += "Manage permissions\n"
                            if role.permissions.manage_guild:
                                perms += "Manage server\n"
                            if role.permissions.manage_channels:
                                perms += "Manage channel\n"
                            if role.permissions.manage_messages:
                                perms += "Manage messages\n"
                            if role.permissions.manage_nicknames:
                                perms += "Manage nicknames\n"
                            if role.permissions.mention_everyone:
                                perms += "Mention everyone\n"
                            if role.permissions.view_audit_log:
                                perms += "View logs\n"
                            if perms == "":
                                perms = "Any"
                            embed = self.create_embed(role.name, "**Role permissions :**\n" + perms, role.color, "")
                            await message.channel.send(embed=embed)
                        return

                    if no_prefix.startswith("server info"):
                        cree_brut = (str(message.guild.created_at).split(" ")[0])
                        cree = (cree_brut.split("-")[2]) + "/" + (cree_brut.split("-")[1]) + "/" + (cree_brut.split("-")[0])
                        nb_humains = 0
                        for members in message.guild.members:
                            if members.bot == 0:
                                nb_humains += 1
                        nb_bots= 0
                        for members in message.guild.members:
                            if members.bot == 1:
                                nb_bots += 1
                        emojis = ""
                        for emoji in message.guild.emojis:
                            emojis += str(emoji) + " "
                        roles = ""
                        for role in message.guild.roles:
                            roles += role.mention + " "
                        roles = "*not yet available*"
                        embed = self.create_embed(message.guild.name, str(Emojis["Owner"]) + " Owner : <@" + str(message.guild.owner_id) + ">\n" + str(Emojis["Calendar"]) + " Created at (*DD/MM/YYYY*) : " + cree + "\n" + str(Emojis["Members"]) + " Humans : "+str(nb_humains)+"\n" + str(Emojis["Bot"]) + " Bots : "+str(nb_bots)+"\nRegion : " + str(message.guild.region) + "\n" + str(Emojis["Boost"]) + " Boost level : " + str(message.guild.premium_tier) + "/3\n" + str(Emojis["Boost"]) + " Boost number : " + str(message.guild.premium_subscription_count) + "\n" + str(Emojis["Add_reaction"]) + " emojis : " + emojis + "\nRoles : " + roles, bot.color, "")
                        embed.set_thumbnail(url=message.guild.icon_url)
                        await message.channel.send(embed=embed)
                        return

                    if no_prefix.startswith("support"):
                        url = "attachment://support_server.png"
                        file = discord.File("../Pictures/support_server.png", filename="support_server.png")
                        embed = self.create_embed_img("Our support server :", "Join our support server if you have questions or suggestions. https://discord.gg/KQmstPw", message.author.color, "", url)
                        await message.channel.send(embed=embed, file=file)
                        return

                    if no_prefix.startswith("thank"):
                        embed = self.create_embed("Thanks to them for their help in the bot creation.", str(Emojis["Dg"]) + " The FRENCH server **Dark's & Graff** (https://discord.gg/PN9aBq9), for the graphics (profile picture, poster advertising...),\n\n**DarkElite | WarZone | FW#5122**, for his advice always useful !", bot.color, "")
                        await message.channel.send(embed=embed)
                        return

                    if no_prefix.startswith("yt"):
                        embed = self.create_embed("The YouTube channel dedicated to the bot :", "[Clash FAMILY YouTube Channel](https://www.youtube.com/channel/UC5jAaxdA0uWJCOfghYORWjA)", bot.color, "")
                        await message.channel.send(embed=embed)
                        return


                MANAGE_CHANNEL = (
                    "close"
                )
                if no_prefix.startswith(MANAGE_CHANNEL):
                    await message.channel.trigger_typing()
                    if message.author.guild_permissions.manage_channels:

                        if no_prefix.startswith("close"):
                            if "ticket-" in message.channel.name:
                                embed = self.create_embed("Close this ticket", ":warning: It will delete this channel !", bot.color, "")
                                a = await message.channel.send(embed=embed)
                                await a.add_reaction(Emojis["Yes"])
                                await a.add_reaction(Emojis["No"])
                            else:
                                embed = self.create_embed("You cannot do this action", "You can only delete ticket channels.", 0xff8000, "")
                                await message.channel.send(embed=embed)
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
                                def_prefix = open("Modifiable_variables/def_prefix.json", "w")
                                def_prefix.write(json_txt)
                                def_prefix.close()
                            except IndexError:
                                embed = self.create_embed("Syntax Error", "You did not enter the new prefix after the command.\n> Example : `" + prefix + "prefix /`", 0xff0000, "")
                                await message.channel.send(embed=embed)
                                return
                            return

                        if no_prefix.startswith("roles TH"):
                            msg = ""
                            for emoji, value in Emojis["Th_emojis"].items():
                                a = discord.utils.get(message.guild.roles, name=value[0])
                                if a is None:
                                    a = await message.guild.create_role(name=value[0])
                                msg += str(emoji) + " to be " + a.mention + "\n"
                            embed = self.create_embed("Click on the emojis to get the matching roles", msg, bot.color, "")
                            a = await message.channel.send(embed=embed)
                            for emoji in Emojis["Th_emojis"].keys():
                                await a.add_reaction(emoji)
                            await message.delete()
                            return

                        if no_prefix.startswith("roles BH"):
                            msg = ""
                            for emoji, value in Emojis["Bh_emojis"].items():
                                a = discord.utils.get(message.guild.roles, name=value[0])
                                if a is None:
                                    a = await message.guild.create_role(name=value[0])
                                msg += str(emoji) + " to be " + a.mention + "\n"
                            embed = self.create_embed("Click on the emojis to get the matching roles", msg, bot.color, "")
                            a = await message.channel.send(embed=embed)
                            for emoji in Emojis["Bh_emojis"].keys():
                                await a.add_reaction(emoji)
                            await message.delete()
                            return

                        if no_prefix.startswith("roles league"):
                            msg = ""
                            for emoji, value in Emojis["League_emojis"].items():
                                a = discord.utils.get(message.guild.roles, name=value[0])
                                if a is None:
                                    a = await message.guild.create_role(name=value[0])
                                msg += str(emoji) + " to be " + a.mention + "\n"
                            embed = self.create_embed("Click on the emojis to get the matching roles", msg, bot.color, "")
                            a = await message.channel.send(embed=embed)
                            for emoji in Emojis["League_emojis"].keys():
                                await a.add_reaction(emoji)
                            await message.delete()
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
                            cat_ticket = await message.guild.create_category(name="Tickets")
                            await cat_ticket.edit(position=3)
                            overwrite = {message.guild.default_role: discord.PermissionOverwrite(send_messages=False, view_channel=True), bot: discord.PermissionOverwrite(send_messages=True, view_channel=True)}
                            z = await message.guild.create_text_channel(name="tickets", overwrites=overwrite, category=cat_ticket)
                            embed = self.create_embed("Ticket :", msg, bot.color, "")
                            a = await z.send(embed=embed)
                            await a.add_reaction(Emojis["Ticket"])
                            embed = self.create_embed("The ticket channel was created !", z.mention, bot.color, "")
                            await message.channel.send(embed=embed)
                            return

                    else:
                        embed = self.create_embed("You cannot do this action", "You are not allowed to do this action. Only administrators of this server can do this action.", 0xff8000, "")
                        await message.channel.send(embed=embed)
                        return

                CREATORS = (
                    "answer",
                    "bot",
                    "id",
                    "list",
                    "mp_gerants",
                    "reaction",
                    "refresh History",
                    "refresh top.gg",
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

                        if no_prefix.startswith("bot"):
                            await message.channel.trigger_typing()
                            try:
                                id = int(message.content.split(" ")[1])
                                lien = discord.utils.oauth_url(id, permissions=discord.Permissions(administrator=True), guild=None, redirect_uri=None)
                                embed = self.create_embed("Add the bot with the ID " + str(id) + " :", lien, bot.color, "")
                                await message.channel.send(embed=embed)
                            except IndexError:
                                embed = self.create_embed("Syntax Error", "You did not put an ID after the command.\n> Example : " + prefix + "bot " + str(self.id), 0xff0000, "")
                                await message.channel.send(embed=embed)
                                return
                            except ValueError:
                                embed = self.create_embed("Syntax Error", "You did not put a good ID after the command.\n> Example : " + prefix + "bot " + str(self.id), 0xff0000, "")
                                await message.channel.send(embed=embed)
                                return
                            return

                        if no_prefix.startswith("id"):
                            id = int(message.content.split(" ")[1])
                            user = message.guild.get_member(id)
                            if user is not None:
                                await message.channel.send(user.mention)
                            else:
                                await message.channel.send("Cette personne n'a pas de serveur commun avec le bot.")
                            return

                        if no_prefix.startswith("list"):
                            servs = {}
                            for guild in self.guilds:
                                ok = 0
                                for member in guild.members:
                                    if not member.bot:
                                        ok += 1
                                servs[guild] = ok
                            msg = ""
                            a = 0
                            z = 0
                            for k in sorted(servs, key=servs.get, reverse=True):
                                a += 1
                                msg += "\n" + str(a + z * 10) + ") The server *" + k.name + "* with **" + str(servs.get(k)) + "** members (owner : *" + k.owner.name + "*)"
                                if a == 10:
                                    embed = self.create_embed("The " + str(z * 10 + 1) + " to " + str((z + 1) * 10) + " best servers (by human members) :", msg, bot.color, "")
                                    await message.channel.send(embed=embed)
                                    a = 0
                                    z += 1
                                    msg = ""
                            if msg != "":
                                embed = self.create_embed("The " + str(z * 10 + 1) + " to " + str((z + 1) * 10) + " best servers (by human members) :", msg, bot.color, "")
                                await message.channel.send(embed=embed)
                            return

                        if no_prefix.startswith("mp_gerants"):
                            for guild in self.guilds:
                                server_owner = guild.owner
                                try:
                                    msg = message.content.split(" ")[1:]
                                    contenu = ""
                                    for part in msg:
                                        contenu += " " + part
                                    await server_owner.send(str(contenu) + "\n*Sent by " + str(message.author) + "*")
                                    embed = self.create_embed(server_owner.name, "This user received the direct message.", server_owner.color, "")
                                    await message.channel.send(embed=embed)
                                except discord.Forbidden:
                                    embed = self.create_embed(server_owner.name, "This user do not want to receive direct message from the bot.", bot.color, "")
                                    await message.channel.send(embed=embed)
                            return

                        if no_prefix.startswith("reaction"):
                            if message.channel_mentions == []:
                                id = message.content.split(" ")[1]
                                reaction = message.content.split(" ")[2]
                                async for msg in message.channel.history(limit=None):
                                    if msg.id == int(id):
                                        emoji = self.get_emoji(int(reaction))
                                        await msg.add_reaction(emoji)
                                        await message.channel.send("The reaction was added")
                                        return
                            else:
                                id = message.content.split(" ")[2]
                                reaction = message.content.split(" ")[3]
                                async for msg in message.channel_mentions[0].history(limit=None):
                                    if msg.id == int(id):
                                        emoji = self.get_emoji(int(reaction))
                                        await msg.add_reaction(emoji)
                                        await message.channel.send("The reaction was added")
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

                        if no_prefix.startswith("refresh top.gg"):
                            await Dbl_client.update_stats(len(self.guilds))
                            await message.channel.send(str(Emojis["Yes"]) + " (https://top.gg/bot/704688212832026724)")
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
                                txt += "\t" + str(tuple[0]) + " : " + str(tuple[1]) + ",\n"
                            txt += "}\n```"
                            await message.channel.send(txt)
                            return

                    else:
                        # embed = self.create_embed("You cannot do this action", "You are not allowed to do this action. Only creators of the bot can do this action.", 0xff8000, "")
                        # await message.channel.send(embed=embed)
                        return


                if message.guild.id == Ids["Support"]:
                    # perms muet
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
                        contenu = ""
                        for part in msg:
                            contenu += " " + part
                        embed = self.create_embed("Suggestion from " + message.author.name + " (" + str(message.author.id) + ")", contenu, message.author.color, "")
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
                        contenu = ""
                        for part in msg:
                            contenu += " " + part
                        embed = self.create_embed("Bug report by " + message.author.name + " (" + str(message.author.id) + ")", contenu, message.author.color, "")
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
                        tickets = self.get_channel(767418391559929906)
                        put_bot = self.get_channel(722025320202633323)
                        feedback = self.get_channel(719827869295050812)
                        guild = self.get_guild(Ids["Support"])
                        bot_creator = discord.utils.get(guild.roles, id=719538013859872880)
                        bot_staff = discord.utils.get(guild.roles, id=743796789769142354)
                        embed = self.create_embed("Welcome in the Support server for Clash INFO !",
                                                  f"Welcome ! Here is the support server of the {bot.mention} bot.\n\n{Emojis['Yes']} You can : {Emojis['Yes']}\n- Take your roles : {auto_roles.mention}\n- Follow the channel {clash_info.mention} to informe all your server about bot updates\n- Ask a question about the bot : {support.mention}\n- Take a ticket to speak with us : {tickets.mention}\n- Send us a suggestion : {sugg.mention}\n- Notify us of a bug : {bug.mention}\n- Test the bot : {test01.mention}, {test02.mention}, {test03.mention}\n- Put the bot on your server : {put_bot.mention}\n- Rate the BOT : {feedback.mention}\n\n⚠️ You must : ⚠️\n- Respect the Discord ToS (https://discord.com/new/terms) and the Discord Guidelines (https://discord.com/new/guidelines)\n- Respect the language of each channel (with the flag emoji in the channel name). Default = English ONLY\n\n{Emojis['No']} You cannot : {Emojis['No']}\n- Put `| Clash INFO` after your name or `[role]` before your name without authorization from an {bot_creator.mention}\n- Put the same profile picture or name as an {bot_staff.mention}\n\nClick on {Emojis['Yes']} to access the whole server.",
                                                  0x00ff00, "")
                        a = await message.channel.send(embed=embed)
                        await a.add_reaction(Emojis["Yes"])
                        return
                    # auto-roles
                    if message.content == prefix + "auto-roles langues" and message.author.id in Ids["Creators"]:
                        await message.channel.trigger_typing()
                        await message.delete()
                        msg = ""
                        for emoji, nom in Emojis["Languages_emojis"].items():
                            langue = discord.utils.get(message.guild.roles, name=nom)
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
                if everyone:
                    for member in message.guild.members:
                        if await self.mention(message, member) == -1:
                            return
                if user_mention != []:
                    for member in user_mention:
                        if not str(member) in liste_ok:
                            liste_ok.append(str(member))
                            if await self.mention(message, member) == -1:
                                return
                if role_mention != []:
                    for role in role_mention:
                        for member in role.members:
                            if not str(member) in liste_ok:
                                liste_ok.append(str(member))
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


            # UTILITAIRE
            # membre info
            if message.content.startswith(prefix + "member info"):
                await message.channel.trigger_typing()
                perms = ""
                if member.guild_permissions.administrator:
                    perms += "Administrator\n"
                if member.guild_permissions.ban_members:
                    perms += "Ban members\n"
                if member.guild_permissions.kick_members:
                    perms += "Kick off members\n"
                if member.guild_permissions.manage_roles:
                    perms += "Manage roles\n"
                if member.guild_permissions.manage_permissions:
                    perms += "Manage permissions\n"
                if member.guild_permissions.manage_guild:
                    perms += "Manage server\n"
                if member.guild_permissions.manage_channels:
                    perms += "Manage channel\n"
                if member.guild_permissions.manage_messages:
                    perms += "Manage messages\n"
                if member.guild_permissions.manage_nicknames:
                    perms += "Manage nicknames\n"
                if member.guild_permissions.mention_everyone:
                    perms += "Mention everyone\n"
                if member.guild_permissions.view_audit_log:
                    perms += "View logs\n"
                rejoint_brut = (str(member.joined_at).split(" ")[0])
                rejoint = (rejoint_brut.split("-")[2]) + "/" + (rejoint_brut.split("-")[1]) + "/" + (rejoint_brut.split("-")[0])
                cree_brut = (str(member.created_at).split(" ")[0])
                cree = (cree_brut.split("-")[2]) + "/" + (cree_brut.split("-")[1]) + "/" + (cree_brut.split("-")[0])
                if perms == "":
                    perms = "Any"
                embed = self.create_embed(member.name, "*The date format is DD/MM/YYYY*\n" + str(Emojis["Invite"]) + " Server join : **" + rejoint + "**.\n" + str(Emojis["Discord"]) + " Discord account creation : **" + cree + "**\n\n**Member permissions :**\n" + perms, member.color, "")
                embed.set_thumbnail(url=member.avatar_url)
                await message.channel.send(embed=embed)
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
                        asyncio.sleep(x)
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


async def test(self, message):
    await ascii(message, (Image.open("../Pictures/Welcome.png")))
    img = await canvas(message, (Image.open("../Pictures/Welcome.png")))
    await ascii(message, img)

async def ascii(message, image):
    # --lettres_taux_noir--
    IMAGE_WIDTH = 60
    IMAGE_HEIGHT = 100
    font = ImageFont.truetype("../ttf/JetBrainsMono-Regular.ttf", 100)
    characteres = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    char = {}
    for i in characteres:
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
        # buffer_output = io.BytesIO()
        # im.save(buffer_output, format="PNG")
        # buffer_output.seek(0)
        # await message.channel.send(file=discord.File(buffer_output, "../Pictures/Welcome.png"))
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

async def canvas(message, image):
    await message.channel.trigger_typing()

    IMAGE_WIDTH, IMAGE_HEIGHT = image.size

    # --- avatar ---
    avatar_asset = message.author.avatar_url

    # read JPG from server to buffer (file-like object)
    buffer_avatar = io.BytesIO()
    await avatar_asset.save(buffer_avatar)
    buffer_avatar.seek(0)

    # read JPG from buffer to Image
    avatar_image = Image.open(buffer_avatar)
    avatar_size = 1080
    image = image.resize((1920, 1080))
    IMAGE_WIDTH, IMAGE_HEIGHT = image.size
    avatar_image = avatar_image.resize((avatar_size, avatar_size))

    background = Image.open("../Pictures/Welcome.png")
    foreground = avatar_image
    x = 0
    y = (IMAGE_HEIGHT - avatar_size) // 2
    background.paste(foreground, (x, y), foreground)
    image = background

    # --- draw on image ---
    # create object for drawing
    draw = ImageDraw.Draw(image)

    # draw text in center
    font = ImageFont.truetype("Supercell-magic-webfont.x-font-ttf", 100)
    text_width, text_height = draw.textsize("Welcome " + message.author.name, font=font)
    x = (IMAGE_WIDTH - text_width) // 2
    y = (IMAGE_HEIGHT - text_height) // 2 - 400
    draw.text((x, y), "Welcome " + message.author.name, fill=(0, 0, 255), font=font)
    text_width, text_height = draw.textsize("Clash INFO support server", font=font)
    x = (IMAGE_WIDTH - text_width) // 2
    y = (IMAGE_HEIGHT - text_height) // 2 + 400
    draw.text((x, y), "Clash INFO support server", fill=(0, 0, 255), font=font)

    # --- sending image ---
    buffer_output = io.BytesIO()
    image.save(buffer_output, format="PNG")
    buffer_output.seek(0)
    await message.author.send("Welcome to the `ServerName` server ! You must check the rules (#channel) to access the whole server.\n\nYou can join our partners :\n- Clash Of Clans Community (discord.gg/XXXXX)\n- Discord Developpers (discord.gg/XXXXX)\n...", file=discord.File(buffer_output, "../Pictures/Welcome.png"))
    return image
