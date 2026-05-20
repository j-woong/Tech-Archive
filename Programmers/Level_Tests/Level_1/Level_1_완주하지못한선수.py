def sollution(participant,completion):
    hash = {}

    for p in participant:
        if p in hash:
            hash[p] += 1
        else:
            hash[p] = 1

    for c in completion:
            hash[c] -= 1

    for key in hash:
        if hash[key] > 0:
            return key

"""
from collections import Counter

def sollution(participant,completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]
"""

"""
import collections

def sollution(participant,completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.key())[0]
"""