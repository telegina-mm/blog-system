from fastapi import FastAPI
from app.routes import users, posts, templates

app = FastAPI(title="Blog API", version="1.0.0")

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(templates.router)

@app.get("/")
async def root():
    return {"message": "Blog API is running. Go to /api/docs or /posts"}