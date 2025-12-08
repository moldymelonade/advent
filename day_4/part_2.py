file = open('Python/advent/day_4/input.txt')
content = file.readlines()
file.close()

check = [
    [-1,-1],[0,-1],[1,-1],
    [-1, 0],       [1, 0],
    [-1, 1],[0, 1],[1, 1]
]

file_len = len(content)
line_len = len(content[0].strip())

total = 1

changed = -1
while changed != 0:
    total += changed
    changed = 0

    log = two_d_array = [[0] * line_len for _ in range(file_len)]

    def increment(x,y):
        for offset in check:
            xPos = x + offset[0]
            yPos = y + offset[1]
            if xPos >= line_len or xPos < 0:
                continue
            if yPos >= file_len or yPos < 0:
                continue
            log[xPos][yPos]+=1


    for x in range(file_len):
        for y in range(line_len):
            if content[x][y] == '.':
                log[x][y] = 4
                continue
            increment(x,y)


    for i in range(len(log)):
        for j in range(len(log[0])):
            if log[i][j] < 4 :
                content[i] = content[i][:j] + '.' + content[i][j+1:]
                changed+=1


print(total)