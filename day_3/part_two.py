file = open('Python/advent/day_3/input.txt')
content = file.readlines()
file.close()


#get the largest number between indices start and end
def get_largest(start, end):
    largestIndex = start
    
    for i in range(start,end):
        curr = int(line[i])
        
        #9 is the largest possible number
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
        
        # if this is the first iteration, start at 0.
        # if not, start at the latest index + 1
        start = 0
        if len(digit_indices) > 0:
            start = digit_indices[-1]+1
        
        # leave enough room for the number to have 12 digits 
        end = length-digits_left+1
        
        digit_indices.append(get_largest(start,end))
    
    #create a string from all of the logged indices
    numstring = ''
    for i in digit_indices:
        numstring += line[i]
        
    #convert the string to an int and add to total
    num = int(numstring)
    total += num

print(total)