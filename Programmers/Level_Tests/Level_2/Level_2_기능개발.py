"""
***로직***
1.  입력 변수  
    progress: 작업의 진도, speeds: 작업의 개발 속도
2.  핵심 변수
    days: 진행 일수를 새는 변수
    complete_days: 진행 일수를 저장해둔 변수
    deploy_day: 현재 배포일의 기준이 되는 일수
    cnt: 함께 배포되는 기능의 갯수
3.  각 단계 로직
    step1: 기능이 진행되는 함수 구현
    - 첫번째 기능부터 for문을 돌려서 days를 1씩 증가시키며 진행속도가 100이 되면 total_days에 저장 
    step2: 배포 그룹화
    - 큐에서 꺼낸 일수를 기준이 되는 일수로 지정함
    - 큐의 데이터를 꺼내고 complete_days 변수의 첫번째 요소와 비교하여 작으면 큐에서 데이터를 꺼내고 cnt를 1씩 증가시킴
    - 기준일보다 오래걸리면 while 중단
    step3: 결과 기록
    - cnt를 answer변수에 추가해줌
4. 예외 처리
    뒤의 기능이 아무리 빨리 끝나도 앞의 기능이 끝나지 않으면 배포될 수 없음을 조건문에 반영. *이때 기준일 비교 while문을 사용함
    빈 큐 처리: 큐에서 데이터를 꺼낼 때 큐가 비어있지 않은지 항상 확인한다.
    
"""
from collections import deque
def solution(progresses, speeds):
    answer = []
    
    complete_days = deque()
    complete = []
    for p,s in zip(progresses,speeds):
        days = 0
        while p < 100:
            days += 1 
            p += s 
        complete_days.append(days) 
    # 5,10,1,1,20,1 -> 1,3,2
    # 일수를 앞 인덱스부터 비교해서 cnt로 관리하면 됌
    
    while complete_days:
        deploy_day = complete_days.popleft()
        cnt = 1
        
        while complete_days and complete_days[0] <= deploy_day:
            complete_days.popleft()
            cnt += 1
            
        answer.append(cnt)
    
    return answer
