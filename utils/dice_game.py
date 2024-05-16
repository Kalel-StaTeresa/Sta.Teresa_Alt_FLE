import os
import datetime
import random
from utils.user import User
from utils.score import Score

class DiceGame:
	
	scorelist = []
	datapath = os.path.join("data", "score.txt")

	def __init__(self):
		if not os.path.exists(self.datapath):
			if open(self.datapath, "x"):
				pass
			else:
				print("Error creating file")
		self.load_scores
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

	def play_game(self):   
		player = User()
		while True:
			turns = 0
			cpu = 0
			playerscore = 0
			fscore = 0
			round = 0
			while turns < 4:
				Dice1 ,Dice2 = random.randrange (1,6), random.randrange (1,6)
				print(f"{player.username} rolled: {Dice1}")
				print(f"CPU rolled: {Dice1}")
				if Dice1 > Dice2:
					print(f"{player.username} won the turn!")
					playerscore += 1
					round += 1
				elif Dice1 < Dice2:
					print(f"CPU won the turn!")
					cpu += 1
				else:
					print(f"The turn is a tie...")
				turns += 1
			if playerscore > cpu:
				print(f"{player.username} won round {round} with a score of {playerscore}")
				fscore += playerscore + 3
				choice = input("Do you want to continue(y)? ")
				if choice == 'y':
					continue
				else:
					break
			elif playerscore > cpu:
				print("CPU won this round.")
				print("Game Over!")
			date = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
			score = Score(player.username, fscore, date, round)
			DiceGame.scorelist.append(score)
			break

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