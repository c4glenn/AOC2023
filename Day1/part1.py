def findFirst(string, num):
    for char in string[::num]:
        try:
            int(char)
            return char
        except:
            continue
    


with open("Day1/input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        total += int(str(findFirst(line, 1)) + str(findFirst(line, -1)))
    print(total)
        