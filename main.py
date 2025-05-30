from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir CORS para frontend local o desplegado
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, reemplazar por la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "1234":
        return {"status": "ok"}
fake_users = {
    "admin": "admin123",
    "user": "password",
    "fernando": "claveSegura"
}
    return {"status": "error"}
