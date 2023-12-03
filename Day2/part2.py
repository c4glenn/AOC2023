with open("Day2/input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()
        colorMax = {
            "red":0,
            "green":0,
            "blue":0
        }

        idnum = line[line.find("Game ")+5:line.find(":")]
        
        games = line[line.find(":")+1:].split(";")
        gameworks = True
        for game in games:
            draws = game.split(",")
            for draw in draws:
                draw = draw.strip()
                if int(draw[:draw.find(" ")]) > colorMax.get(draw[draw.find(" ") + 1:], 0):
                    colorMax[draw[draw.find(" ") + 1:]] = int(draw[:draw.find(" ")])
        power = colorMax["red"] * colorMax["blue"] * colorMax["green"]
        total += power
print(total)