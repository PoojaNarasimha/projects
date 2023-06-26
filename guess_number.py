import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between and 1 and {x}:"))
        if guess<random_number:
            print("Sorry,guess again. Too low")
        elif guess>random_number:
            print("Too high")
    print(f"Yay, Congrats!! You have guessed the number {random_number} correctly")       


def computer_guess(y):
    low = 1
    high = y
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess=random.randint(low,high)
        else:
            guess = low #Also can be high
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)??").lower()
        if feedback == 'h':
            high = guess - 1
            print("Too high")
        elif feedback == 'l':
            low = guess+1
            print("Too Low")

    print(f"Yay, Congrats!! The computer guessed your number {guess} correctly")

computer_guess(10)

guess(10)



