# ----- PACKAGES : -----
import json
import sqlite3
import sys
import time

import coc
import discord.errors
import requests
import topgg

# ----- PROJECT FILES : -----
from Script.import_functions import *

# ----- COMMANDS : -----

# MESSAGES
from Script.Commands.Messages.help import help

from Script.Commands.Messages.auto_roles import auto_roles__th, auto_roles__bh, auto_roles__leagues
from Script.Commands.Messages.buildings_bh import buildings_bh
from Script.Commands.Messages.buildings_th import buildings_th
from Script.Commands.Messages.clan_info import clan_info
from Script.Commands.Messages.clan_members import clan_members
from Script.Commands.Messages.link_coc_account import link_coc_account, unlink_coc_account
from Script.Commands.Messages.member_info import member_info
from Script.Commands.Messages.player_info import player_info
from Script.Commands.Messages.search_clan import search_clan
from Script.Commands.Messages.clan_super_troops_activated import clan_super_troops_activated
from Script.Commands.Messages.bot_info import bot_info

from Script.Commands.Messages.Creators.add_a_bot_id import add_a_bot_id
from Script.Commands.Messages.Creators.add_reaction_with_id import add_reaction_with_id
from Script.Commands.Messages.Creators.download_emojis import download_emojis
from Script.Commands.Messages.Creators.find_user_by_id import find_user_by_id
from Script.Commands.Messages.Creators.reboot import reboot
from Script.Commands.Messages.Creators.refresh_dbl import refresh_dbl
from Script.Commands.Messages.Creators.servers_list import servers_list
from Script.Commands.Messages.Creators.stats import stats

# ----- VARIABLES : -----

# MODIFIABLE VARIABLES
votes_file = open(f"{Useful['secure_folder_path']}votes.json", "r")
Votes = json.load(votes_file)

