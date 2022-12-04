print("Day 4")

def helper(elf1, elf2):
    start = int(elf1.split("-")[0])
    stop = int(elf1.split("-")[1])+1

    start2 = int(elf2.split("-")[0])
    stop2 = int(elf2.split("-")[1])+1

    for x in range(start, stop):
        if x not in range(start2, stop2):
            return False
    
    return True

def is_fully_covered(line):
    elf1 = line.split(",")[0]
    elf2 = line.split(",")[1]
    return helper(elf1, elf2) or helper(elf2, elf1)


def solve_input_file(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    total = 0
    for line in Lines:
        v = line.strip()
        if (is_fully_covered(v)):
            total +=1
    return total

part1 = solve_input_file("input.txt")
print("PART 1: {}".format(part1))

def helper_2(elf1, elf2):
    start = int(elf1.split("-")[0])
    stop = int(elf1.split("-")[1])+1

    start2 = int(elf2.split("-")[0])
    stop2 = int(elf2.split("-")[1])+1

    for x in range(start, stop):
        if x in range(start2, stop2):
            return True
    
    return False

def overlap(line):
    elf1 = line.split(",")[0]
    elf2 = line.split(",")[1]
    return helper_2(elf1, elf2)

def part2(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    total = 0
    for line in Lines:
        v = line.strip()
        if (overlap(v)):
            total +=1
    return total

part2 = part2("input.txt")
print("PART 2: {}".format(part2))