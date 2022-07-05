# Clash-Of-Clans-Discord-Bot


[![Discord](https://img.shields.io/discord/719537805604290650?color=%230000ff&label=Discord&logo=https%3A%2F%2Fdiscord.com%2Fassets%2F2c21aeda16de354ba5334551a883b481.png&logoColor=%2300000000)](https://discord.gg/KQmstPw)
[![Python version](https://img.shields.io/badge/Python-%E2%89%A5%203.9-blue)](https://www.python.org/downloads/)
[![GitHub repo size](https://img.shields.io/github/repo-size/rreemmii-dev/Clash-Of-Clans-Discord-Bot?label=Repo%20Size)]()
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/rreemmii-dev/Clash-Of-Clans-Discord-Bot?label=Code%20Size)]()
[![GitHub Repo stars](https://img.shields.io/github/stars/rreemmii-dev/Clash-Of-Clans-Discord-Bot?label=Stars)](https://github.com/rreemmii-dev/Clash-Of-Clans-Discord-Bot/stargazers)
[![GitHub contributors](https://img.shields.io/github/contributors/rreemmii-dev/Clash-Of-Clans-Discord-Bot?label=Contributors)](https://github.com/rreemmii-dev/Clash-Of-Clans-Discord-Bot/graphs/contributors)


**This project is a Discord Bot about the game Clash Of Clans. It uses the [discord.py](https://github.com/Rapptz/discord.py), [coc.py](https://github.com/mathsman5133/coc.py) and [topggpy](https://github.com/top-gg/python-sdk) libraries.**

If you want to test the bot, you can [add it to your server](https://rreemmii-dev.github.io/invite). You can also join the [support server](https://discord.gg/KQmstPw) to test the bot or to ask for help.


## Table of contents

- [Installation + Setup](#installation--setup)
- [Usage](#usage)
- [Features](#features)
- [Support](#support)
- [License](#license)


## Installation + Setup

```shell
# Clone the repository:
git clone https://github.com/rreemmii-dev/Clash-Of-Clans-Discord-Bot.git

# Download the libraries:
pip install -r Clash-Of-Clans-Discord-Bot\requirements.txt
```

You must follow these steps to create and setup your bot:
- Create a bot following [these steps](https://discordpy.readthedocs.io/en/latest/discord.html). For your invite link, add the `bot` and `applications.commands` scopes, and the required permissions given [here](data/data_source/useful.json) (or the `administrator` permission)
- You will need the [member privileged intent](https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents) to run the bot. If your bot is in more than 100 servers, you will have to make a request for additional intents, which is usually satisfied within a week.
- Unzip [Emojis.zip](Emojis.zip). Then, create a server for each sub-folder (you will have about 8 servers for emojis), and add emojis from each sub-folder to the matching server.

Once it's done, you have to edit the [bot/config.json](bot/config.json) and the [data/data_source/ids.json](data/data_source/ids.json) files. You also have to copy the [secure_folder_template](secure_folder_template), rename it "Secure Folder", add your credentials in your [Secure Folder/login.json](secure_folder_template/login.json) file, and then put the folder path on the [bot/config.json](bot/config.json) file.

You can get here the help you need for each file:

<details>
<summary>

#### Help to fill in the [bot/config.json](bot/config.json) file.

</summary>

In this file, you can choose whether to activate or not some parts of the code (e.g. code using Discord Intents). You have also some initialization of variables to do.

| Field                    | Description                                                                                                                                                       | Requirements                                                                                                                                                                                                                                            |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `main_bot`               | Setting it to `false` will run a beta bot for tests, while setting it to `true` will run your main bot.                                                           | You need two bots to use them as beta and main bots. However, you can only use a main bot, and let `main_bot` at `true`.                                                                                                                                |
| `message_content_intent` | Message Content Intent is used for auto-moderation (with Perspective API) and links detection.                                                                    | Message content is a privileged intent, so you have to enable it in the Discord developer portal.                                                                                                                                                       |
| `top_gg`                 | You can interact with the [top.gg](https://top.gg) API to refresh the bot guilds count.                                                                           | You need to register your bot on [top.gg](https://top.gg).                                                                                                                                                                                              |
| `top_gg_webhooks`        | If it is enabled, you will receive a webhook when someone vote for your bot.                                                                                      | You need to register your bot on [top.gg](https://top.gg).<br/>Then, go to https://top.gg/bot/[bot_id]/webhooks and put http://[your_public_ip_address]:8080/topgg_webhook for "Webhook URL". Do not forget to do a port forwarding for your 8080 port. |
| `perspective_api`        | Perspective API allows you to check the toxicity of a message. When `message_content_intent` is set to `true`, you can moderate messages in your server using it. | You need to get an API key from the Google Cloud Platform. More information [here](https://developers.perspectiveapi.com/s/docs-get-started).                                                                                                           |

</details>

<details>
<summary>

#### Help to fill in the [data/data_source/ids.json](data/data_source/ids.json) file.

</summary>

In this file, you can choose whether to activate or not some parts of the code (e.g. code using Discord Intents). You have also some initialization of variables to do.

| Field                             | Description                                                                                                                                                                                                     |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Users                             |                                                                                                                                                                                                                 |
| `Creators`                        | List of bot creators ids. It is only used to give an access to some text commands like `dltmsg`. Slash commands for creators are set with the `Bot_creators_only_server`.                                       |
| `Bot`                             | Main bot id.                                                                                                                                                                                                    |
| `Bot_beta`                        | Beta bot id.                                                                                                                                                                                                    |
| Servers                           |                                                                                                                                                                                                                 |
| `Support_server`                  | Support server id. You have some functions only for the support server (e.g. Auto-moderation).                                                                                                                 |
| `Bot_creators_only_server`        | The server where all the slash commands for bot creators are. Everybody in this server will be able to use the slash commands for creators, so make sure only bot creators are in this server.                  |
| `Emojis_coc_th_bh_leagues_server` | The server with emojis of Town Halls, Builder Halls, leagues and heroes.                                                                                                                                        |
| `Emojis_coc_troops_spells_server` | The server with emojis of troops and spells.                                                                                                                                                                    |
| `Emojis_coc_war_leagues`          | The server with emojis of clan war leagues.                                                                                                                                                                     |
| `Emojis_coc_main_server`          | The server with other emojis about Clash Of Clans.                                                                                                                                                              |
| `Emojis_discord_main_server`      | The server with emojis of Discord User Interface.                                                                                                                                                               |
| `Emojis_discord_badges_server`    | The server with emojis of Discord badges.                                                                                                                                                                       |
| `Emojis_general_icons_server`     | The server with other emojis.                                                                                                                                                                                   |
| Channels                          |                                                                                                                                                                                                                 |
| `Weekly_stats_channel`            | The channel where the bot sends a weekly message to give the servers number evolution.                                                                                                                          |
| `Monthly_stats_channel`           | The channel were the bot sends a monthly message about its usage stats.                                                                                                                                         |
| `News_channel`                    | The news channel where announcements about the bot are sent.                                                                                                                                                    |
| `Rules_channel`                   | The rules channel.                                                                                                                                                                                              |
| `Status_channel`                  | The channel where the bot sends a message when it is connected, and when the cache is loaded.                                                                                                                   |
| `Guilds_bot_log_channel`          | The channel were the bot sends a message when it joins/leaves a server with more than 100 users (bot are not considered as users). For privacy reasons, please put this channel in the server for bot creators. |
| `Dm_bot_log_channel`              | The channel with the logs of messages sent to the bot with DMs. For privacy reasons, please put this channel in the server for bot creators.                                                                    |
| `Votes_channel`                   | The channel where messages are sent when someone vote for the bot on [top.gg](https://top.gg), with a vote counter per user.                                                                                    |
| `Welcome_channel`                 | The channel where the bot sends a welcome message when a new member arrives.                                                                                                                                    |
| `Perspective_api_channel`         | The channel where messages flagged by the Perspective API are sent.                                                                                                                                             |
| `Secure_folder_backup_channel`    | The channel where the backups of the Secure Folder are sent every week. For privacy reasons, please put this channel in the server for bot creators.                                                            |


</details>

<details>
<summary>

#### Help about the Secure Folder

</summary>

First of all, you have to copy the [secure_folder_template](secure_folder_template) and rename it "Secure Folder".

Then you have to fill in your [Secure Folder/login.json](secure_folder_template/login.json) with your credentials. You can see with the following table when each field is required

| Field                                        | When is it required ?                                         | How to get it ?                                                     |
|----------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------|
| `discord > main`                             | Always Required                                               | Help here: https://discordpy.readthedocs.io/en/latest/discord.html  |
| `discord > beta`                             | Used if `main_bot` is set to `false` in bot/config.json       | Help here: https://discordpy.readthedocs.io/en/latest/discord.html  |
| `clash_of_clans > main > [email / password]` | Always Required                                               | You have to create an account in https://developer.clashofclans.com |
| `clash_of_clans > beta > [email / password]` | Used if `main_bot` is set to `false` in bot/config.json       | You have to create an account in https://developer.clashofclans.com |
| `top_gg > token`                             | Used if `top_gg` is set to `true` in bot/config.json          | Got from https://top.gg/bot/[bot_id]/webhooks                       |
| `top_gg > authorization`                     | Used if `top_gg_webhooks` is set to `true` in bot/config.json | You have to set it in https://top.gg/bot/[bot_id]/webhooks          |
| `perspective_api > token`                    | Used if `perspective_api` is set to `true` in bot/config.json | Help here: https://developers.perspectiveapi.com/s/docs-get-started |                                                           

You can now add your Secure Folder path in the [bot/config.json](bot/config.json) file.

</details>

That's it! You can now run the script

```shell
# Run the script:
python Clash-Of-Clans-Discord-Bot\main.py
```


## Usage



## Features

You can see [here](Commands.md) the list of available commands.


## Support

You can support this project with subscribing our [Patreon](https://www.patreon.com/clash_info)


## License

Distributed under the [BSD 3-Clause License](LICENSE).

[![GitHub](https://img.shields.io/github/license/rreemmii-dev/Clash-Of-Clans-Discord-Bot?label=License)](LICENSE)


---

Discord: [RREEMMII#7368](https://discord.com/channels/@me/490190727612071939)
