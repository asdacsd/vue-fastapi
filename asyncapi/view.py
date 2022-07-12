import asyncio
import time

from fastapi import Depends, WebSocket, WebSocketDisconnect, APIRouter
from starlette.responses import FileResponse

app = APIRouter()


# @app.get("/user", response_model=schemas.MyUser)
# def get_age(db: Session = Depends(get_db)):
#     print('db conn')
#     users = crud.get_user(db)
#     users = {
#         "id": users.id,
#         "age": users.age
#     }
#     return users


def get_age_add():
    yield 100


@app.get('/file')
async def get_file():
    return FileResponse('static/img/about.jpg',
                        filename='file.jpg')


@app.get('/test')
async def test(age=Depends(get_age_add)):
    return {"test": age}


@app.get('/time')
async def get_time():
    return {"time": time.time()}


@app.get('/data/{id}')
async def get_data(id: int):
    await asyncio.sleep(0.5)
    data_list = [
        {
            'name': f'my name is dynamic {id}',
            'age': 'I am 28 years old',
            'city': 'I live in London',
            'phone': 'I have a phone number'
        },
        {
            'name': f'my name is dynamic {id}',
            'age': 'I am 28 years old',
            'city': 'I live in London',
            'phone': 'I have a phone number'
        },
        {
            'name': f'my name is dynamic {id}',
            'age': 'I am 28 years old',
            'city': 'I live in London',
            'phone': 'I have a phone number'
        }
    ]
    return data_list[id]


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, exclude):
        for connection in self.active_connections:
            if connection is exclude:
                continue
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{nickname}")
async def websocket_endpoint(websocket: WebSocket, nickname: str):
    await manager.connect(websocket)
    try:
        await manager.send_personal_message("【你 加入了群聊】", websocket)
        await manager.broadcast(f"【{nickname} 加入了群聊】", exclude=websocket)
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"你: {data}", websocket)
            await manager.broadcast(f"{nickname}: {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"【{nickname} 离开了群聊】", None)
