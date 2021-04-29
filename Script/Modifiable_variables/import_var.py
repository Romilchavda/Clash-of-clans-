import json


prefix_file = open("Script/Modifiable_variables/prefix.json", "r")
prefix = json.load(prefix_file)
prefix_file.close()
Prefix = {}
for guild_id, bot_prefix in prefix.items():
    Prefix[int(guild_id)] = bot_prefix

votes_file = open("Script/Modifiable_variables/votes.json", "r")
votes = json.load(votes_file)
votes_file.close()
Votes = {}
for member_id, points in votes.items():
    Votes[int(member_id)] = points

support_file = open("Script/Modifiable_variables/support_role_ for_tickets.json", "r")
support = json.load(support_file)
support_file.close()
Support = {}
for guild_id, support_id in support.items():
    Support[int(guild_id)] = support_id
