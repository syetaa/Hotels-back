from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.user import users_router
from src.routers.room import rooms_router
from src.routers.order import orders_router
from src.routers.bookmark import bookmarks_router

app = FastAPI()
app.include_router(users_router)
app.include_router(rooms_router)
app.include_router(orders_router)
app.include_router(bookmarks_router)

origins = [
    "http://localhost",
    "https://localhost",
    "http://127.0.0.1",
    "https://127.0.0.1",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def main():
    return {'message': 'Hello World'}
