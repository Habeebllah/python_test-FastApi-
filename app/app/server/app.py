from fastapi import FastAPI

from app.app.server.routes.song import router as SongRouter

app = FastAPI()

app.include_router(SongRouter, tags=["Song"], prefix="/song")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}