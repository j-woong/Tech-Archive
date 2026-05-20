"""
***핵심 로직***
숫자 크기가 아닌 이어붙인 결과를 기준으로 정렬하는 것.
- 숫자를 문자열로 변환한다.
- a+b와 b+a를 비교한다.
- 더 큰 조합이 앞에 오도록 정렬한다.
- 정렬된 문자열을 이어붙인다.
- "000" 같은 경우를 처리하기 위해 int() 후 다시 문자열 변환한다.
"""
# 밑에는 내가 푼 코드로 계속 틀림
"""def solution(numbers):
    answer = ""
    numss = [str(num) for num in numss]
        
    numss = sorted(numss,key = lambda x: (x[0],x) ,reverse=True)
    
    numss = sorted(numss,key = lambda x: int(x)%10,reverse=True)
    
    answer = "".join(numss)
    return answer
"""
# 정답 풀이
from functools import cmp_to_key
def compare(a,b):
    if a+b > b+a:
        return -1
    elif a+b < b+a:
        return 1
    else:
        return 0

def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=cmp_to_key(compare))
    
    answer = "".join(numbers)
    return str(int(answer))