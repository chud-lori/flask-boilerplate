from typing import List, Optional
from pydantic import BaseModel
from src.domain.user import UserData


class RequestUser(BaseModel):
    email: str
    password: str
    name: str
    description: Optional[str] = ""


class ResponseUser(BaseModel):
    status: int
    message: str
    data: UserData


class ResponseUserList(BaseModel):
    status: int
    message: str
    data: List[UserData]
