class PostService:
    def __init__(self) -> None:
        self.posts = []
        self.next_id = 1

    def get_all_posts(self) -> list:
        return self.posts

    def get_post(self, post_id: int) -> dict | None:
        for post in self.posts:
            if post["id"] == post_id:
                return post
        return None

    def create_post(self, post_data: dict) -> dict:
        post = {
            "id": self.next_id,
            "title": post_data["title"],
            "content": post_data["content"],
            "author": post_data.get("author", "Anonymous"),
            "created_at": post_data.get("created_at", ""),
        }
        self.posts.append(post)
        self.next_id += 1
        return post

    def update_post(self, post_id: int, update_data: dict) -> dict | None:
        for post in self.posts:
            if post["id"] == post_id:
                post.update(update_data)
                return post
        return None

    def delete_post(self, post_id: int) -> bool:
        for i, post in enumerate(self.posts):
            if post["id"] == post_id:
                self.posts.pop(i)
                return True
        return False
