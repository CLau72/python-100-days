#############DEBUGGING##############

# The following code was taken from the debugging exercises.
# This will be stored in 2 commits. One commit for the initial bugs
# and a second commit with the solved issues with commented solutions.

# Describe the Problem
def my_function():
    for i in range(1,21):
        if i == 20:
            print("You got it!")
my_function()

# SOLUTION:
# Change range to 1 - 21 since the range instruction is not inclusive

# Reproduce the Bug
from random import randint
dice_imgs = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# SOLUTION:
# Change the randomint to a range of 0 to 5 since arrays are zero indexed

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# SOLUTION
# Original would print nothing if the year was 1994. Added a <= to make 1994 a millennial

# Fix the Errors
age = int(input("How old are you? "))
if age > 16:
    print(f"You can drive at age {age}.")

# SOLUTION
# Make the input an integer and change the print to an fstring


# Print is your Friend
pages = 0
words_per_page = 0
pages = int(input("Number of pages: "))
words_per_page = int(input("Number of words per page: "))
total_words = pages * words_per_page
print(total_words)

# SOLUTION
# words_per_page was not being assigned the input, it was checking for equality.

 # Use a Debugger
def mutate(a_list):
     b_list = []
     for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
     print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# SOLUTION
# Append was happening outside of the for loop. Added it into the for loop so the new list
# was being appended properly.