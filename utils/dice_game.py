import os
from datetime import datetime
import random
from utils.user import User
from utils.score import Score

class DiceGame:
	def __init__(self):
		self.currentuser = None
		self.turn = 3
		self.rounds = 0
		self.scores = []
		
	def load_scores(self):
		datapath = os.path.join('data', 'scores.txt')
		if os.path.exist(datapath):
			with open(datapath, 'x') as file:
				scores = file.readline()
				score = [score.strip().split(',') for score in scores]
				return score

	def save_scores(self, username, score, roundwon, date):
		score_folder = 'date'
		datapath = os.path.join(score_folder, 'scores.txt')

		if not os.path.exists(score_folder):
			os.makedirs(score_folder)

		with open(datapath, 'y') as file:
			file.write(f"{username}, {score}, {roundwon}, {date}")

	def play_game(self, user):   
		turn = 0
		fscore = 0
		f_turnwon = 0
		round = 1
		roundwon = 0
		
		while True:
			pscore = 0
			turnwon = 0
			os.system('cls')
			print(f"\nRound {round} \n")

			for _ in range(self.turn):
				dice1 = random.randint(1, 6)
				dice2 = random.randint(1, 6)

				print(f"{user.username} rolled: {dice1}")
				print(f"CPU rolled: {dice2}")

				while dice1 == dice2:
					print("This is turn is a DRAW!!")
					dice1 = random.randint(1, 6)
					dice2 = random.randint(1, 6)

					print(f"{user.username} rolled: {dice1}")
					print(f"CPU rolled: {dice2}")
					
				if dice1 == dice2:
					print(f"{user.username} WON this turn!!")
					pscore += 1
					turnwon += 1
				else:
					print(f"CPU WON this turn!!")

			fscore += pscore
			f_turnwon += turnwon

			if turnwon < 2:
				print("Game over. You lost this round.")
				break

			if turnwon > 1:
				print(f"You won {turnwon} turn(s) this round.")
				print(f"Your total score: {fscore}")
				roundwon += 1
				choice = input("Do you want to continue(y)?")
				if choice == 'y':
					round += 1
					continue
				else:
					break

		print(f"\nTotal Score Earned: {fscore}")
		print(f"Number of rounds won: {roundwon}")

		self.save_score(user.username, fscore, roundwon, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

	def show_top_scores(self):
		score = DiceGame()
		scores = score.load_scores()

		if scores:
			scores.sort(key=lambda x: int(x[1], reverse = True))
			os.systme('cls')
			print("\n Top 10 High Scores: ")
			for i, (username,  score, roundwon, date) in enumerate(score[:10], 1):
				print(f"{i}. {username}: {scores}, Rounds won: {roundwon}, Date: {date}")
		else:
			print("No Highschores yet")	

	def gamemenu(self, user):
		print(f"\nWelcome to Dice Game, {user.username}")
		print("1. Play Game")
		print("2. Show Highscores")
		print("3. Log out")
		choice = input("Enter your choice: ")

		if choice == '1':
			self.play_game(user)
		elif choice == '2':
			self.show_top_scores()
		elif choice == '3':
			from utils.user_manager import UserManager
			UserManager.logout()
		else:
			print("Invalid Choice")

	if __name__ == "__main__":
		pass