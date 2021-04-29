# ----- PACKAGES : -----
import dbl
import coc
import requests
import json
import sys
import time


# ----- PROJECT FILES : -----
from Script.import_functions import *


# ----- COMMANDS : -----

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
from Script.Commands.Messages.Useful.bot_info import bot_info
from Script.Commands.Messages.Useful.add_the_bot import add_the_bot_default, add_the_bot_administrator
from Script.Commands.Messages.Useful.support_server import support_server
from Script.Commands.Messages.Useful.promote_the_bot import promote_the_bot
from Script.Commands.Messages.Useful.youtube import youtube

from Script.Commands.Messages.Moderation.delete_messages import delete_messages_number, delete_messages_time, delete_messages_all

from Script.Commands.Messages.Creators.add_a_bot_id import add_a_bot_id
from Script.Commands.Messages.Creators.add_reaction_with_id import add_reaction_with_id
from Script.Commands.Messages.Creators.download_emojis import download_emojis
from Script.Commands.Messages.Creators.find_user_by_id import find_user_by_id
from Script.Commands.Messages.Creators.refresh_dbl import refresh_dbl
from Script.Commands.Messages.Creators.servers_list import servers_list


# ----- VARIABLES : -----

# MODIFIABLE VARIABLES
def_prefix = open("Script/Modifiable_variables/prefix.json", "r")
Prefix_txt = def_prefix.read()
def_prefix.close()
Prefix = json.loads(Prefix_txt)

def_votes = open("Script/Modifiable_variables/votes.json", "r")
Votes_txt = def_votes.read()
def_votes.close()
Votes = json.loads(Votes_txt)

def_support = open("Script/Modifiable_variables/support_role_ for_tickets.json", "r")
Support_txt = def_support.read()
def_support.close()
Support = json.loads(Support_txt)


Default_color = 0x00ffff


