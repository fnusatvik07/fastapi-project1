# 🎮 FastAPI Movies API

A simple yet powerful **FastAPI** project demonstrating CRUD operations with data stored in a **JSON file**.
The API lets you view, search, add, update, and delete movies — all with interactive Swagger documentation.

---

## 📁 Project Structure

```
fastapi_movies_app/
│
├── main.py          # FastAPI application with CRUD routes
└── movies.json      # Movie data file
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-movies-api.git
cd fastapi-movies-api
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # For Mac/Linux
venv\Scripts\activate       # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install fastapi uvicorn
```

---

## ▶️ Run the App

```bash
uvicorn main:app --reload
```

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧙‍♂️ API Endpoints

| Method   | Endpoint                                  | Description                      |
| -------- | ----------------------------------------- | -------------------------------- |
| `GET`    | `/movies`                                 | Fetch all movies                 |
| `GET`    | `/movies/{title}`                         | Fetch a specific movie by title  |
| `GET`    | `/movies/?genre={genre}`                  | Fetch movies by genre            |
| `GET`    | `/movies/bydirector/?director={name}`     | Fetch movies by director         |
| `GET`    | `/movies/byyear/?start={year}&end={year}` | Fetch movies within a year range |
| `POST`   | `/movies/add`                             | Add a new movie (JSON body)      |
| `PUT`    | `/movies/update/{title}`                  | Update existing movie details    |
| `DELETE` | `/movies/delete/{title}`                  | Delete a movie by title          |

---

## 💃 Sample JSON Structure

Each movie in `movies.json` follows this format:

```json
{
  "title": "Inception",
  "director": "Christopher Nolan",
  "genre": "Sci-Fi",
  "year": 2010,
  "rating": 8.8
}
```

---

## 💡 Example Usage

### ➤ Add a New Movie

**POST** `/movies/add`

```json
{
  "title": "Oppenheimer",
  "director": "Christopher Nolan",
  "genre": "Biography",
  "year": 2023,
  "rating": 8.9
}
```

### ➤ Get Movies by Director

**GET** `/movies/bydirector/?director=James Cameron`

### ➤ Delete a Movie

**DELETE** `/movies/delete/Titanic`

---

## 💥 Key Features

* Built with **FastAPI** for speed and simplicity
* Uses **JSON file storage** for persistent data
* Fully interactive **Swagger UI** for testing endpoints
* Demonstrates **CRUD operations**, **query parameters**, and **path parameters**

---

## 🔗 Useful Links

* [FastAPI Documentation](https://fastapi.tiangolo.com/)
* [Uvicorn Documentation](https://www.uvicorn.org/)

---

## 🛠️ Future Enhancements

* Integrate with SQLite or PostgreSQL
* Add authentication and role-based access
* Include Pydantic models for validation
* Implement pagination and sorting options
