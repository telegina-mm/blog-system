from fastapi import APIRouter, HTTPException
from app.models.post import Post, PostCreate, PostUpdate
from app.services.post_service import post_service

router = APIRouter(prefix="/api/posts", tags=["posts"])

@router.get("/", response_model=list[Post])
async def get_posts():
    return await post_service.get_all_posts()

@router.get("/{post_id}", response_model=Post)
async def get_post(post_id: int):
    post = await post_service.get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/", response_model=Post)
async def create_post(post_data: PostCreate, author_id: int):
    """Создать пост с указанием author_id через query параметр"""
    try:
        return await post_service.create_post(author_id, post_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{post_id}", response_model=Post)
async def update_post(post_id: int, post_data: PostUpdate):
    post = await post_service.update_post(post_id, post_data)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.delete("/{post_id}")
async def delete_post(post_id: int):
    success = await post_service.delete_post(post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}