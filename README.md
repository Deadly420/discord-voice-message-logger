
# 💬 Discord.py Self-Logging Bot

A powerful self-bot built with `discord.py-self` for logging messages and voice events with colorized terminal output and structured file storage.

> ⚠️ **Disclaimer**: Self-bots are against [Discord's Terms of Service](https://discord.com/terms). Use at your own risk.

---

## ✅ Features

- 🎙 **Voice Event Logging**:
  - User joined/left voice channels
  - Call start/end detection
  - Mute state changes

- 💬 **Message Logging**:
  - Created, edited, and deleted messages
  - Captures attachments and embeds
  - Resolves mentions and role tags

- 📁 **Log Management**:
  - Separate folders per guild, group DM, or DM
  - Auto-rotating log files (500MB max per file)
  - Clean terminal output with ANSI color codes

- 🧠 **Filtering**:
  - Option to log only specific users or guilds

---

## 📦 Requirements

- Python 3.8+
- [`discord.py-self`](https://pypi.org/project/discord.py-self/)
- `colorama`

Install dependencies:
```bash
pip install discord.py-self colorama
```

---

## 🛠️ Setup & Usage

1. **Clone or copy the script**

2. **Insert your Discord token:**
   ```python
   bot.run("YOUR_TOKEN_HERE")
   ```

3. **Run the bot:**
   ```bash
   python selfbot.py
   ```

---

## 🎯 Target Filtering (Optional)

Inside `selfbot.py`, configure these:

```python
LOG_TARGETS_ONLY = True  # Set to True to enable filtering

TARGET_USER_IDS = [123456789012345678]  # User IDs to log
TARGET_GUILD_IDS = [987654321098765432]  # Guild IDs to log
```

- Set `LOG_TARGETS_ONLY` to `True` to activate the filters.
- Leave it `False` to log everything.

---

## 🗃️ File Structure

```
logs/
├── 509594441883975695/         # Guild ID folder
│   ├── message_log.txt         # Rolling message logs
│   └── voice_log.txt           # Rolling voice logs
├── DM/                         # Direct Messages
├── group_1234567890/           # Group DMs
```

- Files automatically rotate if they exceed 500MB.

---

## 🔍 Events Tracked

| Type       | Event                  | Description                          |
|------------|------------------------|--------------------------------------|
| Message    | Created, Edited, Deleted | Captures full message content, mentions, embeds, and attachments |
| Voice      | Joined, Left           | Detects user activity in voice channels |
| Voice      | Call Start, Call End   | Based on user presence in voice channels |
| Voice      | Mute Changes           | Tracks mute/unmute state            |

---

## 🧪 Troubleshooting

- ❌ **Token not working?**
  - Make sure it's a user token, not a bot token. (Again, self-bots violate Discord ToS.)

- 🧼 **Reinstall dependencies**
  ```bash
  pip uninstall discord.py-self
  pip install discord.py-self
  ```

- 🛑 **Permission errors?**
  - Ensure your account has access to the messages or channels you're trying to log.

---

## 🧾 License

**MIT License**

```
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
```
