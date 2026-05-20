"""
def solution(phone_book):
    answer = True
    
    for i in range(len(phone_book)):
        for j in range(1,len(phone_book)):
            if i != j:
                if phone_book[i] in phone_book[j]:
                    answer = False
            
    return answer
"""
def solution(phone_book):
    hash_map = set(phone_book)
    
    for phone in phone_book:
        for i in range(len(phone)):
            if phone[:i] in hash_map:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))
