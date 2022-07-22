import random

while True:
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome")
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tRock, Paper or Scissors Game")
    my_ans = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tChoose:-\t\tRock\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPaper"
                   "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tScissors\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tQuit (to exit)"
                   "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=> ")
    my_ans = my_ans.lower()

    if my_ans == "quit":
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease come again.")
        break

    if my_ans != "rock" and my_ans != "paper" and my_ans != "scissors":
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease choose a correct answer.\n")
        continue

    computer_ans = random.choice(["rock", "paper", "scissors"])
    print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tComputer chose:\t{computer_ans}")

    if my_ans == computer_ans:
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYou tied")
        user_inp = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tChoose:-\tContinue\tQuit (to exit)\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=> ")
        user_inp = user_inp.lower()
        if user_inp not in ("continue", "quit"):
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease choose a correct answer.\n")
            continue
        elif user_inp == "quit":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease come again.")
            break
        else:
            continue
    elif my_ans == "rock" and computer_ans == "scissors":
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYou Win!")
        user_inp = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tChoose:-\tContinue\tQuit (to exit)\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=> ")
        user_inp = user_inp.lower()
        if user_inp not in ("continue", "quit"):
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease choose a correct answer.\n")
            continue
        elif user_inp == "quit":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease come again.")
            break
        else:
            continue
    elif my_ans == "paper" and computer_ans == "rock":
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYou Win!")
        user_inp = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tChoose:-\tContinue\tQuit (to exit)\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=> ")
        user_inp = user_inp.lower()
        if user_inp not in ("continue", "quit"):
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease choose a correct answer.\n")
            continue
        elif user_inp == "quit":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease come again.")
            break
        else:
            continue
    elif my_ans == "scissors" and computer_ans == "paper":
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYou Win!")
        user_inp = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tChoose:-\tContinue\tQuit (to exit)\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=> ")
        user_inp = user_inp.lower()
        if user_inp not in ("continue", "quit"):
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease choose a correct answer.\n")
            continue
        elif user_inp == "quit":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease come again.")
            break
        else:
            continue
    else:
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tYou lose!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTry again.")
        user_inp = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tChoose:-\tContinue\tQuit (to exit)\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=> ")
        user_inp = user_inp.lower()
        if user_inp not in ("continue", "quit"):
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease choose a correct answer.\n")
            continue
        elif user_inp == "quit":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You.\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease come again.")
            break
        else:
            continue


