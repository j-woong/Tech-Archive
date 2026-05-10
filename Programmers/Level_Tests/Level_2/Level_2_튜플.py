"""
***로직***
1. 입력 변수
- s: 집합 기호({, })와 쉼표(,)로 구성된 튜플 표현 문자열
2. 핵심 변수
- s (정제된 데이터): 문자열을 파싱하여 만든 숫자 집합들의 리스트
- answer: 중복을 제거하며 숫자를 순서대로 담아 튜플을 완성할 결과 배열
3. 핵심 로직:
step1: 데이터 정제 및 정렬
- 슬라이싱과 .split()을 이용하여 문자열 s에 불필요한 부분 제거
- 문자열 요소들을 문자열 크기 순으로 정렬
- map함수 이용하여 문자열 s를 이중 배열로 재선언
step2: 튜플 원소 추출
- 이중 for문으로 각 요소가 answer에 없다면 answer에 추가
4. 예외처리:
- answer 내에서 in 연산을 수행할 때, 비교 대상과 저장 대상의 타입을 모두 int로 일치시켜 정확한 비교가 이루어지도록 한다.
"""
def solution(s):
    answer = []
    # 특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.
    s = list(s[2:-2].split('},{'))
    s = sorted(s,key=lambda x:len(x))
    s = [list(map(int,tup.split(','))) for tup in s]
    
    for tup in s:
        for c in tup:
            if c not in answer:
                answer.append(c)
            
    return answer