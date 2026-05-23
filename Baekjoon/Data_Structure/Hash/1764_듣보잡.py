import sys
from collections import defaultdict
#sys.stdin = open("input.txt","r")

n,m = map(int,sys.stdin.readline().split())
roster = defaultdict(int)

for _ in range(n):
    name = sys.stdin.readline().strip()
    
    roster[name] = 1


for _ in range(m):
    name = sys.stdin.readline().strip()

    if name in roster:
        roster[name] += 1

ans = []
for p in roster:
    if roster[p] > 1:
       ans.append(p)

dont_roster = sorted(ans)
print(len(dont_roster))
for p in dont_roster:
    print(p)

"""
# set을 활용한 풀이
hear = set(sys.stdin.readline().strip() for _ in range(n))
see = set(sys.stdin.readline().strip() for _ in range(m))

# 교집합 연산자 (&)
result = sorted(list(hear & see))
"""
