# 219. Contains Duplicate II 문제 풀이

## **문제 설명**

주어진 배열 `nums`와 정수 `k`에 대해, 배열 내에서 `nums[i] == nums[j]`이고 `abs(i - j) <= k`를 만족하는 서로 다른 인덱스 `i`와 `j`가 존재하는지 확인하는 함수입니다.

<br>

## **나의 문제 풀이**

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  const map = new Map(); // 숫자와 인덱스를 저장할 Map 생성

  for (let i = 0; i < nums.length; i++) {
    if (map.has(nums[i]) && i - map.get(nums[i]) <= k) {
      return true; // 중복이 k 이하의 거리에서 발견되면 true 반환
    }
    map.set(nums[i], i); // 키는 nums의 숫자값, 값은 해당숫자가 마지막으로 등한 인덱스
  }
  return false;
};
```

<br>

## 예제와 실행 과정

### 1. nums = [1, 2, 3, 1], k = 3;

```
map = {}
i = 0, nums[i] = 1, map = {1: 0}
i = 1, nums[i] = 2, map = {1: 0, 2: 1}
i = 2, nums[i] = 3, map = {1: 0, 2: 1, 3: 2}
i = 3, nums[i] = 1, map.get(1) = 0, 3-0<=k
return true
```

### 2. nums = [1, 0, 1, 1], k = 1

```
map = {}
i = 0, nums[i] = 1, map = {1: 0}
i = 1, nums[i] = 0, map = {1: 0, 0: 1}
i = 2, nums[i] = 1, map.get(1) = 0, 2-0>1, map = {1: 2, 0: 1}
i = 3, nums[i] = 1, map.get(1) = 2, 3-2<=k
return true
```

### 3. nums = [1, 2, 3, 4], k = 2

```
 map = {}
i = 0, nums[i] = 1, map = {1: 0}
i = 1, nums[i] = 2, map = {1: 0, 2: 1}
i = 2, nums[i] = 3, map = {1: 0, 2: 1, 3: 2}
i = 3, nums[i] = 4, map = {1: 0, 2: 1, 3: 2, 4: 3}
return false
```

<br>

## 복잡도 분석

### 시간 복잡도 : O(n)

- 배열 한 번 순회 **O(n)**
- `map.get` 및 `map.set`은 평균적으로 **O(1)** 배열을 한 번 순회

### 공간 복잡도 : O(n)

- map에 최대 n개의 요소를 저장 → O(n)

<br>
