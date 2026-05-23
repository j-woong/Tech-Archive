import sys
sys.setrecursionlimit(10000)
# sys.stdin = open("input.txt", "r")

n,m = map(int,sys.stdin.readline().split())
adj = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(now,depth):
    if depth == 4:
        print(1)
        sys.exit()

    visited[now] = True

    for next_f in adj[now]:
        if not visited[next_f]:
            dfs(next_f,depth + 1)

    visited[now] = False

for i in range(n):
    dfs(i,0) 

print(0)