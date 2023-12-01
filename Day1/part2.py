options = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

def findFirst(string: str):
    bestIndex = len(string) + 1
    bestOption = ""
    for option, val in options.items():
        ind = string.find(option)
        if ind == -1: continue
        if ind < bestIndex:
            bestIndex = ind
            bestOption = val
    print(line, bestIndex, bestOption)
    return bestOption

def findLast(string: str):
    bestIndex = -1
    bestOption = ""
    for option , val in options.items():
        ind = string.rfind(option)
        if ind == -1: continue
        if ind > bestIndex:
            bestIndex = ind
            bestOption = val
    return bestOption


with open("Day1/input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        num = int(str(findFirst(line)) + str(findLast(line)))
        print(num)
        total += num
    print(total)
        