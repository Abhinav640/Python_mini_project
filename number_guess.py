import random

level=input('''Select your deficulty level
E for Easy
M for Medium
H for Hard\n''')

def easy():
    num=random.randrange(0,101)
    print(num)

    guess = int(input("Enter a number between 0-100: "))
    guesses=1
    rem_guesses=15

    if(num!=guess):
        while num!=guess:
            
            guesses += 1
            rem_guesses -=1
            if rem_guesses == 0:
                print("Game Over")
                quit()

            elif guess>100 or guess<0:
                print("Zada Kabil Mat Bano")
                guess=int(input("Enter a number between 0-100: "))
  
            else:
                if num>guess:
                    guess=int(input(f"{rem_guesses} trys left, please guess any larger number: "))

                else:
                    guess=int(input(f"{rem_guesses} trys left, please guess any smaller number: "))
        if guess==num:
            print("bingo")
    else:    
        print("Adbhoootttt..")

    print(f"Number of try = {guesses}")

def medium():
    num=random.randrange(0,101)
    print(num)

    guess = int(input("Enter a number between 0-100: "))
    guesses=1
    rem_guesses=10

    if(num!=guess):
        while num!=guess:
            
            guesses += 1
            rem_guesses -=1
            if rem_guesses == 0:
                print("Game Over")
                quit()

            elif guess>100 or guess<0:
                print("Zada Kabil Mat Bano")
                guess=int(input("Enter a number between 0-100: "))

            else:
                if num>guess:
                    guess=int(input(f"{rem_guesses} trys left, please guess any larger number: "))

                else:
                    guess=int(input(f"{rem_guesses} trys left, please guess any smaller number: "))
        if guess==num:
            print("bingo")
    else:    
        print("Adbhoootttt..")

    print(f"Number of try = {guesses}")

def hard():
    num=random.randrange(0,101)
    print(num)

    guess = int(input("Enter a number between 0-100: "))
    guesses=1
    rem_guesses=5

    if(num!=guess):
        while num!=guess:
            
            guesses += 1
            rem_guesses -=1
            if rem_guesses == 0:
                print("Game Over")
                quit()

            elif guess>100 or guess<0:
                print("Zada Kabil Mat Bano")
                guess=int(input("Enter a number between 0-100: "))

            else:
                if num>guess:
                    guess=int(input(f"{rem_guesses} trys left, please guess any larger number: "))

                else:
                    guess=int(input(f"{rem_guesses} trys left, please guess any smaller number: "))
        if guess==num:
            print("bingo")
    else:    
        print("Adbhoootttt..")

    print(f"Number of try = {guesses}")

if level.lower()=="e":
    easy()
elif level.lower()=="m":
    medium()
elif level.lower()=="h":
    hard()
else:
    print("Kya chahte ho??")