if __name__ == "__main__":

    print(f"Python : {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print("DBL : " + str(dbl.__version__))
    print("CoC : " + str(coc.__version__))
    print("Discord : " + str(discord.__version__))

    from discord_slash import SlashCommand
    from Script.Clients.discord import Clash_info
    Client_slash = SlashCommand(Clash_info)


    @Client_slash.slash(name="help")
    async def _help(ctx):
        await help(ctx)
        return

    @Client_slash.slash(name="_help")
    async def __help(ctx):
        await help(ctx)
        return


    # Clash Of Clans

    @Client_slash.slash(name="get_player")
    async def _get_player(ctx, player_tag, information):
        await get_player(ctx, player_tag, information)
        return

    @Client_slash.slash(name="get_clan")
    async def _get_clan(ctx, clan_tag):
        await get_clan(ctx, clan_tag)
        return

    @Client_slash.slash(name="search_clan")
    async def _search_clan(ctx, name, number=10):
        await search_clan(ctx, name, number)
        return

    @Client_slash.slash(name="clan_members")
    async def _clan_members(ctx, clan_tag):
        await clan_members(ctx, clan_tag)
        return

    @Client_slash.slash(name="buildings_th")
    async def _buildings_th(ctx, th_level=0):
        await buildings_th(ctx, th_level)
        return

    @Client_slash.slash(name="buildings_bh")
    async def _buildings_bh(ctx, bh_level=0):
        await buildings_bh(ctx, bh_level)
        return

    @Client_slash.subcommand(base="auto_roles", name="th")
    async def _auto_roles_th(ctx, channel=None):
        if channel is None:
            channel = ctx.channel
        await auto_roles_th(ctx, channel)
        return

    @Client_slash.subcommand(base="auto_roles", name="bh")
    async def _auto_roles_bh(ctx, channel=None):
        if channel is None:
            channel = ctx.channel
        await auto_roles_bh(ctx, channel)
        return

    @Client_slash.subcommand(base="auto_roles", name="leagues")
    async def _auto_roles_leagues(ctx, channel=None):
        if channel is None:
            channel = ctx.channel
        await auto_roles_leagues(ctx, channel)
        return

    @Client_slash.slash(name="file")
    async def _file(ctx):
        await coc_file(ctx)
        return


    # USEFUL

    @Client_slash.slash(name="tickets")
    async def _tickets(ctx, text, variable1=None, variable2=None):
        if variable1 is None:
            ticket_channel = ctx.channel
            support = None
        elif variable2 is None:
            ticket_channel = ctx.guild.get_channel(int(variable1))
            if ticket_channel is None:
                support = ctx.guild.get_role(int(variable1))
                ticket_channel = ctx.channel
            else:
                support = None
        else:
            ticket_channel = ctx.guild.get_channel(int(variable1))
            support = ctx.guild.get_role(int(variable2))
        await tickets(ctx, text, ticket_channel, support)
        Support.update({str(ctx.guild.id): support.id})
        return

    @Client_slash.slash(name="close_ticket")
    async def _close_ticket(ctx, channel=None):
        if channel is None:
            channel = ctx.channel
        else:
            channel = ctx.guild.get_channel(int(channel))
        await close_ticket(ctx, channel)
        return

    @Client_slash.slash(name="member_info")
    async def _member_info(ctx, member):
        await member_info(ctx, member)
        return

    @Client_slash.slash(name="role_info")
    async def _role_info(ctx, role):
        await role_info(ctx, role)
        return

    @Client_slash.slash(name="server_info")
    async def _server_info(ctx):
        await server_info(ctx)
        return

    @Client_slash.slash(name="emoji_info")
    async def _emoji_info(ctx, emoji):
        await emoji_info(ctx, emoji)
        return

    @Client_slash.subcommand(base="direct_message", name="member")
    async def _direct_message_member(ctx, member, text):
        await direct_message_member(ctx, member, text)
        return

    @Client_slash.subcommand(base="direct_message", name="role")
    async def _direct_message_member(ctx, role, text):
        await direct_message_role(ctx, role, text)
        return

    @Client_slash.slash(name="poll")
    async def _poll(ctx, question):
        await poll(ctx, question)
        return

    @Client_slash.slash(name="bot_info")
    async def _bot_info(ctx):
        await bot_info(ctx)
        return

    @Client_slash.subcommand(base="add_the_bot", name="default")
    async def _add_the_bot_default(ctx):
        await add_the_bot_default(ctx)
        return

    @Client_slash.subcommand(base="add_the_bot", name="administrator")
    async def _add_the_bot_administrator(ctx):
        await add_the_bot_administrator(ctx)
        return


    @Client_slash.slash(name="support_server")
    async def _support_server(ctx):
        await support_server(ctx)
        return

    @Client_slash.slash(name="promote_the_bot")
    async def _promote_the_bot(ctx):
        await promote_the_bot(ctx)
        return

    @Client_slash.slash(name="youtube")
    async def _youtube(ctx):
        await youtube(ctx)
        return


    # MODERATION

    @Client_slash.subcommand(base="delete_messages", name="number_of_messages")
    async def _delete_messages_number(ctx, number_of_messages):
        await delete_messages_number(ctx, number_of_messages)
        return

    @Client_slash.subcommand(base="delete_messages", name="for_x_minutes")
    async def _delete_messages_time(ctx, minutes):
        await delete_messages_time(ctx, minutes)
        return

    @Client_slash.subcommand(base="delete_messages", name="all")
    async def _delete_messages_all(ctx):
        await delete_messages_all(ctx)
        return


    # CREATORS

    @Client_slash.slash(name="__add_a_bot_id")
    async def ___add_a_bot_id(ctx, id):
        await add_a_bot_id(ctx, id)
        return

    @Client_slash.slash(name="__add_reactino_with_id")
    async def ___add_reaction_with_id(ctx, channel_id, message_id, emoji_id):
        await add_reaction_with_id(ctx, channel_id, message_id, emoji_id)
        return

    @Client_slash.slash(name="__download_emojis")
    async def ___download_emojis(ctx):
        await download_emojis(ctx)
        return

    @Client_slash.slash(name="__find_user_by_id")
    async def ___find_user_by_id(ctx, user_id):
        await find_user_by_id(ctx, user_id)
        return

    @Client_slash.slash(name="__refresh_dbl")
    async def ___refresh_dbl(ctx):
        await refresh_dbl(ctx)
        return

    @Client_slash.slash(name="__servers_list")
    async def ___servers_list(ctx):
        await servers_list(ctx)
        return


    from Script.Clients.discord import Token
    Bot_id = Clash_info.id
    def add_slash_command_json(json_dict):
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/commands"
        req = requests.post(url, headers=headers, json=json_dict)
        print(json_dict.get("name"), req)
        if not req.ok:
            print(json_dict["name"], req.content)
            try:
                time.sleep(req.json()["retry_after"])
                add_slash_command_json(json_dict)
            except:
                pass
    def add_slash_command_json_guild(json_dict):
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/guilds/710237092931829893/commands"
        req = requests.post(url, headers=headers, json=json_dict)
        print(json_dict.get("name"), req)
        if not req.ok:
            print(json_dict["name"], req.content)
            try:
                time.sleep(req.json()["retry_after"])
                add_slash_command_json(json_dict)
            except:
                pass

    def see_slash_commands():
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/commands"
        req = requests.get(url, headers=headers)
        dict = json.loads(req.content)
        print("Slash Commands list : ", end="")
        for command in dict:
            print(command["name"], end=", ")
        print()
    def dlt_slash_command(name):
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/commands"
        req = requests.get(url, headers=headers)
        dict = json.loads(req.content)
        for command in dict:
            if command.get("name") == name:
                url += "/" + str(command.get("id"))
                req = requests.delete(url, headers=headers)
                print(req)
                print(req.content)
        print("Content :", req.content)

    def see_slash_command_guild():
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/guilds/710237092931829893/commands"
        req = requests.get(url, headers=headers)
        print(req.content)
    def dlt_slash_command_guild(id):
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/guilds/710237092931829893/commands/"+str(id)
        req = requests.delete(url, headers=headers)
        print(req.content)


    Clash_info.run(Token)  # Comment this line to create slash commands

    json__help = {
        "name": "_help",
        "description": "Show the help message to use @Clash INFO#3976"
    }
    add_slash_command_json(json__help)
    json_help = json__help
    json_help["name"] = "help"
    add_slash_command_json(json_help)

    # Clash Of Clans
    json_buildings_th = {
        "name": "buildings_th",
        "description": "Show the maximum level for each buildings at the given Town Hall level",
        "options": [{
            "name": "town_hall_level",
            "description": "Town Hall level",
            "required": False,
            "type": 4,
        }]
    }
    add_slash_command_json(json_buildings_th)
    json_buildings_bh = {
        "name": "buildings_bh",
        "description": "Show the maximum level for each buildings at the given Builder Hall level",
        "options": [{
            "name": "builder_hall_level",
            "description": "Builder Hall level",
            "required": False,
            "type": 4,
        }]
    }
    add_slash_command_json(json_buildings_bh)
    json_get_player = {
        "name": "get_player",
        "description": "Show data about the player (with the troops players on the 3rd page)",
        "options": [{
            "name": "player_tag",
            "description": "Clash Of Clans player tag, format : #A1B2C3D4",
            "required": True,
            "type": 3,
        }, {
            "name": "information",
            "description": "Information",
            "required": True,
            "type": 3,
            "choices": [{
                "name": "main",
                "value": "main"
            }, {
                "name": "builder_base",
                "value": "builder_base"
            }, {
                "name": "troops",
                "value": "troops"
            }, {
                "name": "success",
                "value": "success"
            }]

        }]
    }
    add_slash_command_json(json_get_player)
    json_get_clan = {
        "name": "get_clan",
        "description": "Show data about the clan",
        "options": [{
            "name": "clan_tag",
            "description": "Clash Of Clans clan tag, format : #A1B2C3D4",
            "required": True,
            "type": 3,
        }]
    }
    add_slash_command_json(json_get_clan)
    json_search_clan = {
        "name": "search_clan",
        "description": "Search clans by name",
        "options": [{
            "name": "name",
            "description": "Clan name",
            "required": True,
            "type": 3
        }, {
            "name": "number",
            "description": "Number of clans to show",
            "required": False,
            "type": 4
        }]
    }
    add_slash_command_json(json_search_clan)
    json_clan_members = {
        "name": "clan_members",
        "description": "Show the clan members",
        "options": [{
            "name": "clan_tag",
            "description": "Clash Of Clans clan tag, format : #A1B2C3D4",
            "required": True,
            "type": 3,
        }]
    }
    add_slash_command_json(json_clan_members)
    json_auto_roles = {
        "name": "auto_roles",
        "description": "[Administrators only] Create an auto-roles system to give roles",
        "options": [{
            "name": "th",
            "description": "[Administrators only] Create an auto-roles system to give the TH level roles",
            "type": 1,
            "options": [{
                "name": "channel",
                "description": "Channel where it will be the auto-roles system",
                "required": False,
                "type": 7
            }]
        }, {
            "name": "bh",
            "description": "[Administrators only] Create an auto-roles system to give the BH level roles",
            "type": 1,
            "options": [{
                "name": "channel",
                "description": "Channel where it will be the auto-roles system",
                "required": False,
                "type": 7
            }]
        }, {
            "name": "leagues",
            "description": "[Administrators only] Create an auto-roles system to give the league role",
            "type": 1,
            "options": [{
                "name": "channel",
                "description": "Channel where it will be the auto-roles system",
                "required": False,
                "type": 7
            }]
        }]
    }
    add_slash_command_json(json_auto_roles)
    json_file = {
        "name": "file",
        "description": "Give the link for the Clash Of Clans data sheet"
    }
    add_slash_command_json(json_file)


    # Useful
    json_bot_info = {
        "name": "bot_info",
        "description": "Show some information about the bot (including the bot required permissions)"
    }
    add_slash_command_json(json_bot_info)
    json_tickets = {
        "name": "tickets",
        "description": "[Administrators only] Create a ticket category, channel and message",
        "options": [{
            "name": "text",
            "description": "The text of the ticket-message",
            "required": True,
            "type": 3
        }, {
            "name": "ticket_channel",
            "description": "The channel with the ticket-message",
            "required": False,
            "type": 7
        }, {
            "name": "support_role",
            "description": "This role will view all tickets",
            "required": False,
            "type": 8
        }]
    }
    add_slash_command_json(json_tickets)
    json_close = {
        "name": "close_ticket",
        "description": "[Channels managers only] Close the ticket",
        "options": [{
            "name": "channel",
            "description": "The ticket-channel to close",
            "required": False,
            "type": 7
        }]
    }
    add_slash_command_json(json_close)
    json_poll = {
        "name": "poll",
        "description": "Show a poll with the question",
        "options": [{
            "name": "question",
            "description": "The poll question",
            "required": True,
            "type": 3
        }]
    }
    add_slash_command_json(json_poll)
    json_dm = {
        "name": "direct_message",
        "description": "Send a direct message to a member/role",
        "options": [{
            "name": "member",
            "description": "Send a direct message to a member",
            "type": 1,
            "options": [{
                "name": "member",
                "description": "Send a direct message to this member",
                "required": True,
                "type": 6
            }, {
                "name": "text",
                "description": "The text to send to this member",
                "required": True,
                "type": 3
            }]
        }, {
            "name": "role",
            "description": "[Administrators only] Send a direct message to a role",
            "type": 1,
            "options": [{
                "name": "role",
                "description": "Send a direct message to everyone who has this role",
                "required": True,
                "type": 8
            }, {
                "name": "text",
                "description": "The text to send to everyone who has this role",
                "required": True,
                "type": 3
            }]
        }]
    }
    add_slash_command_json(json_dm)
    json_yt = {
        "name": "youtube",
        "description": "Show the YouTube channel dedicated to the bot (bot presentation, news...)"
    }
    add_slash_command_json(json_yt)
    json_member_info = {
        "name": "member_info",
        "description": "Show permissions, when the member joined Discord / the server and his avatar",
        "options": [{
            "name": "member",
            "description": "The member",
            "required": True,
            "type": 6
        }]
    }
    add_slash_command_json(json_member_info)
    json_role_info = {
        "name": "role_info",
        "description": "Show permissions and who have this role",
        "options": [{
            "name": "role",
            "description": "The role",
            "required": True,
            "type": 8
        }]
    }
    add_slash_command_json(json_role_info)
    json_server_info = {
        "name": "server_info",
        "description": "Show some information about the server"
    }
    add_slash_command_json(json_server_info)
    json_add_the_bot = {
        "name": "add_the_bot",
        "description": "Show the link to invite the bot to your server",
        "options": [{
            "name": "administrator",
            "description": "Allows you to add the bot as an administrator, so you will not have to worry about bot permissions",
            "type": 1,
        }, {
            "name": "default",
            "description": "Allows you to manage each permission for the bot",
            "type": 1,
        }]
    }
    add_slash_command_json(json_add_the_bot)
    json_support_server = {
        "name": "support_server",
        "description": "Show the link to join the bot support server"
    }
    add_slash_command_json(json_support_server)
    json_promote_the_bot = {
        "name": "promote_the_bot",
        "description": "Show the links to promote the bot"
    }
    add_slash_command_json(json_promote_the_bot)


    #Moderation
    json_delete_messages = {
        "name": "delete_messages",
        "description": "[Messages managers only] Delete the most recent and not-pinned messages in the current channel",
        "options": [{
            "name": "number_of_messages",
            "description": "[Messages managers only] Delete the most recent and not-pinned messages in the current channel",
            "type": 1,
            "options": [{
                "name": "number_of_messages",
                "description": "Number of messages",
                "required": True,
                "type": 4
            }]
        }, {
            "name": "for_x_minutes",
            "description": "[Messages managers only] Delete not-pinned messages in the current channel sent for x minutes",
            "type": 1,
            "options": [{
                "name": "minutes",
                "description": "Duration in minutes",
                "required": True,
                "type": 4,
            }]
        }, {
            "name": "all",
            "description": "[Messages managers only] Delete ALL not-pinned messages in the current channel",
            "type": 1
        }]
    }
    add_slash_command_json(json_delete_messages)
    json_emoji_info = {
        "name": "emoji_info",
        "description": "Show some information about the emoji",
        "options": [{
            "name": "emoji",
            "description": "The emoji",
            "required": True,
            "type": 3
        }]
    }
    add_slash_command_json(json_emoji_info)

    json_template = {
        "name": "",
        "description": "",
        "options": [{
            "name": "",
            "description": "",
            "required": True,
            "type": 0,
            "choices": [{}, {}]
        }]
    }

    see_slash_commands()
    see_slash_command_guild()

    Clash_info.run(Token)
