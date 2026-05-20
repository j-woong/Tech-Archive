def solution(arr):
    answer = [arr[0]]
    cur_n = arr[0]
    for i in range(1,len(arr)):
        if cur_n != arr[i]:
            answer.append(arr[i])
        cur_n = arr[i]
        
    return answer

"""
def solution(arr):
    ans = []
    for i in arr:
        if len(ans) == 0 or ans[-1] != i:
            ans.append(i)
"""