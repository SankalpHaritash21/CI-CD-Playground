import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_app_is_working(client):
    response = client.get('/')
    assert response.status_code == 200
    # Check that the HTML contains the rendered content from the template
    assert b"<h1 id=\"hello\">Hello, World!</h1>" in response.data
    assert b"<p id=\"intro\">Welcome to my interactive website. Let's make things happen!</p>" in response.data
    assert b"<button id=\"action-btn\">Click Me!</button>" in response.data
