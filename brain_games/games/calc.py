import random 
MATH_SIGNS = ('+', '-', '*')

  
def get_expression_and_answer():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    math_signs = random.choice(MATH_SIGNS) 
    expression = f'{num1} {math_signs} {num2}'
    result = eval(expression)

    return expression, str(result)


