# [level 2] 기능개발 - 42586 문제 풀이

## **문제 설명**

`progresses`와 `speeds` 배열을 기반으로 작업 완료일을 계산하고 배포 단위별로 기능의 수를 반환

<br>

## **나의 문제 풀이**

```javascript
function solution(progresses, speeds) {
  // 배포 단위별로 기능의 수를 저장할 배열
  var answer = [];

  // 작업의 남은 일수를 계산하여 progresses 배열을 업데이트
  for (let i = 0; i < progresses.length; i++) {
    // 각 작업이 완료되기까지 남은 날짜 계산
    // 현재 작업의 진행도와 속도를 기반으로 남은 일수를 반올림하여 구한다
    progresses[i] = Math.ceil((100 - progresses[i]) / speeds[i]);

    // 현재 작업의 완료 날짜가 이전 작업보다 빠르면,
    // 현재 작업의 완료 날짜를 이전 작업의 완료 날짜로 변경
    // 이는 이전 작업과 함께 배포되도록 조정하는 과정
    if (i != 0 && progresses[i - 1] > progresses[i]) {
      progresses[i] = progresses[i - 1];
    }
  }

  let i = 0;
  // 배포 단위별로 작업의 수를 계산
  while (progresses.length) {
    // 현재 작업과 동일한 배포일에 속하는 작업의 수를 계산
    answer.push([...progresses].filter((v) => v == progresses[i]).length);
    // 동일한 배포일에 속하는 작업들을 progresses에서 제거
    progresses = progresses.filter((v) => v !== progresses[i]);
  }
  // 배포 단위별 기능 수 반환
  return answer;
}
```

### 예제 테스트

```javascript
// 입력
const progresses = [93, 30, 55];
const speeds = [1, 30, 5];

// 실행
console.log(solution(progresses, speeds));

// 출력
// [2, 1]
// 설명: 첫 번째와 두 번째 작업은 같은 날 배포되고, 세 번째 작업은 그 다음 날 배포됩니다.
```

### 복잡도 계산

- **시간 복잡도**: **O(n^2)**
- **공간 복잡도**: **O(n)**

<br>

## 다른 문제 풀이

```javascript
function solution(progresses, speeds) {
  const answer = [];

  // 남은 작업 일수 계산
  let days = progresses.map((progress, index) =>
    Math.ceil((100 - progress) / speeds[index])
  );

  // 첫 번째 작업의 완료 예정일 기준
  let maxDay = days[0];

  let count = 0; // 배포될 작업의 개수
  for (let i = 0; i < days.length; i++) {
    if (days[i] <= maxDay) {
      // 현재 작업이 이전 배포일(maxDay)보다 늦지 않으면 같은 배포로 처리
      count++;
    } else {
      // 새로운 배포가 필요한 경우
      answer.push(count); // 이전 배포의 작업 수 저장
      count = 1; // 현재 작업을 새 배포로 카운트
      maxDay = days[i]; // 새로운 기준 배포일 업데이트
    }
  }
  // 마지막 배포의 작업 수 추가
  answer.push(count);

  return answer;
}
```

- 나는 `filter`로 복사를 반복적으로 수행했는데 이 코드는 단순히 days 배열을 한 번 순회하며 처리한다
- 하나의 반복문으로 작업 완료 일수를 확인하고 배포 단위별로 작업을 카운트하므로 시간 복잡도가 줄어듦..
- `filter`와 `while` 대신 `for` 루프를 사용하여 직관적으로 배포 로직을 구현
- `filter`와 `while`로 인해 발생한 추가 연산을 제거했다고 복잡도가 줄어들었다

### 예제 테스트

```javascript
const progresses = [93, 30, 55];
const speeds = [1, 30, 5];
console.log(solution(progresses, speeds)); // [2, 1]

const progresses2 = [95, 90, 99, 99, 80, 99];
const speeds2 = [1, 1, 1, 1, 1, 1];
console.log(solution(progresses2, speeds2)); // [1, 3, 2]
```

### 복잡도 계산

- **시간 복잡도**: **O(n)**
- **공간 복잡도**: **O(n)**

<br>
