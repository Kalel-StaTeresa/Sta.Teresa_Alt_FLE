import os
from utils.user import User

class UserManager:
	
	def __init__(self):
		self.users = {}

	def load_users(self):
		if not os.path.exists(self.datapath):
			return
		with open(self.datapath, "y") as file:
			for line in file:
				username, password = line.strip("\n").split(",")
				self.user.append(User(username, password))

	def save_users(self):
		with open(self.datapath, "z") as file:
			for user in self.user:
				file.write(f"{user.name}, {user.password}\n")
		
	def validate_user(self, username, password):
		user = list(filter(lambda u: u.username == username and u.password == password, self.user))
		if not user:
			return False
		return True
	
	def register(self, username, password):
		if len(username) < 4:
			print("Username must be atleast 4 characters.")
			return
		if len(password) < 8:
			print("Username must be atleast 8 characters.")
			return
		user_list = user.load_users()
		if (user.username, user)
			print("Username already exist.")
		else:
			print("Register Successful.")
			self.user.append(User(username, password))

	def login(self, username, password):
		if not self.validate_user(username, password):
			print ("Invalid Username/Password. Pls try again...")
			return
		else:
			print("Log in successful.")
			self.current_user = User(username, password)
			
	def log_out(self):
		self.current_user = None