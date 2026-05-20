"""
***로직***
1. 입력 변수: 
- numbers: 숫자 배열
- target: 최종적으로 만들 숫자
2. 핵심 변수:
- cur_n: 현재 값을 저장하여 사용
- depth: 숫자를 더한 횟수로 사용할 변수
***이 문제를 마주하며***
- 처음 이문제를 마주했을 때는 dfs구조를 어떻게 짜야하는지, 그리고 return 값을 어떻게 다루는지
굉장히 난해하고 복잡했다. 하지만 cs공부를 해가면서 dfs구조에 대해 이해를 하고 직접 작성해보니 
굉장히 간단하면서도 신기하다는걸 몸소 깨달을 수 있는 시간이었다.
- 
"""
def solution(numbers, target):
    def dfs(cur_n,depth):
        if depth == len(numbers):
            if cur_n == target:
                return 1
            else:
                return 0
            
        return dfs(cur_n + numbers[depth],depth+1) + dfs(cur_n - numbers[depth],depth+1)
            
    return dfs(0,0)
"""
***재풀이***
def solution(numbers, target):
    
    def dfs(curr,depth):
        if depth == len(numbers):
            if curr == target:
                return 1
            else:
                return 0
        
        return dfs(curr + numbers[depth],depth + 1) + dfs(curr - numbers[depth],depth + 1)
            
    return dfs(0,0)
        
        
"""