import sys
input = sys.stdin.readline

# 1. 입력 및 전역 변수 설정
n = int(input())
arr = list(map(int, input().split()))
result = 0 # Swap 횟수 저장

def merge_sort(start, end):
    global result
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid + 1, end)

    # 병합 (Merge) 과정
    idx1, idx2 = start, mid + 1
    temp = []

    while idx1 <= mid and idx2 <= end:
        # 왼쪽 그룹의 값이 더 작거나 같으면 정상 (Swap 불필요)
        if arr[idx1] <= arr[idx2]:
            temp.append(arr[idx1])
            idx1 += 1
        else:
            # 오른쪽 그룹의 값이 더 작으면 앞으로 이동해야 함 (Swap 발생!)
            # 왼쪽 그룹에 남아있는 숫자 개수만큼 버블 정렬 Swap이 일어남
            temp.append(arr[idx2])
            idx2 += 1
            result += (mid - idx1 + 1) # 핵심 로직: 현재 idx1부터 mid까지 개수

    # 남은 데이터 처리
    if idx1 <= mid:
        temp.extend(arr[idx1:mid+1])
    if idx2 <= end:
        temp.extend(arr[idx2:end+1])

    # 정렬된 결과를 원본 배열에 반영
    for k in range(len(temp)):
        arr[start + k] = temp[k]

# 2. 병합 정렬 실행
merge_sort(0, n - 1)

# 3. 결과 출력
print(result)