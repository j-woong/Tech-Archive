from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_w = deque(truck_weights)
    cur_w = 0

    while bridge:
        time += 1
        exited_truck = bridge.popleft()
        cur_w -= exited_truck

        if truck_w:
            if cur_w + truck_w[0] <= weight:
                new_truck = truck_w.popleft()
                bridge.append(new_truck)
                cur_w += new_truck
            else:
                bridge.append(0)
    
    return time