from collections import deque

def solution(priorities, location):
    # (원래 위치, 우선순위)
    queue = deque(
        (i, priority)
        for i, priority in enumerate(priorities)
    )

    # 실행된 프로세스 개수
    order = 0

    while queue:
        current_index, current_priority = queue.popleft()

        if any(
            current_priority < priority
            for _, priority in queue
        ):
            queue.append((current_index, current_priority))

        else:
            order += 1

            if current_index == location:
                return order