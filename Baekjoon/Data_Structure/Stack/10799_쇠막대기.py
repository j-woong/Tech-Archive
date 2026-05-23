import sys
# sys.stdin = open("input.txt", "r")
vps = sys.stdin.readline().strip()
s = []
p = 0 # 막대 갯수

for i in range(len(vps)):
    if vps[i] == '(':
        s.append('(')
        
    else: # 현재 )
        s.pop()

        if vps[i-1] == '(':
            p += len(s)
        else:
            p += 1

print(p)