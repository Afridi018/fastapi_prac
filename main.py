from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def index():
    return {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
