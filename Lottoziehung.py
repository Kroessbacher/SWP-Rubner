import random
"""Task: Program a lottery draw as a method

Use random.getrand()
The algorithm for drawing random numbers must be written so that no random number can be drawn twice.
This means if you had to draw all 45 numbers, you would only be allowed to call the random number generator 45 times.
Draw six numbers and display them on the screen.

Task: Program lottery draw statistics as a method

Perform 1000 draws.
Create a dictionary for statistics that tracks how many times each number was drawn.
Call the statistics method after each draw and increment the counter."""


def main():
    try:
        # User input for number range and number of draws
        start = int(input("Range start: ")) - 1   # subtract 1 so range works correctly
        end = int(input("Range end: "))
        num_draws = int(input("Number of draws: "))

    except ValueError:
        print("That was not a valid number!")
        return

    # Initialize dictionary to count frequency of each number
    frequencies = {i: 0 for i in range(start, end)}

    # Perform the draws
    perform_draws(num_draws, frequencies, start, end)

    # Print results
    for number in range(start, end):
        print(f"Number {number+1:2}: {frequencies[number]} times drawn; "
              f"{frequencies[number]/num_draws*100:.2f}%")

def lottery_draw(numbers, amount):
    """Simulates a single lottery draw and returns the last 6 numbers drawn"""
    for x in range(amount):
        random_index = random.randint(0, len(numbers)-1-x)
        numbers[len(numbers)-1 - x], numbers[random_index] = (
            numbers[random_index], numbers[len(numbers)-1-x]
        )
    return numbers[-6:]

def perform_draws(num_draws, frequencies, start, end):
    """Performs multiple lottery draws and counts how often each number was drawn"""
    for _ in range(num_draws):
        numbers = list(range(start, end))
        drawn_numbers = lottery_draw(numbers, 6)
        for number in drawn_numbers:
            frequencies[number] += 1

if __name__ == "__main__":
    main()
