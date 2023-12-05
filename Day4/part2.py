class Card:
    def __init__(self, number, winingNums, nums) -> None:
        self.number = number
        self.winingNums = winingNums
        self.nums = nums
        self.next = self.count()
        
    
    def count(self):
        count = 0
        for num in self.nums:
            if num in self.winingNums: count += 1 
        return count

cards = []
numsOfCards = []

with open("Day4/input.txt", "r") as f:
    for line in f.readlines():
        number = int(line[line.index(" "):line.index(":")])
        line = line.strip()[line.index(":")+1:]
        wining, nums = line.split("|")
        wining = [int(x) for x in wining.split(" ") if x]
        nums = [int(x) for x in nums.split(" ") if x]
        cards.append(Card(number, wining, nums))
        numsOfCards.append(1)

for card in cards:
    start = card.number + 1
    end = card.number + card.next + 1
    for i, num in enumerate(numsOfCards):
        i = i + 1
        if i in range(start, end):
            numsOfCards[i-1] += numsOfCards[card.number-1]

print(numsOfCards, sum(numsOfCards))
            
