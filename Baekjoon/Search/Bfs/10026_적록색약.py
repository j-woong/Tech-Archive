import sys
from collections import deque
# sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())
grid = [list(sys.stdin.readline().strip()) for _ in range(n)]
dr = [0,1,0,-1]
dc = [1,0,-1,0]

def bfs_blindness(y,x,n,grid,visited):
    queue = deque([(y,x)])
    visited[y][x] = True

    while queue:
        r,c = queue.popleft()

        for i in range(4):
            nr , nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    if grid[r][c] == 'B':
                        if grid[nr][nc] == 'B':
                            visited[nr][nc] = True
                            queue.append((nr,nc))
                    else:
                        if grid[nr][nc] == 'R' or grid[nr][nc] == 'G':
                            visited[nr][nc] = True
                            queue.append((nr,nc))
                        

def bfs_normal(y,x,n,grid,visited):
    queue = deque([(y,x)])
    visited[y][x] = True
    while queue:
        r,c = queue.popleft()

        for i in range(4):
            nr , nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc]:
                    if grid[r][c] == 'R' and grid[nr][nc] == 'R':
                        visited[nr][nc] = True
                        queue.append((nr,nc))
                    elif grid[r][c] == 'G' and grid[nr][nc] == 'G':
                        visited[nr][nc] = True
                        queue.append((nr,nc))
                    elif grid[r][c] == 'B' and grid[nr][nc] == 'B':
                        visited[nr][nc] = True
                        queue.append((nr,nc))

visited1 = [[False] * n for _ in range(n)]
ans_blind = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs_blindness(i,j,n,grid,visited1)
            ans_blind += 1

visited2 = [[False] * n for _ in range(n)]
ans_normal = 0
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs_normal(i,j,n,grid,visited2)
            ans_normal += 1
print(ans_normal,ans_blind)