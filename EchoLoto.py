# EchoLoto - Lottery Simulation Game
# Author: Anderson S.
# Version: 1.0.0
# Description: A lottery simulation game where users select numbers and compare them with random draws.

from random import sample
import time
import sys

# Start timer
start = time.time()

# Defining colors for text output
colors_predefined = {
    "end":"\033[m",
    "purple":"\033[1;35m",
    "red":"\033[1;31m",
    "purplewhite":"\033[1;35;40m"
}

# Function to add color to text
def colorize(text, color):
    """Adds color to the provided text based on predefined color codes."""
    if color in colors_predefined:
        return f"{colors_predefined[color]}{text}{colors_predefined['end']}"
    else:
        return text

# Display welcome message
print(colorize("Let's have a raffle? Give me 6 integer numbers between 1 and 60!", 'purple'))

# Function to collect user numbers
def requisition():
    """Collects 6 unique numbers from the user."""
    user_numbers = []
    while len(user_numbers) < 6:
        try:
            number = int(input(f"Give me the {len(user_numbers) + 1}º number: "))
            if 1 <= number <= 60 and number not in user_numbers:
                user_numbers.append(number)
            else:
                print("This number is already entered or invalid, try again!")
        except ValueError:
            print("Invalid input! Please enter an integer.")
    return user_numbers

# Function to draw 6 random numbers
def draw():
    """Generates 6 unique random numbers between 1 and 60."""
    return sample(range(1, 61), 6)

# Function to compare user numbers with drawn numbers
def compare_numbers(user_numbers, draw_numbers):
    """Compares user numbers with the drawn numbers and counts matches."""
    return len(set(user_numbers) & set(draw_numbers))

# Function to display suspense animation
def suspense():
    """Displays a loading animation for suspense."""
    for i in range(20):
        sys.stdout.write("\r" + "■" * i + " " * (20 - i))
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")

# Function to display game results
def display_results(hits):
    """Displays a message based on the number of matched numbers."""
    messages = {
        6: "Congratulations! You hit all 6 numbers, perfect!",
        5: "Great job! You hit 5 numbers!",
        4: "Well done! You hit 4 numbers!"
    }
    suspense()
    if hits in messages:
        print(colorize(messages[hits], 'purple'))
    elif 1 <= hits <= 3:
        print(colorize(f"Nice try! You hit {hits} numbers!", 'purple'))
    else:
        print(colorize("No hits, better luck next time!", 'purple'))

# Function to ask user if they want to play again
def play_again():
    """Prompts the user to play again and returns True if they choose yes."""
    while True:
        response = input(colorize("Do you want to play again? (yes/no): ", 'red')).lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print(colorize("Invalid response. Please type 'yes' or 'no'.", 'red'))

# Function to display the drawn numbers and user's results
def result(draw_numbers, numbers_hits, user_numbers):
    """Displays the drawn numbers and the user's matched numbers."""
    print(colorize(f"The drawn numbers were: {sorted(draw_numbers)}", 'purple'))
    if numbers_hits > 0:
        numbers_common = sorted(set(user_numbers) & set(draw_numbers))
        print(colorize(f"You matched: {numbers_common}", 'purple'))
    print(colorize(f"Total numbers matched: {numbers_hits}", 'purple'))

# Main game loop
def main():
    """Main game loop to handle user interaction."""
    while True:
        user_numbers = requisition()
        drawn_numbers = draw()
        numbers_hits = compare_numbers(user_numbers, drawn_numbers)
        display_results(numbers_hits)
        result(drawn_numbers, numbers_hits, user_numbers)
        if not play_again():
            break

# Run the game if the script is executed directly
if __name__ == "__main__":
    main()

# End timer and display total time
time_elapsed = time.time() - start
print(colorize(f"The EchoLoto lasted {time_elapsed:.2f} seconds!", 'red'))
