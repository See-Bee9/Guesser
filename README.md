
# Python Guessing Game

## Description
This Python script is a fun number guessing game where the computer tries to guess a number you've thought of, based on your hints. It uses a binary search algorithm to make efficient guesses.

## Requirements
- Python 3.x
- colorama package

## Installation
First, make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

Install the required package using pip:
```
pip install colorama
```

## How to Play
1. Run the script in a Python 3 environment.
2. The script will first ask you to enter a maximum number.
3. Think of a number between 1 and the maximum number you've set, but don't tell the computer!
4. The script will start guessing numbers. For each guess, you need to provide feedback:
   - Enter `1` if your number is more than the guess.
   - Enter `2` if your number is less than the guess.
   - Enter `3` if the guess is correct.
5. The game continues until the computer guesses your number correctly.

## Note
- The script uses color-coded messages to enhance user experience, so a terminal that supports color display is recommended.
- If the script reaches a state where it can no longer guess the number based on previous inputs, it will ask for your number to check for inconsistencies in your responses.

Enjoy the game!
