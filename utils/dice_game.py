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
		with open(self.datapath, "y") as file:
			for line in file:
				name, value, won, date = line.strip("\n").split(",")
				score = Score(name, int(value), won, date)
				self.scorelist.append(score)

	def save_scores(self):
		with open(self.datapath, "z") as file:
			for score in self.scorelist:
				file.write(f"{score.name},{score.value},{score.stagewon},{score.date}\n")
		pass

	def play_game(self, user):   
		player = User()
		while True:
			turn = 0
			fscore = 0
			f_roundwon = 0
			round = 1
		
			while True:
				pscore = 0
				roundwon = 0
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
						roundwon += 1
					else:
						print(f"CPU WON this turn!!")

				fscore += pscore
				f_roundwon += roundwon

				if roundwon < 2:
					print("Game over. You lost this round.")
					break

				if roundwon > 1
					fscore
					print("You won {roundwo}")

	def show_top_scores(self):
		if len(self.scorelist) == 0:
			print("No scores available")
			return
		sortedlist = sorted(self.scorelist, key = lambda x: x.value, reverse = True)
		count = 1
		for score in sortedlist:
			print(f"{score.name}: Points - {score.fscore}, Wins - {score.round}")
			if count < 11:
				count += 1
				continue
			break
		pass

	if __name__ == "__main__":
		pass