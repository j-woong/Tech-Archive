from collections import defaultdict
def solution(clothes):
    hash_map = defaultdict(list)
    
    for c,t in clothes:
        hash_map[t].append(c)
    
    ans = 1
    for t in hash_map:
        ans *= (len(hash_map[t]) + 1)
        
    return ans - 1
"""
import collections
from functools import reduce
def solution(clothes):
    return reduce(lambda:x,y:x*y, [ a+1 for a in collections.Counter([x[1] for x in c].value()]) - 1
"""
