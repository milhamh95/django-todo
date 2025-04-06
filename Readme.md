# Django Todo App

A modern todo application built with Django, PostgreSQL, Redis, and Tailwind CSS. Features user authentication, task management, and background task processing.

## Tech Stack

- **Backend**: Django 5.1.7
- **Database**: PostgreSQL
- **Task Queue**: Huey with Redis
- **Frontend**: Tailwind CSS
- **Static Files**: Whitenoise

## Features

- User registration and login
- Create, read, update, and delete todos
- Background task processing with Huey

## Prerequisites

- Python 3.x
- PostgreSQL
- Redis

## Environment Setup

1. Clone the repository

1. Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate # On Windows: venv\Scripts\activate
```

1. Copy `.env_sample` to `.env` and configure your environment variables:

```env
PG_NAME=django_todo
PG_USER=postgres
PG_PASSWORD=your_password
PG_HOST=localhost
PG_PORT=5433
REDIS_HOST=localhost
REDIS_PORT=6379
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Database Setup

1. Create a PostgreSQL database:

```sql
CREATE DATABASE django_todo;
```

1. Run migrations:

```bash
./manage.py migrate
```

1. Create a superuser:

```bash
./manage.py createsuperuser
```

## Running the Application

1. Start the development server:

```bash
 ./manage.py runserver
```

2. Start the Huey consumer for background tasks:

```bash
./manage.py run_huey --workers 2
```

The application will be available at `http://localhost:8000`
