from fastapi.testclient import TestClient
from main import app  # Esto busca el archivo main.py

client = TestClient(app)

def test_devops_post_success():
    # Headers requeridos por el PDF [cite: 35, 36]
    headers = {
        "X-Parse-REST-API-Key": "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c",
        "X-JWT-KWY": "un-token-unico-por-transaccion"
    }
    # Payload exacto del requerimiento [cite: 20-25]
    payload = {
        "message": "This is a test",
        "to": "Juan Perez",
        "from": "Rita Asturia",
        "time ToLifeSec": 45
    }
    response = client.post("/DevOps", json=payload, headers=headers)
    
    # Verificamos respuesta exitosa [cite: 26-28]
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Juan Perez your message will be send"}

def test_devops_methods_error():
    # Otros métodos deben retornar "ERROR" [cite: 29]
    response = client.get("/DevOps")
    assert response.status_code == 200
    assert response.json() == "ERROR"