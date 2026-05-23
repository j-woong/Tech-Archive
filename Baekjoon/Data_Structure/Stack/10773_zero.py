import sys
sys.stdin = open("input.txt","r")
k = int(sys.stdin.readline())
s = []

for _ in range(k):
    n = int(sys.stdin.readline())   

    if n == 0:
        s.pop()
    else:
        s.append(n)

if s:
    print(sum(s))
else:
    print(0)