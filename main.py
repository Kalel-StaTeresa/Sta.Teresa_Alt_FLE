from utils.dice_game import DiceGame
from utils.user_manager import UserManager
from utils.user import User

class Main:
    def __init__(self):
        self.usermanager = UserManager()
        self.dicegame = DiceGame()

    def main(self):
        while True:
            print("Welcome to Dice Roll Game")
            print("1. Register")
            print("2. Log in")
            print("3. Exit")
            try:
                choice = int(input("Enter your choice or leave blank to cancel: "))
                if choice == 1:
                    username = input ("Enter Username: ")
                    password = input ("Enter password: ")
                    user = User(username, password, 0)
                    self.usermanager.register(user)

                elif choice == 2:
                    username = input ("Enter username: ")
                    password = input ("Enter password: ")
                    user = User(username, password, 0)
                    self.usermanager.login(user)

                elif choice == 3:
                    print ("Exiting game...")
                    exit()
                else:
                    print ("Invalid Input")
            except ValueError as e:
                print(f"Error Occured {e}")

    if __name__ == "__main__":
        main()