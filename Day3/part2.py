import regex as re
import numpy as np



class Number:
    start: tuple[int, int]
    end: tuple[int, int]
    value: int
    
    def __init__(self, start, end, num) -> None:
        self.start = start
        self.end = end    
        self.value = num
    
    def __repr__(self) -> str:
        return f"{self.value} {self.start} {self.end}"

class possibleGear:
    def __init__(self, x, y, num) -> None:
        self.x = x
        self.y = y
        self.num = int(num)
        self.matches = 1
        self.ratio = int(num)
    def check(self, x, y, num):
        if self.x == x and self.y == y:
            self.matches += 1
            self.ratio *= int(num)
            return True
        
            



partNums = []
possibleGears = []

map = []

diftotal = 0
charSet = set()

def checkNum(num:Number) -> bool:
    global diftotal, charSet, map, gearRatioTotal, possibleGears
    #print(num)
    for i in range(num.start[0]-1, num.end[0]+2):
        if int(num.value) == 1:
            print(f"row {i}")
        for j in range(num.start[1]-1, num.end[1]+2):
            if i < 0 or j < 0: continue
            try:
                val = map[i][j]
                if not str(val).isnumeric() and val != ".":
                    #print(f"accepted {val}")
                    
                    if val == "*":
                        for gear in possibleGears:
                            a = gear.check(i, j, num.value)
                            if a:
                                break
                        possibleGears.append(possibleGear(i, j, num.value))
                    diftotal = int(num.value) + diftotal
                    charSet.add(val)
                    #print(diftotal)
                    return True
            except:
                pass
    print(f"Faild {num}")
    

def checkGear(x, y):
    global map, partNums
    matches = []
    for num in partNums:
        newNum = False
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i in range(num.start[0], num.end[0]+1) and j in range(num.start[1], num.end[1]+1):
                    matches.append(int(num.value))
                    newNum = True
                    break
            if newNum: break
        
                    
    print(matches, len(matches))
    if len(matches) == 2:
        return np.prod(matches)
    
        

with open("Day3/input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        map.append(list(line))
        array = re.findall(r'[0-9]+', line)
        last = 0
        for num in array:
            if num == "1":
                print(last)
            start = line.find(num, last)
            n = Number((i, start), (i, start+len(str(num))-1), num)
            partNums.append(n)
            last = start+len(str(num))

partNums = list(filter(checkNum, partNums))
total = 0
for num in partNums:
    #print(num)
    total += int(num.value)

total = 0
for i, row in enumerate(map):
    for j, symbol in enumerate(row):
        if symbol == "*":
            ratio = checkGear(i, j)
            i ratio: total += ratiof
            
print(total)
