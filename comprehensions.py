# List

# 1. Squares of numbers from 1–5
squares = [x**2 for x in range(1, 6)]
print(squares)

# 2. Only even numbers from a list
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# 3. With if-else: "even"/"odd" for numbers 1–6
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 7)]
print(labels)



# Set

# 1. Unique letters (in lowercase)
letters = {char.lower() for char in "PythonComprehension"}
print(letters)

# 2. Squares without duplicates
unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 4]}
print(unique_squares)

# 3. Numbers greater than 10 from a list
over_ten = {x for x in [5, 12, 15, 15, 8, 20] if x > 10}
print(over_ten)


# Dict

# 1. Number and its square
square_dict = {x: x**2 for x in range(1, 6)}
print(square_dict)

# 2. Words and their length
word_lengths = {word: len(word) for word in ["Apple", "Banana", "Kiwi"]}
print(word_lengths)

# 3. Include only even numbers
even_dict = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_dict)
