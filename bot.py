import discord
import responses
from keep_alive import keep_alive
from discord.ext import commands
import os


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        # TODO Add more logic
        if (response == None):
            return
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    # App ID
    # os.environ['token']
    TOKEN = os.environ['token']
    # intents
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    # Client
    # client = discord.Client(intents=intents)
    client = commands.Bot(command_prefix='+', intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now Alive!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        await client.process_commands(message)

    @client.event
    async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome *{member.mention}* to **{guild.name}**!'
            await guild.system_channel.send(to_send)

    @client.event
    async def on_member_remove(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'*{member.mention}* was one of us, unluckly left **{guild.name}**!'
            await guild.system_channel.send(to_send)

    # @client.event
    # async def on_member_ban(guild, member):
    #     guild = member.guild
    #     if guild.system_channel is not None:
    #         to_send = f'*{member.mention}* overflowed from **{guild.name}**, so we deleted this outdated process!'
    #         await guild.system_channel.send(to_send)

    @client.command()
    async def repeat(ctx, times: int, *, arg):
        """Repeats a message multiple times."""
        """+repeat times text"""
        # if (times >= 10):
        #   times = 10
        for i in range(times):
            await ctx.send(arg)

    # Program Start!
    keep_alive()
    client.run(TOKEN)
