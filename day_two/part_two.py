file = open('Python/advent/day_two/input.txt', 'r')
ranges = file.read().split(',')
total = 0


#return if the specified id is valid
def is_valid(id):
    id = str(id)
    length = len(id)
    
    #loop through all possible factors of the length of the id
    for factor in range(1,int(length/2)+1):
        
        #if it's not a valid factor, skip this iteration 
        if length%factor!=0:
            continue
        
        check = id[:factor]
        max_chunks = int(len(id)/factor)
        
        #if id is made up of one looping chunk
        if id == (check*max_chunks):
            return False
    return True
    
    
# determine the starting and ending number for each range of valid IDs
for num_range in ranges:
    nums = num_range.split('-')
    start = int(nums[0])
    end = int(nums[1])
    
    #loop through all numbers in the range
    #add to total if invalid
    for i in range(start,end+1):
        if not(is_valid(i)):
            total += i

print(total)