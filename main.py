# ----- PACKAGES : -----
import coc
import json

import discord.errors
import requests
import sqlite3
import sys
import time
import topgg

# ----- PROJECT FILES : -----
from Data.utils import Utils
from Script.import_functions import *


# ----- COMMANDS : -----

# MESSAGES
from Script.Commands.Messages.help import help

from Script.Commands.Messages.Clash_Of_Clans.buildings_bh import buildings_bh
from Script.Commands.Messages.Clash_Of_Clans.buildings_th import buildings_th
from Script.Commands.Messages.Clash_Of_Clans.coc_file import coc_file
from Script.Commands.Messages.Clash_Of_Clans.clan_info import clan_info
from Script.Commands.Messages.Clash_Of_Clans.clan_members import clan_members
from Script.Commands.Messages.Clash_Of_Clans.search_clan import search_clan
from Script.Commands.Messages.Clash_Of_Clans.auto_roles import auto_roles_th, auto_roles_bh, auto_roles_leagues
from Script.Commands.Messages.Clash_Of_Clans.link_coc_account import link_coc_account
from Script.Commands.Messages.Clash_Of_Clans.player_info import player_info

from Script.Commands.Messages.Useful.add_the_bot import add_the_bot_default, add_the_bot_administrator
from Script.Commands.Messages.Useful.github import github
from Script.Commands.Messages.Useful.promote_the_bot import promote_the_bot
from Script.Commands.Messages.Useful.support_server import support_server
from Script.Commands.Messages.Useful.youtube import youtube
from Script.Commands.Messages.Useful.bot_info import bot_info
from Script.Commands.Messages.Useful.emoji_info import emoji_info
from Script.Commands.Messages.Useful.member_info import member_info
from Script.Commands.Messages.Useful.role_info import role_info
from Script.Commands.Messages.Useful.server_info import server_info
from Script.Commands.Messages.Useful.direct_message import direct_message_member, direct_message_role
from Script.Commands.Messages.Useful.poll import poll
from Script.Commands.Messages.Useful.tickets import tickets, close_ticket

from Script.Commands.Messages.Moderation.delete_messages import delete_messages_number, delete_messages_time, delete_messages_all

from Script.Commands.Messages.Creators.add_a_bot_id import add_a_bot_id
from Script.Commands.Messages.Creators.add_reaction_with_id import add_reaction_with_id
from Script.Commands.Messages.Creators.download_emojis import download_emojis
from Script.Commands.Messages.Creators.find_user_by_id import find_user_by_id
from Script.Commands.Messages.Creators.refresh_dbl import refresh_dbl
from Script.Commands.Messages.Creators.servers_list import servers_list
from Script.Commands.Messages.Creators.stats import stats


# ----- VARIABLES : -----

# MODIFIABLE VARIABLES
def_votes = open(Utils["secure_folder_path"] + "votes.json", "r")
Votes_text = def_votes.read()
def_votes.close()
Votes = json.loads(Votes_text)

def_support = open(Utils["secure_folder_path"] + "support_for_tickets.json", "r")
Support_text = def_support.read()
def_support.close()
Support = json.loads(Support_text)


Default_color = 0x00ffff


