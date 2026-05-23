import sys

# sys.stdin = open("input.txt","r")
n,m = map(int,sys.stdin.readline().split())
visited = [False] * (n+1)
ans = []

def backtracking(depth):
    if depth == m:
        print(*ans)
        return
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            
            backtracking(depth + 1)

            ans.pop()
            visited[i] = False


backtracking(0)