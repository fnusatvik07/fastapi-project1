from fastapi import FastAPI, Body, HTTPException
import json
from pathlib import Path

app = FastAPI(title="🎬 Movie Library API")

DATA_FILE = Path("movies.json")


# Utility functions
def read_movies():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def write_movies(movies):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2)


# 1️⃣ Get all movies
@app.get("/movies")
async def get_all_movies():
    return read_movies()


# 2️⃣ Get a movie by title
@app.get("/movies/{title}")
async def get_movie(title: str):
    for movie in read_movies():
        if movie["title"].casefold() == title.casefold():
            return movie
    raise HTTPException(status_code=404, detail="Movie not found")


# 3️⃣ Get movies by genre
@app.get("/movies/")
async def get_movies_by_genre(genre: str):
    result = [m for m in read_movies() if m["genre"].casefold() == genre.casefold()]
    return result or {"message": "No movies found for this genre"}


# 4️⃣ Get movies by director
@app.get("/movies/bydirector/")
async def get_movies_by_director(director: str):
    result = [m for m in read_movies() if m["director"].casefold() == director.casefold()]
    return result or {"message": "No movies found for this director"}


# 5️⃣ Get movies by year range (e.g., ?start=1990&end=2010)
@app.get("/movies/byyear/")
async def get_movies_by_year(start: int, end: int):
    result = [m for m in read_movies() if start <= m["year"] <= end]
    return result or {"message": f"No movies found between {start}-{end}"}


# 6️⃣ Add a new movie
@app.post("/movies/add")
async def add_movie(new_movie=Body()):
    movies = read_movies()
    if any(m["title"].casefold() == new_movie["title"].casefold() for m in movies):
        raise HTTPException(status_code=400, detail="Movie already exists")
    movies.append(new_movie)
    write_movies(movies)
    return {"message": "Movie added successfully", "movie": new_movie}


# 7️⃣ Update movie by title
@app.put("/movies/update/{title}")
async def update_movie(title: str, updated_movie=Body()):
    movies = read_movies()
    for i, m in enumerate(movies):
        if m["title"].casefold() == title.casefold():
            movies[i] = updated_movie
            write_movies(movies)
            return {"message": "Movie updated successfully", "movie": updated_movie}
    raise HTTPException(status_code=404, detail="Movie not found")


# 8️⃣ Delete movie
@app.delete("/movies/delete/{title}")
async def delete_movie(title: str):
    movies = read_movies()
    for i, m in enumerate(movies):
        if m["title"].casefold() == title.casefold():
            deleted = movies.pop(i)
            write_movies(movies)
            return {"message": f"Deleted '{deleted['title']}' successfully"}
    raise HTTPException(status_code=404, detail="Movie not found")
