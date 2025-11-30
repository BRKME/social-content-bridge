# ❓ Frequently Asked Questions (FAQ)

## General Questions

### What does this bot do?

The bot takes messages you send to it, processes them with AI (translates, improves style), and automatically publishes them to your Telegram channel (full version) and Twitter (short version ≤280 characters).

### Is this bot free?

The bot code is free and open-source. However, you'll need to pay for:
- **OpenAI API**: ~$0.0004 per message (~$0.12/month for 10 posts/day)
- **VPS hosting** (optional): $4-6/month for 24/7 operation
- **Twitter API** and **Telegram** are free

### Do I need programming knowledge?

Basic knowledge helps, but detailed setup instructions are provided. If you can:
- Use command line (copy/paste commands)
- Edit text files
- Follow step-by-step instructions

Then you can set this up! 🎉

---

## Setup Questions

### Where do I get API keys?

- **Telegram Bot**: [@BotFather](https://t.me/botfather) - free
- **Twitter**: [Developer Portal](https://developer.twitter.com) - free
- **OpenAI**: [Platform](https://platform.openai.com) - paid, ~$0.0004/message
- **Your User ID**: [@userinfobot](https://t.me/userinfobot) - free

### How do I get my Telegram User ID?

Send any message to [@userinfobot](https://t.me/userinfobot) and it will reply with your user ID (a number like `123456789`).

### What's the difference between bot token and user ID?

- **Bot Token**: Authenticates your bot (from @BotFather)
- **User ID**: Your personal Telegram ID (ensures only you can use the bot)

### Can multiple people use the same bot?

Currently, only one authorized user (specified in `AUTHORIZED_USER_ID`) can use the bot. You can modify the code to support multiple users.

---

## Twitter API Questions

### Do I need Twitter API approval?

You need to create a Twitter developer account, which requires:
- Phone number verification
- Explanation of use case (just be honest - personal content automation)
- Usually approved within minutes to hours

### What Twitter API version do I need?

You need **Twitter API v2** with **OAuth 1.0a** authentication. The free tier works fine!

### How do I get OAuth 1.0a credentials?

1. Create app in Twitter Developer Portal
2. Go to app settings
3. Click "User authentication settings"
4. Enable OAuth 1.0a
5. Set permissions to "Read and Write"
6. Generate tokens

### Twitter says "Duplicate content"?

Twitter blocks duplicate tweets. Wait a few minutes or change the text slightly.

---

## OpenAI Questions

### Why OpenAI instead of free alternatives?

OpenAI (GPT-4o mini) provides excellent quality for:
- Translation (Russian → English)
- Style improvement
- Hashtag generation

Free alternatives (like Groq) work but may have lower quality. You can modify the code to use them!

### How much does OpenAI cost?

GPT-4o mini costs:
- Input: $0.150 per 1M tokens
- Output: $0.600 per 1M tokens
- **~$0.0004 per message**

For 10 posts/day: **~$0.12/month**
For 100 posts/day: **~$1.20/month**

Very affordable! 💰

### Can I use other AI models?

Yes! The code can be modified to use:
- Claude (Anthropic)
- Gemini (Google)
- Groq (free!)
- Local models (Llama, etc.)

See CONTRIBUTING.md for details.

### How do I set spending limits?

1. Go to [OpenAI Platform](https://platform.openai.com)
2. Go to Settings → Billing → Usage limits
3. Set monthly budget limit
4. Set email notifications

---

## Telegram Questions

### Can I use the bot in multiple channels?

Currently one channel per bot. You can run multiple bot instances for different channels.

### Does the bot need admin rights?

Yes, the bot needs to be an admin in your Telegram channel with "Post messages" permission.

### How do I add bot to my channel?

1. Go to your channel settings
2. Administrators → Add Administrator
3. Search for your bot username
4. Give "Post messages" permission

### Can the bot post to private channels?

Yes! Use channel ID (like `-1001234567890`) instead of username.

### How do I get my channel ID?

1. Add bot to channel as admin
2. Forward a message from the channel to [@userinfobot](https://t.me/userinfobot)
3. It will show the channel ID

---

## Usage Questions

### What content can I send?

✅ **Supported:**
- Text messages (any language)
- Photos (JPEG, PNG)
- Messages with text + photo
- Photo-only (AI generates caption)

❌ **Not supported:**
- Videos
- Multiple photos (only first is used)
- GIFs, stickers, audio
- Documents

### Why only first image?

For simplicity and Twitter compatibility. Could be extended to support multiple images (Twitter allows up to 4).

### Can I edit the message before publishing?

Currently, the bot publishes automatically. You can modify the code to add a confirmation step.

### How long does processing take?

Usually 2-5 seconds:
- AI processing: 1-3 seconds
- Publishing: 1-2 seconds

### What if I send wrong message?

Delete it from your channel/Twitter manually. The bot doesn't have an "undo" feature (yet).

---

## Technical Questions

### What Python version do I need?

Python 3.9 or higher. Recommended: Python 3.11+

### Can I run this on Windows?

Yes! All instructions work on Windows, Mac, and Linux.

### Do I need a server?

For 24/7 operation, yes. Options:
- VPS ($4-6/month)
- Raspberry Pi (one-time ~$35-75)
- Your computer (free but must stay on)

### Can I use shared hosting?

No, you need SSH access and ability to run Python scripts. VPS or dedicated server required.

### How much RAM does it need?

Very little! 512 MB RAM is enough. Recommended: 1 GB for comfort.

---

## Troubleshooting

### "Module not found" error?

```bash
pip install -r requirements.txt
```

### "Missing required environment variables"?

Check your `.env` file:
- Does it exist? (`ls -la .env`)
- Are all values filled in? (`cat .env`)
- No spaces around `=`? (Correct: `KEY=value`, not `KEY = value`)

### Bot doesn't respond to my messages?

1. Check if bot is running (`systemctl status content-bridge`)
2. Verify your user ID is correct in `.env`
3. Check logs (`journalctl -u content-bridge -f`)
4. Make sure you're messaging the correct bot

### "Unauthorized" error from Telegram?

Your bot token is incorrect. Get a new one from [@BotFather](https://t.me/botfather).

### "Forbidden" error when posting to channel?

Bot is not admin in the channel or lacks "Post messages" permission.

### Twitter publishing fails?

1. Check credentials in `.env`
2. Verify OAuth 1.0a is enabled
3. Check permissions are "Read and Write"
4. Wait a few minutes (rate limits)

### Images don't upload?

1. Check image format (JPEG/PNG)
2. Check file size (<5MB)
3. Check disk space (`df -h`)
4. Check logs for errors

### OpenAI "Rate limit" error?

You're sending too many requests. Wait a minute or upgrade your OpenAI plan.

### OpenAI "Insufficient credits" error?

Add credits to your OpenAI account at [platform.openai.com/account/billing](https://platform.openai.com/account/billing).

---

## Cost & Performance

### What's the total monthly cost?

Minimal setup:
- OpenAI: $0.12-1.20/month (depends on usage)
- VPS: $4-6/month (optional, for 24/7)
- Twitter: Free
- Telegram: Free

**Total: $4-7/month** for 24/7 operation with moderate usage.

### Can I reduce costs?

Yes!
- Use free AI (Groq, Gemini free tier)
- Run on Raspberry Pi or old computer
- Reduce posting frequency

### Is there a free option?

Yes! Use:
- **Groq** (free AI with generous limits)
- **Run locally** on your computer (free hosting)
- **Telegram + Twitter APIs** are free

Only cost: ~$0 with Groq!

---

## Privacy & Security

### Is my data stored anywhere?

No! The bot:
- Processes messages in real-time
- Doesn't store any content
- Temporary images are deleted after publishing

### Who can see my API keys?

Only you (if you keep `.env` secure). Never share your `.env` file!

### Can I make the repo private?

Yes! Fork it and make your fork private. The code is open-source under MIT license.

### What data goes to OpenAI?

Only the text you send to the bot. OpenAI:
- Processes the text
- Returns improved version
- May store for 30 days (per their policy)
- Does not use for training (with API)

---

## Feature Requests

### Can you add [feature]?

Open an issue on GitHub! Or submit a pull request. See CONTRIBUTING.md.

### Planned features?

Potential future additions:
- Multiple channel support
- Video support
- Instagram integration
- Scheduling
- Analytics
- Multiple AI providers
- Web dashboard

### Can I add custom AI prompts?

Yes! Edit `bot/ai_processor.py` and modify the `_build_prompt()` method.

---

## Getting Help

### Where can I get help?

1. Check this FAQ
2. Read README.md and DEPLOYMENT.md
3. Check existing GitHub issues
4. Open a new issue with:
   - Error messages
   - Logs
   - What you've tried

### How do I report bugs?

See CONTRIBUTING.md for bug report template. Include:
- OS and Python version
- Error messages
- Steps to reproduce
- What you expected vs what happened

---

## Miscellaneous

### Can I use this commercially?

Yes! MIT license allows commercial use. Just keep the license file.

### Can I modify the code?

Yes! Fork it, modify it, make it yours! MIT license is very permissive.

### Will you maintain this project?

Yes! Issues and PRs are welcome. Project is actively maintained.

### Can I donate?

Stars ⭐ on GitHub are appreciated! Or contribute code/documentation.

### Who made this?

This is an open-source project. See CONTRIBUTING.md to become a contributor!

---

**Still have questions?** Open an issue on GitHub! 🙋‍♂️
