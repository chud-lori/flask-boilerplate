from src.application.user_service import UserService
from src.repository.psql.psql_user import PsqlUserRepository
from src.transport.request_interface import RequestUser, ResponseUser, ResponseUserList

class UserController:
    def __init__(self) -> None:
        self.user_service = UserService(PsqlUserRepository)

    def create_user(self, user_data: RequestUser):
        user = self.user_service.save_user(user_data)
        http_response = ResponseUser(1, "user created", user)
        return http_response.model_dump()

    def get_user_all(self):
        users = self.user_service.select_user_all()
        http_response = ResponseUserList(1, "get all users", users)
        return http_response.model_dump()

    def get_user_by_id(self, user_id: str):
        user_data = self.user_service.select_user(user_id)
        http_response = ResponseUser(1, "get user", user_data)
        return http_response.model_dump()
