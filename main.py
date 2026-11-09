"""
1.3 Control Structures: Coding Practice
Follow-up to the guided notes.

How to use this file:
- Read the prompt in the comments above each exercise.
- Replace "pass" with your code. Delete "pass" once you've written code.
- Some prompts ask a conceptual question. Answer it in a comment right below the prompt.
- To test a function, uncomment the matching "print" line at the bottom of the file
  and run the file.
"""


# =====================================================================
# PART 1: CONDITIONALS (if, elif, else, nested if, not)
# =====================================================================

# Exercise 1.1
# Write a function called grade_letter that takes a number score and
# returns a letter grade as a string:
#   90 or above -> "A"
#   80 to 89    -> "B"
#   70 to 79    -> "C"
#   60 to 69    -> "D"
#   below 60    -> "F"
def grade_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C" 
    elif score >= 60:
        return "D"
    else:
        return "F"

# Exercise 1.2
# Conceptual question: In grade_letter, what would go wrong if you checked
# "score >= 60" first instead of "score >= 90"? Write your answer below.
# Your answer: it will include grade range that are not accurate to the letter it's printing.
#We need the order to reduce of possibilities with each statement.


# Exercise 1.3
# Write a function called is_empty that takes a list and returns True if the
# list has no items and False otherwise.
# Rule: do NOT use == with an empty list. Use truthiness with "not".
def is_empty(items):
    if not items:
        return True
    else:
        return False


# Exercise 1.4
# Write a function called describe_number that takes an integer and returns:
#   "zero"      if the number is 0
#   "positive"  if the number is greater than 0
#   "negative"  otherwise
# Use if, elif, and else.
def describe_number(n):
    if n == 0:
        return "zero"
    elif n > 0:
        return "positive"
    else:
        return "negative"


# =====================================================================
# PART 2: WHILE LOOPS
# =====================================================================

# Exercise 2.1
# Write a function called countdown that takes a starting number n and prints
# the numbers from n down to 1, one per line, then prints "Liftoff!".
# Use a while loop and make sure you update your counter so the loop ends.
def countdown(n):
    # while loop that prints our number out
    while n > 0:
        print(n)
        n = n-1
    print("Liftoff!")


# Exercise 2.2
# Write a function called total_until_negative that takes a list of numbers and
# adds them up with a while loop, stopping when it reaches a negative number.
# Return the total. Do not include the negative number.
# Example: [4, 5, -1, 10] should return 9.
def total_until_negative(nums):
    total = 0
    i = 0
    while 0 < len(nums) and nums(n) >= 0:
        total = total + nums(n)
    return total  #? ask for help  


# Exercise 2.3
# Conceptual question: The loop in countdown would run forever if you forgot
# to update the counter. What is the name for the variable that controls
# when a while loop stops? Write your answer below.
# Your answer:it is called a counter variable it keeps track of the loop
# and helps the while loop know when to stop looping


# =====================================================================
# PART 3: FOR LOOPS, range(), enumerate(), AND DICTIONARIES
# =====================================================================

# Exercise 3.1
# Write a function called even_numbers that takes an integer n and returns a
# list of the even numbers from 0 up to n (inclusive if n is even).
# Use range() with a step. Example: even_numbers(6) returns [0, 2, 4, 6].
def even_numbers(n):
    numbers = []
    for i in range(0, n + 1, 2):
        numbers.append(i)
    return numbers


# Exercise 3.2
# Write a function called print_multiples_of_three that prints every multiple
# of 3 from 3 through 30, one per line. Use range(start, stop, step).
def print_multiples_of_three():
    for i in range(3, 31, 3):
        print(i)
    


# Exercise 3.3
# Write a function called print_numbered_list that takes a list of strings and
# prints them as a numbered list starting at 1.
# Example: ["apple", "pear"] prints:
#   1. apple
#   2. pear
# Use enumerate(). Remember that enumerate() starts counting at 0,
# so you will need to add 1 to the index.
def print_numbered_list(items):
    


