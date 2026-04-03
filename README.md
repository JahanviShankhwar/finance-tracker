# Finance Tracker API

## Overview
This is a backend system built using FastAPI to manage financial transactions.

## Features
- CRUD operations for transactions
- Filter transactions by type and category
- Case-insensitive filtering
- Summary (total income, total expense, balance)

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite

## How to Run
1. Create virtual environment:
   python -m venv venv

2. Activate:
   venv\Scripts\activate

3. Install dependencies:
   pip install fastapi uvicorn sqlalchemy

4. Run server:
   uvicorn app.main:app --reload

## API Docs
http://127.0.0.1:8000/docs
