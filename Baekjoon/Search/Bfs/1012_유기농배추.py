import sys
from collections import deque
# sys.stdin = open("input.txt","r")

dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs(m,n,y,x,grid,visited):
        queue = deque([(y,x)])
        visited[y][x] = True
        
        while queue:
            r,c = queue.popleft()

            for i in range(4):
                nr,nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if grid[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        queue.append((nr,nc))
    
t = int(sys.stdin.readline())
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())

    grid = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        grid[y][x] = 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(m,n,i,j,grid,visited)
                ans += 1

    print(ans)