if __name__ == "__main__":

    print(f"Python : {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n"
          f"DBL : {topgg.__version__}\n"
          f"CoC : {coc.__version__}\n"
          f"Discord : {discord.__version__}")

    from discord_slash import SlashCommand
    from Script.Clients.discord_client import Clash_info

    Client_slash = SlashCommand(Clash_info)

    connection_modifiable = sqlite3.connect(f"{Useful['secure_folder_path']}Modifiable.sqlite")
    cursor_modifiable = connection_modifiable.cursor()

    connection_constants = sqlite3.connect("Data/Constants/Constants.sqlite")
    connection_constants.row_factory = sqlite3.Row
    cursor_constants = connection_constants.cursor()


    async def check_cmd_perms(ctx):
        # print(vars(ctx))
        # chan = Clash_info.get_channel(ctx.channel_id)
        # print(ctx.channel_id, chan)
        # if chan.type == "private":
        #     return True
        if not ctx.guild_id or Clash_info.get_channel(ctx.channel_id) is None:
            await ctx.send("Slash commands are not available with neither threads nor direct messages. Please use classic text channels to use slash commands.")
            return -1
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
                    text += f"\n{perm}"
                if len(missing_bot_perms) == 1:
                    text += "\nPlease grant it to the bot and send again the command."
                else:
                    text += "\nPlease grant them to the bot and send again the command."
            if missing_user_perms:
                text += "You don't have this/these permission(s) :"
                for perm in missing_user_perms:
                    text += f"\n{perm}"
                if len(missing_user_perms) == 1:
                    text += "\nThis permission is required to use this command."
                else:
                    text += "\nThese permissions are required to use this command."
            embed = create_embed("Missing permissions", text, 0xFF0000, "", channel.guild.me.avatar_url)
            await ctx.send(embed=embed)
            return -1
        return True


    def edit_commands_used(user_id, cmd):
        text = f"""INSERT INTO BotUsage(user_id) SELECT({user_id}) WHERE NOT EXISTS(SELECT 1 FROM BotUsage WHERE user_id={user_id})"""
        cursor_modifiable.execute(text)
        text = f"""UPDATE BotUsage SET {cmd} = (SELECT {cmd} FROM BotUsage WHERE user_id={user_id})+1 WHERE user_id={user_id}"""
        cursor_modifiable.execute(text)
        connection_modifiable.commit()


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
        await auto_roles__bh(ctx, channel)
        edit_commands_used(ctx.author_id, "auto_roles__bh")
        return

    @Client_slash.subcommand(base="auto_roles", name="leagues")
    async def _auto_roles_leagues(ctx, channel=None):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        if channel is None:
            channel = ctx.channel
        await auto_roles__leagues(ctx, channel)
        edit_commands_used(ctx.author_id, "auto_roles__leagues")
        return

    @Client_slash.subcommand(base="auto_roles", name="th")
    async def _auto_roles_th(ctx, channel=None):
        if await check_cmd_perms(ctx) == -1:  # TODO : Check with the ctx.channel permission, instead of channel permission
            return
        await ctx.defer()
        if channel is None:
            channel = ctx.channel
        await auto_roles__th(ctx, channel)
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

    @Client_slash.slash(name="player_info")
    async def _player_info(ctx, player_tag, information):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await player_info(ctx, player_tag, information)
        edit_commands_used(ctx.author_id, "player_info")
        return

    @Client_slash.slash(name="search_clan")
    async def _search_clan(ctx, name):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await search_clan(ctx, name)
        edit_commands_used(ctx.author_id, "search_clan")
        return

    @Client_slash.slash(name="clan_super_troops_activated")
    async def _clan_super_troops_activated(ctx, clan_tag, super_troop):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await clan_super_troops_activated(ctx, clan_tag, super_troop)
        edit_commands_used(ctx.author_id, "clan_super_troops_activated")
        return

    @Client_slash.slash(name="link_coc_account")
    async def _link_coc_account(ctx, player_tag, api_token):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await link_coc_account(ctx, player_tag, api_token)
        edit_commands_used(ctx.author_id, "link_coc_account")
        return

    @Client_slash.slash(name="unlink_coc_account")
    async def _unlink_coc_account(ctx, player_tag):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await unlink_coc_account(ctx, player_tag)
        edit_commands_used(ctx.author_id, "unlink_coc_account")
        return

    @Client_slash.slash(name="member_info")
    async def _member_info(ctx, member):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await member_info(ctx, member)
        edit_commands_used(ctx.author_id, "member_info")
        return

    @Client_slash.slash(name="bot_info")
    async def _bot_info(ctx):
        if await check_cmd_perms(ctx) == -1:
            return
        await ctx.defer()
        await bot_info(ctx)
        edit_commands_used(ctx.author_id, "bot_info")
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

    @Client_slash.slash(name="__reboot")
    async def ___reboot(ctx):
        await ctx.defer()
        await reboot(ctx)
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
        await ctx.defer()
        await stats(ctx)
        return


    from Script.Clients.discord_client import Token

    Bot_id = Clash_info.id


    def add_slash_command_json(json_dict):
        headers = {"Authorization": f"Bot {Token}"}
        url = f"https://discord.com/api/v8/applications/{Bot_id}/commands"
        req = requests.post(url, headers=headers, json=json_dict)
        print(json_dict.get("name"), req)
        if not req.ok:
            print(json_dict["name"], req.content)
            if "retry_after" in list(req.json().keys()):
                time.sleep(req.json()["retry_after"])
                add_slash_command_json(json_dict)


    def add_slash_command_json_guild(json_dict):
        headers = {"Authorization": f"Bot {Token}"}
        url = f"https://discord.com/api/v8/applications/{Bot_id}/guilds/710237092931829893/commands"
        req = requests.post(url, headers=headers, json=json_dict)
        print(json_dict.get("name"), req)
        if not req.ok:
            print(json_dict["name"], req.content)
            if "retry_after" in list(req.json().keys()):
                time.sleep(req.json()["retry_after"])
                add_slash_command_json(json_dict)


    def see_slash_commands():
        headers = {"Authorization": f"Bot {Token}"}
        url = f"https://discord.com/api/v8/applications/{Bot_id}/commands"
        req = requests.get(url, headers=headers)
        json_dict = json.loads(req.content)
        print("Slash Commands list : ", end="")
        for command in json_dict:
            print(command["name"], end=", ")
        print()


    def dlt_slash_command(name):
        headers = {"Authorization": f"Bot {Token}"}
        url = f"https://discord.com/api/v8/applications/{Bot_id}/commands"
        req = requests.get(url, headers=headers)
        json_dict = json.loads(req.content)
        for command in json_dict:
            if command.get("name") == name:
                url += f"/{(command.get('id'))}"
                req = requests.delete(url, headers=headers)
                print(req)
                print(req.content)
        print("Content :", req.content)


    def see_slash_command_guild():
        headers = {"Authorization": f"Bot {Token}"}
        url = f"https://discord.com/api/v8/applications/{Bot_id}/guilds/710237092931829893/commands"
        req = requests.get(url, headers=headers)
        print(req.content)


    def dlt_slash_command_guild(command_id):
        headers = {"Authorization": f"Bot {Token}"}
        url = f"https://discord.com/api/v8/applications/{Bot_id}/guilds/710237092931829893/commands/{command_id}"
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
        from Script.Commands.Components.Select_menu.auto_roles import auto_roles__th
        await auto_roles__th(ctx)
        from Script.Commands.Components.Select_menu.auto_roles import auto_roles__bh
        await auto_roles__bh(ctx)
        from Script.Commands.Components.Select_menu.auto_roles import auto_roles__league
        await auto_roles__league(ctx)
        from Script.Commands.Components.Select_menu.change_search_clan import change_search_clan
        await change_search_clan(ctx)
        from Script.Commands.Components.Button.joined_guild_message import joined_guild_message
        await joined_guild_message(ctx)
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
    json_link_coc_account = {
        "name": "link_coc_account",
        "description": "Link your Clash Of Clans account to your Discord account",
        "options": [{
            "name": "player_tag",
            "description": "Your Clash Of Clans tag",
            "required": True,
            "type": 3,
        }, {
            "name": "api_token",
            "description": "Your API token, findable in the game settings",
            "required": True,
            "type": 3,
        }]
    }
    add_slash_command_json(json_link_coc_account)
    json_unlink_coc_account = {
        "name": "unlink_coc_account",
        "description": "Unlink your Clash Of Clans account from your Discord account",
        "options": [{
            "name": "player_tag",
            "description": "Your Clash Of Clans tag",
            "required": True,
            "type": 3,
        }]
    }
    add_slash_command_json(json_unlink_coc_account)
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
        }]
    }
    add_slash_command_json(json_search_clan)
    json_clan_super_troops_activated = {
        "name": "clan_super_troops_activated",
        "description": "Show which player has activated the super troop in the clan",
        "options": [{
            "name": "clan_tag",
            "description": "Clash Of Clans clan tag, format : #A1B2C3D4",
            "required": True,
            "type": 3,
        }, {
            "name": "super_troop",
            "description": "The wanted super troop",
            "required": True,
            "type": 3,
            "choices": [{
                "name": "Super Barbarian",
                "value": "Super Barbarian"
            }, {
                "name": "Super Archer",
                "value": "Super Archer"
            }, {
                "name": "Super Giant",
                "value": "Super Giant"
            }, {
                "name": "Sneaky Goblin",
                "value": "Sneaky Goblin"
            }, {
               "name": "Super Wall Breaker",
               "value": "Super Wall Breaker"
            }, {
               "name": "Rocket Balloon",
               "value": "Rocket Balloon"
            }, {
               "name": "Super Wizard",
               "value": "Super Wizard"
            }, {
                "name": "Super Dragon",
                "value": "Super Dragon"
            }, {
               "name": "Inferno Dragon",
               "value": "Inferno Dragon"
            }, {
               "name": "Super Minion",
               "value": "Super Minion"
            }, {
               "name": "Super Valkyrie",
               "value": "Super Valkyrie"
            }, {
               "name": "Super Witch",
               "value": "Super Witch"
            }, {
               "name": "Ice Hound",
               "value": "Ice Hound"
            }, {
                "name": "Super Bowler",
                "value": "Super Bowler"
            }]
        }]
    }
    add_slash_command_json(json_clan_super_troops_activated)
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
    json_bot_info = {
        "name": "bot_info",
        "description": "Show some information about the bot"
    }
    add_slash_command_json(json_bot_info)

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
