# D1stanceC0mmander

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

D1stanceC0mmander is a powerful tool that enables users without the required permissions to execute commands through a Discord bot on an alternative server.

## DISCLAIMER ⚠️ !!!

I'm not responsible for any damage or disrespect on others or server. I'm only making scripts for other people.
This is for educational purposes only

## More advanced explanation

This bot and python works using discord's api to run on python. To make this work you will need to create a server with you and your bot, then make owner of other server add the bot with the necesary permision(Admin). Then from your very own server you can simply excute commands on others server ! (With their permision.)
(You can still try it tho without their permision😉)

## Features

- **Spam Command:** Spam a message in a server channel with customizable parameters.
- **User Info Command:** Display detailed information about a user.
- **Assign Role Command:** Assign a role to a member in a specified server.
- **Clear Command:** Clear a specified number of messages in a channel.
- **Joined Server Command:** Display detailed information about each server the bot is in.
- **Export Servers Command:** Export information about joined servers to a text file.
- **Display Commands Command:** Display available commands in an embed and remove other commands.

## Create a server

Create a server were there's no one. It will be our control center.

## Create the bot

1. In order to create the bot and get his token, go to [Discord Developer Portal](https://discord.com/developers/applications).
2. Create a new application, then name it to be credible for others to add it more easily and finally accepts Discord Developer terms.
3. You can personalise the bot (Add a pfp or a description)
4. Go into bot section, click Reset token then it will display the bot token. Note it somewere we will need it after.
5. Still in bot section scroll down a little bit then in Privileged Gateway Intents activate all of 3 (PRESENCE INTENT, SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT).
6. Finally go into 0Auth2 tab, scroll at the bottom the you will see OAuth2 URL Generator, Select bot then select the permision the bot will have, I will choose admin for simplicity.
7. Copy the GENERATED URL, add it to your server and send the url to the owner of the victims server.

And there you go ! You've created your bot and add it to your server and the victims server.

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
```

## License

This project is licensed under the MIT License - see the LICENSE.txt file for details.
