import psycopg2

from domain.user import User, UserRepository


class PsqlUserRepository(UserRepository):
    def __init__(self, connection_url: str) -> None:
        self.connection_url = connection_url
        self.connection = None

    def _connect(self):
        if not self.connection or self.connection.closed:
            self.connection = psycopg2.connect(self.connection_string)

    def _disconnect(self):
        if self.connection and not self.connection.closed:
            self.connection.close()

    def select_user(self, user_id: int) -> User:
        user_data: User = User(user_id, "lori@mail.com", "dqwdiq", "lori", "the people", "12-03-2012")
        return user_data

    def save_user(self, user: User) -> tuple(int, str):
        return 1, "Save PSQL"

    def __del__(self):
        self._disconnect()

psql_repository: PsqlUserRepository = PsqlUserRepository("localhost:5432")
