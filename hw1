import time

def divide_by_six(integerlist):
    """ This function outputs a list where, if the integer on
    the input list is divisible by six, the corresponding
    output is 1 else the output is 0 """
    return list(map(lambda x: int((x/6).is_integer()), integerlist))

total_time= []
TRIALS = 100
ARRAY_SIZE = 2000
for x in range(TRIALS):
    start_time = time.time()
    print(divide_by_six([i for i in range(ARRAY_SIZE)]))
    total_time.append(time.time() - start_time)

print(sum(total_time) / len(total_time))

