from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, List
from pydantic import BaseModel

@dataclass
class User:
    id: Optional[str] = "" # hash
    email: str
    password: str
    name: str
    description: str
    created_at: Optional[str] = ""
    updated_at: Optional[str] = ""


class UserData(BaseModel):
    id: Optional[str] = "" # hash
    email: str
    name: str
    description: str
    created_at: Optional[str] = ""
    updated_at: Optional[str] = ""


class UserRepository(ABC):
    @abstractmethod
    def select_user_all(self) -> List[UserData]:
        ...

    @abstractmethod
    def select_user_by_id(self, user_id: str) -> UserData:
        ...

    @abstractmethod
    def save_user(self, user: User) -> tuple(int, str):
        ...
