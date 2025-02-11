from brain_games.manual import run_game
from brain_games.games. even import get_question_and_answer
EVEN_INSTRRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(get_question_and_answer, EVEN_INSTRRUCTION)
    
 
if __name__ == "__main__":
    main()
