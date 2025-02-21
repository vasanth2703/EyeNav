from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


@app.websocket("/ws")
async def connect(websocket: WebSocket):
    try:
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await websocket.send_json(data)
    except WebSocketDisconnect:
        print("WebSocket disconnected!")
    except Exception as e:
        print(f"Error: {e}")
