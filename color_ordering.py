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
        option = random.choice([1, 2, 3])
        print(option)

    #This print function is my test print, which I alter the contents of to check that various aspects of the code work.
    print(solution)

#While working on elements that could become infinite loops, I commented out the function call as a precaution.
color_ordering_puzzle()