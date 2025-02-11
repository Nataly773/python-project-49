import random 


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
        
    return True


def get_num_and_prime_ans():
    number = random.randint(1, 100)
    answer = 'yes' if is_prime(number) else 'no'
    return number, answer

