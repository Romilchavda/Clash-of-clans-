# Allows users to link their Clash Of Clans accounts with their Discord account

import json

import coc.utils

from Data.Variables.import_var import Linked_accounts
from Data.Constants.useful import Useful
from Script.Clients.clash_of_clans_client import Clash_of_clans
from Script.import_functions import create_embed


async def link_coc_account(ctx, player_tag, api_token):
    player_tag = coc.utils.correct_tag(player_tag)
    is_correct_token = await Clash_of_clans.verify_player_token(player_tag, api_token)
    if is_correct_token:
        if ctx.author.id not in list(Linked_accounts.keys()):
            Linked_accounts.update({ctx.author.id: {"Clash Of Clans": []}})
        Linked_accounts[ctx.author.id].update({"Clash Of Clans": Linked_accounts[ctx.author.id]["Clash Of Clans"] + [player_tag]})
        embed = create_embed("Accounts linked", f"Your Discord account is now linked with the Clash Of Clans account `{player_tag}`", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.send(embed=embed, hidden=True)
        json_text = json.dumps(Linked_accounts, sort_keys=True, indent=4)
        linked_account_file = open(f"{Useful['secure_folder_path']}linked_accounts.json", "w")
        linked_account_file.write(json_text)
        linked_account_file.close()
    else:
        await ctx.send(f"Player not found\nThere is no player with the tag `{player_tag}`.", hidden=True)
    return


async def unlink_coc_account(ctx, player_tag):
    player_tag = coc.utils.correct_tag(player_tag)
    if player_tag in Linked_accounts[ctx.author.id]["Clash Of Clans"]:
        Linked_accounts[ctx.author.id]["Clash Of Clans"].pop(Linked_accounts[ctx.author.id]["Clash Of Clans"].index(player_tag))
        if Linked_accounts[ctx.author.id]["Clash Of Clans"] == []:
            Linked_accounts.pop(ctx.author.id)
        json_text = json.dumps(Linked_accounts, sort_keys=True, indent=4)
        linked_account_file = open(f"{Useful['secure_folder_path']}linked_accounts.json", "w")
        linked_account_file.write(json_text)
        linked_account_file.close()
        embed = create_embed("Accounts unlinked", f"Your Discord account is no longer linked with the Clash Of Clans account `{player_tag}`", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.send(embed=embed, hidden=True)
    else:
        embed = create_embed("Account not linked", f"Your Discord account is not linked with the Clash Of Clans account `{player_tag}`", ctx.guild.me.color, "", ctx.guild.me.avatar_url)
        await ctx.send(embed=embed, hidden=True)
    return
