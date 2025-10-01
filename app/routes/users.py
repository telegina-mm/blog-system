from fastapi import APIRouter, HTTPException, status
from app.models.user import User, UserCreate, UserUpdate
from app.services.user_service import user_service

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/", response_model=list[User])
async def get_users():
    """Получить список всех пользователей"""
    return await user_service.get_all_users()

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Получить пользователя по ID"""
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate):
    """Создать нового пользователя"""
    try:
        user = await user_service.create_user(user_data)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_data: UserUpdate):
    """Обновить данные пользователя"""
    user = await user_service.update_user(user_id, user_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    """Удалить пользователя"""
    success = await user_service.delete_user(user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {"message": "User deleted successfully"}