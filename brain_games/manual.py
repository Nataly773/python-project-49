import prompt
from brain_games.const import number_of_rounds


def run_game(get_question_and_answer, instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f"Hello, {name}!\n"
          f'{instruction}')
    for i in range(number_of_rounds):
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\n'
                                    f'Your answer: ')
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}''.\n"
                  f"Let's try again, {name}!")
                  
            return
    print(F"Congratulations, {name}!")