# 📁 Project Structure

Visual guide to the project organization.

## Directory Tree

```
social-content-bridge/
│
├── 📄 main.py                      # Entry point - run this to start the bot
│
├── 📋 requirements.txt             # Python dependencies
│
├── 🔧 .env.example                 # Template for environment variables
├── 🔧 .env                         # Your actual credentials (create this, not in repo)
├── 🚫 .gitignore                   # Files to ignore in git
│
├── 📖 README.md                    # Main documentation
├── 📖 QUICKSTART.md                # Quick setup guide
├── 📖 EXAMPLES.md                  # Usage examples
├── 📖 DEPLOYMENT.md                # Deployment instructions
├── 📖 FAQ.md                       # Frequently asked questions
├── 📖 CHEATSHEET.md                # Quick reference
├── 📖 CONTRIBUTING.md              # Contribution guidelines
├── 📖 PROJECT_STRUCTURE.md         # This file
│
├── ⚖️  LICENSE                      # MIT License
│
├── 🤖 bot/                         # Main bot modules
│   ├── __init__.py
│   ├── telegram_handler.py        # Receives messages, orchestrates flow
│   ├── ai_processor.py            # Processes text with OpenAI
│   ├── telegram_publisher.py      # Publishes to Telegram channel
│   └── twitter_publisher.py       # Publishes to Twitter
│
├── ⚙️  config/                     # Configuration
│   ├── __init__.py
│   └── settings.py                # Loads and validates environment variables
│
└── 🛠️  utils/                      # Utility modules
    ├── __init__.py
    ├── image_handler.py           # Image download, optimization, cleanup
    └── logger.py                  # Colored logging setup
```

## File Descriptions

### Root Files

#### `main.py`
- **Purpose**: Entry point for the application
- **What it does**: Initializes and runs the bot
- **How to use**: `python main.py`

#### `requirements.txt`
- **Purpose**: List of Python dependencies
- **What it does**: Defines packages needed to run the bot
- **How to use**: `pip install -r requirements.txt`

#### `.env.example`
- **Purpose**: Template for environment variables
- **What it does**: Shows which variables you need to set
- **How to use**: Copy to `.env` and fill in your credentials

#### `.gitignore`
- **Purpose**: Git ignore rules
- **What it does**: Prevents committing sensitive files (like `.env`)
- **Important**: NEVER commit `.env` to git!

### Bot Module (`bot/`)

#### `telegram_handler.py`
**The main orchestrator** 🎯

- Receives messages from user
- Downloads images if present
- Calls AI processor
- Calls publishers
- Handles errors
- Sends status updates

**Key class**: `TelegramHandler`

**Main methods**:
- `handle_message()` - Processes incoming messages
- `start_command()` - /start command
- `help_command()` - /help command
- `run()` - Starts the bot

#### `ai_processor.py`
**The brain** 🧠

- Processes text with OpenAI GPT-4o mini
- Translates Russian to English
- Improves writing style
- Creates full and short versions
- Generates hashtags
- Handles image-only messages

**Key class**: `AIProcessor`

**Main methods**:
- `process_message()` - Main processing function
- `_build_prompt()` - Creates AI prompt
- `_generate_image_description()` - For image-only posts

#### `telegram_publisher.py`
**Telegram poster** 📢

- Publishes to Telegram channel
- Handles text and images
- Supports HTML formatting

**Key class**: `TelegramPublisher`

**Main method**:
- `publish()` - Publishes to channel

#### `twitter_publisher.py`
**Twitter poster** 🐦

- Publishes to Twitter
- Uploads images
- Handles tweet length (≤280 chars)

**Key class**: `TwitterPublisher`

**Main method**:
- `publish()` - Creates tweet

### Config Module (`config/`)

#### `settings.py`
**Configuration manager** ⚙️

- Loads environment variables from `.env`
- Validates required settings
- Provides global config object
- Creates temp directory

**Key class**: `Config`

**Accessed as**: `from config import config`

### Utils Module (`utils/`)

#### `image_handler.py`
**Image utilities** 🖼️

- Downloads images from Telegram
- Optimizes images for social media
- Handles size/format conversion
- Cleans up temporary files

**Key class**: `ImageHandler`

**Main methods**:
- `download_image()` - Downloads from Telegram
- `optimize_image()` - Compresses for Twitter (≤5MB)
- `cleanup()` - Removes temp files

#### `logger.py`
**Logging setup** 📝

- Configures colored console output
- Sets log levels
- Formats log messages

**Main function**: `setup_logger(name)`

## Data Flow

```
1. User sends message to bot
         ↓
2. TelegramHandler receives it
         ↓
3. Downloads image (if present)
    ↓                              ↓
4. ImageHandler.download()    Image stored in temp/
         ↓
5. AIProcessor.process_message()
    ↓                              ↓
6. OpenAI API call            Returns: full_text, short_text
         ↓
7. TelegramPublisher.publish(full_text, image)
    ↓                              ↓
8. Posted to channel          ✅ Telegram success
         ↓
9. TwitterPublisher.publish(short_text, image)
    ↓                              ↓
10. Posted to Twitter         ✅ Twitter success
         ↓
11. ImageHandler.cleanup()
         ↓
12. Temp files removed
         ↓
13. User gets success message
```

