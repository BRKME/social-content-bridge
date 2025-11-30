# 🐙 GitHub Setup Guide

Пошаговая инструкция по загрузке проекта на GitHub.

## Вариант 1: Через веб-интерфейс GitHub (Самый простой)

### Шаг 1: Создайте репозиторий на GitHub

1. Зайдите на [github.com](https://github.com)
2. Нажмите кнопку "+" в правом верхнем углу → "New repository"
3. Заполните:
   - **Repository name**: `social-content-bridge`
   - **Description**: `Telegram bot for cross-posting content to Telegram and Twitter with AI processing`
   - **Visibility**: Public (или Private, если хотите)
   - ⚠️ **НЕ СТАВЬТЕ галочки** на "Add a README file", "Add .gitignore", "Choose a license" (у нас уже всё есть!)
4. Нажмите "Create repository"

### Шаг 2: Загрузите файлы

GitHub покажет вам страницу с инструкциями. Выполните команды:

```bash
# Перейдите в папку с проектом
cd social-content-bridge

# Инициализируйте git (если ещё не сделано)
git init

# Добавьте все файлы
git add .

# Создайте первый коммит
git commit -m "Initial commit: Social Content Bridge Bot"

# Добавьте remote
git remote add origin https://github.com/ВАШ_USERNAME/social-content-bridge.git

# Загрузите на GitHub
git branch -M main
git push -u origin main
```

### Шаг 3: Проверьте

Обновите страницу на GitHub - все файлы должны появиться! ✅

---

## Вариант 2: GitHub Desktop (Для тех, кто не любит командную строку)

### Шаг 1: Установите GitHub Desktop

1. Скачайте с [desktop.github.com](https://desktop.github.com)
2. Установите и войдите в аккаунт

### Шаг 2: Добавьте проект

1. File → Add Local Repository
2. Выберите папку `social-content-bridge`
3. GitHub Desktop обнаружит файлы

### Шаг 3: Создайте репозиторий

1. Нажмите "Publish repository"
2. Заполните:
   - Name: `social-content-bridge`
   - Description: `Telegram bot for cross-posting`
   - Public или Private
3. Нажмите "Publish repository"

Готово! 🎉

---

## Вариант 3: Командная строка (Для опытных)

```bash
cd social-content-bridge

# Инициализация
git init

# Добавить все файлы
git add .

# Первый коммит
git commit -m "Initial commit: Social Content Bridge Bot"

# Создать репозиторий на GitHub через CLI (если установлен gh)
gh repo create social-content-bridge --public --source=. --remote=origin --push

# ИЛИ вручную добавить remote и запушить
git remote add origin https://github.com/USERNAME/social-content-bridge.git
git branch -M main
git push -u origin main
```

---

## ⚠️ ВАЖНО: Проверьте перед загрузкой!

### ✅ Обязательно проверьте:

1. **Файл `.env` НЕ должен быть в репозитории!**
   ```bash
   # Проверьте, что .env в .gitignore
   cat .gitignore | grep .env
   # Должно показать: .env
   ```

2. **НЕТ API ключей в коде**
   - Проверьте, что нигде в коде нет ваших реальных ключей
   - Все ключи должны быть только в `.env` файле

3. **`.env.example` должен быть пустым**
   ```bash
   # Проверьте содержимое
   cat .env.example
   # Должны быть только названия переменных, БЕЗ реальных значений
   ```

### 🔍 Команда для проверки:

```bash
# Посмотрите, что будет загружено
git status

# Посмотрите содержимое файлов, которые будут загружены
git diff --cached
```

---

## После загрузки на GitHub

### 1. Обновите README.md

Замените в README.md:

```markdown
git clone https://github.com/yourusername/social-content-bridge.git
```

на:

```markdown
git clone https://github.com/ВАШ_USERNAME/social-content-bridge.git
```

### 2. Добавьте темы (Topics)

На странице репозитория:
1. Нажмите на шестеренку рядом с "About"
2. Добавьте topics:
   - `telegram-bot`
   - `twitter-bot`
   - `openai`
   - `python`
   - `automation`
   - `social-media`
   - `content-management`

### 3. Настройте Description

В разделе "About" добавьте:
```
🤖 Telegram bot that auto-posts content to Telegram channels and Twitter with AI-powered translation and optimization
```

### 4. Добавьте Website (опционально)

Если у вас есть демо или сайт, добавьте ссылку.

---

## Работа с репозиторием

### Внесение изменений

```bash
# 1. Внесите изменения в код

# 2. Посмотрите, что изменилось
git status

# 3. Добавьте изменения
git add .

# 4. Сделайте коммит
git commit -m "Описание изменений"

# 5. Загрузите на GitHub
git push
```

### Клонирование на другой компьютер

```bash
git clone https://github.com/ВАШ_USERNAME/social-content-bridge.git
cd social-content-bridge
pip install -r requirements.txt
cp .env.example .env
# Заполните .env своими ключами
python main.py
```

### Обновление с GitHub

```bash
git pull
```

---

## Защита секретов

### GitHub Secrets (для CI/CD)

Если планируете использовать GitHub Actions:

1. Settings → Secrets and variables → Actions
2. New repository secret
3. Добавьте:
   - `TELEGRAM_BOT_TOKEN`
   - `OPENAI_API_KEY`
   - и т.д.

### .gitignore уже настроен

Файл `.gitignore` уже защищает:
- `.env` - ваши секреты
- `__pycache__/` - кэш Python
- `temp/` - временные файлы
- и другие

---

## Создание релизов

### Когда проект стабильный:

1. На GitHub: Releases → Create a new release
2. Tag: `v1.0.0`
3. Title: `v1.0.0 - Initial Release`
4. Description:
   ```markdown
   ## Features
   - ✅ AI-powered text processing
   - ✅ Telegram channel publishing
   - ✅ Twitter publishing
   - ✅ Image optimization
   - ✅ Automatic translation (RU→EN)
   
   ## Requirements
   - Python 3.9+
   - OpenAI API key
   - Telegram Bot token
   - Twitter API credentials
   ```
5. Publish release

---

## README Badges (красивые значки)

Добавьте в начало README.md:

```markdown
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)
```

Результат:
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## GitHub Issues Templates

### Создайте `.github/ISSUE_TEMPLATE/bug_report.md`:

```markdown
---
name: Bug Report
about: Report a bug
title: '[BUG] '
labels: bug
---

**Describe the bug**
A clear description of the bug.

**To Reproduce**
Steps to reproduce:
1. ...
2. ...

**Expected behavior**
What should happen.

**Logs**
Paste relevant logs here.

**Environment**
- OS: [e.g., Ubuntu 22.04]
- Python: [e.g., 3.11]
```

---

## Полезные команды Git

```bash
# Посмотреть статус
git status

# Посмотреть историю
git log --oneline

# Отменить последний коммит (но сохранить изменения)
git reset --soft HEAD~1

# Посмотреть разницу
git diff

# Посмотреть удаленные репозитории
git remote -v

# Обновить URL репозитория
git remote set-url origin https://github.com/NEW_USERNAME/social-content-bridge.git
```

---

## Проблемы и решения

### "remote: Repository not found"

→ Проверьте URL:
```bash
git remote -v
git remote set-url origin https://github.com/CORRECT_USERNAME/social-content-bridge.git
```

### "failed to push some refs"

→ Сначала стяните изменения:
```bash
git pull origin main --rebase
git push
```

### "Permission denied (publickey)"

→ Настройте SSH ключ или используйте HTTPS:
```bash
git remote set-url origin https://github.com/USERNAME/social-content-bridge.git
```

### Случайно закоммитили .env

⚠️ СРОЧНО:
```bash
# Удалить файл из истории
git rm --cached .env
git commit -m "Remove .env from repository"
git push

# ВАЖНО: Сразу же поменяйте ВСЕ API ключи!
# Они теперь скомпрометированы!
```

---

## Контрольный список ✅

Перед загрузкой на GitHub:

- [ ] `.env` файл в `.gitignore`
- [ ] `.env` не добавлен в git
- [ ] Нет реальных API ключей в коде
- [ ] README.md заполнен
- [ ] LICENSE файл на месте
- [ ] requirements.txt актуален
- [ ] Проект протестирован локально

После загрузки:

- [ ] Репозиторий создан
- [ ] Все файлы загружены
- [ ] README правильно отображается
- [ ] Topics добавлены
- [ ] Description заполнен
- [ ] .env не виден в репозитории

---

## Дальнейшие шаги

1. ⭐ Попросите друзей поставить звезду
2. 📢 Поделитесь проектом
3. 🔄 Регулярно обновляйте
4. 📝 Ведите CHANGELOG
5. 🐛 Отвечайте на Issues
6. 🤝 Принимайте Pull Requests

---

## Полезные ссылки

- [GitHub Docs](https://docs.github.com)
- [Git Tutorial](https://git-scm.com/docs/gittutorial)
- [Markdown Guide](https://guides.github.com/features/mastering-markdown/)
- [GitHub Desktop](https://desktop.github.com)

---

**Удачи с вашим проектом на GitHub!** 🚀

Не забудьте добавить ссылку на ваш репозиторий в README после создания!
