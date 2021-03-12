from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class SongSchema(BaseModel):
    id: int
    name: str = Field(...)
    duration:  = Field(...)
    created_at: str = Field(...)



    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "duration": "jdoe@x.edu.ng",
                "created_at": "Water resources engineering",

            }
        }


class UpdateSongModel(BaseModel):
    name: Optional[str]
    duration: Optional[EmailStr]
    created_at: Optional[str]


    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "duration": "jdoe@x.edu.ng",
                "created_at": "Water resources and environmental engineering",

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