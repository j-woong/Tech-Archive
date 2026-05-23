import sys
from collections import Counter
sys.stdin = open("input.txt", "r")
N = int(sys.stdin.readline())
arr = [ int(sys.stdin.readline()) for _ in range(N) ]
    
print(round(sum(arr)/N))

arr.sort()
print(arr[N//2])

counter = Counter(arr).most_common()
max_freq = counter[0][1]

if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print(counter[1][0])
else:
    print(counter[0][0])    

print(max(arr)-min(arr))

