import random
MIN_INSTRRUCTION_LENGTH, MAX_INSTRRUCTION_LENGTH = 5, 10


def get_progression_and_miss_num():
    start, step = random.randint(1, 100), random.randint(1, 100)
    prog_length = random.randint(MIN_INSTRRUCTION_LENGTH, 
     MAX_INSTRRUCTION_LENGTH)
    miss_index = random.randint(0, prog_length - 1)
    progr = []
    for i in range(prog_length):  
        progr.append(start + step * i)
    missed_num = progr[miss_index]
    progr[miss_index] = ".."
    progr_with_miss_index = ' '.join(map(str, progr))
    return progr_with_miss_index, str(missed_num)





