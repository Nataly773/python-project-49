import random 
from brain_games.manual import run_game
from brain_games.const import CALC_INSTRRUCTION, MATH_SIGNS 

  
def get_expression_and_answer():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_signs = random.choice(MATH_SIGNS) 
    expression = f'{num1} {math_signs} {num2}'
    result = eval(expression)

    return expression, str(result)


def run_calc_game():
    run_game(get_expression_and_answer, CALC_INSTRRUCTION)
