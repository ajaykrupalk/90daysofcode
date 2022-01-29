n = 9

#checking for cells which are empty or simply just have the value zero
def isEmpty(arr,l):
    for row in range(n):
        for col in range(n):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

#checking if the number is already present in the column
def isColSafe(grid,i,j,num):
    for col in range(n):
        if grid[i][col]==num:
            return False
    return True

#checking if the number is already present in the row
def isRowSafe(grid,i,j,num):
    for row in range(n):
        if grid[row][j]==num:
            return False
    return True

#checking if the number is present in the 3*3 box
def isBoxSafe(grid,i,j,num):
    for r in range(3):
        for c in range(3):
            if grid[i+r][j+c] == num:
                return False
    return True

#checking if the placement of number satisfies all conditions
def isCellSafe(grid,row,col,num):
    return isColSafe(grid,row,col,num) and isRowSafe(grid,row,col,num) and isBoxSafe(grid,row-row%3,col-col%3,num)

#solve the sudoku problem
def solve(grid):
    l = [0,0]

    if (not isEmpty(grid,l)):
        return True
    
    row = l[0]
    col = l[1]

    for num in range(1,10):
        if isCellSafe(grid,row,col,num):#if all conditions are satisfied
            grid[row][col] = num#assign a number to the current cell

            if solve(grid):#recursive call for the next empty cell
                return True

            grid[row][col] = 0#backtracking
    
    return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

if solve(grid):
    for i in grid:
        print(i) 
else:
    print("Solution does not exist")