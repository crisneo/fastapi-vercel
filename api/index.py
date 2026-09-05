from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Vercel API",
    description="Simple REST API deployed on Vercel",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI!",
        "status": "running"
    }


@app.get("/api/hello")
def hello(name: str = "World"):
    return {
        "message": f"Hello, {name}!"
    }


@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": f"User {user_id}"
    }