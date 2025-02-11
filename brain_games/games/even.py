from random import randint
from brain_games.manual import run_game

EVEN_INSTRRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = randint(0, 100)
    answer = "yes" if is_even(question) else "no"
    return question, answer


def run_even_game():
    run_game(get_question_and_answer, EVEN_INSTRRUCTION)