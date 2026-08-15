from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 대기 중인 트럭
    trucks = deque(truck_weights)

    # 다리 길이만큼 빈 공간(0)으로 시작
    bridge = deque([0] * bridge_length)

    # 현재 다리 위의 총 무게
    current_weight = 0

    # 경과 시간
    time = 0

    while bridge:
        time += 1

        # 다리 맨 앞의 트럭이 다리를 빠져나감
        out_truck = bridge.popleft()
        current_weight -= out_truck

        # 아직 기다리는 트럭이 있다면
        if trucks:
            next_truck = trucks[0]

            # 다음 트럭을 올려도 무게 제한을 넘지 않는 경우
            if current_weight + next_truck <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                current_weight += truck

            # 무게 제한 때문에 트럭을 올릴 수 없는 경우
            else:
                bridge.append(0)

    return time