import sys

# sys.stdin = open("input.txt","r")
n,m = map(int,sys.stdin.readline().split())
ans = []

def solve(depth):
    if depth == m:
        print(*ans)
        return 
    
    for i in range(1,n+1):
        ans.append(i)

        solve(depth+1)

        ans.pop()

solve(0)
    