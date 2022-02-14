# ----- PACKAGES : -----
import discord

# ----- PROJECT FILES : -----
from Script.import_functions import create_embed

# ----- COMMANDS : -----
# ON_READY
from Script.Commands.On_Ready.ready_loop import ready_loop

# GUILD
from Script.Commands.Guild.guild_join import guild_join
from Script.Commands.Guild.guild_remove import guild_remove

# MEMBER
from Script.Commands.Member.member_join import member_join
from Script.Commands.Member.member_remove import member_remove

# ----- CONST VARIABLES -----
from Data.Constants.import_const import Ids
from Script.import_emojis import Emojis


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

    # RECEIVED MESSAGE
    async def on_message(self, message):
        if message.author.bot and message.author.id != self.id:
            return
        if str(message.channel.type) == "private":
            channel = self.get_channel(Ids["Dm_bot_log_channel"])
            if message.author.id != self.id:
                await message.author.send("Hello !\nI am a bot, so I cannot answer you !\nSupport server :\nhttps://discord.gg/KQmstPw")
                await channel.send(f"```{message.content}``` from :\n{message.author} (`{message.author.id}`)\nMessage_id : `{message.id}`")
            return
        else:
            bot = message.guild.me

        # ----- TEST -----
        if message.content.startswith("@perspectiveapi") and message.guild.id == 719537805604290650:
            text = " ".join(message.content.split(" ")[1::])
            from googleapiclient import discovery

            API_KEY = "AIzaSyCyfa2bogomLYoWEwFI947M6DWpwr2w37Y"
            client = discovery.build(
                "commentanalyzer",
                "v1alpha1",
                developerKey=API_KEY,
                discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
                static_discovery=False,
            )
            analyze_request = {
                "comment": {"text": text},
                "requestedAttributes": {
                    "TOXICITY": {},
                    "SEVERE_TOXICITY": {},
                    "IDENTITY_ATTACK": {},
                    "INSULT": {},
                    "PROFANITY": {},
                    "THREAT": {}
                }
            }

            response = client.comments().analyze(body=analyze_request).execute()
            txt = f"Text : `{text}`\n"
            for attribute, data in response["attributeScores"].items():
                txt += f"{attribute} : {data['spanScores'][0]['score']['value']} ({data['spanScores'][0]['score']['type']})\n"
            await message.reply(txt)
        if message.author.id in [490190727612071939]:
            if message.content == "test":
                return
            if message.content.startswith("dltmsg") and message.channel.permissions_for(message.author).manage_messages:
                number = int(message.content.split(" ")[1])
                message_numbers = 0
                async for msg in message.channel.history(limit=number + 1):
                    if not msg.pinned:
                        message_numbers += 1
                        await msg.delete()
                message_numbers -= 1
                embed = create_embed("Messages deleted", f"{message_numbers: ,} messages deleted", message.guild.me.color, "", message.guild.me.avatar_url)
                msg = await message.channel.send(embed=embed)
                import asyncio
                await asyncio.sleep(10)
                await msg.delete()
                return
            if message.content == "clean_dm":
                dm_channel = await message.author.create_dm()
                async for text in dm_channel.history(limit=None):
                    if text.author == bot:
                        await text.delete()
                await message.add_reaction(Emojis["Yes"])
                return
            if message.content == "rules":
                await message.channel.trigger_typing()
                must = f":warning: You must :warning:\n- Respect the [Discord ToS](https://discord.com/new/terms) and the [Discord Guidelines](https://discord.com/new/guidelines)\n- Speak English ONLY, other language are prohibited"
                cannot = f"{Emojis['No']} You cannot : {Emojis['No']}\n- Do spam or self-promotion, in a channel or with DM\n- Pretend to be someone else (a staff member or not) by having the same profile picture or the same name as the user"
                punishment = f"The disrespect of a rule will lead you from a recall to order to a definitive ban"
                embed = create_embed("Welcome in the Support server for Clash INFO !", f"Welcome ! Here is the support server of the {bot.mention} bot.\n\n{must}\n\n{cannot}\n\n{punishment}", 0x00ff00, "", message.guild.me.avatar_url)
                await message.channel.send(embed=embed)
                return
        return
