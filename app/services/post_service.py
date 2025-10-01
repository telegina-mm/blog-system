from datetime import datetime
from typing import List, Optional
from app.models.post import Post, PostCreate, PostUpdate

class PostService:
    def __init__(self):
        self.posts: List[Post] = []
        self.next_id = 1

    async def get_all_posts(self) -> List[Post]:
        return self.posts

    async def get_post_by_id(self, post_id: int) -> Optional[Post]:
        return next((post for post in self.posts if post.id == post_id), None)

    async def create_post(self, author_id: int, post_data: PostCreate) -> Post:
        now = datetime.now()
        post = Post(
            id=self.next_id,
            authorId=author_id,
            title=post_data.title,
            content=post_data.content,
            createdAt=now,
            updatedAt=now
        )
        self.posts.append(post)
        self.next_id += 1
        return post

    async def update_post(self, post_id: int, post_data: PostUpdate) -> Optional[Post]:
        post = await self.get_post_by_id(post_id)
        if not post:
            return None
        
        update_data = post_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            if value is not None:
                setattr(post, field, value)
        
        post.updatedAt = datetime.now()
        return post

    async def delete_post(self, post_id: int) -> bool:
        post = await self.get_post_by_id(post_id)
        if post:
            self.posts.remove(post)
            return True
        return False

post_service = PostService()