'''
5. Number Guessing Game
Beginner
Concepts: while, if-else, functions
Requirements
•	Generate a random number from 1 to 100.
•	Ask the player to guess the number.
•	Display “Too high” or “Too low.”
•	Limit the player to seven attempts.
•	Display the final result.
Bonus: Add easy, medium, and hard difficulty levels with different attempt limits
'''
import random

def generate_num(func):
    def wrap():
        a = random.randint(0-100)
        return func(a)
    return wrap

@generate_num
def guess_game(num):
    count = 7
    while True: