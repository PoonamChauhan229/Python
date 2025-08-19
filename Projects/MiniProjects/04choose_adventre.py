name=input("Type your name? ")
print("Welcome",name,"to the Adventure ! ")

answer=input("You are on a dirt road, it has come to an end and you go left or right , Which way would you like to go? ").lower()

if answer =="left":
    answer=input("You come to a river,you can walk around it or swim across, Type walk to walk around and swim to swim across: ").lower()
    if answer=="swim":
        print("You swam across and were eaten by an alligator . ")
    elif answer =="walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option,You loose")
elif answer =="right":
    answer=input("You come to a bridge, it looks wobbly , do you want to cross it or head back ? Tpe cross/back ")
    if answer=="back":
        print("You go back and loose")
    elif answer=="cross":
        answer=input("You cross the bridgr and meet a stranger. Do ou talk to them (yes/no)")
        if answer=="yes":
            print("You talk to the stranger and they give you gold.You WIN!")
        elif answer=="no"
        print("You ignore the starnger and thy are offended and you loose.")
        else:
            print("Not a valid option, You Loose !")

    else:
        print("Not a valid option, You loose")
else:
        print("Not a valid option,You loose")