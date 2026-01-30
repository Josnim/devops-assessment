from fastapi import FastAPI, Header, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()

# Endpoint requerido: /DevOps [cite: 18]
@app.post("/DevOps")
async def devops_post(
    request: Request,
    x_parse_rest_api_key: str = Header(None, alias="X-Parse-REST-API-Key"),
    x_jwt_kwy: str = Header(None, alias="X-JWT-KWY")
):
    # Validación de API Key [cite: 30, 31, 32]
    if x_parse_rest_api_key != "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c":
        return JSONResponse(status_code=403, content={"detail": "Invalid API Key"})
    
    # Validación de JWT (debe ser único por transacción) [cite: 36, 39]
    if not x_jwt_kwy:
        return JSONResponse(status_code=401, content={"detail": "JWT Required"})

    try:
        data = await request.json()
        # Retornamos el saludo usando el campo "to" del JSON [cite: 26, 27, 28]
        return {"message": f"Hello {data['to']} your message will be send"}
    except Exception:
        return JSONResponse(status_code=400, content="ERROR")

# Otros métodos HTTP deben retornar "ERROR" [cite: 29]
@app.api_route("/DevOps", methods=["GET", "PUT", "DELETE", "PATCH"])
async def error_handler():
    return JSONResponse(content="ERROR")