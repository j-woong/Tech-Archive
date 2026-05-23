import sys

# sys.stdin = open("input.txt","r")
n,m = map(int,sys.stdin.readline().split())
ans = []

def backtracking(depth,start):
    if depth == m:
        print(*ans)
        return

    for i in range(start,n+1):
        ans.append(i)
            
        backtracking(depth + 1,i + 1)

        ans.pop()


backtracking(0,1)        