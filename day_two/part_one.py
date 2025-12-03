file = open('Python/advent/day_two/input.txt', 'r')
ranges = file.read().split(',')
total = 0

#return if the specified id is valid
def is_valid(id):
    id = str(id)
    
    # a number with an uneven length has to be valid
    if len(id)%2 == 1:
        return True
    
    half = int(len(id)/2)
    #check if the first half equals the last half
    if id[:half] == id[half:]:
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