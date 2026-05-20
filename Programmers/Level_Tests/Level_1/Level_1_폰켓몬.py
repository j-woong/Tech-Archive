def solution(nums):
    pick_pocket = len(nums)//2
    type_pocket = len(set(nums))
    
    return min(pick_pocket,type_pocket)

        