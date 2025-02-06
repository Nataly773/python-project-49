import random 
from brain_games.manual import run_game
from brain_games.const import prime_instruction


def is_prime(num):
    if num <2:
         return False

    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return True


def get_num_and_prime_ans():
    number = random.randint(1,100)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer


def run_prime_game():
    run_game(get_num_and_prime_ans,prime_instruction)