import sys
sys.stdin = open("input.txt","r")
sys.setrecursionlimit(10000)
n = int(sys.stdin.readline())
a,b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())

    adj[x].append(y)
    adj[y].append(x)

def Dfs(now,n_of_rel,want):
    visited[now] = True

    if now == want:
        return n_of_rel
    
    for next_com in adj[now]:
        if not visited[next_com]:
            result = Dfs(next_com,n_of_rel+1,want)
            if result != -1:
                return result
            
    return -1

print(Dfs(a,0,b))