dial_ptr = 50
file = open('Python/advent/day_one_input.txt', 'r')
count = 0

for line in file:
    mult = 1
    if line[0] == 'L':
        mult = -1
    distance = int(line[1:])
    dial_ptr += (mult*distance)
    dial_ptr %= 100
    if dial_ptr == 0:
        count+=1

file.close()
print(count)