import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEest Fitness Tracker" in response.data

def test_add_workout(client):
    # Add a workout
    response = client.post("/add", data={"workout": "Running", "duration": "30"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Running - 30 minutes" in response.data

def test_add_invalid_duration(client):
    # Try to add a workout with invalid duration
    response = client.post("/add", data={"workout": "Swimming", "duration": "abc"}, follow_redirects=True)
    assert response.status_code == 200
    # Should not add invalid workout
    assert b"Swimming - abc minutes" not in response.data

def test_no_workouts_message(client):
    # Clear workouts list
    from app import workouts
    workouts.clear()
    response = client.get("/")
    assert b"No workouts logged yet." in response.data