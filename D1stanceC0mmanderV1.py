# -----------------------------------
#                                   |
#        MADE BY $*P!NGU1*$         |
#       D1stance C0mmander V1       |
# -----------------------------------

# -----------------------------------
#         Remember to put           |
#          Your bot token           |
#          in DOTENV File           |
# -----------------------------------


import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Configuration
intents = discord.Intents.all()
TOKEN = os.getenv('TOKEN')
ALLOWED_SERVER_ID = int(os.getenv('ALLOWED_SERVER_ID'))

# Constants
MADE_BY_TEXT = "MADE BY $*P!NGU1*$"

bot = commands.Bot(command_prefix='!', intents=intents)


def create_standard_embed(title, color):
    embed = discord.Embed(title=title, color=color)
    embed.set_footer(text=MADE_BY_TEXT)
    return embed


# Function to check if a server is allowed
def is_allowed_server(ctx):
    return ctx.guild.id == ALLOWED_SERVER_ID


# Check if the server is allowed before executing any command
@bot.before_invoke
async def check_allowed_server(ctx):
    if not is_allowed_server(ctx):
        raise commands.CommandError("Command not allowed in this server.")

# -----------------------------------
#                                   |
#   DEFINING BOT'S COMMANDS         |
#                                   |
# -----------------------------------


@bot.command(name='spam',
             help='Spam a message in a server channel. Usage: !spam <message> <count> <server_id> <channel_id>. If <message> has space put message in quotes.')
async def spam(ctx, message, count_str, server_id_str, channel_id_str):
    try:
        count = int(count_str)
        server_id = int(server_id_str)
        channel_id = int(channel_id_str)

        server = bot.get_guild(server_id)
        channel = server.get_channel(channel_id)

        if server is not None and channel is not None:
            for _ in range(count):
                await channel.send(message)
            await ctx.send(f'Successfully spammed {count} messages in #{channel.name} of server {server.name}.')
        else:
            await ctx.send('Invalid server or channel ID.')
    except ValueError:
        await ctx.send('Invalid input. Please provide valid numeric values for count, server ID, and channel ID.')
    except Exception as e:
        await ctx.send(f'An error occurred: {e}')


@bot.command(name='user_info', help='Display information about a user. Usage: !user_info <user_id>')
async def user_info(ctx, user_id: int):
    try:
        # Fetch the user by ID from any server the bot is in
        user = await bot.fetch_user(user_id)

        embed = create_standard_embed(title=f'{user.name}#{user.discriminator}', color=discord.Color.orange())

        # Use avatar_url from the User object
        embed.set_thumbnail(url=user.avatar.url)

        embed.add_field(name='User ID', value=user.id, inline=False)

        # Check the member in all servers the bot is in
        for guild in bot.guilds:
            member_in_guild = guild.get_member(user.id)
            if member_in_guild:
                embed.add_field(name=f'Joined Server - {guild.name}',
                                value=member_in_guild.joined_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)

        embed.add_field(name='Created Account', value=user.created_at.strftime('%Y-%m-%d %H:%M:%S'), inline=False)

        # Add more fields as needed

        await ctx.send(embed=embed)

    except discord.NotFound:
        await ctx.send("User not found.")


@bot.command(name='assign_role',
             help='Assign a role to a member. Usage: !assign_role <server_id> <role_id> <member_mention>')
async def asign_role(ctx, server_id: int, role_id: int, member: discord.Member):
    server = bot.get_guild(server_id)
    role = server.get_role(role_id)

    # Check if the bot is in the specified server and has the necessary permissions
    if server is not None and role is not None and bot.user in server.members:
        await member.add_roles(role)
        await ctx.send(f'Role {role.name} assigned to {member.display_name} in server {server.name}.')
    else:
        await ctx.send('Invalid server or role ID, or the bot lacks permissions.')


@bot.command(name='clear',
             help='Clears a specified number of messages. Usage: !clear <amount> [<server_id>] [<channel_id>]')
async def clear(ctx, amount: int, server_id: int = None, channel_id: int = None):
    if server_id is not None and channel_id is not None:
        server = bot.get_guild(server_id)
        channel = server.get_channel(channel_id)

        # Check if the bot is in the specified server and has the necessary permissions
        if server is not None and channel is not None and bot.user in server.members and channel.permissions_for(
                server.me).manage_messages:
            await channel.purge(limit=amount + 1)
            await ctx.send(f'Cleared {amount} messages in #{channel.name} of server {server.name}.')
        else:
            await ctx.send('Invalid server or channel ID, or the bot lacks permissions.')
    else:
        # Clear messages in the current server and channel
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Cleared {amount} messages in #{ctx.channel.name} of server {ctx.guild.name}.')


