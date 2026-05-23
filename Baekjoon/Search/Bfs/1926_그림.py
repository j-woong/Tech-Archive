import sys
from collections import deque
# sys.stdin = open("input.txt","r")
n,m = map(int,sys.stdin.readline().split())
grid = [ list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[False] * m for i in range(n)]
dr = [-1,0,1,0]
dc = [0,1,0,-1]

ans = []
def Bfs(start_r,start_c):
    queue = deque([(start_r,start_c)])
    visited[start_r][start_c] = True
    area = 1
    
    while queue:
        r,c = queue.popleft()

        for i in range(4):
            nr,nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr,nc))
                    area += 1   
    return area

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and not visited[i][j]:
            ans.append(Bfs(i,j))

if not ans:
    print(0)
    print(0)
else:
    print(len(ans))
    print(max(ans))