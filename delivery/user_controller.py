from domain.user import User
from application.user_service import UserService
from repository.psql.psql_user import PsqlUserRepository

class UserController:
    def __init__(self) -> None:
        self.user_service = UserService(PsqlUserRepository)
    def create_user(self, user_data: User):
        self.user_service.save_user(user_data)
        return {
            "status": 1,
            "message": ""
        }

    def get_user_by_id(self, user_id: str):
        user_data = self.user_service.select_user(user_id)
        return user_data
