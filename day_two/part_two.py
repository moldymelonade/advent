file = open('Python/advent/day_two/input.txt', 'r')
ranges = file.read().split(',')
total = 0


#return if the chunk of specified length loops in id 
def looping_chunk(id, chunk_length):
    
    #the model chunk to compare against
    check = id[:chunk_length]
    max_chunks = int(len(id)/chunk_length)
    
    #loop through all possible chunks of this string
    for chunk_number in range(1,max_chunks):
        
        #get the starting position of the chunk in id
        start = chunk_number*chunk_length
        chunk = id[start:start+chunk_length]
        
        if chunk != check:
            return False
        
    #if all chunks match the model, return True
    return True


#return if the specified id is valid
def is_valid(id):
    id = str(id)
    length = len(id)
    
    #loop through all possible factors of the length of the id
    for factor in range(1,int(length/2)+1):
        
        #if it's not a valid factor, skip this iteration 
        if length%factor!=0:
            continue
        
        if looping_chunk(id, factor):
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