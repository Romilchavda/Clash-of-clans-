import json

from Data.Constants.useful import Useful

votes_file = open(f"{Useful['secure_folder_path']}votes.json", "r")
votes = json.load(votes_file)
votes_file.close()
Votes = {}
for member_id, points in votes.items():
    Votes[int(member_id)] = points

linked_accounts_file = open(f"{Useful['secure_folder_path']}linked_accounts.json", "r")
linked_accounts = json.load(linked_accounts_file)
linked_accounts_file.close()
Linked_accounts = {}
for member_id, tag in linked_accounts.items():
    Linked_accounts[int(member_id)] = tag
