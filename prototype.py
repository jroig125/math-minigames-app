import random
import time


class DifficultyNotDefinedError(BaseException):
    pass


def generate_digit(difficulty):
    if difficulty == "easy":
        return random.randint(0, 9)
    if difficulty == "medium":
        return random.randint(0, 25)
    if difficulty == "hard":
        return random.randint(-20, 50)
    else:
        raise DifficultyNotDefinedError("Difficulty not yet defined.")


def countdown(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)
    print("Go!\n")


def main():
    difficulties = ['easy', 'medium', 'hard']
    intro = f"Welcome to practice mode. Choose your difficulty: {difficulties}.\n"
    difficulty = input(intro).lower()

    while difficulty not in difficulties:
        difficulty = input(f"Please enter {difficulties}.\n").lower()

    is_ready = input(f"Mode set to {difficulty}. Press enter when ready.\n")
    while is_ready:
        is_ready = input("Press enter when ready.\n")

    countdown(3)

    start_time = time.time()
    amount_correct = 0
    for i in range(10):
        digit_1 = generate_digit(difficulty)
        digit_2 = generate_digit(difficulty)
        correct_answer = digit_1 + digit_2

        user_answer = int(input(f'{digit_1} + {digit_2}\n'))

        if user_answer == correct_answer:
            print("Correct!")
            amount_correct += 1
        else:
            print("Incorrect.")
    elapsed_time = round(time.time() - start_time)
    print(f'You got {amount_correct} correct out of 10. It took you {elapsed_time} seconds.')


if __name__ == "__main__":
    main()
