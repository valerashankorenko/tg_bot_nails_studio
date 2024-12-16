# Telegram-бот с веб-интерфейсом для приема заявок

## О проекте
Веб-приложение на FastAPI, которое будет взаимодействовать с Telegram-ботом через WebApp и вебхуки. В основе проекта — асинхронное взаимодействие с базой данных SQLite с помощью SQLAlchemy, что позволит нам реализовать масштабируемое и эффективное приложение.

## Цель


## Автор проекта:
Валерий Шанкоренко<br/>
Github: 👉 [Valera Shankorenko](https://github.com/valerashankorenko)<br/>
Telegram: 📱 [@valeron007](https://t.me/valeron007)<br/>
E-mail: 📧 valerashankorenko@yandex.by<br/>

## Стек технологий
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat-square&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-003B2D?style=flat-square&logo=uvicorn&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-3F4B3D?style=flat-square&logo=sqlalchemy&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-0D4D3A?style=flat-square&logo=alembic&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-4B8BBE?style=flat-square&logo=pydantic&logoColor=white)
![Aiosqlite](https://img.shields.io/badge/Aiosqlite-4B8BBE?style=flat-square&logo=python&logoColor=white)
![Pydantic Settings](https://img.shields.io/badge/Pydantic%20Settings-4B8BBE?style=flat-square&logo=python&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-4B8BBE?style=flat-square&logo=python&logoColor=white)
![Aiogram](https://img.shields.io/badge/aiogram-4B8BBE?style=flat-square&logo=python&logoColor=white)

## Как запустить проект локально:
1. Клонировать репозиторий и перейти в его директорию в командной строке:
```shell
git clone git@github.com:valerashankorenko/tg_bot_nails_studio.git
```
2. Переход в директорию tg_bot_nails_studio
```shell
cd tg_bot_nails_studio
```
3. Cоздать и активировать виртуальное окружение:
 - для Linux/MacOS
```shell
python3 -m venv venv
source venv/bin/activate
```
- для Windows
```shell
python -m venv venv
source venv/Scripts/activate
```
4. Обновить пакетный менеджер pip
```shell
python3 -m pip install --upgrade pip
```
5. Установить зависимости из файла requirements.txt:
```shell
pip install -r requirements.txt
```
6. В корневой директории создать файл .env и заполнить своими данными:
```
BOT_TOKEN=bot_token 
BASE_SITE=https://7016-80-85-143-232.ngrok-free.app*
ADMIN_ID=your_tg_id
```
7. Применение миграций
```shell
alembic upgrade head
```
8. Запуск проекта
```shell
uvicorn app.main:app
```

#### *Создание временного домена с поддержкой HTTPS с использованием Ngrok

Следуйте этим простым шагам, чтобы создать временный домен с поддержкой HTTPS для вашего приложения:

1. Перейдите на сайт [Ngrok](https://ngrok.com/) и зарегистрируйтесь.
   
2. Скачайте утилиту Ngrok для вашей операционной системы со [страницы загрузки](https://ngrok.com/download).

3. Откройте загруженный файл и выполните команду для добавления вашего токена аутентификации:
```bash
ngrok config add-authtoken your_token
```
4. Запустите туннель на нужном порту, заменив PORT на номер порта вашего приложения:
```bash
ngrok http PORT
```
Например, для порта 5050 команда будет выглядеть так:
```bash
ngrok http 5050
```
