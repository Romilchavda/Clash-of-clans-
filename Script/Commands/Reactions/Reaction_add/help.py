from Script.import_emojis import Emojis
from Script.Modifiable_variables.import_var import Prefix
from Script.import_functions import create_embed


async def reaction_add_help(self, reaction, member):
    if (reaction.emoji in [Emojis["Yes"], "1️⃣", "2️⃣", "3️⃣", Emojis["Info"]]) and ("Help" in reaction.message.embeds[0].title) or ("Commands" in reaction.message.embeds[0].title) or ("Information" in reaction.message.embeds[0].title):
        try:
            prefix = Prefix[member.guild.id]
        except KeyError:
            prefix = self.default_prefix
        if reaction.emoji == Emojis["Yes"]:
            closed = create_embed("Help : Slash commands list", "", member.guild.me.color, "", member.guild.me.avatar_url)
            closed.add_field(name="Clash Of Clans :", value="get_player\nget_clan\nsearch_clan\nclan_members\nbuildings_th\nbuildings_bh\nauto_roles [th|bh|leagues]\nfile", inline=True)
            closed.add_field(name="Useful :", value="bot_info\ntickets / close_ticket\npoll\ndirect_message [member|role]\nmember_info\nrole_info\nserver_info\nadd_the_bot\nsupport_server\npromote_the_bot", inline=True)
            closed.add_field(name="Moderation :", value="delete_messages [number_of_messages|for_x_minutes|all]", inline=True)
            await reaction.message.edit(embed=closed)
            await reaction.remove(member)
        if reaction.emoji == "1️⃣":
            d1 = f"**{prefix}th [Level]** : Show the max level for your buildings at your Town Hall level.\n**{prefix}bh [Level]** : Show the max level for your buildings at your Builder Hall level.\n**{prefix}player [Tag CoC]** : Show data about the player (with the troops players on the 3rd page).\n**{prefix}clan [Tag CoC]** : Show data about the clan.\n**{prefix}members [Tag CoC]** : Show the clan members list.\n**{prefix}search clan [Name] [Number of Clans]** : Search clans by name.\n**{prefix}roles TH** : Create an auto-roles system to give the roles (created by the bot if they did not exist) with reactions\n**{prefix}roles BH** : Create an auto-roles system to give the roles (created by the bot if they did not exist) with reactions\n**{prefix}roles league** : Create an auto-roles system to give the roles (created by the bot if they did not exist) with reactions\n**{prefix}bases [TH level]** : Show bases for your TH level *(Not yet available)*\n**{prefix}coc** : Give the link for the Clash Of Clans data sheet."
            embed1 = create_embed("▬▬▬ Clash Of Clans Commands ▬▬▬", d1, member.guild.me.color, "Click on 1, 2 or 3 to change page. Click on (i) to get bot information. Click on ✅ to see the slash commands help.\nHelp page 1/3", member.guild.me.avatar_url)
            await reaction.message.edit(embed=embed1)
            await reaction.remove(member)
        if reaction.emoji == "2️⃣":
            d2 = f"**{prefix}prefix [New prefix]** : Change the bot prefix for this server.\n**{prefix}tickets [The text for the tickets]** : Create a ticket category, a ticket channel and a message with a reaction to create tickets\n**{prefix}close** : Close the ticket (with a confirmation).\n**{prefix}poll [Question]** : Show a poll with the question. Click on {Emojis['End']} to get the poll result.\n**{prefix}dm [@user] | [text]** : Send a direct message to the member (@everyon and @role for administrators only). *do not forget the* | *!*\n**{prefix}yt** : Show the YouTube channel dedicated to the bot (bot presentation, news...).\n**{prefix}member info [@member]** : Show permissions, when member joined Discord and the server and his avatar.\n**{prefix}role info [@role]** : Show permissions and who have this role.\n**{prefix}server info** : Show some information about the server.\n**{prefix}bot info** : Show some information about the bot (including the bot required permissions).\n**{prefix}age [year] [month] [day] *[hour]* *[minute]* *[second]*** : Show your age with days and with seconds ! You must your birth's information with UTC-0. *hour, minute and second are optionals.\n**{prefix}invite** (or **{prefix}add**) : Show the link to invite the bot in your server.\n**{prefix}support** : Show the link to join the support server of the bot.\n**{prefix}promote** : Show the links to promote the bot.\n**{prefix}ping** : Show if the bot is online and the ping value.\n"
            embed2 = create_embed("▬▬▬ Useful Commands ▬▬▬", d2, member.guild.me.color, "Click on 1, 2 or 3 to change page. Click on (i) to get bot information. Click on ✅ to see the slash commands help.\nHelp page 2/3", member.guild.me.avatar_url)
            await reaction.message.edit(embed=embed2)
            await reaction.remove(member)
        if reaction.emoji == "3️⃣":
            d3 = f"**{prefix}delete [Number of messages]** : Delete the most recent and not-pinned messages in the current channel.\n**{prefix}delete time [Duration in min] ** : Delete the most recent and not-pinned messages in the current channel.\n**{prefix}delete all** :  Delete all not-pinned messages in the current channel.\n**{prefix}kick [@user]** : Kick the member.\n**{prefix}ban [@user]** : Ban the member."
            embed3 = create_embed("▬▬▬ Moderation Commands ▬▬▬", d3, member.guild.me.color, "Click on 1, 2 or 3 to change page. Click on (i) to get bot information. Click on ✅ to see the slash commands help.\nHelp page 3/3", member.guild.me.avatar_url)
            await reaction.message.edit(embed=embed3)
            await reaction.remove(member)
        if reaction.emoji == Emojis["Info"]:
            d_info = f"__General Information :__\nCreators : @RREEMMII#8416 and @Arth04#6447.\nLanguage : English {Emojis['Languages_emojis']['English']}\nBot ID : {704688212832026724}\nPrefix on this server : `{prefix}`\nHelp command : `{prefix}help`\n\n__Technical Information :__\nCoded with : python {Emojis['Python']}\nRun on : Raspberry pi 3b"
            embed_info = create_embed("▬▬▬ Bot Information ▬▬▬", d_info, member.guild.me.color, "Click on 1, 2 or 3 to change page. Click on (i) to get bot information. Click on ✅ to see the slash commands help.\nHelp info page", member.guild.me.avatar_url)
            await reaction.message.edit(embed=embed_info)
            await reaction.remove(member)
    return
