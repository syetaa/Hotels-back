import ssl

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

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain('./cert.pem', keyfile='./key.pem')

origins = [
    "http://localhost",
    "https://localhost",
    "http://127.0.0.1",
    "https://127.0.0.1",
    "http://0.0.0.0",
    "https://0.0.0.0",
    "http://147.45.136.142",
    "https://147.45.136.142",
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
