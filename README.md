# Discord.py-Self Logging Bot

A simple self-bot script using `discord.py-self` for logging voice and message events on Discord.

## Features
- Logs voice events such as user joins, leaves, call starts, and call ends.
- Logs message events including creation, deletion, and edits.
- Outputs logs with colored terminal formatting and stores them in text files.
- Supports logging embeds and attachments in messages.
- Handles group DMs and direct messages.
- Lightweight and efficient logging mechanism.

## Requirements
- Python 3.8+
- `discord.py-self` library

## Installation
It is recommended to use a virtual environment to manage dependencies and avoid conflicts.

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
2. Install the required library:
   ```bash
   pip install discord.py-self
   ```
3. Save the provided script as `selfbot.py`.
4. Insert your Discord token into `bot.run("")`.
5. Run the script using:
   ```bash
   python selfbot.py
   ```

## Target Filtering
To enable targeted logging, configure the following options in `selfbot.py`:

```python
LOG_TARGETS_ONLY = False  # Set to True to log only specific users/guilds
TARGET_USER_IDS = [1199251895399759962]  # Add user IDs to log
TARGET_GUILD_IDS = [509594441883975695]  # Add guild IDs to log
```

- If `LOG_TARGETS_ONLY` is `True`, only the specified users and guilds will be logged.
- If `LOG_TARGETS_ONLY` is `False`, logging applies to all users and guilds.

## Script Overview
```python
import discord
from discord.ext import commands
import datetime

# Configuration
LOG_TARGETS_ONLY = False  # Set to False to log everyone
TARGET_USER_IDS = [
    1199251895399759962
]

TARGET_GUILD_IDS = [
    509594441883975695
]

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

# Voice Logging Functions
# - Get channel participants
# - Log voice events

# Message Logging Functions
# - Log message events (create, delete, edit)

# Event Listeners
# - on_voice_state_update
# - on_member_update
# - on_message
# - on_message_delete
# - on_message_edit

bot.run("")  # Insert your Discord token here
```

## Usage
- Run the script:
  ```bash
  python selfbot.py
  ```
- The bot will log messages and voice events automatically.

## Troubleshooting
- Ensure you have entered a valid Discord token.
- If you encounter issues with `discord.py-self`, try reinstalling:
  ```bash
  pip uninstall discord.py-self
  pip install discord.py-self
  ```
- Running into permission errors? Make sure your account has necessary access to the channels you want to log.

## Disclaimer
Using self-bots is against Discord's Terms of Service. Proceed at your own risk.

## License

MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

