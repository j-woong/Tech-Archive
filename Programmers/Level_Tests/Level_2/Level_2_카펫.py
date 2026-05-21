"""
***로직***
1. 입력 변수
- brown, yellow: 각각 테두리, 알맹이를 나타내는 변수
2. 핵심 변수
- tile, hor, ver: 각각 전체 격자 갯수, 카펫의 가로,새로 갯수를 나타내는 변수
3. 핵심 로직
step1: 핵심 변수 생성
- 전체 격자 갯수를 나타내는 tile 변수 생성
- 각각 가로, 새로 갯수를 나타내는 hor,ver 변수 생성
step2: 갈색 범위의 가로, 새로 갯수 파악
- 전체 타일개수의 제곱근값부터 범위를 잡고 중첩문을 돌림
- 효율성을 위해 큰거 부터 줄여나가면서 ver과 hor 파악
step3: 정답 출력
- 가로 길이와 세로 길이의 각각 -2를 한 값들의 곱이 노란색 부분이기 때문에 맞다면 정답 리턴
4. 예외 처리
- 정답 리턴하기 전에 노란색 부분의 갯수가 맞는지 조건을 세우고 부합하면 정답 리턴
"""
import math
def solution(brown, yellow):    
    tile = brown + yellow
    hor, ver = 0,0

    for i in range(int(math.sqrt(tile)),2,-1):
        if tile % i == 0:
            ver = i
            hor = tile // ver
            
            if (hor - 2) * (ver - 2) == yellow:
                return [hor,ver]