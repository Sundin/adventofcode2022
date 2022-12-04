print("Day 3")


def find_letter(line):
    length = len(line)
    split_here = length // 2
    half1 = line[0:split_here]
    half2 = line[split_here:length]
    for c in half1:
        if c in half2:
            return c

def get_priority(letter):
    all = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return all.find(letter)

def solve(line):
    letter = find_letter(line)
    return get_priority(letter)

def solve_input_file(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    total = 0
    for line in Lines:
        v = line.strip()
        if (v != ""):
            s = solve(v)
            #print(s)
            total +=s
    return total

part1 = solve_input_file("input.txt")
print("PART 1: {}".format(part1))

def find_badge(elf1, elf2, elf3):
    for c in elf1:
        if c in elf2:
            if c in elf3:
                return c

def sum_badges(filename):
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    total = 0
    for x in range(0, len(Lines), 3):
        badge = find_badge(Lines[x], Lines[x+1], Lines[x+2])
        total += get_priority(badge)
    return total

part2 = sum_badges("input.txt")
print("PART 2: {}".format(part2))