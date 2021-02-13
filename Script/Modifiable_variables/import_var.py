import json


def_prefix = open("Script/Modifiable_variables/def_prefix.json", "r")
prefix = json.load(def_prefix)
def_prefix.close()
Prefix = {}
for guild_id, bot_prefix in prefix.items():
    Prefix[int(guild_id)] = bot_prefix

def_history = open("Script/Modifiable_variables/def_history.json", "r")
History_txt = def_history.read()
def_history.close()
History = json.loads(History_txt)

def_votes = open("Script/Modifiable_variables/def_votes.json", "r")
votes = json.load(def_votes)
def_votes.close()
Votes = {}
for member_id, points in votes.items():
    Votes[int(member_id)] = points

def_support = open("Script/Modifiable_variables/def_support_tickets.json", "r")
support = json.load(def_support)
def_support.close()
Support = {}
for guild_id, support_id in support.items():
    Support[int(guild_id)] = support_id
