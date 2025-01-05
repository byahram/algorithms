# 121. Best Time to Buy and Sell Stock 문제 풀이

## **문제 설명**

날짜별 주식 가격이 주어졌을 때, 얻을 수 있는 최대 이익을 계산하는 문제이다.

단 하루를 선택하여 주식을 사고, 그 이후의 날 중 하나를 선택하여 주식을 팔아 최대 이익을 얻고자 한다. (매도는 매수 이후에만 가능합니다.)

<br>

## **나의 문제 풀이**

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  /**
   * 배열에서 최소 가격을 추적하고, 각 날의 가격에서 최소 가격을 뺀 값을 사용해 최대 이익을 계산하는 방식
   */

  let minPrice = Infinity; // 최소 가격 초기화
  let maxProfit = 0; // 최대 수익 초기화

  for (let i = 0; i < prices.length; i++) {
    // 최소 가격 갱신: 매일 주식 가격이 최소 가격보다 낮으면 minPrice를 업데이트
    if (prices[i] < minPrice) {
      minPrice = prices[i];
    }
    // 현재 가격에서 최소 가격을 뺀 값으로 최대 수익 갱신
    // 각 날의 가격(prices[i])에서 지금까지의 minPrice를 빼서 이익을 계산하고, 그 값이 maxProfit보다 크면 업데이트
    else if (prices[i] - minPrice > maxProfit) {
      maxProfit = prices[i] - minPrice;
    }
  }
  return maxProfit;
};
```

- [Infinity란?](./STUDY.md)

### 예제와 실행 과정

```
prices = [7, 1, 5, 3, 6, 4]:

첫날(7): minPrice = 7, maxProfit = 0
둘째 날(1): minPrice = 1, maxProfit = 0
셋째 날(5): profit = 5 - 1 = 4, maxProfit = 4
넷째 날(3): profit = 3 - 1 = 2, maxProfit = 4 (갱신 X)
다섯째 날(6): profit = 6 - 1 = 5, maxProfit = 5
여섯째 날(4): profit = 4 - 1 = 3, maxProfit = 5 (갱신 X)
최종 결과: maxProfit = 5
```

### 복잡도

- 시간 복잡도: **O(n)** 배열을 한 번 순회합니다.
- 공간 복잡도: **O(1)** (추가 메모리 사용 없음).

<br>

## **다른 문제 풀이**

```javascript
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let max = 0; // 최대 이익을 저장하는 변수
  let min = prices[0]; // 최소 매수가격을 저장하는 변수 (초기값: 첫 번째 날의 주식 가격)

  // 주식 가격 배열을 순회
  for (let i = 0; i < prices.length; i++) {
    // 현재까지의 최대 이익 계산:
    // 현재 가격(prices[i])에서 최소 매수가격(min)을 뺀 값과 기존 최대 이익(max) 중 더 큰 값을 저장
    max = Math.max(max, prices[i] - min);

    // 최소 매수가격 갱신:
    // 현재 가격(prices[i])과 기존 최소 매수가격(min) 중 더 작은 값을 저장
    min = Math.min(min, prices[i]);
  }
  // 최대 이익 반환
  return max;
};
```

- [MDN Math 객체 문서](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Math)

### 예제와 실행 과정

```
prices = [7, 1, 5, 3, 6, 4]:

첫날(7):
    최대 이익: max = Math.max(0, 7 - 7) = 0
    최소 매수가격: min = Math.min(7, 7) = 7
둘째 날(1):
    최대 이익: max = Math.max(0, 1 - 7) = 0
    최소 매수가격: min = Math.min(7, 1) = 1
셋째 날(5):
    최대 이익: max = Math.max(0, 5 - 1) = 4
    최소 매수가격: min = Math.min(1, 5) = 1
넷째 날(3):
    최대 이익: max = Math.max(4, 3 - 1) = 4
    최소 매수가격: min = Math.min(1, 3) = 1
다섯째 날(6):
    최대 이익: max = Math.max(4, 6 - 1) = 5
    최소 매수가격: min = Math.min(1, 6) = 1
여섯째 날(4):
    최대 이익: max = Math.max(5, 4 - 1) = 5
    최소 매수가격: min = Math.min(1, 4) = 1
최종 결과: maxProfit = 5
```

### 핵심 개념

- **최소 매수가격 추적 (min)**: 주식을 가장 싸게 사기 위한 기준.
- **현재 이익 계산 (prices[i] - min)**: 매일의 가격에서 최소 매수가격을 빼서 이익을 계산.
- **최대 이익 갱신 (max)**: 지금까지 계산한 이익 중 가장 큰 값을 저장.

### 복잡도

- 시간 복잡도: **O(n)** (배열을 한 번 순회)
- 공간 복잡도: **O(1)** (추가 메모리 사용 없음)

<br>
