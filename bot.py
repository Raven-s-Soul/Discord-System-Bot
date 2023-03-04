import discord
import responses
from keep_alive import keep_alive
import os


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        #TODO Add more logic
        if(response == None ):
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
    # Client
    client = discord.Client(intents=intents)

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

    # Program Start!
    keep_alive()
    client.run(TOKEN)
