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
6. Применение миграций
```shell
alembic upgrade head
```
7. Запуск проекта
```shell
uvicorn app.main:app
```