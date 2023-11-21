from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: str # hash
    email: str
    password: str
    name: str
    description: str
    created_at: str
    updated_at: Optional[str] = ""


class UserRepository(ABC):
    @abstractmethod
    def select_user(self, user_id: int) -> User:
        ...

    def save_user(self, user: User) -> tuple(int, str):
        ...
