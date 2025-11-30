# 🚀 Quick Start Guide

## Step 1: Install Python

Make sure you have Python 3.9+ installed:

```bash
python --version
```

## Step 2: Install Dependencies

```bash
cd social-content-bridge
pip install -r requirements.txt
```

## Step 3: Get API Keys

### Telegram Bot
1. Message [@BotFather](https://t.me/botfather) → `/newbot`
2. Get your bot token
3. Message [@userinfobot](https://t.me/userinfobot) to get your user ID

### Twitter API
1. Go to https://developer.twitter.com/en/portal/dashboard
2. Create app with OAuth 1.0a
3. Set permissions: Read and Write
4. Get all 5 credentials

### OpenAI API
1. Go to https://platform.openai.com/api-keys
2. Create new API key
3. Add $5-10 credits

## Step 4: Configure

```bash
cp .env.example .env
nano .env  # or use any text editor
```

Fill in ALL the values in `.env`:

```env
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz  # From BotFather
TELEGRAM_CHANNEL_ID=@your_channel                        # Your channel
AUTHORIZED_USER_ID=123456789                             # From userinfobot
TWITTER_API_KEY=abc123...                                # From Twitter
TWITTER_API_SECRET=xyz789...
TWITTER_ACCESS_TOKEN=123-abc...
TWITTER_ACCESS_SECRET=def456...
TWITTER_BEARER_TOKEN=AAAAAAA...
OPENAI_API_KEY=sk-proj-...                               # From OpenAI
```

## Step 5: Run

```bash
python main.py
```

You should see:

```
============================================================
Social Content Bridge Bot
============================================================
🚀 Starting bot...
📢 Channel: @your_channel
👤 Authorized user: 123456789
```

## Step 6: Test

1. Open your bot in Telegram
2. Send `/start`
3. Forward any message with text/image
4. Bot will process and publish automatically! ✨

## Common Issues

### "Missing required environment variables"
→ Check your `.env` file, make sure all values are filled

### Bot doesn't respond
→ Make sure you're using the correct user ID from @userinfobot

### Twitter fails
→ Double-check you have OAuth 1.0a credentials, not OAuth 2.0

### OpenAI errors
→ Make sure you have credits in your OpenAI account

## Need Help?

Check the full [README.md](README.md) for detailed instructions and troubleshooting!
