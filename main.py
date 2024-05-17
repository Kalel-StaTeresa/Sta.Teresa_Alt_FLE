from utils.dice_game import DiceGame
from utils.user_manager import UserManager
from utils.user import User

class Main:
    def __init__(self):
        self.usermanager = UserManager()
        self.dicegame = DiceGame()

    def main(self):
        while True:
            print("\nWelcome to Dice Roll Game")
            print("1. Register")
            print("2. Log in")
            print("3. Exit")
            try:
                choice = input("Enter your choice (or leave blank to cancel): ").strip()
                if choice == "":
                    print("No input given, cancelling the current operation.")
                    continue
                
                choice = int(choice)
                if choice == 1:
                    username = input("Enter Username: ").strip()
                    password = input("Enter Password: ").strip()
                    if username and password:
                        user = User(username, password)
                        if self.usermanager.register(user):
                            print(f"User {username} registered successfully.")
                        else:
                            print(f"User {username} could not be registered.")
                    else:
                        print("Username and password cannot be empty.")
                    continue

                elif choice == 2:
                    username = input("Enter Username: ").strip()
                    password = input("Enter Password: ").strip()
                    if username and password:
                        if self.usermanager.login(username, password):
                            print(f"User {username} logged in successfully.")
                            self.dicegame.gamemenu(User(username, password))
                        else:
                            print("Invalid username or password.")
                    else:
                        print("Username and password cannot be empty.")
                    continue

                elif choice == 3:
                    print("Exiting game...")
                    break

                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid input, please enter a number.")

if __name__ == "__main__":
    main = Main()
    main.main()
