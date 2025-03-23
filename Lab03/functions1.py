import random
import itertools
import math

# Task 1: Convert grams to ounces
def grams_to_ounces(grams):
    return 28.3495231 * grams

# Task 2: Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Task 3: Solve the chickens and rabbits puzzle
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

# Task 4: Filter prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))

# Task 5: Print all permutations of a string
def string_permutations(s):
    return list(map("".join, itertools.permutations(s)))

# Task 6: Reverse words in a sentence
def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

# Task 7: Check if list contains 3 next to 3
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Task 8: Check if list contains 007 in order
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# Task 9: Compute volume of a sphere
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

# Task 10: Return list with unique elements
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Task 11: Check if a word is palindrome
def is_palindrome(s):
    return s == s[::-1]

# Task 12: Print histogram
def histogram(lst):
    for num in lst:
        print("*" * num)

# Task 13: Guess the number game
def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    guesses = 0
    while True:
        guess = int(input("Take a guess. "))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

# Task 14: Import and use functions
if __name__ == "__main__":
    print(grams_to_ounces(100))
    print(fahrenheit_to_celsius(100))
    print(solve(35, 94))
    print(filter_prime([10, 15, 3, 7, 19, 23, 50]))
    print(string_permutations("abc"))
    print(reverse_sentence("We are ready"))
    print(has_33([1, 3, 3]))
    print(spy_game([1, 2, 4, 0, 0, 7, 5]))
    print(sphere_volume(5))
    print(unique_elements([1, 2, 2, 3, 4, 4, 5]))
    print(is_palindrome("madam"))
    histogram([4, 9, 7])
    # guess_the_number()  # Uncomment to play
