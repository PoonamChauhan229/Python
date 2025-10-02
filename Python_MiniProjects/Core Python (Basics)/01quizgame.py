print("Welcome to the Quiz Game")

playing=input("Do you want to play ?")

if playing.lower() !='yes':
    quit()

print("Okay! Lets Play")

score=0

answer=input("What does CPU stand for? ")
if answer.lower()=="central processing unit":
    print("Correct Answer")
    score+=1
else:
    print("Incorrect Answer")  

answer=input("What does GPU stand for? ")
if answer.lower()=="graphic processing unit":
    print("Correct Answer")
    score+=1
else:
    print("Incorrect Answer")

answer=input("What does RAM stand for? ")
if answer.lower()=="random access memory":
    print("Correct Answer")
    score+=1
else:
    print("Incorrect Answer")

answer=input("What does PSU stand for? ")
if answer.lower()=="power supply unit":
    print("Correct Answer")
    score+=1
else:
    print("Incorrect Answer") 

print("You got",score,"questions correct")
print("You got",(score/4)*100,"%")


