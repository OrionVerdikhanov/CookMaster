# CookMaster

CookMaster - это веб-приложение для публикации и поиска кулинарных рецептов, разработанное с использованием Django и современных веб-технологий.

## Основные функции

- Публикация рецептов с фотографиями
- Категоризация рецептов
- Поиск рецептов
- Система авторизации пользователей
- Личный кабинет с управлением рецептами

## Технологии

- Python 3.8+
- Django 4.2+
- HTML5/CSS3
- JavaScript
- SQLite

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/OrionVerdikhanov/CookMaster.git
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Запустите сервер:
```bash
python manage.py runserver
```

## Лицензия

MIT License
