from domain.user import User, UserRepository

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def select_user(self, user_id: int):
        return self.repository.select_user(user_id)

    def save_user(self, user: User):
        return self.repository.save_user(user)
