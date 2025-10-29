import random 

def guess_no():
    guess = random.randint(1, 10)
    attempts = 0 
    max_attempts = 5
    print("Welcome in the Guess the number game:)")
    while True:
        try:
            guess_no = int(input("Guess the number between 1 to 10: "))
            attempts+=1
            if guess_no < guess :
                print("It is Too low!")
            elif guess_no > guess:
                print("It is Too high!")
            else:
                print(f"Congratulations! You've guessed the correct number {guess} in {attempts} attempts.")
            break
        except ValueError:
            print("Please enter a valid number.")

            if attempts == max_attempts:
                print(f"Sorry!! You have passed your all{attempts}from{max_attempts}")
            else:
                print("Wrong!")
guess_no()
