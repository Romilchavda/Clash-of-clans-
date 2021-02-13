import requests
import json

Token = "NzA0Njg4MjEyODMyMDI2NzI0.Xtzs2Q.OHf1nOi8qqojyF1xKi84bJl8KgM"
Bot_id = 704688212832026724

def see_slash_command_guild():
    headers = {"Authorization": "Bot " + Token}
    url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/guilds/710237092931829893/commands"
    req = requests.get(url, headers=headers)
    dict = json.loads(req.content)
    print(dict)
    print("Slash Commands Guild list : ", end="")
    for command in dict:
        print(command["name"], end=", ")
    print()

def dlt_slash_command_guild(id):
    headers = {"Authorization": "Bot " + Token}
    url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/guilds/710237092931829893/commands/" + str(id)
    req = requests.delete(url, headers=headers)
    print(req.content)

def add_slash_command_json(json_dict):
    headers = {"Authorization": "Bot " + Token}
    url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/commands"
    req = requests.post(url, headers=headers, json=json_dict)
    print(json_dict.get("name"), req)
    if not req.ok:
        print(json_dict["name"], req.content)

def add_slash_command_json_guild(json_dict):
    headers = {"Authorization": "Bot " + Token}
    url = "https://discord.com/api/v8/applications/" + str(Bot_id) + "/guilds/710237092931829893/commands"
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
see_slash_command_guild()

