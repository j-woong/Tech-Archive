"""
***로직***
1. 입력 변수
- clothes: 의상의 정보가 담겨있는 배열
2. 핵심 변수
- fashion: 종류별로 갯수 파악을 위한 해시
3. 핵심 로직
step1: 해시 테이블 생성
- collections 함수에서 defaultdict 모듈을 이용해 fashion 해시 생성
step2: 배열 순회 및 해시 추가
- 배열을 순회하며 두번째 요소를 key값으로 하여 해시에 갯수랑 1개씩 증가
step3: 조합 갯수 출력
- 조합의 갯수는 (의상 개수 + 입지 않은 경우)를 곱해가며 구할 수 있음
- fashion의 values값을 순회하며 갯수를 answer변수에 곱함. 
- 마지막에 전부 입지 않은 경우 -1을 하며 출력
4. 예외 처리
- 벌거숭이 케이스 방어: 결과 출력 시에 전부 입지 않은 경우를 빼고 출력을 해야함.
"""
# 재풀이
from collections import defaultdict
def solution(clothes):
    fashion = defaultdict(int)
    
    for c in clothes:
        fashion[c[1]] += 1
        
    print(fashion)
    
    answer = 1
    for v in fashion.values():
        answer *= (v + 1)
        
    return answer - 1
"""
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