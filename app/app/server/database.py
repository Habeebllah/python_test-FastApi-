from bson.objectid import ObjectId
from decouple import config
import motor.motor_asyncio

#MONGO_DETAILS = "mongodb://localhost:27017"
MONGO_DETAILS = config('MONGO_DETAILS')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.songs

song_collection = database.get_collection("songs_collection")


def song_helper(song) -> dict:
    return {
        "id": str(song["_id"]),
        "fullname": song["fullname"],
        "email": song["email"],
        "course_of_study": song["course_of_study"],
        "year": song["year"],
        "GPA": song["gpa"],
    }


# Retrieve all songs present in the database
async def retrieve_songs():
    songs = []
    async for song in song_collection.find():
        songs.append(song_helper(song))
    return songs


# Add a new song into to the database
async def add_song(song_data: dict) -> dict:
    song = await song_collection.insert_one(song_data)
    new_song = await song_collection.find_one({"_id": song.inserted_id})
    return song_helper(new_song)


# Retrieve a song with a matching ID
async def retrieve_song(id: str) -> dict:
    song = await song_collection.find_one({"_id": ObjectId(id)})
    if song:
        return song_helper(song)


# Update a song with a matching ID
async def update_song(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    song = await song_collection.find_one({"_id": ObjectId(id)})
    if song:
        updated_song = await song_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_song:
            return True
        return False


# Delete a song from the database
async def delete_song(id: str):
    song = await song_collection.find_one({"_id": ObjectId(id)})
    if song:
        await song_collection.delete_one({"_id": ObjectId(id)})
        return True