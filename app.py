from flask import Flask
from application.user_service import UserRepository

app = Flask(__name__)

# @app.route('/')
# def ro():
#     return 'LORI'



if __name__ == '__main__':
    app.run()
