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
    line = line.strip()
    length = len(line)
    
    # get largest number.
    # make sure to leave enough space to form a two digit number.
    largest = get_largest(0,length-1)
    second = get_largest(largest+1, length)
    
    #convert number string to int
    num = int(line[largest] + line[second])
    
    total += num
    
print(total)