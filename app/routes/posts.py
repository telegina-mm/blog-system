from fastapi import APIRouter, HTTPException

from app.models.post import PostCreate, PostUpdate
from app.services.post_service import PostService

router = APIRouter(prefix="/api/posts", tags=["posts"])
post_service = PostService()


@router.get("/{post_id}")
async def get_post(post_id: int) -> dict:
    post = post_service.get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found") from None
    return post


@router.post("/")
async def create_post(post: PostCreate) -> dict:
    new_post = post_service.create_post(post.dict())
    return new_post


@router.put("/{post_id}")
async def update_post(post_id: int, post: PostUpdate) -> dict:
    updated_post = post_service.update_post(post_id, post.dict(exclude_unset=True))
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found") from None
    return updated_post


@router.delete("/{post_id}")
async def delete_post(post_id: int) -> dict:
    if not post_service.delete_post(post_id):
        raise HTTPException(status_code=404, detail="Post not found") from None
    return {"message": "Post deleted successfully"}
