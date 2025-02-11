import random 
import math
from brain_games.manual import run_game

GCD_INSTRRUCTION = "Find the greatest common divisor of given numbers."
MIN_INSTRRUCTION_LENGTH, MAX_INSTRRUCTION_LENGTH = 5, 10



def get_nums_and_gcd():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    nums = f"{num1} {num2}"
    gcd = math.gcd(num1, num2)
    return nums, str(gcd)


def run_gcd_game():
    run_game(get_nums_and_gcd, GCD_INSTRRUCTION)