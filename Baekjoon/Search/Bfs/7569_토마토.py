import sys
from collections import deque
# sys.stdin = open("input.txt","r")

m,n,h = map(int,sys.stdin.readline().split())
grid = [[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

dz = [-1,1,0,0,0,0]
dy = [0,0,-1,0,1,0]
dx = [0,0,0,1,0,-1]

queue = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if grid[k][i][j] == 1:
                queue.append((k,i,j))

def bfs():
    while queue:
        z,y,x = queue.popleft()

        for i in range(6):
            nz,ny,nx = z + dz[i], y + dy[i] ,x + dx[i]
            if  0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if grid[nz][ny][nx] == 0:
                    queue.append((nz,ny,nx))
                    grid[nz][ny][nx] = grid[z][y][x] + 1

bfs()

ans = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if grid[k][i][j] == 0:
              print(-1)
              exit()  

            else:
                if ans < grid[k][i][j]:
                    ans = grid[k][i][j]
                    
if ans == 1:
    print(0)
else:
    print(ans-1)
    