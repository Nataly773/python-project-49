from random import randint


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = randint(0, 100)
    answer = "yes" if is_even(question) else "no"
    return question, answer