if __name__ == "__main__":

    print(f"Python : {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print("DBL : " + str(topgg.__version__))
    print("CoC : " + str(coc.__version__))
    print("Discord : " + str(discord.__version__))

    from discord_slash import SlashCommand
    from Script.Clients.discord_client import Clash_info
    Client_slash = SlashCommand(Clash_info)

    connection_modifiable = sqlite3.connect(Utils["secure_folder_path"] + "Modifiable.sqlite")
    cursor_modifiable = connection_modifiable.cursor()

    connection_constants = sqlite3.connect("Data/Constants.sqlite")
    connection_constants.row_factory = sqlite3.Row
    cursor_constants = connection_constants.cursor()


    async def check_cmd_perms(ctx):
        if ctx.data['name'] == "_help":
            ctx.data['name'] = "help"
        cursor_constants.execute(f"""SELECT user_permissions, bot_permissions FROM RequiredPermissions WHERE command_name = '{ctx.data["name"]}'""")
        perms_dict = dict(cursor_constants.fetchall()[0])
        if perms_dict["bot_permissions"]:
            perms_dict["bot_permissions"] += ", embed_links, external_emojis, send_messages, view_channel"
        else:
            perms_dict["bot_permissions"] = "embed_links, external_emojis, send_messages, view_channel"
        if perms_dict["user_permissions"]:
            perms_dict["user_permissions"] += ", use_slash_commands"
        else:
            perms_dict["user_permissions"] = "use_slash_commands"
        channel = Clash_info.get_channel(ctx.channel_id)
        me = channel.guild.me
        missing_bot_perms = []
        for perm in perms_dict["bot_permissions"].split(", "):
            if not getattr(channel.permissions_for(me), perm):
                missing_bot_perms.append(perm)
        missing_user_perms = []
        if perms_dict["user_permissions"]:
            for perm in perms_dict["user_permissions"].split(", "):
                if not getattr(channel.permissions_for(ctx.author), perm):
                    missing_user_perms.append(perm)
        if missing_bot_perms or missing_user_perms:
            text = ""
            if "send_messages" in missing_bot_perms or "view_channel" in missing_bot_perms:
                try:
                    await ctx.author.send("The bot doesn't have the 'send_messages' or the 'view_channel' permission(s) ! Please grant it/them to the bot and send again the command.")
                except discord.errors.Forbidden:
                    pass
                return -1
            if "embed_links" in missing_bot_perms:
                await ctx.send("The bot doesn't have the 'embed_links' permission ! Please grant it to the bot and send again the command.")
                return -1
            if missing_bot_perms:
                text += "The bot doesn't have the permission(s) :"
                for perm in missing_bot_perms:
                    text += "\n" + perm
                text += "\nPlease grant it/them to the bot and send again the command."
            if missing_user_perms:
                text += "You don't have this/these permission(s) :"
                for perm in missing_user_perms:
                    text += "\n" + perm
                text += "\nThis/These permission(s) is/are required to use this command."  # TODO : Split 2 cases ?
            embed = create_embed("Missing permissions", text, 0xFF0000, "", channel.guild.me.avatar_url)
            await ctx.send(embed=embed)
            return -1
        return


    def edit_commands_used(user_id, cmd):
        text = f"""INSERT INTO BotUsage(user_id) SELECT({user_id}) WHERE NOT EXISTS(SELECT 1 FROM BotUsage WHERE user_id={user_id})"""
        cursor_modifiable.execute(text)
        text = f"""UPDATE BotUsage SET {cmd} = (SELECT {cmd} FROM BotUsage WHERE user_id={user_id})+1 WHERE user_id={user_id}"""
        cursor_modifiable.execute(text)
        connection_modifiable.commit()


    # TODO : Replace @decorator by functions => less "\n" ?
    @Client_slash.slash(name="help")
    async def _help(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await help(ctx)
        edit_commands_used(ctx.author_id, "help")
        return

    @Client_slash.slash(name="_help")
    async def __help(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await help(ctx)
        edit_commands_used(ctx.author_id, "help")
        return


    # Clash Of Clans

    @Client_slash.subcommand(base="auto_roles", name="bh")
    async def _auto_roles_bh(ctx, channel=None):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        if channel is None:
            channel = ctx.channel
        await auto_roles_bh(ctx, channel)
        edit_commands_used(ctx.author_id, "auto_roles__bh")
        return

    @Client_slash.subcommand(base="auto_roles", name="leagues")
    async def _auto_roles_leagues(ctx, channel=None):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        if channel is None:
            channel = ctx.channel
        await auto_roles_leagues(ctx, channel)
        edit_commands_used(ctx.author_id, "auto_roles__leagues")
        return

    @Client_slash.subcommand(base="auto_roles", name="th")
    async def _auto_roles_th(ctx, channel=None):
        if await check_cmd_perms(ctx) == -1:  # TODO : Check with the ctx.channel permission, instead of channel permission
            return
        await ctx.defer()
        if channel is None:
            channel = ctx.channel
        await auto_roles_th(ctx, channel)
        edit_commands_used(ctx.author_id, "auto_roles__th")
        return

    @Client_slash.slash(name="buildings_bh")
    async def _buildings_bh(ctx, builder_hall_level=0):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await buildings_bh(ctx, builder_hall_level)
        edit_commands_used(ctx.author_id, "buildings_bh")
        return

    @Client_slash.slash(name="buildings_th")
    async def _buildings_th(ctx, town_hall_level=0):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await buildings_th(ctx, town_hall_level)
        edit_commands_used(ctx.author_id, "buildings_th")
        return

    @Client_slash.slash(name="clan_info")
    async def _clan_info(ctx, clan_tag):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await clan_info(ctx, clan_tag)
        edit_commands_used(ctx.author_id, "clan_info")
        return

    @Client_slash.slash(name="clan_members")
    async def _clan_members(ctx, clan_tag):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await clan_members(ctx, clan_tag)
        edit_commands_used(ctx.author_id, "clan_members")
        return

    @Client_slash.slash(name="file")
    async def _file(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await coc_file(ctx)
        edit_commands_used(ctx.author_id, "file")
        return

    @Client_slash.slash(name="player_info")
    async def _player_info(ctx, player_tag, information):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await player_info(ctx, player_tag, information)
        edit_commands_used(ctx.author_id, "player_info")
        return

    @Client_slash.slash(name="search_clan")
    async def _search_clan(ctx, name, number=10):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await search_clan(ctx, name, number)
        edit_commands_used(ctx.author_id, "search_clan")
        return


    # USEFUL

    @Client_slash.subcommand(base="add_the_bot", name="administrator")
    async def _add_the_bot_administrator(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await add_the_bot_administrator(ctx)
        edit_commands_used(ctx.author_id, "add_the_bot__administrator")
        return

    @Client_slash.subcommand(base="add_the_bot", name="default")
    async def _add_the_bot_default(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await add_the_bot_default(ctx)
        edit_commands_used(ctx.author_id, "add_the_bot__default")
        return

    @Client_slash.slash(name="bot_info")
    async def _bot_info(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await bot_info(ctx)
        edit_commands_used(ctx.author_id, "bot_info")
        return

    @Client_slash.subcommand(base="direct_message", name="member")
    async def _direct_message_member(ctx, member, text):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await direct_message_member(ctx, member, text)
        edit_commands_used(ctx.author_id, "direct_message__member")
        return

    @Client_slash.subcommand(base="direct_message", name="role")
    async def _direct_message_member(ctx, role, text):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await direct_message_role(ctx, role, text)
        edit_commands_used(ctx.author_id, "direct_message__role")
        return

    @Client_slash.slash(name="emoji_info")
    async def _emoji_info(ctx, emoji):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await emoji_info(ctx, emoji)
        edit_commands_used(ctx.author_id, "emoji_info")
        return

    @Client_slash.slash(name="github")
    async def _github(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await github(ctx)
        edit_commands_used(ctx.author_id, "github")
        return

    @Client_slash.slash(name="link_coc_account")
    async def _link_coc_account(ctx, player_tag, player_token):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await link_coc_account(ctx, player_tag, player_token)
        edit_commands_used(ctx.author_id, "link_coc_account")
        return

    @Client_slash.slash(name="member_info")
    async def _member_info(ctx, member):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await member_info(ctx, member)
        edit_commands_used(ctx.author_id, "member_info")
        return

    @Client_slash.slash(name="poll")
    async def _poll(ctx, question):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await poll(ctx, question)
        edit_commands_used(ctx.author_id, "poll")
        return

    @Client_slash.slash(name="promote_the_bot")
    async def _promote_the_bot(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await promote_the_bot(ctx)
        edit_commands_used(ctx.author_id, "promote_the_bot")
        return

    @Client_slash.slash(name="role_info")
    async def _role_info(ctx, role):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await role_info(ctx, role)
        edit_commands_used(ctx.author_id, "role_info")
        return

    @Client_slash.slash(name="server_info")
    async def _server_info(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await server_info(ctx)
        edit_commands_used(ctx.author_id, "server_info")
        return

    @Client_slash.slash(name="support_server")
    async def _support_server(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await support_server(ctx)
        edit_commands_used(ctx.author_id, "support_server")
        return

    @Client_slash.slash(name="tickets")
    async def _tickets(ctx, text, ticket_channel=None, support_role=None):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        if ticket_channel is None:
            ticket_channel = ctx.channel
        if support_role is not None:
            Support.update({ctx.guild.id: support_role.id})
        else:
            Support.pop(ctx.guild.id, None)
        await tickets(ctx, text, ticket_channel, support_role)
        edit_commands_used(ctx.author_id, "tickets")
        return

    @Client_slash.slash(name="close_ticket")
    async def _close_ticket(ctx, channel=None):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        if channel is None:
            channel = ctx.channel
        await close_ticket(ctx, channel)
        edit_commands_used(ctx.author_id, "close_ticket")
        return

    @Client_slash.slash(name="youtube")
    async def _youtube(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await youtube(ctx)
        edit_commands_used(ctx.author_id, "youtube")
        return


    # MODERATION

    @Client_slash.subcommand(base="delete_messages", name="all")
    async def _delete_messages_all(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await delete_messages_all(ctx)
        edit_commands_used(ctx.author_id, "delete_messages__all")
        return

    @Client_slash.subcommand(base="delete_messages", name="for_x_minutes")
    async def _delete_messages_time(ctx, minutes):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await delete_messages_time(ctx, minutes)
        edit_commands_used(ctx.author_id, "delete_messages__for_x_minutes")
        return

    @Client_slash.subcommand(base="delete_messages", name="number_of_messages")
    async def _delete_messages_number(ctx, number_of_messages):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await delete_messages_number(ctx, number_of_messages)
        edit_commands_used(ctx.author_id, "delete_messages__number_of_messages")
        return


    # CREATORS

    @Client_slash.slash(name="__add_a_bot_id")
    async def ___add_a_bot_id(ctx, bot_id):
        await ctx.defer()
        await add_a_bot_id(ctx, int(bot_id))
        return

    @Client_slash.slash(name="__add_reaction_with_id")
    async def ___add_reaction_with_id(ctx, channel_id, message_id, emoji_id):
        await ctx.defer()
        await add_reaction_with_id(ctx, int(channel_id), int(message_id), int(emoji_id))
        return

    @Client_slash.slash(name="__download_emojis")
    async def ___download_emojis(ctx, recreate_emojis_zip):
        await ctx.defer()
        await download_emojis(ctx, recreate_emojis_zip)
        return

    @Client_slash.slash(name="__find_user_by_id")
    async def ___find_user_by_id(ctx, user_id):
        await ctx.defer()
        await find_user_by_id(ctx, int(user_id))
        return

    @Client_slash.slash(name="__refresh_dbl")
    async def ___refresh_dbl(ctx):
        await ctx.defer()
        await refresh_dbl(ctx)
        return

    @Client_slash.slash(name="__servers_list")
    async def ___servers_list(ctx):
        await ctx.defer()
        await servers_list(ctx)
        return

    @Client_slash.slash(name="__stats")
    async def ___stats(ctx):
        await ctx.defer
        await stats(ctx)
        return


    from Script.Clients.discord_client import Token
    Bot_id = Clash_info.id
    def add_slash_command_json(json_dict):
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/commands"
        req = requests.post(url, headers=headers, json=json_dict)
        print(json_dict.get("name"), req)
        if not req.ok:
            print(json_dict["name"], req.content)
            if "retry_after" in list(req.json().keys()):
                time.sleep(req.json()["retry_after"])
                add_slash_command_json(json_dict)
    def add_slash_command_json_guild(json_dict):
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/guilds/710237092931829893/commands"
        req = requests.post(url, headers=headers, json=json_dict)
        print(json_dict.get("name"), req)
        if not req.ok:
            print(json_dict["name"], req.content)
            if "retry_after" in list(req.json().keys()):
                time.sleep(req.json()["retry_after"])
                add_slash_command_json(json_dict)

    def see_slash_commands():
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/commands"
        req = requests.get(url, headers=headers)
        json_dict = json.loads(req.content)
        print("Slash Commands list : ", end="")
        for command in json_dict:
            print(command["name"], end=", ")
        print()
    def dlt_slash_command(name):
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/commands"
        req = requests.get(url, headers=headers)
        json_dict = json.loads(req.content)
        for command in json_dict:
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
    def dlt_slash_command_guild(command_id):
        headers = {"Authorization": "Bot " + Token}
        url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/guilds/710237092931829893/commands/"+str(command_id)
        req = requests.delete(url, headers=headers)
        print(req.content)


    @Clash_info.event
    async def on_component(ctx):
        from Script.Commands.Components.Select_menu.change_th_lvl import change_th_lvl
        await change_th_lvl(ctx)
        from Script.Commands.Components.Select_menu.change_bh_lvl import change_bh_lvl
        await change_bh_lvl(ctx)
        from Script.Commands.Components.Select_menu.change_player_info_page import change_player_stats_page
        await change_player_stats_page(ctx)
        return


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
    json_clan_info = {
        "name": "clan_info",
        "description": "Show data about the clan",
        "options": [{
            "name": "clan_tag",
            "description": "Clash Of Clans clan tag, format : #A1B2C3D4",
            "required": True,
            "type": 3,
        }]
    }
    add_slash_command_json(json_clan_info)
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
    json_file = {
        "name": "file",
        "description": "Give the link for the Clash Of Clans data sheet"
    }
    add_slash_command_json(json_file)
    json_link_coc_account = {
        "name": "link_coc_account",
        "description": "Link your Clash Of Clans account to your Discord account",
        "options": [{
            "name": "player_tag",
            "description": "Your Clash Of Clans tag",
            "required": True,
            "type": 3,
        }, {
            "name": "player_token",
            "description": "Your token",
            "required": True,
            "type": 3,
        }]
    }
    add_slash_command_json(json_link_coc_account)
    json_player_info = {
        "name": "player_info",
        "description": "Show data about the player",
        "options": [{
            "name": "player_tag",
            "description": "Clash Of Clans player tag, format : #A1B2C3D4",
            "required": True,
            "type": 3,
        }, {
            "name": "information",
            "description": "Information wanted",
            "required": True,
            "type": 3,
            "choices": [{
                "name": "main",
                "value": "main"
            }, {
                "name": "troops",
                "value": "troops"
            }, {
                "name": "success",
                "value": "success"
            }]

        }]
    }
    add_slash_command_json(json_player_info)
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

    # Useful
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
    json_bot_info = {
        "name": "bot_info",
        "description": "Show some information about the bot"
    }
    add_slash_command_json(json_bot_info)
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
    json_dm = {
        "name": "direct_message",
        "description": "[Administrators only] Send a direct message to a member/role",
        "options": [{
            "name": "member",
            "description": "[Administrators only] Send a direct message to a member",
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
    json_github = {
        "name": "github",
        "description": "You can check our GitHub to help us to improve the bot"
    }
    add_slash_command_json(json_github)
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
    json_promote_the_bot = {
        "name": "promote_the_bot",
        "description": "Show the links to promote the bot"
    }
    add_slash_command_json(json_promote_the_bot)
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
    json_support_server = {
        "name": "support_server",
        "description": "Show the link to join the bot support server"
    }
    add_slash_command_json(json_support_server)
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
    json_yt = {
        "name": "youtube",
        "description": "Show the YouTube channel dedicated to the bot (bot presentation, news...)"
    }
    add_slash_command_json(json_yt)


    # Moderation
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
