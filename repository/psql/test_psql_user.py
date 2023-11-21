import unittest
from unittest.mock import MagicMock, patch
from repository.psql.psql_user import PsqlUserRepository
from your_module.domain.user import User

class TestUserPostgreSQLRepository(unittest.TestCase):
    def setUp(self):
        self.mocked_connection = MagicMock()
        self.mocked_cursor = MagicMock()
        self.mocked_connection.cursor.return_value = self.mocked_cursor

    @patch('flask_boilerplate.repository.psql')
    def test_get_user_by_id(self, mock_connect):
        user_repository = PsqlUserRepository("fake_connection_string")
        mock_connect.return_value = self.mocked_connection

        # Mock the database query result
        self.mocked_cursor.fetchone.return_value = (1, 'test_user')

        # Call the method under test
        user = user_repository.get_user_by_id(1)

        # Assertions
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.username, 'test_user')

        # Verify that the connection and cursor were called
        mock_connect.assert_called_once_with("fake_connection_string")
        self.mocked_connection.cursor.assert_called_once()
        self.mocked_cursor.execute.assert_called_once_with("SELECT * FROM users WHERE user_id = %s", (1,))

    @patch('your_module.infrastructure.user_repository_postgresql.psycopg2.connect')
    def test_save_user(self, mock_connect):
        user_repository = PsqlUserRepository("fake_connection_string")
        mock_connect.return_value = self.mocked_connection

        user = User(user_id=1, username='test_user')

        # Call the method under test
        user_repository.save_user(user)

        # Verify that the connection and cursor were called
        mock_connect.assert_called_once_with("fake_connection_string")
        self.mocked_connection.cursor.assert_called_once()
        self.mocked_cursor.execute.assert_called_once_with("INSERT INTO users (user_id, username) VALUES (%s, %s)", (1, 'test_user'))

if __name__ == '__main__':
    unittest.main()
