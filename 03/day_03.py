import sys


def EvaluateJoltage(bank):
    a = max(bank[:-1])
    i = bank.find(a, 0, len(bank))
    b = max(bank[i + 1:])
    return a + b

def GreedyEvaluateJoltage(bank, free_batteries):
    window = len(bank) - free_batteries + 1 
    a = max(bank[:window])
    i = bank.find(a, 0, window)
    if free_batteries == 1:
        return a
    else:
        return a + GreedyEvaluateJoltage(bank[i + 1:], free_batteries - 1)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    total_joltage = sum([int(GreedyEvaluateJoltage(bank, 12)) for bank in lines])
    print(total_joltage)
