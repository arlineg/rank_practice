# Simple bot; gives next move on grid.
def nextMove(n,r,c,grid):
    for i in range(0,n):
        for j in range(0,n):
            if grid[i][j] == 'p': # preferably, we'd store this since she's immobile
                if r-i > 0:
                    return "UP"
                elif r-i < 0:
                    return "DOWN"
                elif c-j > 0:
                    return "LEFT"
                else:
                    return "RIGHT"
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
