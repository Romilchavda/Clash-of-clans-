import json


prefix_file = open("Data/Modifiable_variables/prefix.json", "r")
prefix = json.load(prefix_file)
prefix_file.close()
Prefix = {}
for guild_id, bot_prefix in prefix.items():
    Prefix[int(guild_id)] = bot_prefix

votes_file = open("Data/Modifiable_variables/votes.json", "r")
votes = json.load(votes_file)
votes_file.close()
Votes = {}
for member_id, points in votes.items():
    Votes[int(member_id)] = points

support_file = open("Data/Modifiable_variables/support_for_tickets.json", "r")
support = json.load(support_file)
support_file.close()
Support = {}
for guild_id, support_id in support.items():
    Support[int(guild_id)] = support_id

no_dm_file = open("Data/Modifiable_variables/no_dm.json", "r")
No_dm = json.load(no_dm_file)
no_dm_file.close()

linked_players_file = open("Data/Modifiable_variables/linked_players.json", "r")
linked_players = json.load(linked_players_file)
linked_players_file.close()
Linked_players = {}
for member_id, tag in linked_players.items():
    Linked_players[int(member_id)] = tag
