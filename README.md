# 🧠 Notes API

Modern Notes Management API built with **FastAPI + PostgreSQL + SQLAlchemy**.  
Clean architecture, CRUD operations, search, pagination and ready frontend client.

---

## 🚀 Overview

Notes API — это backend сервис для работы с заметками.

Поддерживает:
- создание заметок
- получение списка
- поиск по title
- пагинацию (skip / limit)
- обновление
- удаление
- frontend (HTML + JS)

---

## ✨ Features

- 📝 Create notes
- 📖 Read notes
- 🔎 Search by title
- 📦 Pagination (skip / limit)
- ✏️ Update notes
- ❌ Delete notes
- 🌐 CORS enabled
- ⚡ FastAPI performance
- 🗄 PostgreSQL + SQLAlchemy
- 🔐 Pydantic validation

---

## 🧱 Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- HTML / CSS / JS (frontend)

---

## 📁 Project Structure

```text
app/
├── main.py        # API routes
├── models.py      # DB models
├── schemas.py     # Pydantic schemas
├── crud.py        # DB logic
├── database.py    # DB connection
└── frontend/
    └── index.html
