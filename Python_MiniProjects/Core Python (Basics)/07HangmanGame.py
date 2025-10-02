import random

HANGMANPICS = [
"""
  +---+
      |
      |
      |
     ===""",
"""
  +---+
  O   |
      |
      |
     ===""",
"""
  +---+
  O   |
  |   |
      |
     ===""",
"""
  +---+
  O   |
 /|   |
      |
     ===""",
"""
  +---+
  O   |
 /|\\  |
      |
     ===""",
"""
  +---+
  O   |
 /|\\  |
 /    |
     ===""",
"""
  +---+
  O   |
 /|\\  |
 / \\  |
     ==="""
]


# WordList
wordList=["python","hangman","developer","variable"]

# Pick a random word > Make it UpperCase
randomWord=random.choice(wordList).upper()
guessed=[]
wrong=0

print("Welcome to the Hangman Show")

while wrong <len(HANGMANPICS)-1:
    display=""
    for ch in randomWord:
        if ch in guessed:
            display+=ch+" "
        else:
            display+="_ "
    print(HANGMANPICS[wrong])
    print("Word",display.strip()) 

    # Check if player has guessed the word
    if "_" not in display:
        print(f"You won, the word was{randomWord} which is = {display}")
        break

    guessWord=input("Guess a letter:").upper()

    if guessWord in randomWord:
        if guessWord not in guessed:
            guessed.append(guessWord)
            print(f"Great!!!,The guessword is the part of RandomWord {guessWord} \n")
        else:
            print("You already guessed that letter!\n")
    else:
            wrong+=1
            print(f"Wrong guess! You have {len(HANGMANPICS)-1-wrong} chances left.\n")
            print(f"Sorry!!! Pls try another word \n")
    
    if wrong == len(HANGMANPICS)-1:
        print(HANGMANPICS[wrong])
        print(f"Game Over, Chances Exhausted , The word was {randomWord}")


   