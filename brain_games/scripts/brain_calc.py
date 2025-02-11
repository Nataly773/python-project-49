from brain_games.manual import run_game
from brain_games.games.calc import get_expression_and_answer
CALC_INSTRRUCTION = 'What is the result of the expression?'


def main():
    run_game(get_expression_and_answer, CALC_INSTRRUCTION)


if __name__ == "__main__":
    main()
