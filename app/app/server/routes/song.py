from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.app.server.database import (
    add_song,
    delete_song,
    retrieve_song,
    retrieve_song,
    update_song,
)
from app.app.server.model import (
    ErrorResponseModel,
    ResponseModel,
    SongSchema,
    UpdateSongModel,
)

router = APIRouter()                                                                                         


@router.post("/", response_description="Song data added into the database")
async def add_song_data(song: SongSchema = Body(...)):
    song = jsonable_encoder(song)
    new_song = await add_song(song)
    return ResponseModel(new_song, "Song added successfully.")

@router.get("/", response_description="Songs retrieved")
async def get_songs():
    songs = await retrieve_song()
    if songs:
        return ResponseModel(songs, "Songs data retrieved successfully")
    return ResponseModel(songs, "Empty list returned")


@router.get("/{id}", response_description="Song data retrieved")
async def get_song_data(id):
    song = await retrieve_song(id)
    if song:
        return ResponseModel(song, "Song data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Song doesn't exist.")


@router.put("/{id}")
async def update_song_data(id: str, req: UpdateSongModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_song = await update_song(id, req)
    if updated_song:
        return ResponseModel(
            "Song with ID: {} name update is successful".format(id),
            "Song name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the song data.",
    )


@router.delete("/{id}", response_description="Song data deleted from the database")
async def delete_song_data(id: str):
    deleted_song = await delete_song(id)
    if deleted_song:
        return ResponseModel(
            "Song with ID: {} removed".format(id), "Song deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Song with id {0} doesn't exist".format(id)
    )