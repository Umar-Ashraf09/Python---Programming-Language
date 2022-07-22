import random

counter = 1
my_points = 0
computer_points = 0
while counter <= 5:
    print(f"Round {counter}")
    my_ans = input("Choose: rock, paper, scissors or quit")
    my_ans = my_ans.lower()
    if my_ans == "quit":
        print("Thank you. Please come again.")
        break
    if my_ans != "rock" and my_ans != "paper" and my_ans != "scissors":
        print("Wrong Input! Please choose a correct answer.")
        continue
    computer_ans = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_ans}")
    if my_ans == computer_ans: #tie
        my_points += 1
        print(f"My points {my_points}")
        computer_points += 1
        print(f"Computer points {computer_points}")
        counter += 1
        continue
    elif my_ans == "rock" and computer_ans == "scissors":
        my_points += 1
        print(f"My points {my_points}")
        print(f"Computer points {computer_points}")
        counter += 1
        continue
    elif my_ans == "paper" and computer_ans == "rock":
        my_points += 1
        print(f"My points {my_points}")
        print(f"Computer points {computer_points}")
        counter += 1
        continue
    elif my_ans == "scissors" and computer_ans == "paper":
        my_points += 1
        print(f"My points {my_points}")
        print(f"Computer points {computer_points}")
        counter += 1
        continue
    else:
        computer_points += 1
        print(f"My points {my_points}")
        print(f"Computer points {computer_points}")
        counter += 1
        continue

if my_points == 3 or my_points == 4 or my_points == 5:
    print("You Win!")
else:
    print("You lose!")