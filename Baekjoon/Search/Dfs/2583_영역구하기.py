import sys
sys.setrecursionlimit(10000)
# sys.stdin = open("input.txt","r")
m,n,k = map(int,sys.stdin.readline().split())

grid = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dr = [-1,0,1,0]
dc = [0,1,0,-1]

for _ in range(k):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

    for i in range(y1,y2):
        for j in range(x1,x2):          
            grid[i][j] = 1

def dfs(r,c):
    visited[r][c] = True
    size = 1

    for i in range(4):
        nr,nc = r + dr[i], c + dc[i]
        if 0 <= nr < m and 0 <= nc < n:
            if grid[nr][nc] == 0 and not visited[nr][nc]:
                size += dfs(nr,nc)

    return size

ans = []

for i in range(m):
    for j in range(n):
        if grid[i][j] == 0 and not visited[i][j]:
            ans.append(dfs(i,j))

print(len(ans))
print(*(sorted(ans)))