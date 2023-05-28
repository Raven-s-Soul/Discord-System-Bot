import discord
import asyncio
import responses
from keep_alive import keep_alive
from discord.ext import commands
import os
import config
import yt_dlp
import url_finder


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        # TODO Add more logic
        if (response == None):
            return
        # print("Answering")
        await message.author.send(
            response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


async def join_channel(voice_clients, message):
    try:
        voice_client = await message.author.voice.channel.connect()
        voice_clients[voice_client.guild.id] = voice_client
    except Exception as err:
        print(err)


async def delete_message(message):
    try:
        await message.delete()
    except Exception as err:
        print(err)


def run_discord_bot():
    # App ID
    TOKEN = os.environ['token']
    # TOKEN = ''
    # intents
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    # Client
    # client = discord.Client(intents=intents)
    client = commands.Bot(
        command_prefix=config.global_operator, intents=intents)
    client.remove_command("help")

    # Music settings
    voice_clients = {}
    yt_dl_opts = {'format': 'bestaudio', 'noplaylist': 'True'}
    ytdl = yt_dlp.YoutubeDL(yt_dl_opts)
    ffmpeg_options = {
        'before_options':
        '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn'
    }

    #############################################
    # Base Events                               #
    #############################################

    @client.event
    async def on_ready():
        print(f'{client.user} is now Alive!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = message.author
        user_message = message.content
        channel = message.channel

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        #############################################
        # Music                                     #
        #############################################

        # Join channel
        if user_message.split()[0] == (config.global_operator+"join"):
            await join_channel(voice_clients, message)
            await delete_message(message)

        # Leave & Pause
        if user_message.split()[0] == (config.global_operator+"leave"):
            voice_clients[message.guild.id].pause()
            await voice_clients[message.guild.id].disconnect()
            await delete_message(message)

        # Join & Play
        if user_message.split()[0] == (config.global_operator+"play"):
            await join_channel(voice_clients, message)
            try:
                url = user_message.split()[1]
                if "youtu.be/" not in url:
                    # 6 is the number of char +play + 1 for the space
                    url = url_finder.yt_url(user_message[6:])
                loop = asyncio.get_event_loop()
                data = await loop.run_in_executor(
                    None, lambda: ytdl.extract_info(url, download=False))
                song = data['url']
                # player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable='ffmpeg\\ffmpeg.exe') #For Replit remove last arg!
                player = discord.FFmpegPCMAudio(
                    song, **ffmpeg_options, executable='ffmpeg\\ffmpeg.exe')
                voice_clients[message.guild.id].play(player)
                # End Core function
                await delete_message(message)
                # Deliver Notification
                await message.channel.send(data.get('title', None) + ' - suggested by ' + str(username))
                return
            except Exception as err:
                print(err)

        # Pause Current Song
        if user_message.split()[0] == (config.global_operator+"pause"):
            try:
                voice_clients[message.guild.id].pause()
                await delete_message(message)
            except Exception as err:
                print(err)

        # Resume Current Song
        if user_message.split()[0] == (config.global_operator+"resume"):
            try:
                voice_clients[message.guild.id].resume()
                await delete_message(message)
            except Exception as err:
                print(err)

        # Stop Current Song
        if user_message.split()[0] == (config.global_operator+"stop"):
            try:
                voice_clients[message.guild.id].stop()
                await voice_clients[message.guild.id].disconnect()
                await delete_message(message)
            except Exception as err:
                print(err)

        #############################################
        # Custom Commands  1                        #
        #############################################

        if user_message[0] == config.global_operator:
            # If the user message contains a '?' in front of the text, it becomes a private message
            user_message = user_message[1:]  # [1:] Removes the '+'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
        await client.process_commands(message)

    @ client.event
    async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome *{member.mention}* to **{guild.name}**!'
            await guild.system_channel.send(to_send)

    @ client.event
    async def on_member_remove(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'*{member.mention}* was one of us, unluckly left **{guild.name}**!'
            await guild.system_channel.send(to_send)

    #############################################
    # Custom Commands  2                        #
    #############################################

    @ client.command()
    async def repeat(ctx, times: int, *, arg):
        """Repeats a message multiple times."""
        """+repeat times string/text"""
        if (times > 10):
            times = 10
        for i in range(times):
            await ctx.send(arg)

    #############################################
    # Program Start!                            #
    #############################################
    async def main():
        async with client:
            await client.start(TOKEN)

    keep_alive()
    asyncio.run(main())
