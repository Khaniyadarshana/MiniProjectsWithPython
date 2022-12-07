#Snake Water Gun Game
import random
lst = ['s', 'w', 'g']

chance = 10
no_of_chance = 0
computer_score = 0
human_score = 0

print("\t \t \t \t Snake Water Gun \n \n")
print("Rules: The snake drinks the water, the gun shoots the snake, and gun has no effect on water.")
print("Press s fr Snake\nw for water\ng for gun \n")

#Use while loop for chances
while no_of_chance < chance:
    _input = input('Snake, Water, Gun')
    _random = random.choice(lst)

    #Case 1: Handling a tie
    if _input == _random:
        print("Its a tie\n0 point to each \n")

    #Case 2: if user enter S & random is g
    elif _input =='s' and _random == 'g':
        computer_score = computer_score + 1
        print(f"You chose {_input} and computer chose {_random}\n")
        print("Computer wins 1 point\n")
        print(f"Score Board:\n Computer:{computer_score} You:{human_score} \n")

    #Case 3: if user enter s & random is w
    elif _input == 's' and _random == 'w':
        human_score = human_score + 1
        print(f"You chose {_input} and computer chose {_random}\n")
        print("Human wins 1 point\n")
        print(f"Score Board:\n Computer:{computer_score} You:{human_score} \n")

    #Case 4: if user enter w & random is s
    elif _input == "w" and _random == "s":
        computer_score = computer_score + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_score} and your point is {human_score} \n ")

    #Case 5: if user enters w & random is g
    elif _input == 'w' and _random == 'g':
        human_score = human_score + 1
        print(f"You chose {_input} and computer chose {_random}\n")
        print("Human wins 1 point\n")
        print(f"Score Board:\n Computer:{computer_score} You:{human_score} \n")

    # Case 6: if user enters g & random is s
    elif _input == 'g' and _random == 's':
        human_score = human_score + 1
        print(f"You chose {_input} and computer chose {_random}\n")
        print("Human wins 1 point\n")
        print(f"Score Board:\n Computer:{computer_score} You:{human_score} \n")

    # Case 7: if user enter g & random is w
    elif _input == "g" and _random == "w":
        computer_score = computer_score + 1
        print(f"your guess {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_score} and your point is {human_score} \n ")

    #All other cases
    else:
        print("Please check your input\n")

    no_of_chance = no_of_chance + 1
    print(f"You have {chance - no_of_chance} chances left out of {chance}\n")

print("Game Over")
print(f"Final score: \n You: {human_score} Computer: {computer_score}")
if computer_score == human_score:
    print("Its a Tie")
elif computer_score > human_score:
    print("Computer Won, Better luck next time")
else:
    print("You Won, Congratulations!")
