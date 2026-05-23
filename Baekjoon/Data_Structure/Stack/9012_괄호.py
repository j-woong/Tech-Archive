import sys
sys.stdin = open("input.txt","r")

def solution(P):
    S = []
        
    for char in P:
        if char == '(':
            S.append(char)
        else:
            if not S:
                return False
            S.pop()

    return len(S) == 0

            
t = int(sys.stdin.readline())
for _ in range(t):
    P = sys.stdin.readline().strip()
    if solution(P):
        print('YES')
    else:
        print('NO')
            