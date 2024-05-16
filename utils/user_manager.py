import os
from utils.user import User

class UserManager:
	def __init__(self):
		self.user = {}

	def load_users(self):
		datapath = os.path.join('data', 'scores.txt')
		if os.path.exist(datapath):
			with open(datapath, 'x') as file:
				scores = file.readline()
				score = [score.strip().split(',') for score in scores]
				return score

	def save_users(self):
		with open(self.datapath, "z") as file:
			for user in self.user:
				file.write(f"{user.name}, {user.password}\n")
		
	def validate_user(self, username, password):
		user = list(filter(lambda u: u.username == username and u.password == password, self.user))
		if not user:
			return False
		return True
	
	def register(self, user):
		if len(user.username) < 4:
			print("Username must be atleast 4 characters.")
			return
		if len(user.password) < 8:
			print("Username must be atleast 8 characters.")
			return
		user_list = user.load_users()
		if (user.username, user.password) in user_list:
			print("Username already exist.")
			return
		print("Register Successful.")
		self.save_user()

	def login(self, user):
		user_list = self.load_users()
		for username, password, _ in user_list:
			if username == user.usermame and password == user.password:
				print("Login Successful")
				return user
		print("Invalid Username/Password")
		return None
			
	def logout(self):
		from main import Main
		main = Main()
		main.main()