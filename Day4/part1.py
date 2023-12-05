def score(winingNums, nums):
    count = 0
    for num in nums:
        if num in winingNums: count += 1 
    return 2 ** (count-1) if count else 0


with open("Day4/input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        line = line.strip()[line.index(":")+1:]
        wining, nums = line.split("|")
        wining = [int(x) for x in wining.split(" ") if x]
        nums = [int(x) for x in nums.split(" ") if x]
        total += score(wining, nums)
print(total)
