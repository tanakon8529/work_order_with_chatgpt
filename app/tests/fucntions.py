# Create a test file, e.g., test_testing.py

from fastapi.testclient import TestClient
from app.main import app
from app.routes.testing import Testing

client = TestClient(app)

def test_testing_endpoint():
    testing_instance = Testing()
    response = client.get("/test")

    # Check if the endpoint returns a 200 OK status code
    assert response.status_code == 200

    # Check if the response contains the expected message
    expected_message = {"message": "Test successful"}
    assert response.json() == expected_message

def test_testing_endpoint_error_handling():
    testing_instance = Testing()
    
    # Simulate an error by passing an invalid parameter
    response = client.get("/test?error=true")

    # Check if the endpoint returns a 500 Internal Server Error status code
    assert response.status_code == 500

    # Check if the response contains the expected error message
    expected_message = {"detail": "An error occurred during the test."}
    assert response.json() == expected_message
