from typing import Tuple

from src.domain.user import User, UserRepository

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def select_user_all(self):
        return self.repository.select_user_all()

    def select_user(self, user_id: int):
        return self.repository.select_user(user_id)

    def save_user(self, user: User) -> Tuple[int, str]:
        self.repository.save_user(user)
        return 1, "success"
