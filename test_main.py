from fastapi.testclient import TestClient
from main import app  

client = TestClient(app)

def test_devops_post_success():
    headers = {
        "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
        "X-JWT-KWY": "un-token-unico-por-transaccion"
    }
    payload = {
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "time ToLifeSec": 45
    }
    response = client.post("/DevOps", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Juan Perez your message will be send"}

def test_devops_methods_error():
    response = client.get("/DevOps")
    assert response.status_code == 200
    assert response.json() == "ERROR"