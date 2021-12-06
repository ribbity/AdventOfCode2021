def part1():
    with open('./input.txt') as f:
        lines = f.readlines()
        depthIncreases = 0
        prevDepth = lines[0]
        for line in lines:
            if line >= prevDepth:
                depthIncreases += 1
            prevDepth = line
        print("Measurements increases: ", str(depthIncreases))

def windowSum(l: list, index: int) -> int:
    return int(l[index].strip()) + int(l[index + 1].strip()) + int(l[index + 2].strip())

def part2():
    with open('./input.txt') as f:
        lines = f.readlines()
        increases = 0
        if len(lines) >= 3:
            prevWindow = windowSum(lines,0)
            for i in range(1,len(lines)-1):
                try:
                    thisWindow = windowSum(lines, i)
                    if thisWindow > prevWindow:
                        increases += 1
                    prevWindow = thisWindow
                except:
                    break
    print("Window measurement increases:", increases)

part1()
part2()