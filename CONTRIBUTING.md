# 🤝 Contributing to Social Content Bridge

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Ways to Contribute

- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit code improvements
- 🌍 Add translations
- ⭐ Star the project!

## Getting Started

1. **Fork the repository**
   ```bash
   # Click "Fork" button on GitHub
   ```

2. **Clone your fork**
   ```bash
   git clone https://github.com/yourusername/social-content-bridge.git
   cd social-content-bridge
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   ```bash
   # Edit files
   ```

5. **Test your changes**
   ```bash
   python main.py
   ```

6. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: your feature description"
   ```

7. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Describe your changes

## Code Style

- Use Python 3.9+ features
- Follow PEP 8 style guide
- Add docstrings to functions
- Use type hints where appropriate
- Keep functions focused and small
- Write descriptive variable names

### Example

```python
async def process_message(self, text: str, has_image: bool = False) -> Dict[str, str]:
    """
    Process message text and generate versions.
    
    Args:
        text: Original message text
        has_image: Whether message has an image
        
    Returns:
        Dictionary with 'full_text' and 'short_text' keys
    """
    # Implementation
    pass
```

## Testing

Before submitting:

1. Test with text-only messages
2. Test with images
3. Test with Russian text
4. Test error handling
5. Check logs for errors

## Reporting Bugs

**Before reporting:**
- Check existing issues
- Test with latest version
- Verify it's not a configuration issue

**Include in report:**
- OS and Python version
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs
- Screenshots if relevant

### Bug Report Template

```markdown
**Environment:**
- OS: [e.g., Ubuntu 22.04]
- Python version: [e.g., 3.11.0]
- Bot version: [e.g., 1.0.0]

**Description:**
[Clear description of the bug]

**Steps to Reproduce:**
1. [First step]
2. [Second step]
3. [...]

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happens]

**Logs:**
```
[Paste relevant logs]
```

**Screenshots:**
[If applicable]
```

## Suggesting Features

**Before suggesting:**
- Check if already requested
- Think about use cases
- Consider implementation complexity

**Include in suggestion:**
- Clear description
- Use case/motivation
- Expected behavior
- Alternative solutions considered

### Feature Request Template

```markdown
**Feature Description:**
[Clear, concise description]

**Motivation:**
[Why is this needed?]

**Use Case:**
[How would this be used?]

**Proposed Solution:**
[How could this work?]

**Alternatives:**
[Other ways to achieve this?]
```

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows project style
- [ ] Tested locally
- [ ] Documentation updated
- [ ] No unnecessary files included
- [ ] Commit messages are clear

### PR Description Template

```markdown
## Description
[What does this PR do?]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Other: [describe]

## Testing
[How was this tested?]

## Screenshots
[If applicable]

## Related Issues
Fixes #[issue number]
```

## Development Setup

### Install Development Dependencies

```bash
pip install -r requirements.txt
pip install black flake8 mypy pytest
```

### Code Formatting

```bash
# Format code
black .

# Check style
flake8 .

# Type checking
mypy .
```

## Project Structure

```
social-content-bridge/
├── bot/                    # Bot modules
│   ├── telegram_handler.py    # Main handler
│   ├── ai_processor.py         # AI processing
│   ├── telegram_publisher.py   # Telegram publishing
│   └── twitter_publisher.py    # Twitter publishing
├── config/                 # Configuration
│   └── settings.py             # Settings management
├── utils/                  # Utilities
│   ├── image_handler.py        # Image processing
│   └── logger.py               # Logging
└── main.py                 # Entry point
```

## Adding New Features

### Example: Adding Instagram Support

1. Create `bot/instagram_publisher.py`:
```python
class InstagramPublisher:
    """Publish content to Instagram."""
    
    async def publish(self, text: str, image_path: Path) -> bool:
        """Publish to Instagram."""
        # Implementation
        pass
```

2. Update `bot/telegram_handler.py`:
```python
from bot.instagram_publisher import InstagramPublisher

class TelegramHandler:
    def __init__(self):
        # ...
        self.instagram_publisher = InstagramPublisher()
```

3. Add to publish flow:
```python
instagram_success = await self.instagram_publisher.publish(
    short_text, 
    image_path
)
```

4. Update documentation
5. Test thoroughly
6. Submit PR!

## Adding AI Provider Support

### Example: Adding Claude Support

1. Update `config/settings.py`:
```python
self.AI_PROVIDER = os.getenv('AI_PROVIDER', 'openai')
self.ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
```

2. Update `bot/ai_processor.py`:
```python
if self.provider == 'openai':
    # OpenAI implementation
elif self.provider == 'anthropic':
    # Claude implementation
```

3. Update `.env.example`
4. Update README.md
5. Test
6. Submit PR!

## Documentation

When updating docs:

- Keep language simple and clear
- Add examples where helpful
- Update all relevant files
- Check for broken links
- Verify formatting

## Community Guidelines

- Be respectful and constructive
- Help others when possible
- Give credit where due
- Focus on the issue, not the person
- Welcome newcomers

## Questions?

- Open an issue for questions
- Check existing discussions
- Be patient - maintainers are volunteers!

## Recognition

Contributors will be added to:
- README.md acknowledgments
- GitHub contributors page

Thank you for contributing! 🎉
