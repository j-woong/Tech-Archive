import sys

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0
for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(now):
    global cnt
    visited[now] = True

    for next_com in adj[now]:
        if not visited[next_com]:
            cnt += 1
            dfs(next_com)
    return cnt
    
dfs(1)
print(cnt)