import random

print(random.randrange(0,5)) # not include 5

top_of_range=input("Type a number? ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("Please type a number larger than 0")
        quit()      
else:
    print("Please type a number next time !")
    quit()

randomNumber=random.randrange(0,top_of_range)

# user guess

guesses=0
while True:
    guesses+=1
    user_guess=input("Make a guess? ")
    if user_guess.isdigit():
        user_guess=int(user_guess)        
    else:
        print("Please type a Number")
        continue
    
    if user_guess==randomNumber:
            print("You Got it")
            break
    elif user_guess>randomNumber:
        print("You are above the number")
    else:
        print("You are below the number")

print("perfect Match,You got it in : ",guesses ,"attempts")
