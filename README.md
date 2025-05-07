# Yatube API

REST API для социальной сети **Yatube**, где пользователи могут публиковать посты, подписываться на авторов, оставлять комментарии и вступать в группы.

---

## Возможности

- Регистрация пользователей и выдача JWT-токенов
- Публикация, редактирование и удаление постов
- Подписка на других пользователей
- Комментирование постов
- Объединение постов в группы
- Пагинация и поиск

---

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/a-aganesov/api_final_yatube.git
cd yatube_api
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Выполните миграции:
```bash
python manage.py migrate
```

5. Запустите сервер:
```bash
python manage.py runserver
```

## Аутентификация
Используется JWT
- Получить токен:
```json
POST /api/v1/jwt/create/
{
  "username": "your_username",
  "password": "your_password"
}
```
- Обновить токен
```json
POST /api/v1/jwt/refresh/
{
  "refresh": "your_refresh_token"
}
```

## Документация
Доступна по следующему адресу после запуска сервера:
```http
http://127.0.0.1:8000/redoc/
```