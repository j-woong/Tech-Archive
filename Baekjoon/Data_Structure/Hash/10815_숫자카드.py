import sys
sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline())
arr1 = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))

def Hashing(arr1,arr2):
    ans = []
    hash_map = set(arr1)    
    for i in range(len(arr2)):
        if arr2[i] in hash_map:
            ans.append('1')
        else:
            ans.append('0')
        
    print(" ".join(ans))
        
Hashing(arr1,arr2)