import sys
from collections import deque
# sys.stdin = open("input.txt","r")
N,M,V = map(int,sys.stdin.readline().split())

adj = [[] for _ in range(N+1)]
visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())

    adj[u].append(v)
    adj[v].append(u)

for i in range(N+1):
    adj[i].sort()

def Dfs(now):
    visited_dfs[now] = True
    print(now,end=" ")

    for next_com in adj[now]:
        if not visited_dfs[next_com]:
            Dfs(next_com)

def Bfs(now):
    visited_bfs[now] = True
    queue = deque([now])
    
    while queue:
        cur_n = queue.popleft()
        print(cur_n,end = " ")
       
        for next_com in adj[cur_n]:
            if not visited_bfs[next_com]:
                visited_bfs[next_com] = True
                queue.append(next_com)


Dfs(V)
print()
Bfs(V)