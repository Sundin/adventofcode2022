print("Day 1")

file1 = open('input.txt', 'r')
Lines = file1.readlines()

totals = []
current = 0
# Strips the newline character
for line in Lines:
    v = line.strip()
    #print("{}".format(v))
    if (v == ""):
        print(current)
        totals.append(current)
        current = 0
    else:
        current += int(v)

print(current)
totals.append(current)

max = 0
for t in totals:
    if (t > max):
        max = t

print("MAX: {}".format(max))

totals.remove(max)

max2 = 0
for t in totals:
    if (t > max2):
        max2 = t
totals.remove(max2)

max3 = 0
for t in totals:
    if (t > max3):
        max3 = t

topthree = max + max2 + max3

print("TOP THREE: {}".format(topthree))
