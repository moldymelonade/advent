
# return the absolute distance the dial should turn
def absolute_rotation(line):
    #determines direction
    mult = 1
    if line[0] == 'L':
        mult = -1
        
    distance = int(line[1:])
    return (mult*distance)


def part_one():
    count = 0
    dial_ptr = 50
    file = open('Python/advent/day_one/input.txt', 'r')
    for line in file:
        distance = absolute_rotation(line)
        
        #turn the dial the specified distance
        dial_ptr += distance
        
        # round pointer to the actual position of the dial
        dial_ptr %= 100
        
        #increment if on zero
        if dial_ptr == 0:
            count+=1
    file.close()
    return count


def part_two():
    count = 0
    dial_ptr = 50
    file = open('Python/advent/day_one/input.txt', 'r')
    for line in file:
        start = dial_ptr
        distance = absolute_rotation(line)
        
        # turn the dial the specified distance 
        dial_ptr += distance
        
        # left turns require an extra increment when zero is crossed
        # when dial starts at zero, do not increment.
        if dial_ptr <= 0 and start != 0:
            count+=1

        # determines how many times zero was crossed in turn
        count+=abs(dial_ptr)//100
        
        # round pointer to the actual position of the dial
        dial_ptr %= 100
    file.close()
    return count


print(f'part one answer: {part_one()}')
print(f'part two answer: {part_two()}')