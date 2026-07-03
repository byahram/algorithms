import math

def solution(progresses, speeds):
    # 각 작업의 남은 기간 계산하여 리스트화
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    answer = []
    front = 0 # 배포 기준 위치

    for i in range(len(days)):
        # 현재 기준(front) 작업보다 오래 걸리는 작업을 만나면 배포 수행
        if days[front] < days[i]:
            answer.append(i - front)
            front = i # 새로운 기준 작업 설정

    # 마지막 남은 작업들 배포
    answer.append(len(days) - front)
    return answer