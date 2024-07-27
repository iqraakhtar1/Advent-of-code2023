with open("advent9.txt", "r") as file:
    data = file.read()

def next_nums(nums):
    new_nums = []
    for i in range(len(nums) - 1):
        new_nums.append(nums[i + 1] - nums[i])
    return new_nums

ans = 0
for line in data.splitlines():
    nums = [int(n) for n in line.split()]
    table = [nums]
    while True:
        new_nums = next_nums(nums)
        table.append(new_nums)
        if new_nums.count(0) == len(new_nums):
            break
        nums = new_nums

    table[-1].append(0)
    for r in range(len(table) - 2, -1, -1):
        table[r].append(table[r][-1] + table[r + 1][-1])
    ans += table[0][-1]

print(ans,"part 1")

ans = 0
for line in data.splitlines():
    nums = [int(n) for n in line.split()]
    table = [nums]
    while True:
        new_nums = next_nums(nums)
        table.append(new_nums)
        if new_nums.count(0) == len(new_nums):
            break
        nums = new_nums

    table[-1].insert(0, 0)
    for r in range(len(table) - 2, -1, -1):
        table[r].insert(0, table[r][0] - table[r + 1][0])
    ans += table[0][0]

print(ans, "part 2")