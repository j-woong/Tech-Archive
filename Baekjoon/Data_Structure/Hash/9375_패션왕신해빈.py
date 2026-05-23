import sys
from collections import defaultdict

# sys.stdin = open("input.txt","r")
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    fashion = defaultdict(int)
    for _ in range(n):
        c,k = list(sys.stdin.readline().split())
        fashion[k] += 1

    ans = 1
    for k in fashion:
        ans *= (fashion[k] + 1)

    print(ans-1)