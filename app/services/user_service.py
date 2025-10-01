from datetime import datetime
from typing import List, Optional
from app.models.user import UserInDB, UserCreate, UserUpdate

class UserService:
    def __init__(self):
        self.users: List[UserInDB] = []
        self.next_id = 1

    async def get_all_users(self) -> List[UserInDB]:
        return self.users

    async def get_user_by_id(self, user_id: int) -> Optional[UserInDB]:
        return next((user for user in self.users if user.id == user_id), None)

    async def get_user_by_login(self, login: str) -> Optional[UserInDB]:
        return next((user for user in self.users if user.login == login), None)

    async def create_user(self, user_data: UserCreate) -> UserInDB:
        if await self.get_user_by_login(user_data.login):
            raise ValueError("User with this login already exists")
        
        now = datetime.now()
        user = UserInDB(
            id=self.next_id,
            email=user_data.email,
            login=user_data.login,
            password=user_data.password,
            createdAt=now,
            updatedAt=now
        )
        self.users.append(user)
        self.next_id += 1
        return user

    async def update_user(self, user_id: int, user_data: UserUpdate) -> Optional[UserInDB]:
        user = await self.get_user_by_id(user_id)
        if not user:
            return None
        
        update_data = user_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            if value is not None:
                setattr(user, field, value)
        
        user.updatedAt = datetime.now()
        return user

    async def delete_user(self, user_id: int) -> bool:
        user = await self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            return True
        return False

user_service = UserService()