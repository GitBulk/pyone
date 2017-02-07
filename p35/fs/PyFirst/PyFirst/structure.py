import random

myName = ''

def print_welcome():
    print("Hello! What is your name?")
    myName = input()
    print("Well, " + myName + ", I am thinking of a number between 1 and 20.")

def play_game():
    guessTaken = 0
    number = random.randint(1, 20)
    while guessTaken < 6:
        print("Take guess")
        guess = input()
        guess = int(guess)
        guessTaken = guessTaken + 1
        if guess < number:
            print("Your guess is too low")
    
        if guess > number:
            print("Your guess is too high")

        if guess == number:
            break

    if guess == number:
        guessTaken = str(guessTaken)
        print("Good job, " + myName + "! You guessed my number in " + guessTaken + " guesses!")

    if guess != number:
        number = str(number)
        print("Nope, The number I was thinking of was " + number)

if __name__ == "__main__":
    print_welcome()
    play_game()