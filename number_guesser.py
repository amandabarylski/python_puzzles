import random

def number_guesser():
    #randint to get a whole number ranging from 1 to 1000
    num = random.randint(1, 1000)

    count = 0
    win = False

    while not win:
        guess = input("Guess a number from 1 to 1000:")
        #A try/except block to ensure that users enter a number, with the game contained inside
        try:
            guess = int(guess)
            if guess == num:
                win = True
            elif guess < num:
                print(f'The number is greater than {guess}.')
            elif guess > num:
                print(f'The number is smaller than {guess}.')
            #count goes up by one after each guess prior to checking for victory
            count += 1
    
            if win:
                print(f'Congratulations! It took you {count} {"try" if count == 1 else "tries"} to reach the number {num}.')
        except:
            print('Not a number, please try again!')


    
number_guesser()