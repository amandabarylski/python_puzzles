import random
import itertools

#I started by declaring the two lists that I will be making randomized copies of.
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
index_numbers = [0, 1, 2, 3, 4, 5, 6]

def color_ordering_puzzle():
    #The first step was to create randomized lists that I could then use to generate the puzzle.
    #I also used the join method to create a solution string to check user input against.
    color_order = random.sample(colors, len(colors))
    solution = ", ".join(color for color in color_order)

    first_select = random.sample(index_numbers, len(index_numbers))
    second_select = random.sample(index_numbers, len(index_numbers))

    #Next I created an empty list to contain the generated hints.
    hints = []

    #Before starting the while loop with the puzzle-solving, I needed hints to show the user.
    #I used the zip function to pair up the index numbers from the first and second select lists.
    for i, j in zip(first_select, second_select):
        #To make the hints less predictable, I used random to select one of three options.
        option = random.choice([1, 2, 3])
        #Since some of my hint ideas had to do with where one color is in relation to another,
        #I made other hints for if an index number was paired up with itself.
        if i == j:
            if option == 1:
                if i == 0:
                    hints.append(f'{color_order[i]} is in the first position.')
                else:
                    hints.append(f'{color_order[i]} is not in the first position.')
            elif option == 2:
                if i == 6:
                    hints.append(f'{color_order[i]} is in the last position.')
                else:
                    hints.append(f'{color_order[i]} is not in the last position.')
            elif option == 3:
                if i == 3:
                    hints.append(f'{color_order[i]} is in the middle position.')
                elif i < 3:
                    hints.append(f'{color_order[i]} is before the middle postion.')
                elif i > 3:
                    hints.append(f'{color_order[i]} is after the middle postion.')
        else:
            #I made more nested if statements than I expected in order to produce better hints.
            #My first attempt was repetetive and probably unsolvable.
            if option == 1:
                if i < j:
                    hints.append(f'{color_order[i]} is before {color_order[j]}.')
                else:
                    hints.append(f'{color_order[i]} is after {color_order[j]}.')
            elif option == 2:
                if abs(i - j) == 1:
                    hints.append(f'{color_order[i]} is next to {color_order[j]}.')
                else:
                    hints.append(f'{color_order[i]} is {abs(i - j)} away from {color_order[j]}.')
            elif option == 3:
                if i == 0 or j == 0:
                    if abs(i - j) == 1:
                        hints.append(f'Either {color_order[i]} or {color_order[j]} is in the first position and they are next to each other.')
                    else:
                        hints.append(f'Either {color_order[i]} or {color_order[j]} is in the first position and they are not next to each other.')
                elif i == 6 or j == 6:
                    if abs(i - j) == 1:
                        hints.append(f'Either {color_order[i]} or {color_order[j]} is in the last position and they are next to each other.')
                    else:
                        hints.append(f'Either {color_order[i]} or {color_order[j]} is in the last position and they are not next to each other.')
                else:
                    hints.append(f'Neither {color_order[i]} nor {color_order[j]} is in the first or last position.')


    #With the hints generated and compiled into a list, they can be used in the game itself, contained in a while loop.
    #A couple of variables are needed as well to track whether the player has won and how many times they have guessed.
    win = False
    count = 0
    while count < 3 and not win:
        #A note for the player on how many guesses they have remaining
        print(f'You can guess {3 - count} more times.')
        #The list of hints
        for hint in hints:
            print(hint)
        #Rules on how to format the answer
        print('Make sure you separate each color with a comma and a single space, and spell them correctly!')

        #User input for the answer
        answer = input('Type your answer here:')

        #Checking the answer agains the solution, using .lower() in case the user typed any uppercase letters.
        #The count gets incremented no matter what, but win is switched to True if the answer is correct.
        if answer.lower() == solution:
            win = True
            count += 1
        else:
            count += 1
    
    if win:
        print(f'Congratulations! It took you {count} try/tries to reach the answer.')
    else:
        print(f'The solution was: {solution}. Better luck next time!')




    #This print function is my test print, which I alter the contents of to check that various aspects of the code work.
    #Commented out after it was no longer needed.
    # print(hints, solution)

#While working on elements that could become infinite loops, I commented out the function call as a precaution.
color_ordering_puzzle()