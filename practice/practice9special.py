# Game developer: Uday
import random
print("Welcome the snake, water and gun: by Uday ")
game_list = ["s", "w", "g"]
i = 1

score_computer = 0
score_you = 0


def winner(a):
    """
    This is for declaration of winner   
    """
    win_declare = a + " win"
    return win_declare


while (i <= 10):
    print("""Enter s for Snake
    Enter w for Water
    Enter g for Gun""")

    user_choice = input("Enter your choice: ")
    choice_game_list = random.choice(game_list)
    if choice_game_list == user_choice:
        print(winner("no one"))
    elif choice_game_list == "s" and user_choice == "w":
        score_computer = score_computer + 1
        print(winner("Computer"))
    elif choice_game_list == "s" and user_choice == "g":
        score_you = score_you + 1
        print(winner("You"))
    elif choice_game_list == "w" and user_choice == "s":
        score_you = score_you + 1
        print(winner("You"))
    elif choice_game_list == "w" and user_choice == "g":
        score_computer = score_computer + 1
        print(winner("Computer"))
    elif choice_game_list == "g" and user_choice == "s":
        score_computer = score_computer + 1
        print(winner("Computer"))
    elif choice_game_list == "g" and user_choice == "w":
        score_you = score_you + 1
        print(winner("You"))
    else:
        print("please Enter a write input")
    print("Your score is ", score_you)
    print("Computer score is ", score_computer)
    if score_you > score_computer:
        print("You win")
    elif score_you < score_computer:
        print("Computer win")
        print("Better luck next time")
    elif score_you == score_computer:
        print("tie between you and comp")
    i += 1
