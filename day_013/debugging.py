#############DEBUGGING##############

# The following code was taken from the debugging exercises.
# This will be stored in 2 commits. One commit for the initial bugs
# and a second commit with the solved issues with commented solutions.

# Describe the Problem
def my_function():
    for i in range(1,20):
        if i == 20:
            print("You got it!")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")

# Fix the Errors
age = input("How old are you? ")
if age > 16:
    print("You can drive at age {age}.")

# Print is your Friend
pages = 0
words_per_page = 0
pages = int(input("Number of pages: "))
words_per_page == int(input("Number of words per page: "))
total_words = pages * words_per_page
print(total_words)


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])