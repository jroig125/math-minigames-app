import random


class Problem():
    def __init__(self, difficulty: str, type: str):
        self.difficulty = difficulty
        self.type = type
        problem = self.generate_question()
        self.problem = problem[0]
        self.answers = problem[1]
        self.correct_answer = problem[2]

    def generate_question(self):
        if self.type == 'Adding and Subtracting Integers':
            return add_subtract_integers(self.difficulty)

    def __str__(self):
        answer_labels = ['a', 'b', 'c', 'd', 'e']
        answer_text = ''
        for answer in range(len(self.answers)):
            answer_text += f'{answer_labels[answer]}. {self.answers[answer]}\n'

        correct_answer_text = f'Correct answer: {self.correct_answer}\n'

        return self.problem + answer_text + correct_answer_text


def generate_digit(difficulty):
    if difficulty == "easy":
        return random.randint(-5, 9)
    if difficulty == "medium":
        return random.randint(-9, 25)
    if difficulty == "hard":
        return random.randint(-20, 50)
    else:
        raise DifficultyNotDefinedError("Difficulty not yet defined.")


def add_subtract_integers(difficulty):
    digit_1 = generate_digit(difficulty)
    digit_2 = generate_digit(difficulty)
    problem = f'{digit_1} + {digit_2}\n'
    correct_answer = digit_1 + digit_2
    answers = asi_answer_gen(digit_1, digit_2, correct_answer)
    return problem, answers, correct_answer


# asi = add/subtract integers
def asi_answer_gen(digit_1, digit_2, correct_answer):
    # intentionally incorrect answers
    subtract_ans = digit_1 - digit_2
    flip_subtract_ans = digit_2 - digit_1
    negative_ans = -correct_answer
    add_one_ans = correct_answer + 1
    sub_one_ans = correct_answer - 1

    intentional_answers = {subtract_ans, flip_subtract_ans, negative_ans, add_one_ans, sub_one_ans}

    # all one more or one less than one of the intentionally incorrect answers
    distract_answers = set()
    for answer in intentional_answers:
        distract_answers.add(answer + 1)
        distract_answers.add(answer - 1)

    # likelihood for intentional incorrects is 75%; 25% for other distractions
    answers = set()
    answers.add(correct_answer)
    while len(answers) < 5:
        if random.random() < 0.75 and len(intentional_answers) > 0:
            answers.add(intentional_answers.pop())
        else:
            answers.add(distract_answers.pop())

    answers = list(answers)
    random.shuffle(answers)

    return answers


class DifficultyNotDefinedError(BaseException):
    pass


def main():
    difficulties = ['easy', 'medium', 'hard']
    for difficulty in difficulties:
        print(Problem(difficulty, 'Adding and Subtracting Integers'))


if __name__ == "__main__":
    main()