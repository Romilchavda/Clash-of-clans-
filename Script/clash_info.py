# ----- PACKAGES : -----
import json


# ----- PROJECT FILES : -----
from Data.utils import Utils
from Script.import_functions import *


# ----- COMMANDS : -----

# ON_READY
from Script.Commands.On_Ready.ready_loop import ready_loop

# GUILD
from Script.Commands.Guild.guild_join import guild_join
from Script.Commands.Guild.guild_remove import guild_remove

# MEMBER
from Script.Commands.Member.member_join import member_join
from Script.Commands.Member.member_remove import member_remove

# REACTION add
from Script.Commands.Raw_Reaction.Reaction_add.close_ticket import reaction_add_close_ticket
from Script.Commands.Raw_Reaction.Reaction_add.show_link_vote import reaction_add_show_link_vote
# REACTION remove


# RAW_REACTION add
from Script.Commands.Raw_Reaction.Raw_Reaction_add.auto_roles import raw_reaction_add_auto_roles
from Script.Commands.Raw_Reaction.Raw_Reaction_add.auto_roles_languages import raw_reaction_add_auto_roles_languages
from Script.Commands.Raw_Reaction.Raw_Reaction_add.check_rules import raw_reaction_add_check_rules
from Script.Commands.Raw_Reaction.Raw_Reaction_add.create_ticket import raw_reaction_add_create_ticket
from Script.Commands.Raw_Reaction.Raw_Reaction_add.delete_ticket import raw_reaction_add_delete_ticket
from Script.Commands.Raw_Reaction.Raw_Reaction_add.end_poll import raw_reaction_add_end_poll
from Script.Commands.Raw_Reaction.Raw_Reaction_add.feedback import raw_reaction_add_feedback
from Script.Commands.Raw_Reaction.Raw_Reaction_add.follow_news_support import raw_reaction_add_follow_news_support
# RAW_REACTION remove
from Script.Commands.Raw_Reaction.Raw_Reaction_remove.auto_roles import raw_reaction_remove_auto_roles
from Script.Commands.Raw_Reaction.Raw_Reaction_remove.auto_roles_languages import raw_reaction_remove_auto_roles_languages
from Script.Commands.Raw_Reaction.Raw_Reaction_remove.check_rules import raw_reaction_remove_check_rules
from Script.Commands.Raw_Reaction.Raw_Reaction_remove.feedback import raw_reaction_remove_feedback


# CONST VARIABLES
from Data.Const_variables.import_const import Ids
from Script.import_emojis import Emojis


# MODIFIABLE VARIABLES
from Data.Modifiable_variables.import_var import Votes


