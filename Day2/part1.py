colorMax = {
    "red":12,
    "green":13,
    "blue":14
}

with open("Day2/input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        
        idnum = line[line.find("Game ")+5:line.find(":")]
        
        games = line[line.find(":")+1:].split(";")
        gameworks = True
        for game in games:
            draws = game.split(",")
            for draw in draws:
                draw = draw.strip()
                if int(draw[:draw.find(" ")]) > colorMax.get(draw[draw.find(" ") + 1:], 0):
                    gameworks = False
                    break
        if(gameworks): print(idnum, line) 
        total += int(idnum) if gameworks else 0
        
print(total)