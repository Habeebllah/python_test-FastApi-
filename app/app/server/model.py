from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID


class SongSchema(BaseModel):
    song_id: UUID
    name: str = Field(...)
    duration: str = Field(...)
    created_at: datetime



    class Config:
        schema_extra = {
            "example": {
                "song_id": '1',
                "name": "stand it up",
                "duration": "2 mins",
                "created_at": "02-04-2021",

            }
        }


class UpdateSongModel(BaseModel):
    song_id: UUID
    name: str = Field(...)
    duration: str = Field(...)
    created_at: datetime



    class Config:
        schema_extra = {
            "example": {
                 "song_id": '1',
                "name": "stand it up",
                "duration": "2 mins",
                "created_at": "02-04-2021",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}