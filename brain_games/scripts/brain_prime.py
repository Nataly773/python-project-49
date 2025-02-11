from brain_games.manual import run_game
from brain_games.games.prime import get_num_and_prime_ans
PRIME_INSTRRUCTION = 'Answer "yes" if given number is prime. Otherwise answer \
"no".'


def main():
    run_game(get_num_and_prime_ans, PRIME_INSTRRUCTION)
    
 
if __name__ == "__main__":
    main()