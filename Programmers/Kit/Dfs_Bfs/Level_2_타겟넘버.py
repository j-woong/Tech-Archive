"""
***로직***
1. 입력 변수: 
- numbers: 숫자 배열
- target: 최종적으로 만들 숫자
2. 핵심 변수:
- cur_n: 현재 값을 저장하여 사용
- depth: 숫자를 더한 횟수로 사용할 변수

"""
def solution(numbers, target):
    answer = 0

    def dfs(cur_n,depth):
        if depth == len(numbers):
            if cur_n == target:
                return 1
            else:
                return 0
            
        return dfs(cur_n + numbers[depth],depth+1) + dfs(cur_n - numbers[depth],depth+1)
            
    return dfs(0,0)
        