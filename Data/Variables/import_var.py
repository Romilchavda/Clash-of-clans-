import json

from Data.Constants.useful import Useful

votes_file = open(f"{Useful['secure_folder_path']}votes.json", "r")
votes = json.load(votes_file)
votes_file.close()
Votes = {}
for member_id, points in votes.items():
    Votes[int(member_id)] = points

support_file = open(f"{Useful['secure_folder_path']}support_for_tickets.json", "r")
support = json.load(support_file)
support_file.close()
Support = {}
for guild_id, support_id in support.items():
    Support[int(guild_id)] = support_id

linked_accounts_file = open(f"{Useful['secure_folder_path']}linked_accounts.json", "r")
linked_accounts = json.load(linked_accounts_file)
linked_accounts_file.close()
Linked_accounts = {}
for member_id, tag in linked_accounts.items():
    Linked_accounts[int(member_id)] = tag