## Important Variables

### Environment Variables (in `.env`)

| Variable | Source | Purpose |
|----------|--------|---------|
| `TELEGRAM_BOT_TOKEN` | @BotFather | Bot authentication |
| `TELEGRAM_CHANNEL_ID` | Your channel | Where to post |
| `AUTHORIZED_USER_ID` | @userinfobot | Who can use bot |
| `TWITTER_API_KEY` | Twitter Dev Portal | Twitter auth |
| `TWITTER_API_SECRET` | Twitter Dev Portal | Twitter auth |
| `TWITTER_ACCESS_TOKEN` | Twitter Dev Portal | Twitter auth |
| `TWITTER_ACCESS_SECRET` | Twitter Dev Portal | Twitter auth |
| `TWITTER_BEARER_TOKEN` | Twitter Dev Portal | Twitter auth |
| `OPENAI_API_KEY` | OpenAI Platform | AI processing |

### Directories Created at Runtime

```
social-content-bridge/
├── temp/              # Temporary image storage (created automatically)
│   └── *.jpg         # Downloaded images (deleted after use)
```

## Dependencies Overview

### Core Dependencies

- **python-telegram-bot** - Telegram Bot API wrapper
- **tweepy** - Twitter API wrapper
- **openai** - OpenAI API client
- **python-dotenv** - Environment variable management
- **Pillow** - Image processing
- **aiohttp** - Async HTTP requests
- **colorlog** - Colored console logs

### Why Each Dependency?

| Package | Purpose | Can be removed? |
|---------|---------|-----------------|
| python-telegram-bot | Telegram integration | ❌ Core |
| tweepy | Twitter integration | ❌ Core |
| openai | AI processing | ⚠️ Can swap for other AI |
| python-dotenv | Load .env file | ❌ Core |
| Pillow | Image optimization | ⚠️ If no images |
| aiohttp | Async networking | ❌ Required by other libs |
| colorlog | Pretty logs | ✅ Optional |

## Module Dependencies

```
main.py
 └── bot.telegram_handler
      ├── config.settings ──→ python-dotenv
      ├── utils.image_handler
      │    └── Pillow
      ├── bot.ai_processor
      │    └── openai
      ├── bot.telegram_publisher
      │    └── python-telegram-bot
      └── bot.twitter_publisher
           └── tweepy
```

## Configuration Flow

```
1. Load .env file
    ↓
2. config.settings.py reads variables
    ↓
3. Config() class validates them
    ↓
4. Global 'config' object created
    ↓
5. All modules import: from config import config
    ↓
6. Access values: config.TELEGRAM_BOT_TOKEN
```

## Error Handling Flow

```
Try to process message
    ↓
Error occurs?
    ├─ Yes → Log error
    │         ├─ Send error message to user
    │         ├─ Clean up temp files
    │         └─ Continue running
    │
    └─ No → Success!
            ├─ Send success message
            ├─ Clean up temp files
            └─ Continue running

Bot never crashes on single message errors!
```

## Security Considerations

### ✅ Secure

- `.env` in `.gitignore`
- Only authorized user can use bot
- Temp files cleaned up
- API keys never logged

### ⚠️ Be Careful

- Keep `.env` file private
- Don't share logs publicly (may contain message content)
- Set OpenAI spending limits
- Monitor API usage

### ❌ Never Do

- Commit `.env` to git
- Share API keys publicly
- Run as root (on server)
- Disable security checks

## Performance

### Resource Usage

- **CPU**: Very low (~1-5% when idle, ~20-30% when processing)
- **RAM**: ~50-150 MB
- **Disk**: Minimal (temp images deleted)
- **Network**: Only during API calls

### Bottlenecks

1. **OpenAI API** - Typically 1-3 seconds
2. **Image upload** - Depends on image size and connection
3. **Telegram/Twitter APIs** - Usually fast (<1 second)

### Optimization Tips

- Keep images reasonably sized
- Use appropriate log level (INFO for production)
- Clean temp directory regularly
- Monitor API rate limits

## Extending the Bot

### Adding New AI Provider

1. Create new method in `ai_processor.py`
2. Add API key to `config/settings.py`
3. Update `.env.example`
4. Add to `requirements.txt` if needed

### Adding New Social Platform

1. Create `bot/platform_publisher.py`
2. Add credentials to `config/settings.py`
3. Update `telegram_handler.py` to call it
4. Update documentation

### Adding Features

1. Modify relevant module
2. Test locally
3. Update documentation
4. Submit PR (optional)

## Testing Strategy

### Local Testing

```bash
# 1. Setup
cp .env.example .env
# Fill in .env

# 2. Install
pip install -r requirements.txt

# 3. Run
python main.py

# 4. Test
# Send messages to bot
# Check logs
# Verify posts in channel/Twitter
```

### Production Testing

```bash
# After deploying to VPS
systemctl status content-bridge
journalctl -u content-bridge -f
# Send test message
# Monitor logs
```

## Maintenance

### Regular Tasks

- **Weekly**: Check logs for errors
- **Monthly**: Update dependencies
- **As needed**: Rotate API keys

### Updates

```bash
# Pull latest code
git pull

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart
systemctl restart content-bridge
```

---

**Questions about structure?** See FAQ.md or open an issue! 💬
