file = open('Python/advent/day_3/input.txt')
content = file.readlines()
file.close()


def get_largest(start, end):
    largestIndex = start
    for i in range(start,end):
        curr = int(line[i])
        if curr == 9:
            largestIndex = i
            break
        if curr > int(line[largestIndex]):
            largestIndex = i
    return largestIndex


total = 0
for line in content:
    digit_indices = []
    line = line.strip()
    length = len(line)
    for digits_left in range(12,0,-1):
        start = 0
        if len(digit_indices) > 0:
            start = digit_indices[-1]+1
        end = length-digits_left+1
        digit_indices.append(get_largest(start,end))
    numstring = ''
    for i in digit_indices:
        numstring += line[i]
    num = int(numstring)
    print(num)
    total += num
print(total)