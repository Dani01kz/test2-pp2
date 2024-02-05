
import random
def guess():
    x = input("Hello! What is your name? :")
    num = random.randint(1,20)
    print(f"Well, {x}, I am thinking of a number between 1 and 20.")
    i = 0
    while True:
        i+=1
        print("Take a guess.")
        some_num = int(input())
        if some_num == num:
            print(f"Good job, {x}! You guessed my number in {i} guesses!")
            break
        elif(some_num > num):
            print("Your guess is too big")
            continue
        elif(some_num < num):
            print("Your guess is too low")
            continue
        
guess()