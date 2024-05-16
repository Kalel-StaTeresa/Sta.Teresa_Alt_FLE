from utils.dice_game import DiceGame
from utils.user_manager import UserManager

usermanager = UserManager()
dicegame = DiceGame()

def main():
    
    while True:
        print("Welcome to Dice Roll Game")
        print("1. Register")
        print("2. Log in")
        print("3. Exit")
        try:
            choice = int(input("Enter your choice or leave blank to cancel: "))
            if choice == 1:
                username = ''
                password = ''
                while True:
                    username = input ("Enter Username: ")
                    if len(username) < 4:
                        print("Username must be atleast 4 characters.")
                        continue
                    password = input ("Enter password: ")
                    if len(password) < 8:
                        print("Username must be atleast 8 characters.")
                        continue
                    break
                usermanager.register(username, password)
                return
            elif choice == 2:
                username = input ("Enter username: ")
                password = input ("Enter password: ")
                usermanager.login(username, password)
            elif choice == 3:
                print ("Exiting game...")
                break
            else:
                print ("Invalid Input")
        except ValueError as e:
            print(f"Error Occured {e}")

def the_game(user):
    print("\nWelcome to Dice Game, {usermanager.current_user.username}")
    print("1. Start")
    print("2. Show Top Scores")
    print('3. Log out')
    choice = int(input("Enter choice: "))
    loggedUser = usermanager.current_user.username
    try:
        while True:
            if choice == 1:
                dicegame.play_game(loggedUser)
            elif choice == 2:
                dicegame.show_top_scores()
            elif choice == 3:
                print ("Logging Out...")
                usermanager.log_out()
                dicegame.save_scores()
            else:
                print ("Invalid Input")
    except ValueError as e:
            print(f"Error Occured {e}")
        
if __name__ == "__main__":
    main()