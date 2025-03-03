import discord # pip install discord.py-self
from discord.ext import commands
import datetime

import time

# Terminal colors
CYAN = "\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RED = "\033[31m"
MAGENTA = "\033[35m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

bot = commands.Bot(command_prefix="!", self_bot=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} [ID: {bot.user.id}]')
    print(f'{YELLOW}[INFO]{RESET} Bot is running on Discord.py version {discord.__version__}')

def get_channel_participants(channel):
    """Get number of participants in any channel type."""
    try:
        if isinstance(channel, (discord.VoiceChannel, discord.StageChannel)):
            return len(channel.members)
        elif isinstance(channel, discord.GroupChannel):
            return len(channel.voice.voice_states) if channel.voice else 0
        elif isinstance(channel, discord.DMChannel):
            return len(channel.voice_states)
        return 0
    except AttributeError:
        return 0

def log_voice_event(action, member, channel, timestamp):
    action_colors = {
        "CALL_START": GREEN,
        "CALL_END": RED,
        "USER_LEFT": ORANGE,
        "USER_JOINED": MAGENTA
    }
    action_color = action_colors.get(action, RESET)

    # Get channel context
    if isinstance(channel, discord.DMChannel):
        context = f"DM:{channel.id}"
        guild_name = "DM"
        context_color = ORANGE
        channel_name = f"DM with {channel.recipient}"
    elif isinstance(channel, discord.GroupChannel):
        context = f"Group:{channel.id}"
        guild_name = "Group DM"
        context_color = MAGENTA
        channel_name = channel.name
    elif channel.guild:
        context = f"Guild:{channel.guild.id}"
        guild_name = channel.guild.name
        context_color = CYAN
        channel_name = channel.name
    else:
        context = "Unknown"
        guild_name = "Unknown"
        context_color = RESET
        channel_name = "Unknown"

    user_id = member.id
    user_name = str(member)

    # Colored console output
    colored_log = (
        f"{CYAN}[{timestamp}]{RESET} | "
        f"{action_color}{action.ljust(12)}{RESET} | "
        f"{context_color}{context.ljust(25)}{RESET} | "
        f"Guild: {guild_name.ljust(30)} | "
        f"User:{str(user_id).ljust(20)} | "
        f"{BLUE}{user_name.ljust(25)}{RESET} in "
        f"{GREEN}{channel_name.ljust(20)}{RESET}"
    )
    print(colored_log)

    # Text file logging
    log_entry = (
        f"[{timestamp}] | "
        f"{action.ljust(10)} | "
        f"{context.ljust(25)} | "
        f"Guild: {guild_name.ljust(30)} | "
        f"User:{user_id} | "
        f"{user_name.ljust(25)} in "
        f"{channel_name}\n"
    )

    try:
        with open("voice_log.txt", "a", encoding="utf-8") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Voice log error: {e}")

def log_message(action, message, timestamp):
    action_colors = {
        "CREATED": GREEN,
        "DELETED": RED,
        "EDITED": YELLOW
    }
    action_term_color = action_colors.get(action, RESET)

    if message.guild:
        context, location, guild_name, context_color = f"Guild:{message.guild.id}", f"#{message.channel}", message.guild.name, CYAN
    elif isinstance(message.channel, discord.GroupChannel):
        context, location, guild_name, context_color = f"Group:{message.channel.id}", "Group DM", "Group DM", MAGENTA
    else:
        context, location, guild_name, context_color = f"DM:{message.channel.id}", "DM", "DM", ORANGE

    def html_escape(text):
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#39;")

    content = html_escape(message.content)
    author_name = html_escape(str(message.author))
    channel_name = html_escape(str(message.channel))
    guild_name_escaped = html_escape(guild_name)

    attachments = message.attachments
    attachments_str = " ".join(attachment.url for attachment in attachments) if attachments else ""
    console_attachments = f"{YELLOW}[Attachments: {attachments_str}]{RESET}" if attachments else ""

    def process_embeds(embeds):
        embed_content = []
        for embed in embeds:
            details = [
                f"Title: {embed.title}" if embed.title else "",
                f"Description: {embed.description}" if embed.description else "",
                *[f"Field: {field.name} - {field.value}" for field in embed.fields],
                f"Image: {embed.image.url}" if embed.image else "",
                f"Thumbnail: {embed.thumbnail.url}" if embed.thumbnail else "",
                f"Footer: {embed.footer.text}" if embed.footer else "",
                f"Author: {embed.author.name}" if embed.author else ""
            ]
            embed_content.append(" | ".join(filter(None, details)))
        return f" [Embed: {' | '.join(embed_content)}]" if embed_content else ""

    embed_str = process_embeds(message.embeds)

    # Console output
    colored_log = (
        f"{CYAN}[{timestamp}]{RESET} | "
        f"{action_term_color}{action.ljust(12)}{RESET} | "
        f"{context_color}{context.ljust(25)}{RESET} | "
        f"Guild: {guild_name.ljust(30)} | "
        f"Auth:{str(message.author.id).ljust(20)} | "
        f"{BLUE}{author_name.ljust(25)}{RESET} in "
        f"{GREEN}{location.ljust(20)}{RESET}: {content}{embed_str}"
        f"{console_attachments}{embed_str}"  # Added attachments display
    )
    print(colored_log)

    # Text file logging
    log_entry = (
        f"[{timestamp}] | "
        f"{action.ljust(10)} | "
        f"{context.ljust(25)} | "
        f"Guild: {guild_name.ljust(30)} | "
        f"Auth:{message.author.id} | "
        f"{author_name.ljust(25)} in "
        f"{location}: {message.content}"
    )
    
    if attachments_str:
        log_entry += f" [Attachments: {attachments_str}]"
    if embed_str:
        log_entry += f" {embed_str}"
    log_entry += "\n"

    try:
        with open("message_log.txt", "a", encoding="utf-8") as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Message log error: {e}")

@bot.event
async def on_voice_state_update(member, before, after):
    timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

    # Only trigger events on actual channel changes
    if before.channel != after.channel:
        # Handle leaving previous channel
        if before.channel is not None:
            log_voice_event("USER_LEFT", member, before.channel, timestamp)
            
            # Check if channel is now empty
            participants = get_channel_participants(before.channel)
            if participants == 1:  # If there's only the leaving member left
                log_voice_event("CALL_END", member, before.channel, timestamp)

        # Handle joining new channel
        if after.channel is not None:
            log_voice_event("USER_JOINED", member, after.channel, timestamp)
            
            # Check if first participant
            participants = get_channel_participants(after.channel)
            if participants == 1:  # Current user just joined
                log_voice_event("CALL_START", member, after.channel, timestamp)

@bot.event
async def on_member_update(before, after):
    timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    
    # Detect if the mute state changed
    if before.mute != after.mute:
        action = "MUTE_CHANGED"
        log_voice_event(action, after, after.guild, timestamp)  # Replace with actual channel/guild if needed

@bot.event
async def on_message(message):
    timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    log_message("CREATED", message, timestamp)
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    log_message("DELETED", message, timestamp)

@bot.event
async def on_message_edit(before, after):
    timestamp = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    log_message("EDITED", after, timestamp)

bot.run("") # Use your actual Discord token
