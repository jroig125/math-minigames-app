'''
Later Ideas
1. Adaptive difficulties
2. Competitive (Timed) Mode
'''

from problem import Problem

def game(difficulty):
    print(f'{difficulty} difficulty selected.')
    print('Current topic is Adding and Subtracting Integers.')
    print('Current mode is practice.')
    # TODO: (maybe use prototype) Option to enter number of problems desired or infinite with manual exit
    # TODO: Produce correct number of problems using for loop
    # TODO: Accept answers by letter or number
    # TODO: Return whether individual answer is correct or incorrect
    # TODO: Return stats at the end


def main():
    print("Hello! Welcome to Math Minigames!")

    waiting = True
    difficulties = ['e', 'm', 'h']
    while waiting:
        difficulty = input("Please select a difficulty: [e]asy, [m]edium, or [h]ard, or enter q to quit.\n")
        if difficulty in difficulties:
            game(difficulty)
        elif difficulty == 'q':
            # TODO: Return daily stats
            print("See you next time!")
            waiting = False
        else:
            print("Please enter e, m, or h to choose your difficulty.")


if __name__ == "__main__":
    main()