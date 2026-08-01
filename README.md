# Smart Expense Tracker API
## Overview

The Smart Expense Tracker API is a RESTful API built using FastAPI to manage personal expenses. It allows users to add, view, filter, calculate totals, and delete expenses. Expense data is stored in a local JSON file, so no database setup is required.

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Automatic API documentation using Swagger UI


## Tech Stack

- Python 3
- FastAPI
- Pytest
- JSON File Storage



## Project Structure

```
smart-expense-tracker/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
│
├── src/
│   ├── main.py
│   ├── models.py
│   ├── storage.py
│   └── expenses.json
│
└── tests/
    └── test_api.py
```


## Installation

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Server

```bash
uvicorn src.main:app --reload
```

Server runs at

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```



## Run Tests

```bash
pytest
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /expenses | Add an expense |
| GET | /expenses | View all expenses |
| GET | /expenses?category=Food | Filter by category |
| GET | /expenses/total | Calculate total expenses |
| GET | /expenses/total?category=Food | Calculate total by category |
| DELETE | /expenses/{expense_id} | Delete an expense |


## Bonus Feature

OpenAPI/Swagger documentation is available automatically through FastAPI.

Swagger UI:
http://127.0.0.1:8000/docs