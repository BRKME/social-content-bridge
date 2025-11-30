# 🚀 Deployment Guide

This guide explains how to deploy your bot to run 24/7.

## Option 1: Local Computer (Simplest)

Just run the bot on your computer:

```bash
python main.py
```

**Pros:**
- ✅ Free
- ✅ Easy to test and debug
- ✅ Full control

**Cons:**
- ❌ Computer must stay on
- ❌ Bot stops if computer sleeps/restarts
- ❌ Uses your internet connection

---

## Option 2: VPS (Recommended for 24/7)

Deploy to a Virtual Private Server like DigitalOcean, AWS, or Hetzner.

### Step 1: Get a VPS

**Recommended providers:**
- [DigitalOcean](https://www.digitalocean.com) - $4-6/month
- [Hetzner](https://www.hetzner.com) - €4-5/month
- [AWS Lightsail](https://aws.amazon.com/lightsail/) - $3.50/month
- [Vultr](https://www.vultr.com) - $2.50-6/month

**Specs needed:**
- 1 CPU core
- 512 MB - 1 GB RAM
- 10 GB storage
- Ubuntu 20.04 or 22.04

### Step 2: Connect to VPS

```bash
ssh root@your_vps_ip
```

### Step 3: Install Python and Git

```bash
apt update
apt install -y python3 python3-pip git
```

### Step 4: Clone and Setup

```bash
cd /opt
git clone https://github.com/yourusername/social-content-bridge.git
cd social-content-bridge
pip3 install -r requirements.txt
```

### Step 5: Configure Environment

```bash
nano .env
```

Paste your credentials and save (Ctrl+X, then Y, then Enter).

### Step 6: Test Run

```bash
python3 main.py
```

Press Ctrl+C to stop.

### Step 7: Create Systemd Service

Create service file:

```bash
nano /etc/systemd/system/content-bridge.service
```

Paste this configuration:

```ini
[Unit]
Description=Social Content Bridge Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/social-content-bridge
ExecStart=/usr/bin/python3 /opt/social-content-bridge/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Save and exit.

### Step 8: Enable and Start Service

```bash
systemctl daemon-reload
systemctl enable content-bridge
systemctl start content-bridge
```

### Step 9: Check Status

```bash
systemctl status content-bridge
```

You should see "active (running)" in green.

### Step 10: View Logs

```bash
journalctl -u content-bridge -f
```

Press Ctrl+C to exit.

### Useful Commands

```bash
# Stop bot
systemctl stop content-bridge

# Start bot
systemctl start content-bridge

# Restart bot
systemctl restart content-bridge

# View logs
journalctl -u content-bridge -f

# View last 100 lines
journalctl -u content-bridge -n 100
```

### Update Bot on VPS

```bash
cd /opt/social-content-bridge
git pull
systemctl restart content-bridge
```

---

## Option 3: Raspberry Pi

Perfect for home 24/7 deployment!

### Requirements
- Raspberry Pi 3 or 4
- MicroSD card (16GB+)
- Raspberry Pi OS installed

### Steps

1. **SSH into Pi:**
```bash
ssh pi@raspberrypi.local
```

2. **Update system:**
```bash
sudo apt update
sudo apt upgrade -y
```

3. **Follow VPS steps 4-10** (same process)

**Pros:**
- ✅ One-time cost (~$35-75)
- ✅ Low power consumption
- ✅ Runs at home
- ✅ Full control

**Cons:**
- ❌ Depends on home internet
- ❌ Power outages affect it

---

## Option 4: Docker (Advanced)

### Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

### Create docker-compose.yml

```yaml
version: '3.8'

services:
  bot:
    build: .
    container_name: content-bridge-bot
    restart: unless-stopped
    env_file:
      - .env
    volumes:
      - ./temp:/app/temp
```

### Run with Docker

```bash
docker-compose up -d
```

### View logs

```bash
docker-compose logs -f
```

---

## Option 5: Cloud Platforms

### Heroku (Simple but paid)

1. Install Heroku CLI
2. Create `Procfile`:
```
worker: python main.py
```
3. Deploy:
```bash
heroku create
git push heroku main
heroku ps:scale worker=1
```

**Cost:** ~$7/month for hobby dyno

### Railway (Easy deployment)

1. Go to [railway.app](https://railway.app)
2. Connect GitHub repo
3. Add environment variables
4. Deploy automatically

**Cost:** Free tier available, then ~$5/month

### Google Cloud Run / AWS Lambda

Not recommended for this bot (designed for long-running processes).

---

## Security Best Practices

### 1. Firewall

On VPS, only allow SSH and necessary ports:

```bash
ufw allow 22/tcp
ufw enable
```

### 2. Regular Updates

```bash
apt update && apt upgrade -y
```

### 3. Backup .env File

Keep a backup of your `.env` file somewhere safe!

### 4. Monitor Logs

Check logs regularly for errors:

```bash
journalctl -u content-bridge -f
```

### 5. Set Spending Limits

- OpenAI: Set monthly budget limit
- Twitter: Monitor API usage
- VPS: Set billing alerts

---

## Monitoring

### Check if Bot is Running

```bash
systemctl status content-bridge
```

### Check Memory Usage

```bash
free -h
```

### Check Disk Space

```bash
df -h
```

### Check Bot Process

```bash
ps aux | grep python
```

---

## Troubleshooting Deployment

### Bot stops after SSH disconnect

→ Use systemd service (Option 2, Step 7)

### "Permission denied" errors

→ Run with sudo or create dedicated user

### Out of memory errors

→ Upgrade VPS RAM or optimize code

### Bot doesn't start on boot

→ Enable service:
```bash
systemctl enable content-bridge
```

---

## Cost Comparison

| Option | Initial | Monthly | Effort |
|--------|---------|---------|--------|
| Local PC | Free | $0 | Low |
| VPS | $0 | $4-6 | Medium |
| Raspberry Pi | $35-75 | $0-2 | Medium |
| Heroku | $0 | $7 | Low |
| Railway | $0 | $0-5 | Low |

**Recommended:** VPS for $4-6/month - best balance of price, reliability, and control!

---

## Need Help?

If you have deployment issues:
1. Check the logs
2. Verify all environment variables
3. Test locally first
4. Check firewall settings
5. Open an issue on GitHub
