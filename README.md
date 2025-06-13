# VK Community Post Generator

Простой ассистент для генерации и публикации контента о новостях ИИ во "ВКонтакте". Скрипт создаёт текст поста, промпт и изображение через OpenAI, публикует всё в сообщество и выводит статистику за последнюю неделю.

## Функционал

- 🤖 Генерация текста поста с помощью GPT-4
- 🎨 Создание изображений через DALL-E
- 📊 Анализ статистики сообщества
- 🔄 Автоматическая публикация контента
- 📈 Отслеживание эффективности постов

## Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/yourusername/vk-community-post-generator.git
cd vk-community-post-generator

# Установите зависимости
pip install -r requirements.txt
```

Создайте файл `.env` по примеру `.env.example` и укажите в нём токен VK, ID сообщества и ключ OpenAI.

## Переменные окружения

- `OPENAI_API_KEY` — ключ OpenAI.
- `VK_TOKEN` — сервисный токен сообщества.
- `VK_GROUP_ID` — числовой ID сообщества без `-`.

## Запуск

```bash
python main.py
```

## Зависимости

- Python 3.8+
- vk_api
- openai
- python-dotenv
- Pillow

## Лицензия

MIT License
