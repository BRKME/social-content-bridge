# 📝 Usage Examples

## Example 1: Russian Text → English

**You send to bot:**
```
Вчера я посетил удивительную выставку современного искусства. 
Картины были невероятно красочными и эмоциональными. 
Очень рекомендую всем любителям искусства!
```

**Bot publishes to Telegram (full version):**
```
Yesterday, I visited an amazing contemporary art exhibition. 
The paintings were incredibly colorful and emotional. 
I highly recommend it to all art lovers!
```

**Bot publishes to Twitter (short version):**
```
Amazing contemporary art exhibition! Colorful, emotional paintings. 
Highly recommend! 🎨 #art #exhibition #contemporary #culture
```

---

## Example 2: English Text Improvement

**You send to bot:**
```
today i went to new restaurant and food was good 
the service also nice i think u should try it
```

**Bot publishes to Telegram (full version):**
```
Today, I visited a new restaurant and the food was excellent. 
The service was also wonderful. I highly recommend you try it!
```

**Bot publishes to Twitter (short version):**
```
Tried a new restaurant today - excellent food and wonderful service! 
Highly recommend checking it out! 🍽️ #foodie #restaurant #dining
```

---

## Example 3: Text with Image

**You send to bot:**
```
Закат на пляже сегодня был особенно красивым
[image of sunset]
```

**Bot publishes to Telegram:**
```
The sunset on the beach today was particularly beautiful
[image]
```

**Bot publishes to Twitter:**
```
Beautiful beach sunset today! Nature at its finest 🌅 
#sunset #beach #nature #photography #beautiful
[image]
```

---

## Example 4: Image Only (No Text)

**You send to bot:**
```
[image of food]
```

**Bot generates and publishes:**

**Telegram:**
```
Delicious meal beautifully presented! Perfect combination of flavors and colors. 
A true culinary masterpiece. 🍽️
[image]
```

**Twitter:**
```
Culinary perfection! Beautiful presentation and amazing flavors 😋 
#food #foodporn #delicious #instafood #yummy
[image]
```

---

## Example 5: Long Article → Short Tweet

**You send to bot:**
```
Artificial Intelligence is revolutionizing the way we work and live. 
From healthcare to transportation, AI is making processes more efficient 
and accurate. Machine learning algorithms can now predict diseases, 
optimize traffic flow, and even create art. However, we must also 
consider the ethical implications and ensure that AI development 
benefits all of humanity. The future is exciting, but we must 
proceed thoughtfully and responsibly.
```

**Bot publishes to Telegram (full version):**
```
Artificial Intelligence is revolutionizing how we work and live. 
From healthcare to transportation, AI makes processes more efficient and accurate. 
ML algorithms can now predict diseases, optimize traffic, and create art. 
However, we must consider ethical implications and ensure AI benefits all humanity. 
The future is exciting, but we must proceed thoughtfully and responsibly.
```

**Bot publishes to Twitter (short version):**
```
AI is revolutionizing work and life - from healthcare to art! 
But we must consider ethics and ensure it benefits everyone. 
Exciting future ahead! 🤖 #AI #technology #future #ethics
```

---

## Bot Commands

### `/start`
Shows welcome message:
```
🤖 Social Content Bridge Bot

I will help you republish content to your Telegram channel and Twitter!

📝 How to use:
1. Forward any message to me (text and/or image)
2. I will process it with AI
3. I will automatically publish to your channel and Twitter

🔧 Use /help for more information
```

### `/help`
Shows detailed help:
```
📖 Help

Features:
✅ Translate Russian to English
✅ Improve text style
✅ Generate short version for Twitter (≤280 chars)
✅ Add relevant hashtags
✅ Support images (first image only)
✅ Generate captions for image-only posts

What to send:
• Text messages
• Messages with images
• Images only (AI will generate caption)

Not supported:
• Videos
• Multiple images (only first is used)
• Audio files

🔐 Only authorized user can use this bot
```

---

## Processing Flow

```
1. You send message to bot
   ↓
2. Bot downloads image (if present)
   ↓
3. Bot sends text to OpenAI GPT-4o mini
   ↓
4. AI processes:
   - Detects language
   - Translates if Russian
   - Improves style
   - Creates full version
   - Creates short version (<280 chars)
   - Adds relevant hashtags
   ↓
5. Bot publishes full version → Telegram channel
   ↓
6. Bot publishes short version → Twitter
   ↓
7. Bot notifies you: ✅ Success or ❌ Error
```

---

## Status Messages

While processing, you'll see:

```
⏳ Processing your message...
🤖 Processing with AI...
📤 Publishing to Telegram...
🐦 Publishing to Twitter...

Publishing complete!
✅ Telegram | ✅ Twitter

📝 Full text: 145 chars
🐦 Short text: 267 chars
```

If something fails:
```
Publishing complete!
✅ Telegram | ❌ Twitter

📝 Full text: 145 chars
🐦 Short text: 267 chars
```

---

## Tips for Best Results

1. **Clear Text**: Write clear, complete sentences for best AI processing
2. **Image Quality**: Use high-quality images (will be optimized automatically)
3. **Context**: Provide context in your text - AI works better with full information
4. **Length**: Don't worry about length - AI will handle it
5. **Language**: Russian automatically translates to English
6. **Hashtags**: AI adds relevant hashtags automatically - no need to include them

---

## What NOT to Send

❌ Videos (not supported)
❌ Multiple images (only first will be used)
❌ Audio files
❌ Documents
❌ Stickers
❌ GIFs

---

## Cost per Message

With GPT-4o mini (~$0.0004 per message):

- 10 messages/day = **$0.12/month**
- 30 messages/day = **$0.36/month**
- 100 messages/day = **$1.20/month**

Very affordable! 💰
