"""
1. 입력 변수
- files: 정렬해야 할 원본 파일명들이 담긴 문자열 배열
2. 핵심 변수
- start: 파일명 내에서 NUMBER(숫자) 영역이 시작되는 인덱스를 가리키는 포인터
- end: NUMBER(숫자) 영역이 끝나고 TAIL(문자) 영역이 시작되는 인덱스를 가리키는 포인터
- parsed_files: 정렬 기준이 될 [HEAD, NUMBER, 원본파일명] 쌍을 묶어서 보관할 임시 배열
3. 핵심 로직
- step1: 포인터 기반 영역 탐색 (문자열 파싱)
  각 파일명을 한 글자씩 순회하며 최초로 숫자를 만나는 순간 start 포인터를 고정함.
  이후 숫자를 계속 수집하다가 '숫자가 아닌 문자'를 만나는 순간 연속성이 깨진 것이므로 end 포인터를 찍고 즉시 루프를 탈출(break)함.
- step2: 슬라이싱을 통한 덩어리 분리
  수집한 두 포인터를 기준으로 오리지널 파일명을 head (f[:start])와 number (f[start:end])로 정교하게 슬라이싱하여 추출함.
- step3: 커스텀 다중 조건 정렬
  파이썬의 sorted() 함수와 key=lambda 구조를 활용하여 2단계 정렬을 수행함.
  1순위 조건: HEAD 영역의 대소문자를 통일하기 위해 소문자 변환값(x[0].lower()) 적용
  2순위 조건: NUMBER 영역의 수식적 크기 비교를 위해 정수형 변환값(int(x[1])) 적용
- step4: 정답 추출
  정렬이 완료된 배열을 순회하며 튜플 내부에 보관해 두었던 '원본 파일명'만 리스트 컴프리헨션으로 쏙 빼내어 최종 반환함.
4. 예외 처리
- TAIL 영역 내 '가짜 숫자' 유입 방지: 
  숫자를 수집하던 중 문자를 만나면 그 즉시 break를 걸어주어, TAIL 영역에 등장하는 무관한 숫자 인덱스가 최댓값(max) 연산 등으로 인해 NUMBER 영역에 오염되는 것을 원천 차단함.
- NUMBER 길이 제한 예외 대응: 
  숫자가 연속되더라도 (현재 인덱스 - start >= 5) 조건에 도달하면 최대 길이 규칙에 따라 그 즉시 end를 지정하고 조기 탈출함.
- 파일명이 숫자로 끝나는 케이스 방지: 
  문자열 맨 끝까지 숫자가 이어져 end 포인터가 지정되지 않은 경우(-1), end 값을 파일명 전체 길이(len(f))로 강제 보정하여 슬라이싱 오류를 방지함.
"""
def solution(files):
    answer = []
    for f in files:
        start = -1
        end = -1
        for i in range(len(f)):
            if f[i].isdigit():
                if start == -1:
                    start = i
                    
                if i - start >= 5:
                    end = i
                    break
            else:
                if start != -1:
                    end = i
                    break
        if end == -1:
            end = len(f)
            
        head = f[:start]
        number = f[start:end]
        answer.append((head.lower(),number,f))
    answer = sorted(answer,key= lambda x: (x[0],int(x[1])))
    return list(x[2] for x in answer)