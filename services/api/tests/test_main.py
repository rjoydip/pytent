import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "Hello from UV!"