# Exercise 3.4
# Write a function called highest_scorer that takes a dictionary where the keys
# are student names and the values are scores. It should print each student's
# name and score, then return the name of the student with the highest score.
# Example: {"Ana": 95, "Ben": 82} prints both lines and returns "Ana".
# Use .items() to get both the key and the value.
def highest_scorer(scores):
    pass


# Exercise 3.5
# Conceptual question: What does this loop print, and why?
#     d = {"red": 1, "blue": 2}
#     for k in d:
#         print(k)
# Your answer: it prints red and blue because the loop goes through the
# dict keys it doesn't print the nums b/c those are the values


# =====================================================================
# PART 4: break, continue, AND return
# =====================================================================

# Exercise 4.1
# Write a function called index_of_first_negative that takes a list of numbers
# and returns the index of the first negative number. If there is no negative
# number, return -1. Use return inside the loop.
def index_of_first_negative(nums):
     for index in range(len(nums)):
        if nums[index] < 0:
            return index
   


# Exercise 4.2
# Write a function called print_without_vowels that takes a string and prints
# each character that is NOT a vowel (a, e, i, o, u), one per line.
# Use continue to skip the vowels.
def print_without_vowels(word):
    pass


# Exercise 4.3
# Write a function called has_pair_with_sum that takes a list of numbers and a
# target number. It should return True if any two numbers in the list add up to
# the target, and False otherwise.
# Hint: this needs a nested for loop. Use return as soon as you find a pair.
# Example: has_pair_with_sum([2, 7, 11], 9) returns True (2 + 7 = 9).
def has_pair_with_sum(nums, target):
    pass


# Exercise 4.4
# Conceptual question: In the nested loop from Exercise 4.3, if you used break
# instead of return when you found a pair, what would happen? Would the
# function still return the right answer? Write your answer below.
# Your answer:


# =====================================================================
# PART 5: FIND AND FIX THE BUGS
# =====================================================================

# Exercise 5.1
# This function is supposed to print 5, 4, 3, 2, 1 but runs forever.
# Find the bug and fix it. Replace the "pass" in the function body with the fix.
def bugged_countdown():
    n = 5
    while n > 0:
        print(n)
        n = n -1


# Exercise 5.2
# This code should print each fruit and its price, but it crashes.
# Fix it so it works.
def bugged_prices():
    prices = {"apple": 1.20, "pear": 0.80}
    for fruit, price in prices:
        print(fruit, price)


# =====================================================================
# PART 6: CHALLENGE
# =====================================================================

# Exercise 6.1
# Write a function called fizzbuzz that takes an integer n and prints the
# numbers from 1 to n, but:
#   - prints "FizzBuzz" if the number is divisible by both 3 and 5
#   - prints "Fizz" if the number is divisible by 3 only
#   - prints "Buzz" if the number is divisible by 5 only
#   - otherwise prints the number itself
# Hint: check the FizzBuzz case first. Think about why the order matters.
def fizzbuzz(n):
    for number in range(1, n + 1):
        if number / 3 == 0 and number/5 == 0:
            print("FizzBuzz")
        elif number / 3 == 0:
            print("Fizz")
        elif number / 5 == 0:
            print("Buzz")
        else:
            print(number)


# =====================================================================
# TESTING YOUR WORK
# Uncomment a line to test a function. Run the file to see the output.
# =====================================================================

if __name__ == "__main__":
    print(grade_letter(85))            # Expected: B
    print(is_empty([]))                # Expected: True
    print(describe_number(-4))         # Expected: negative
    countdown(3)                       # Expected: 3, 2, 1, Liftoff!
    #print(total_until_negative([4, 5, -1, 10]))   # Expected: 9
    # print(even_numbers(6))             # Expected: [0, 2, 4, 6]
    # print_multiples_of_three()         # Expected: 3, 6, 9, ... 30
    # print_numbered_list(["apple", "pear"])
    # print(highest_scorer({"Ana": 95, "Ben": 82}))   # Expected: Ana
    # print(index_of_first_negative([3, 8, -2, 5]))   # Expected: 2
    # print_without_vowels("python")
    # print(has_pair_with_sum([2, 7, 11], 9))         # Expected: True
    # bugged_countdown()
    # bugged_prices()
    # fizzbuzz(15)
    pass
