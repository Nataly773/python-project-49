from brain_games.manual import run_game
from brain_games.games.progression import get_progression_and_miss_num
PROGRRESSION_INSTRRUCTION = 'What number is missing in the progression?'


def main():
    run_game(get_progression_and_miss_num, PROGRRESSION_INSTRRUCTION)

 
if __name__ == "__main__":
    main()