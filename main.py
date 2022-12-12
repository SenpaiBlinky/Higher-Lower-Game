import random
from art import logo, vs
from game_data import data
import os

def game():

    # Game Setup
    points = 0
    random_one = random.randint(0, len(data)-1)
    replay = True

    while replay == True:
    # REPEAT
        random_two = random.randint(0, len(data)-1)

        if random_two == random_one:
            while random_one == random_two:
                random_two = random.randint(0, len(data))

        os.system("cls")
        print(logo)

        person_a = data[random_one]
        person_a_followers = person_a['follower_count']
        print(f"Compare A: {person_a['name']} a {person_a['description']}, from {person_a['country']}")

        print(vs)

        person_b = data[random_two]
        person_b_followers = person_b['follower_count']
        print(f"Compare B: {person_b['name']} a {person_b['description']}, from {person_b['country']}")

        user_guess = input("Who has more followers? Type 'a' or 'b' ")

        if user_guess == "a" and person_a_followers > person_b_followers:
            points += 1
            random_two = random.randint(0, len(data)-1)
        elif user_guess == "b" and person_a_followers < person_b_followers:
            points += 1
            random_one = random_two
            random_two = random.randint(0, len(data)-1)
        else:
            print("wrong choice")
            replay = False
            
    print(f"You're streak was {points}")
    play_again = input("Would you like to play again? Type 'y'or 'n'")

    if play_again == "y":
        game()
game()

    

