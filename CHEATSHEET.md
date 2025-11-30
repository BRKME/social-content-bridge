# 📋 Cheat Sheet

Quick reference for common tasks.

## Installation

```bash
git clone https://github.com/yourusername/social-content-bridge.git
cd social-content-bridge
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
python main.py
```

## Environment Variables

```bash
TELEGRAM_BOT_TOKEN=         # From @BotFather
TELEGRAM_CHANNEL_ID=        # Your channel @username or ID
AUTHORIZED_USER_ID=         # From @userinfobot
TWITTER_API_KEY=            # Twitter developer portal
TWITTER_API_SECRET=         
TWITTER_ACCESS_TOKEN=       
TWITTER_ACCESS_SECRET=      
TWITTER_BEARER_TOKEN=       
OPENAI_API_KEY=             # From platform.openai.com
```

## Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Show welcome message |
| `/help` | Show help and features |

## Local Development

```bash
# Run bot
python main.py

# Stop bot
Ctrl + C

# View in debug mode
LOG_LEVEL=DEBUG python main.py
```

## VPS Deployment

```bash
# Install dependencies
apt update && apt install -y python3 python3-pip git

# Clone and setup
cd /opt
git clone <repo-url>
cd social-content-bridge
pip3 install -r requirements.txt
nano .env  # Add credentials

# Create service
nano /etc/systemd/system/content-bridge.service

# Enable and start
systemctl daemon-reload
systemctl enable content-bridge
systemctl start content-bridge

# Check status
systemctl status content-bridge

# View logs
journalctl -u content-bridge -f
```

## Systemd Service Commands

```bash
systemctl start content-bridge      # Start bot
systemctl stop content-bridge       # Stop bot
systemctl restart content-bridge    # Restart bot
systemctl status content-bridge     # Check status
systemctl enable content-bridge     # Enable auto-start
systemctl disable content-bridge    # Disable auto-start
journalctl -u content-bridge -f     # Live logs
journalctl -u content-bridge -n 100 # Last 100 lines
```

## Docker

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down

# Restart
docker-compose restart

# Rebuild
docker-compose up -d --build
```

## Git Workflow

```bash
# Clone
git clone <repo-url>

# Create branch
git checkout -b feature/my-feature

# Check status
git status

# Add changes
git add .

# Commit
git commit -m "Description"

# Push
git push origin feature/my-feature

# Update from main
git pull origin main
```

## Troubleshooting

### Bot not responding
```bash
# Check if running
systemctl status content-bridge

# Check logs
journalctl -u content-bridge -n 50

# Restart
systemctl restart content-bridge
```

### Environment variable errors
```bash
# Verify .env exists
ls -la .env

# Check contents (hide sensitive data when sharing!)
cat .env

# Reload if changed
systemctl restart content-bridge
```

### Twitter API errors
```bash
# Check credentials in .env
# Verify OAuth 1.0a is enabled
# Check rate limits on developer.twitter.com
```

### OpenAI errors
```bash
# Check API key is valid
# Verify credits in account
# Check usage limits
```

## File Locations

```
/opt/social-content-bridge/     # Bot files (VPS)
/etc/systemd/system/            # Service file
/tmp/ or temp/                  # Temporary images
~/.openai/                      # OpenAI cache (if any)
```

## Logs Location

```bash
# Systemd logs
journalctl -u content-bridge

# If logging to file
tail -f /var/log/content-bridge.log
```

## Monitoring

```bash
# Check bot process
ps aux | grep python

# Check memory usage
free -h

# Check disk space
df -h

# Check CPU usage
top

# Check network
netstat -tuln
```

## Backup

```bash
# Backup .env
cp .env .env.backup

# Backup entire project
tar -czf content-bridge-backup.tar.gz social-content-bridge/

# Restore
tar -xzf content-bridge-backup.tar.gz
```

## Update Bot

```bash
cd /opt/social-content-bridge
git pull
pip3 install -r requirements.txt --upgrade
systemctl restart content-bridge
```

## Testing

```bash
# Test locally
python main.py

# Send test message
# Forward a message to your bot

# Check logs
journalctl -u content-bridge -f
```

## Useful Links

- Telegram BotFather: https://t.me/botfather
- Get User ID: https://t.me/userinfobot
- Twitter Dev Portal: https://developer.twitter.com
- OpenAI Platform: https://platform.openai.com
- Project Repo: [Add your GitHub URL]

## Quick Fixes

### "Module not found"
```bash
pip install -r requirements.txt
```

### "Permission denied"
```bash
chmod +x main.py
# or run with: python3 main.py
```

### Port already in use
```bash
# Find process
lsof -i :8080
# Kill process
kill -9 <PID>
```

### Out of memory
```bash
# Check usage
free -h
# Upgrade VPS or add swap
```

## Cost Tracking

```bash
# OpenAI usage
# Check: platform.openai.com/usage

# Twitter API usage
# Check: developer.twitter.com/en/portal/dashboard

# VPS costs
# Check your provider dashboard
```

## Security

```bash
# Change permissions
chmod 600 .env

# Update packages
apt update && apt upgrade -y

# Check for security updates
apt list --upgradable

# Enable firewall
ufw enable
ufw allow 22
```

## Performance Tips

- Use SSD VPS for better I/O
- Set appropriate LOG_LEVEL (INFO for production)
- Clean temp files regularly
- Monitor OpenAI costs
- Set rate limits if needed

## Getting Help

1. Check logs first
2. Review documentation
3. Search existing issues
4. Open new issue with details
5. Join community discussions

---

**Pro Tip:** Bookmark this page for quick reference! 🔖
