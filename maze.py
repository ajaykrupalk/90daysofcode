n = 4

def isSafe(maze, i, j,visited):
    if (i == -1 or i==n or j==-1 or j==n or visited[i][j] or maze[i][j] == 0):
        return False

    return True

def solveMaze(maze, x, y, path, possiblePath, visited):
    if x == n-1 and y==n-1:
        possiblePath.append(path)
        return

    visited[x][y]=True

    if isSafe(maze,x+1,y,visited):
        path += "D"
        solveMaze(maze,x+1,y,path,possiblePath, visited)
        path = path[:-1]

    if isSafe(maze,x,y-1,visited):
        path += "L"
        solveMaze(maze,x,y-1,path,possiblePath,visited)
        path = path[:-1]

    if isSafe(maze,x,y+1,visited):
        path += "R"
        solveMaze(maze,x,y+1,path,possiblePath,visited)
        path = path[:-1]

    if isSafe(maze,x-1,y,visited):
        path += "U"
        solveMaze(maze,x-1,y,path,possiblePath, visited)
        path = path[:-1]
     
    visited[x][y] = False

def solve(maze):
    path = ""
    possiblePath = []
    visited = [[False]*n for i in range(n)]

    solveMaze(maze,0,0,path,possiblePath,visited)
    print("Possible paths: ",possiblePath)
    print("Minimum number of steps: ",len(min(possiblePath)))
    # for i in range(len(possiblePath)):
    #     print(possiblePath[i])
    # print(possiblePath)
    # print([i for i in visited])

maze = [
    [1,0,0,0],
    [1,1,0,0],
    [1,1,0,0],
    [1,1,1,1],
]
solve(maze)