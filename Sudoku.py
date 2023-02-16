# Edit the list below to change the board

board = [[2,8,0,0,9,7,3,0,0],
         [4,0,7,0,3,0,8,0,0],
         [0,3,5,0,0,8,0,0,6],
         [0,0,0,0,1,3,0,8,0],
         [8,0,1,0,0,0,5,0,7],
         [0,5,0,7,8,0,0,0,0],
         [3,0,0,8,0,0,7,2,0],
         [0,0,8,0,2,0,4,0,3],
         [0,0,4,3,7,0,0,5,8]]

##---------------------------------------------------    

# Takes an input number and cell, then checks to see if the number is a valid play
def validate(bo, num, pos):
    
    # Checks the 3x3 set the currently selected cell is in
    boundY = (pos[0]//3)*3
    boundX = (pos[1]//3)*3 
    for j in range(boundY, boundY + 3):
        for i in range(boundX, boundX + 3):
            if bo[j][i] == num and (j,i) != pos:
                return False
    
    # Checks the column the currently selected cell is in
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Checks the row the currently selected cell is in
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
                       
    return True
 
         
# Searches for the next available empty cell (signified by 0)
def search(bo):
    for i in range(len(bo)):
        for j in range (len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

# Iterates through each empty cell and tries numbers 1~9 until a valid play is made
# If it is stuck and no more valid moves are possible, it will revert the previous cell to 0 and try again with a different number
# This will repeat until the board is solved
def solve(brd):

    coords = search(brd)
    if coords == None:
        return True
        
    for x in range(1,10):
        if validate(brd, x, (coords[0], coords[1])):
            brd[coords[0]][coords[1]] = x
            
            if solve(brd):
                return True
                
            brd[coords[0]][coords[1]] = 0
            
    return False

##---------------------------------------------------  

# Prints the board before and after solving
print("Board:")
for x in board:
    print(x)

print("---------------------------")
solve(board)

print("Solution:")
for x in board:
    print(x)

print("---------------------------")
exit = input("\nPress any key to quit...")
