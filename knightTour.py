def isSafe(n,board,x,y):
    #checking if the co-ordinates are not out of range and if co-ordinates are not visited
    if (x>=0 and y>=0 and x<n and y<n and board[x][y] == -1):
        return True
    return False

def knightTour(n):
    board = [[-1]*n for i in range(n)]#initialising the whole board to -1
    possibleMove(n,board,0,0,0)
    for i in board:
        print(i)

def possibleMove(n,board,x,y,counter):
    if counter == n**2:#checking if 5*5 boxes are visited
        return True
    if isSafe(n,board,x,y):
        board[x][y] = counter#assigning each visited cell to the number of steps
        #A knight can have 8 (x,y) possible moves
        x_possible = [2, 1, -1, -2, -2, -1, 1, 2]
        y_possible = [1, 2, 2, 1, -1, -2, -2, -1]
        for x_move,y_move in zip(x_possible,y_possible):#iterates through the lists and results in (x,y) co-ordinates
            if possibleMove(n, board, x+x_move, y+y_move, counter+1):#recursive call for next move
                return True
        #if the 8 possible moves are not possible, set the current cell to -1
        board[x][y] = -1
        return False

knightTour(5)