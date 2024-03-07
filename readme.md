# D1stanceC0mmander

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

D1stanceC0mmander is a potent tool that empowers users without the required permissions to execute commands through a Discord bot on an alternative server.

## DISCLAIMER ⚠️ !!!

I am not responsible for any damage or disrespect caused to others or their servers. I am solely creating scripts for other people. This is for educational purposes only.

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

## Create a Server

Create a server where there's no one. It will be our control center.

## Create the Bot

1. To create the bot and get its token, go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application, then name it to be credible for others to add it more easily and finally accept Discord Developer terms.
3. Personalize the bot (Add a profile picture or a description).
4. Go into the bot section, click Reset token, then it will display the bot token. Note it somewhere; we will need it after.
5. Still in the bot section, scroll down a little bit then in Privileged Gateway Intents activate all three (PRESENCE INTENT, SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT).
6. Finally, go into the OAuth2 tab, scroll at the bottom, and you will see OAuth2 URL Generator. Select bot, then select the permission the bot will have; I will choose admin for simplicity.
7. Copy the GENERATED URL, add it to your server, and send the URL to the owner of the victim's server.

And there you go! You've created your bot and added it to your server and the victim's server.

## Getting Started

1. Clone the repository: `git clone https://github.com/independent-coder/D1stanceC0mmander.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Create a `.env` file and add your Discord bot token and other configurations.
4. Run the bot: `python D1stanceC0mmander.py`

Feel free to explore and contribute to make D1stanceC0mmander even more powerful!

## Configuration

Make sure to set up your `.env` file with the following configurations:

```dotenv
TOKEN=your_discord_bot_token
ALLOWED_SERVER_ID=your_allowed_server_id


## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.
```
