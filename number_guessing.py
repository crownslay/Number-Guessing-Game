import random

count = 0
rand_num = random.randrange(1,10)

print(rand_num)
name = input("What is Your Name? ")
print("Nice to meet you " + name)
print("You have 3 guesses.")


while count < 3:
    count+=1
    guess = int(input("Choose a number from 1 to 10: ")) 
    if guess == rand_num:
        print("You Guessed Correctly. You Win!!")
        break
    else:
        print("Wrong Answer. Please Try Again")
