# Creates the Useful constant

import discord
import json

useful_file = open("Data/Constants/useful.json", "r")
Useful = json.load(useful_file)
useful_file.close()

required_permissions = discord.Permissions.none()
for permission in Useful["required_permissions"]:
    setattr(required_permissions, permission, True)
Useful["required_permissions"] = required_permissions
