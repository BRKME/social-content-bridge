#!/usr/bin/env python3
"""
Social Content Bridge Bot

A Telegram bot that reposts content to Telegram channel and Twitter.
Processes messages with AI to translate, improve style, and generate short versions.
"""

import sys
from bot.telegram_handler import TelegramHandler
from utils.logger import setup_logger

logger = setup_logger(__name__)


def main():
    """Main entry point."""
    try:
        logger.info("=" * 60)
        logger.info("Social Content Bridge Bot")
        logger.info("=" * 60)
        
        # Initialize and run bot
        handler = TelegramHandler()
        handler.run()
        
    except KeyboardInterrupt:
        logger.info("\n👋 Bot stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
