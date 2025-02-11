from brain_games.manual import run_game
from brain_games.games.gcd import get_nums_and_gcd
GCD_INSTRRUCTION = "Find the greatest common divisor of given numbers."


def main():
    run_game(get_nums_and_gcd, GCD_INSTRRUCTION)
 
if __name__ == "__main__":
    main()