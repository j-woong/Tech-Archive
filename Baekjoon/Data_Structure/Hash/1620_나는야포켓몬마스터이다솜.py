import sys
from collections import defaultdict
# sys.stdin = open("input.txt","r")
name_to_number = defaultdict(int)
number_to_name = defaultdict(list)

n,m = map(int,sys.stdin.readline().split())

for i in range(1,n+1):
    pocket = sys.stdin.readline().strip()

    name_to_number[pocket] = i
    number_to_name[i] = pocket

for _ in range(m):
    res = sys.stdin.readline().strip()
    if res.isdigit():
        print(number_to_name[int(res)])
    elif res.isalpha():
        print(name_to_number[res])
