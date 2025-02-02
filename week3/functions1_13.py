import random

def guess_the_number(): 
    print("Hello! What is your name?") 
    name = input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number_to_guess = random.randint(1, 20) # generate a random number between 1 and 20
    guesses_taken = 0 # initialize the number of guesses taken

    while True: # loop until the user guesses the correct number
        print("\nTake a guess.")
        guess = int(input()) # get the user's guess
        guesses_taken += 1 # increment the number of guesses taken

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

if __name__ == "__main__":
    guess_the_number()