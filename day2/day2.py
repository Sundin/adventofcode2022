print("Day 2")

def line_score(line):
    print(line)
    return points(line[2]) + result(line[2], line[0])

def points(me):
    if(me == "X"):
        return 1
    elif(me == "Y"):
        return 2
    elif(me == "Z"):
        return 3

def result(me, opponent):
    if(me == "X"):
        if(opponent=="A"):
            return 3
        elif(opponent=="B"):
            return 0
        elif(opponent=="C"):
            return 6
    elif(me == "Y"):
        if(opponent=="A"):
            return 6
        elif(opponent=="B"):
            return 3
        elif(opponent=="C"):
            return 0
    elif(me == "Z"):
        if(opponent=="A"):
            return 0
        elif(opponent=="B"):
            return 6
        elif(opponent=="C"):
            return 3


file1 = open('test.txt', 'r')
Lines = file1.readlines()
total = 0
for line in Lines:
    v = line.strip()
    if (v != ""):
        s = line_score(v)
        print(s)
        total +=s

print("TEST TOTAL: {}".format(total))

file1 = open('input.txt', 'r')
Lines = file1.readlines()
total = 0
for line in Lines:
    v = line.strip()
    if (v != ""):
        s = line_score(v)
        print(s)
        total +=s

print("TOTAL PART 1: {}".format(total))

## PART 2
print("#########")

def what_to_choose(result, opponent):
    if(result == "X"):
        if(opponent=="A"):
            return "Z"
        elif(opponent=="B"):
            return "X"
        elif(opponent=="C"):
            return "Y"
    elif(result == "Y"):
        if(opponent=="A"):
            return "X"
        elif(opponent=="B"):
            return "Y"
        elif(opponent=="C"):
            return "Z"
    elif(result == "Z"):
        if(opponent=="A"):
            return "Y"
        elif(opponent=="B"):
            return "Z"
        elif(opponent=="C"):
            return "X"

def line_score_2(line):
    print(line)
    me = what_to_choose(line[2], line[0])
    return points(me) + result(me, line[0])

file1 = open('test.txt', 'r')
Lines = file1.readlines()
total = 0
for line in Lines:
    v = line.strip()
    if (v != ""):
        s = line_score_2(v)
        print(s)
        total +=s

print("TEST TOTAL: {}".format(total))

file1 = open('input.txt', 'r')
Lines = file1.readlines()
total = 0
for line in Lines:
    v = line.strip()
    if (v != ""):
        s = line_score_2(v)
        print(s)
        total +=s

print("TOTAL PART 2: {}".format(total))