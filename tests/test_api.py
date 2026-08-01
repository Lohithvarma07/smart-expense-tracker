from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Petrol",
            "amount": 450,
            "category": "Transport",
            "date": "2026-08-01"
        }
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Petrol"
    assert data["amount"] == 450
    assert data["category"] == "Transport"


def test_get_expenses():
    response = client.get("/expenses")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_filter_by_category():
    response = client.get("/expenses?category=Transport")

    assert response.status_code == 200

    for expense in response.json():
        assert expense["category"] == "Transport"


def test_total_expenses():
    response = client.get("/expenses/total")

    assert response.status_code == 200

    data = response.json()

    assert "total" in data


def test_total_by_category():
    response = client.get("/expenses/total?category=Transport")

    assert response.status_code == 200

    data = response.json()

    assert "total" in data


def test_delete_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Delete Test",
            "amount": 100,
            "category": "Test",
            "date": "2026-08-01"
        }
    )

    expense_id = response.json()["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")

    assert delete_response.status_code == 200

    assert delete_response.json()["message"] == "Expense deleted successfully"