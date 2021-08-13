board = [
    [1,0,0,4,8,9,0,0,6],
    [7,3,0,0,0,0,0,4,0],
    [0,0,0,0,0,1,2,9,5],
    [0,0,7,1,2,0,6,0,0],
    [5,0,0,7,0,3,0,0,8],
    [0,0,6,0,9,5,7,0,0],
    [9,1,4,6,0,0,0,0,0],
    [0,2,0,0,0,0,0,3,7],
    [8,0,0,5,1,2,0,0,4]
]
def solve(bo):  #using recurssion
    print(bo)
    find = find_empty(bo) #once we reach the last end bloack that means we finished finding the solution
    if not find: 
         return True #returning true cuz this means we have found the solution
    else: 
        row, col = find

    for i in range(1,10):
        if findvalid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
                             


def findvalid(bo, num, pos):

    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range (len(bo)):
        if bo[i][pos[1]] == num and pos[0 ] != i :
            return False 

    #check box
    box_x = pos[1]  // 3
    box_y = pos[0]  // 3

    for i in range(box_y * 3 , box_y*3 + 3):  
        for j in range(box_x * 3 , box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True



def print_board(bo):

    for i in range (len(bo)):
        if i % 3 == 0 and i!=0:
            print("- - - - - - - - -")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j !=0:   #so that a line won't be print immediately on the left
                print ("|", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+ " ", end ="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range (len(bo[0])):    # this one is for the legth of each rowrow empty space"0
            if bo[i][j] == 0:           # to check if that position is zero
                return (i,j) #row, col
    return None  #if theres no empty squares

print_board(board)
solve(board)
print(" ________________")
print_board(board)
                