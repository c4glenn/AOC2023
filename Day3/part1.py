import regex as re



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
        



partNums = []

map = []

diftotal = 0
charSet = set()

def checkNum(num:Number) -> bool:
    global diftotal, charSet, map
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
                    diftotal = int(num.value) + diftotal
                    charSet.add(val)
                    #print(diftotal)
                    return True
            except:
                pass
    print(f"Faild {num}")
        

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

sybmolSet = set()

for row in map:
    for symbol in row:
        sybmolSet.add(symbol)
    
print(total, diftotal, sybmolSet.difference(charSet), charSet)