@bot.command(name='joined_server', help='Display detailed information about each server the bot is in')
async def joined_server(ctx):
    embed = create_standard_embed(title='Joined Servers Information', color=discord.Color.yellow())

    for guild in bot.guilds:
        permissions = guild.me.guild_permissions
        formatted_permissions = "\n".join(
            [f"- {perm.replace('_', ' ').title()}" for perm, value in permissions if value])

        if permissions.administrator:
            permissions_text = "Admin"
        else:
            permissions_text = f"Bot Permissions: \n{formatted_permissions or 'None'}\n(Might not be enough for some actions)"

        owner = guild.owner
        owner_text = f"Owner: {owner.name}#{owner.discriminator}" if owner else "Owner: Not available"

        member_count = guild.member_count
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        categories = len(guild.categories)
        verification_level = guild.verification_level
        created_at = guild.created_at.strftime('%Y-%m-%d %H:%M:%S')

        channels_text = f"Channels: {text_channels} Text, {voice_channels} Voice, {categories} Categories"
        verification_text = f"Verification Level: {verification_level}"
        created_at_text = f"Created At: {created_at}"
        member_count_text = f"Members: {member_count}"

        # Display role names
        roles_text = ', '.join([role.name for role in guild.roles])

        embed.add_field(
            name=guild.name,
            value=f"Server ID: {guild.id}\n{permissions_text}\n{owner_text}\n{channels_text}\n{verification_text}\n{created_at_text}\n{member_count_text}\nRoles: {roles_text}",
            inline=False
        )
    await ctx.send(embed=embed)


@bot.command(name='export_servers', help='Export information about joined servers to a text file')
async def export_servers(ctx):
    # Create a file named 'joined_servers_info.txt'
    file_path = 'joined_servers_info.txt'

    with open(file_path, 'w') as file:
        file.write('Joined Servers Information:\n\n')

        for guild in bot.guilds:
            permissions = guild.me.guild_permissions
            formatted_permissions = "\n".join(
                [f"- {perm.replace('_', ' ').title()}" for perm, value in permissions if value])

            if permissions.administrator:
                permissions_text = "Admin"
            else:
                permissions_text = f"Bot Permissions: \n{formatted_permissions or 'None'}\n(Might not be enough for some actions)"

            owner = guild.owner
            owner_text = f"Owner: {owner.name}#{owner.discriminator}" if owner else "Owner: Not available"

            member_count = guild.member_count
            text_channels = len(guild.text_channels)
            voice_channels = len(guild.voice_channels)
            categories = len(guild.categories)
            verification_level = guild.verification_level
            created_at = guild.created_at.strftime('%Y-%m-%d %H:%M:%S')

            # Display role names
            roles_text = ', '.join([role.name for role in guild.roles])

            channels_text = f"Channels: {text_channels} Text, {voice_channels} Voice, {categories} Categories"
            verification_text = f"Verification Level: {verification_level}"
            created_at_text = f"Created At: {created_at}"
            member_count_text = f"Members: {member_count}"

            file.write(f"Server: {guild.name}\n"
                       f"Server ID: {guild.id}\n"
                       f"{permissions_text}\n"
                       f"{owner_text}\n"
                       f"{channels_text}\n"
                       f"{verification_text}\n"
                       f"{created_at_text}\n"
                       f"{member_count_text}\n"
                       f"Roles: {roles_text}\n\n")

    await ctx.send(f'Joined server information exported to `{file_path}`.')


# Define a command to display commands in an embed
@bot.command(name='display_commands', help='Displays available commands in an embed and removes other commands')
async def display_commands(ctx):
    embed = create_standard_embed(title='Available Commands', color=discord.Color.yellow())

    for command in bot.commands:
        embed.add_field(name=f'!{command.name}', value=command.help, inline=False)

    # Remove other commands
    await ctx.channel.purge(check=lambda m: m.author == bot.user and m.content.startswith('!'))

    # Send the embed
    await ctx.send(embed=embed)


# Run the bot with your token
bot.run(TOKEN)
