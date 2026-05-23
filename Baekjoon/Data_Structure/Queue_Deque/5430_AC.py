import sys
from collections import deque
# sys.stdin = open("input.txt","r")

def solution(ac,n,arr):    
    if n == 0:
        queue = deque()
    else:
        clean_arr = arr.strip('[]').split(',')
        queue = deque(clean_arr)

    rev = False # False 정방향, True 역방향
    for r in ac:
        if r == 'R':
            rev = not rev
        elif r == 'D':
            if queue:
                if not rev :
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print('error')
                return False
    if rev:
        queue.reverse()

    print(f"[{','.join(queue)}]")
    
t = int(sys.stdin.readline())
for _ in range(t):
    AC = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().strip()
    solution(AC,n,arr)
    