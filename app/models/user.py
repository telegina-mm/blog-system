from pydantic import BaseModel, Field, field_validator


class User(BaseModel):
    id: int
    username: str
    email: str
    createdAt: str


class UserCreate(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50,
        pattern=r"^\S+$",
        description="Username must be 3-50 characters without spaces",
    )
    email: str
    password: str = Field(
        min_length=6, max_length=100, description="Password must be 6-100 characters"
    )

    @field_validator("password")
    @classmethod
    def password_no_spaces(cls, v: str) -> str:
        if " " in v:
            raise ValueError("Password should not contain spaces")
        return v


class UserUpdate(BaseModel):
    username: str | None = Field(
        None,
        min_length=3,
        max_length=50,
        pattern=r"^\S+$",
        description="Username must be 3-50 characters without spaces",
    )
    email: str | None = None
    password: str | None = Field(
        None,
        min_length=6,
        max_length=100,
        description="Password must be 6-100 characters",
    )

    @field_validator("password")
    @classmethod
    def password_no_spaces(cls, v: str | None) -> str | None:
        if v and " " in v:
            raise ValueError("Password should not contain spaces")
        return v


class UserInDB(User):
    password: str
