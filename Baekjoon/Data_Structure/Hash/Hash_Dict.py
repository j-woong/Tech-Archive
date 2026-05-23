# Hash_Dict.py 예시

# 1. 빈 딕셔너리 생성
my_hash = {}

# 2. 데이터 삽입 (Key: 이름, Value: 번호)
my_hash["Kim"] = "010-1234-5678"
my_hash["Lee"] = "010-9876-5432"

# 3. 데이터 조회 (탐색 속도가 리스트보다 훨씬 빠름!)
if "Kim" in my_hash:
    print(f"Kim의 번호: {my_hash['Kim']}")

# 4. 데이터 삭제
del my_hash["Lee"]

# 5. [꿀팁] Counter를 이용한 빈도수 계산 (해시 응용)
from collections import Counter

items = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = Counter(items) 
# 결과: {'apple': 3, 'banana': 2, 'orange': 1} -> 자동으로 해시 맵 생성
print(counts["apple"]) # 3