def part1():
    total = 0
    for inp in inputVals:
        for i in range(1, len(inp)):
            if horizontalSplit(inp, i):
                total += 100 * i
                break

        for i in range(1, len(inp[0])):
            if verticalSplit(inp, i):
                total += i
                break

    print("Part 1:", total)

def part2():
    total = 0
    for inp in inputVals:
        for i in range(1, len(inp)):
            if horizontalSplitSmudge(inp, i):
                total += 100 * i
                break

        for i in range(1, len(inp[0])):
            if verticalSplitSmudge(inp, i):
                total += i
                break
    print("Part 2:", total)

def horizontalSplit(inp, rowsAbove):
    below = inp[rowsAbove:]
    above = inp[:rowsAbove][::-1]
    for i in range(min(len(below), len(above))):
        for j in range(len(below[0])):
            if below[i][j] != above[i][j]:
                return False
    return True

def verticalSplit(inp, colsLeft):
    for i in inp:
        left = i[:colsLeft][::-1]
        right = i[colsLeft:]
        for j in range(min(len(left), len(right))):
            if left[j] != right[j]:
                return False
    return True

def horizontalSplitSmudge(inp, rowsAbove):
    below = inp[rowsAbove:]
    above = inp[:rowsAbove][::-1]
    corrected = 0
    for i in range(min(len(below), len(above))):
        for j in range(len(below[0])):
            if below[i][j] != above[i][j]:
                corrected += 1
                if corrected != 1:
                    return False
    return corrected == 1

def verticalSplitSmudge(inp, colsLeft):
    corrected = 0
    for i in inp:
        left = i[:colsLeft][::-1]
        right = i[colsLeft:]
        for j in range(min(len(left), len(right))):
            if left[j] != right[j]:
                corrected += 1
                if corrected != 1:
                    return False
    return corrected == 1

inputVals = []
cur = []
f = open("advent13.txt")
for line in f:
    if line == "\n":
        inputVals.append(cur)
        cur = []
    else:
        line = line.replace("\n", "")
        cur.append(line)
inputVals.append(cur)


part1()
part2()