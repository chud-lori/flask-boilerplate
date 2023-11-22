from domain.user import User, UserRepository

class EsUserRepository(UserRepository):
    def select_user_by_id(self, user_id: hash) -> User:
        user_data: User = User(user_id, "lori@mail.com", "dqwdiq", "lori", "the people", "12-03-2012")
        return user_data

    def save_user(self, user: User) -> tuple(int, str):
        return 1, "Save PSQL"