class Bot(discord.Client):
    def __init__(self, intents):
        super().__init__(intents=intents)
        self.default_prefix = None
        self.id = None

    # READY
    async def on_ready(self):
        from Script.Clients.top_gg_client import Dbl_client
        Dbl_client.bot = self
        await ready_loop(self)

    # MESSAGE DELETED
    async def on_message_delete(self, message):
        if message.guild:
            if message.guild.id == Ids["Support_server"] and (message.author.id not in [704688212832026724, 710119855348645888]):
                channel = message.guild.get_channel(895290013561000006)
                embed = create_embed(f"{message.author} ({message.author.id})", message.channel.mention + "\n\n" + message.content, message.guild.me.color, "", message.guild.me.avatar_url)
                await channel.send(embed=embed)
                if message.embeds:
                    await channel.send(embed=message.embeds[0])
        return

    # GUILD
    async def on_guild_join(self, guild):
        await guild_join(self, guild)
        return

    async def on_guild_remove(self, guild):
        await guild_remove(self, guild)
        return

    # MEMBER
    async def on_member_join(self, member):
        await member_join(self, member)
        return

    async def on_member_remove(self, member):
        await member_remove(self, member)
        return

    # REACTION
    async def on_reaction_add(self, reaction, member):
        if (not member.bot) and (reaction.message.guild is not None) and (reaction.message.author.id == self.id) and (reaction.message.embeds != []):
            await reaction_add_close_ticket(self, reaction, member)
            await reaction_add_show_link_vote(self, reaction, member)
        return

    # RAW REACTION
    async def on_raw_reaction_add(self, raw_reaction):
        if raw_reaction.member.bot:
            return

        channel = self.get_channel(raw_reaction.channel_id)
        if not getattr(channel.permissions_for(channel.guild.me), "read_messages"):
            return
        raw_reaction.message = None
        async for message in channel.history(limit=None):
            if message.id == raw_reaction.message_id:
                raw_reaction.message = message
                break
        if (raw_reaction.message is not None) and (raw_reaction.message.guild is not None) and (raw_reaction.message.author.id == self.id) and (raw_reaction.message.embeds != []):
            raw_reaction.complete_emoji = self.get_emoji(raw_reaction.emoji.id)
            await raw_reaction_add_follow_news_support(self, raw_reaction)
            await raw_reaction_add_auto_roles(self, raw_reaction)
            await raw_reaction_add_check_rules(self, raw_reaction)
            await raw_reaction_add_auto_roles_languages(self, raw_reaction)
            await raw_reaction_add_create_ticket(self, raw_reaction)
            await raw_reaction_add_delete_ticket(self, raw_reaction)
            await raw_reaction_add_end_poll(self, raw_reaction)
            await raw_reaction_add_feedback(self, raw_reaction)
        return

    async def on_raw_reaction_remove(self, raw_reaction):
        channel = self.get_channel(raw_reaction.channel_id)
        if not getattr(channel.permissions_for(channel.guild.me), "read_messages"):
            return
        raw_reaction.member = channel.guild.get_member(raw_reaction.user_id)
        if (raw_reaction.member is None) or raw_reaction.member.bot:
            return

        raw_reaction.message = None
        async for message in channel.history(limit=None):
            if message.id == raw_reaction.message_id:
                raw_reaction.message = message
                break
        if (raw_reaction.message is not None) and (raw_reaction.message.guild is not None) and (raw_reaction.message.author.id == self.id) and (raw_reaction.message.embeds != []):
            raw_reaction.complete_emoji = self.get_emoji(raw_reaction.emoji.id)
            await raw_reaction_remove_auto_roles(self, raw_reaction)
            await raw_reaction_remove_check_rules(self, raw_reaction)
            await raw_reaction_remove_auto_roles_languages(self, raw_reaction)
            await raw_reaction_remove_feedback(self, raw_reaction)
        return

    # RECEIVED MESSAGE
    async def on_message(self, message):
        if message.author.bot and message.author.id != self.id:
            if message.channel.id == Ids["Votes_channel"] and message.author.name == "Top.gg":
                member_id = int(message.embeds[0].description.split("ID : ")[1])
                member = self.get_user(member_id)
                vote = int(message.embeds[0].title.split(" ")[1])
                if member_id not in list(Votes.keys()):
                    Votes[member.id] = vote
                else:
                    Votes[member.id] += vote
                json_text = json.dumps(Votes, sort_keys=True, indent=4)
                def_votes = open(Utils["secure_folder_path"] + "votes.json", "w")
                def_votes.write(json_text)
                def_votes.close()
                vote_copy = dict(Votes)
                vote = {}
                for member_id, member_votes in vote_copy.items():
                    member = self.get_user(int(member_id))
                    vote[member.mention] = member_votes
                vote = sorted(vote.items(), key=lambda t: t[1])
                text = ""
                for user_vote_tuple in vote:
                    text += f"{user_vote_tuple[0]} have voted {user_vote_tuple[1]} times !\n"
                embed = create_embed("Votes for Clash INFO", text, message.guild.me.color, "", message.guild.me.avatar_url)
                await message.channel.send(embed=embed)
                return
            else:
                return
        if str(message.channel.type) == "private":
            channel = self.get_channel(Ids["Dm_bot_channel"])
            if message.author.id != self.id:
                await message.author.send("Hello !\nI am a bot, so I cannot answer for your question ! You can ask it in the support server :\nhttps://discord.gg/KQmstPw\n```Default help command : /help \n(you can see it with sending @Clash INFO#3976 on your server)```")
                await channel.send(f"```{message.content}``` from :\n{message.author} (`{message.author.id}`)\nMessage_id : `{message.id}`")
            return
        else:
            bot = message.guild.me
        # test
        if message.author.id in [490190727612071939]:
            if message.content == "nf":
                from Script.Commands.Messages.Clash_Of_Clans.best_donations import best_donations
                await best_donations(message, "2YP09PCL9")
            if message.content == "test@":
                from Script.Commands.Messages.Creators.servers_list import servers_list
                await servers_list(message)
            if message.content == "clean_dm":
                dm_channel = await message.author.create_dm()
                async for text in dm_channel.history(limit=None):
                    if text.author == bot:
                        await text.delete()
                await message.add_reaction(Emojis["Yes"])
                return
            if message.content == "rules":
                await message.channel.trigger_typing()
                must = f":warning: You must :warning:\n- Respect the [Discord ToS](https://discord.com/new/terms) and the [Discord Guidelines](https://discord.com/new/guidelines)\n- Respect the language of each channel (a flag emoji is present in front of the channel name if the spoken language is not English). Default = English ONLY"
                cannot = f"{Emojis['No']} You cannot : {Emojis['No']}\n- Put `[role]` after your nickname if you do not have this role in the server\n- Try to pretend to be someone else (a Staff member or not) by having same profile picture or name as the user is strictly prohibited"
                punishment = f"If you do not respect these rules, the Staff can choose your punishment from a call to order to a ban"
                embed = create_embed("Welcome in the Support server for Clash INFO !", f"Welcome ! Here is the support server of the {bot.mention} bot.\n\n{must}\n\n{cannot}\n\n{punishment}\n\nPlease READ and accept the rules by clicking on {Emojis['Yes']} to access the whole server.", 0x00ff00, "", message.guild.me.avatar_url)
                msg = await message.channel.send(embed=embed)
                await msg.add_reaction(Emojis["Yes"])
                return
            # auto-roles
            if message.content == "auto-roles languages":
                await message.channel.trigger_typing()
                await message.delete()
                text = ""
                for emoji, name in Emojis["Languages_emojis"].items():
                    language = discord.utils.get(message.guild.roles, name=name)
                    text += str(emoji) + " if you speak " + language.mention + "\n"
                embed = create_embed("Click on the emojis to get the matching roles", text, bot.color, "", message.guild.me.avatar_url)
                msg = await message.channel.send(embed=embed)
                for emoji in Emojis["Languages_emojis"].keys():
                    await msg.add_reaction(emoji)
                return
            # feedback
            if message.content == "feedback":
                await message.channel.trigger_typing()
                embed = create_embed("How do you like this bot ? Put a mark from 1 to 10", "", bot.color, "", message.guild.me.avatar_url)
                msg = await message.channel.send(embed=embed)
                await message.delete()
                for emoji in Emojis["Numbers"].values():
                    await msg.add_reaction(emoji)
                return
        return
