import os
from utils.user import User

class UserManager:
    def __init__(self):
        self.users = []
        self.data_file = os.path.join('data', 'users.txt')
        self.load_users()

    def load_users(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                for line in file:
                    username, password = line.strip().split(',')
                    self.users.append(User(username, password))

    def save_users(self):
        with open(self.data_file, 'w') as file:
            for user in self.users:
                file.write(f"{user.username},{user.password}\n")

    def register(self, user):
        if not any(u.username == user.username for u in self.users):
            self.users.append(user)
            self.save_users()
            return True
        return False

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return True
        return False

    def logout(self):
        print("User logged out successfully.")
