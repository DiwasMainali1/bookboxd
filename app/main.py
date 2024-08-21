from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Bookbox API"}

@app.get("/books")
async def get_books():
    # This is a placeholder. We'll implement actual book fetching later.
    return {"books": ["Book 1", "Book 2", "Book 3"]}