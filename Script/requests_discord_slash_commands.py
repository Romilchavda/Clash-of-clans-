import requests
import json

bot = 1
if bot == 0:
    Token = "NzA0Njg4MjEyODMyMDI2NzI0.Xtzs2Q.OHf1nOi8qqojyF1xKi84bJl8KgM"
    Bot_id = 704688212832026724
else:
    Token = "NzEwMTE5ODU1MzQ4NjQ1ODg4.Xrv0pg.9bxFnAVKTFbq4Qhkq5x8xYT-M9c"
    Bot_id = 710119855348645888

def see_slash_command_guild(guild_id=710237092931829893):
    headers = {"Authorization": "Bot " + Token}
    url = f"https://discord.com/api/v8/applications/{Bot_id}/guilds/{guild_id}/commands"
    req = requests.get(url, headers=headers)
    dict = json.loads(req.content)
    print(dict)
    print("Slash Commands Guild list : ", end="")
    for command in dict:
        print(command["name"], end=", ")
    print()

def dlt_slash_command_guild(id, guild_id=710237092931829893):
    headers = {"Authorization": "Bot " + Token}
    url = f"https://discord.com/api/v8/applications/{Bot_id}/guilds/{guild_id}/commands/{id}"
    req = requests.delete(url, headers=headers)
    print(req.content)

def add_slash_command_json(json_dict):
    headers = {"Authorization": "Bot " + Token}
    url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/commands"
    req = requests.post(url, headers=headers, json=json_dict)
    print(json_dict.get("name"), req)
    if not req.ok:
        print(json_dict["name"], req.content)

def add_slash_command_json_guild(json_dict, guild_id = 710237092931829893):
    headers = {"Authorization": "Bot " + Token}
    url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/guilds/" + str(guild_id) + "/commands"
    req = requests.post(url, headers=headers, json=json_dict)
    print(json_dict.get("name"), req)
    if not req.ok:
        print(json_dict["name"], req.content)

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
    req = requests.delete(url, headers=headers)
    dict = json.loads(req.content)
    for command in dict:
        if command.get("name") == name:
            url += "/" + str(command.get("id"))
            req = requests.delete(url, headers=headers)
            print(req)
            print(req.content)
    print("Content :", req.content)


see_slash_commands()
try:
    see_slash_command_guild()
except:
    print("No guild commands")
"""
json_add_a_bot_by_id = {
    "name": "__add_a_bot",
    "description": "Add the bot with the given id",
    "options": [{
        "name": "bot_id",
        "description": "The bot id",
        "type": 4,
        "required": True
    }]
}
add_slash_command_json_guild(json_add_a_bot_by_id, guild_id=808814347224481863)
json_add_reaction_with_id = {
    "name": "__add_reaction_with_id",
    "description": "Add a reaction everywhere with channel/message/emoji id",
    "options": [{
        "name": "channel_id",
        "description": "The channel id",
        "type": 4,
        "required": True
    }, {
        "name": "message_id",
        "description": "The message id",
        "type": 4,
        "required": True
    }, {
        "name": "emoji_id",
        "description": "The emoji id",
        "type": 4,
        "required": True
    }]
}
add_slash_command_json_guild(json_add_reaction_with_id, guild_id=808814347224481863)
json_find_user_by_id = {
    "name": "__find_user_by_id",
    "description": "Find a user with the given id",
    "options": [{
        "name": "user_id",
        "description": "The user id",
        "type": 4,
        "required": True
    }]
}
add_slash_command_json_guild(json_find_user_by_id, guild_id=808814347224481863)
json_servers_list = {
    "name": "__servers_list",
    "description": "Show all the servers with the bot"
}
add_slash_command_json_guild(json_servers_list, guild_id=808814347224481863)
json_refresh_dbl = {
    "name": "__refresh_dbl",
    "description": "Refresh the top.gg servers counter"
}
add_slash_command_json_guild(json_refresh_dbl, guild_id=808814347224481863)
"""
