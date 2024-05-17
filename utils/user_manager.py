import os
from utils.user import User

class UserManager:
    def __init__(self):
        self.users = []

    def register(self, user):
        if not any(u.username == user.username for u in self.users):
            self.users.append(user)
            return True
        return False

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

    def logout(self):
        print("User logged out successfully.")
