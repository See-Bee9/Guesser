import math
import os
from colorama import Fore, Style, init

init()  # Initialize colorama

def clear_console():
    # Clear console command for different operating systems
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def make_accusation(past_guess, response, user_number):
    if response == "too high" and user_number >= past_guess:
        return "You said it was less than {}! 😠".format(past_guess)
    elif response == "too low" and user_number <= past_guess:
        return "You said it was more than {}! 😠".format(past_guess)
    return None

def guess_number(max_number):
    max_guesses = math.ceil(math.log2(max_number))
    clear_console()
    print(Fore.CYAN + "Think of a number between 1 and {}.".format(max_number) + Style.RESET_ALL)
    print(Fore.GREEN + "I can guess your number in at most {} guesses!".format(max_guesses) + Style.RESET_ALL)

    low = 1
    high = max_number
    guesses = 0
    guess_history = []

    while True:
        if low > high:  # Invalid state
            user_number = int(input(Fore.RED + "I'm confused! What was your number? " + Style.RESET_ALL))
            for past_guess, response in guess_history:
                accusation = make_accusation(past_guess, response, user_number)
                if accusation:
                    print(Fore.RED + "You cheater, " + accusation + Style.RESET_ALL)
                    return
            print(Fore.GREEN + "Oops! Looks like I made a mistake. Sorry about that!" + Style.RESET_ALL)
            return

        guesses += 1
        guess = (low + high) // 2
        clear_console()
        print(Fore.YELLOW + "Guess {}: My guess is {}".format(guesses, guess) + Style.RESET_ALL)
        print("1: My number is more than {}".format(guess))
        print("2: My number is less than {}".format(guess))
        print("3: Correct")
        response = input("Enter your response (1, 2, or 3): ")

        if response == "3":
            print(Fore.GREEN + "Great! I've guessed your number in {} guesses!".format(guesses) + Style.RESET_ALL)
            break
        elif response == "2":
            high = guess - 1
            guess_history.append((guess, "too high"))
        elif response == "1":
            low = guess + 1
            guess_history.append((guess, "too low"))
        else:
            print(Fore.RED + "Please enter a valid response (1, 2, or 3)." + Style.RESET_ALL)
            guesses -= 1  # Invalid response doesn't count as a guess

def main():
    try:
        max_number = int(input("Enter the maximum number: "))
        guess_number(max_number)
    except ValueError:
        print(Fore.RED + "Please enter a valid integer." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
