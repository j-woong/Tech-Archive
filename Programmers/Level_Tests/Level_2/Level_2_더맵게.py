import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    ans = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)

        new_scoville = min1 + (min2*2)
        heapq.heappush(scoville,new_scoville)

        ans += 1

    return ans