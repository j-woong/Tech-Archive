import sys
sys.setrecursionlimit(10000)
# sys.stdin = open("input.txt","r")
n = int(sys.stdin.readline())

nums = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split()))

max_val = -float('inf')
min_val = float('inf')

def solve(depth,current_res):
    global max_val,min_val

    if depth == n:
        max_val = max(max_val,current_res)
        min_val = min(min_val,current_res)
        return

    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            
            next_res = current_res
            if i == 0: 
                next_res += nums[depth]
            elif i == 1:
                next_res -= nums[depth]
            elif i == 2:
                next_res *= nums[depth]
            else:
                if current_res < 0:
                    next_res = -(-next_res // nums[depth])
                else:
                    next_res //= nums[depth]

            solve(depth+1,next_res)
            op[i] += 1

solve(1,nums[0])

print(max_val)
print(min_val)