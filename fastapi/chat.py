import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import List
from datetime import datetime
from fastapi import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast_message(self, message: str):
        now = datetime.now().strftime("%H:%M")
        for connection in self.active_connections:
            await connection.send_text(f"{now} - {message}")

manager = ConnectionManager()

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast_message(data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8002)
