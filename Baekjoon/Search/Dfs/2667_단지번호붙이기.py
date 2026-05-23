import sys

# sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())

grid = [ list(map(int,sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n) ]

dr = [-1,0,1,0]
dc = [0,1,0,-1]
def dfs(r,c):
    visited[r][c] = True
    cnt = 1

    for i in range(4):
        nr , nc = r + dr[i] , c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if grid[nr][nc] == 1 and not visited[nr][nc]:
                # 중요 !!! -> 재귀 호출 할떄마다 cnt를 증가시킴 / dfs 핵심 코드
                cnt += dfs(nr,nc)

    return cnt

ans = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:        
            count = dfs(i,j)
            ans.append(count)

print(len(ans))
for cnt in sorted(ans):
    print(cnt)