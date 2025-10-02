import random
def roll_dice(num_dice,num_sides):
    results=[]
    for _ in range(num_dice):
        results.append(random.randint(1,num_sides))
        return results;

def main():
    print("Welcome to the Dice Roller ?")

    while True:
        try:
            num_dice=int(input("Enter the Number of Dice to roll:"))
            num_sides=int(input("Enter the Number of Sides on the Dice:"))
        except ValueError:
            print("Please enter Valid Numbers")
            continue
        results=roll_dice(num_dice,num_sides)
        print(f"Results:{results}")
        print(f"Total:{sum(results)}\n")

        play_again=input("Do you want to roll yes/no :").strip().lower()
        if play_again!="yes":
            print("Thanks for Playing")
            break;

if __name__=="__main__":
    main()