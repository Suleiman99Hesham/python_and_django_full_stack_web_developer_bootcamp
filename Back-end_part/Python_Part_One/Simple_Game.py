###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
comp_number = digits[:3]
print(comp_number)

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

def compare_and_find(num, list_digits):
    count = 0
    for i in num:
        if i in list_digits:
            count += 1
    if count > 0:
        if (num[0] == list_digits[0] or num[2] == list_digits[1]
            or num[2] == list_digits[2]):
            return "Match"
        return "Close"
    return "Nope"

while True:    
    guess = [int(i) for i in list((input("What is your guess? ")))]
    if guess == comp_number:
        break
    print(compare_and_find(guess,comp_number))

print("Congratulations, you have reached the correct result successfully")