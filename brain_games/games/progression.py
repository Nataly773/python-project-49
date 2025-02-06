import random
from brain_games.manual import run_game
from brain_games.const import progression_instruction, min_progression_length,\
      max_progression_length 


def get_progression_and_miss_num():
    start, step = random.randint(1, 100), random.randint(1, 100)
    prog_length = random.randint(min_progression_length, max_progression_length)
    miss_index = random.randint(0, prog_length - 1)
    progr = []
    for i in range(prog_length):  
        progr.append(start + step * i)
    missed_num = progr[miss_index]
    progr[miss_index] = ".."
    progr_with_miss_index = ' '.join(map(str, progr))
    return progr_with_miss_index, str(missed_num)


def run_progression_game():
    run_game(get_progression_and_miss_num, progression_instruction)



