import random 
import math
MIN_INSTRRUCTION_LENGTH, MAX_INSTRRUCTION_LENGTH = 5, 10


def get_nums_and_gcd():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    nums = f"{num1} {num2}"
    gcd = math.gcd(num1, num2)
    return nums, str(gcd)


