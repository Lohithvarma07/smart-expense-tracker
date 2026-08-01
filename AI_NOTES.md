# AI Usage Notes

## Stack
FastAPI (Python), Pydantic for validation, JSON file storage, pytest for tests.

## AI Tools Used

- ChatGPT (OpenAI): Used for project scaffolding, endpoint implementation, explanations, and documentation.
- Claude (Anthropic): Used to review the implementation, suggest improvements, and review the README and AI_NOTES documentation.


## 1. Which parts were AI-generated vs. written by me

### AI-assisted

- Generated the initial FastAPI project structure.
- Suggested the Pydantic models for request validation.
- Generated the initial JSON storage helper functions.
- Generated the first version of the REST API endpoints.
- Generated the initial pytest test cases.
- Helped draft the README and AI_NOTES files.

### Written/implemented by me

- I reviewed all AI-generated code before integrating it into the project and modified it where necessary to ensure it met the assignment requirements.
- Implemented the API endpoint logic by integrating the Pydantic models, JSON storage layer, and FastAPI routes into a working application.
- Wrote and organized the CRUD workflow for creating, retrieving, filtering, calculating totals, and deleting expenses.
- Configured the FastAPI project and verified that all endpoints were running correctly.
- Implemented the JSON read/write integration to ensure expense data persisted across requests.
- Verified and refined the API endpoint behavior to match the assignment requirements, including correct HTTP status codes and request validation.
- Manually tested every endpoint using FastAPI's Swagger UI (`/docs`) and validated the responses against the expected results.
- Verified that expense data was correctly persisted in `expenses.json` after creating, retrieving, and deleting records.

## 2. What I validated, tested, or changed, and why

Before using the AI-generated code, I reviewed and tested it to ensure it met the assignment requirements.

Some specific examples include:

- When I initially ran `pytest`, it reported **"collected 0 items"** because the test file was not being discovered correctly. I corrected the project structure and verified that pytest successfully discovered and executed all six tests.
- Manually tested every endpoint using FastAPI's `/docs` interface to verify that the request and response matched the assignment requirements.
- Verified that expenses were correctly written to and loaded from `expenses.json` after creating and deleting multiple records to ensure data persistence worked as expected.
- Compared the results of the overall total and category-wise total endpoints with manually calculated values to confirm the calculations were correct.
- Confirmed that invalid requests, such as negative expense amounts or missing required fields, returned FastAPI's validation errors instead of storing invalid data.
- Verified that deleting a non-existent expense returned a **404 Not Found** response instead of incorrectly reporting success.

## 3. AI suggestions I didn't use, and why

- SQLite/database support, because the assignment explicitly allowed JSON file storage.
- Docker support, because it was optional and outside the required scope.
- Additional optional features such as search or monthly summaries, to keep the implementation focused on the required functionality.

I used FastAPI's built-in Swagger UI (`/docs`) throughout development to manually test each endpoint and verify that the API behavior matched the assignment requirements.