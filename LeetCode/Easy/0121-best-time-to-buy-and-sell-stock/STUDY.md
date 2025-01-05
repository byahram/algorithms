# Infinity란?

자바스크립트에서 Infinity는 무한대를 의미하는 숫자 타입의 상수이다.
Infinity는 수학적으로 생각하면 "매우 큰 수"로, 모든 유한한 숫자보다 크다.

```javascript
console.log(Infinity > 1000000000); // true
console.log(Infinity > Number.MAX_SAFE_INTEGER); // true
```

<br>

## Infinity를 사용하는 이유

minPrice를 초기화할 때, 주어진 배열에서 최소값을 찾아야 하므로 어떤 숫자와 비교해도 큰 값을 설정해주는 것이 필요하다. Infinity는 모든 숫자보다 크기 때문에 배열을 탐색하면서 자연스럽게 minPrice를 갱신할 수 있다.

<br>

## 대안 없이 0으로 초기화하면?

```js
let minPrice = 0;
```

- 배열의 첫 번째 숫자가 양수(예: prices = [3, 2, 6, 4])인 경우, minPrice가 항상 0으로 유지

```js
prices[i] - minPrice; // 항상 prices[i] - 0
```

- 제대로 된 최소값 비교가 이루어지지 않아 잘못된 결과가 나온다.

<br>

## Infinity를 사용한 동작 원리

```js
let minPrice = Infinity; // 처음에는 아주 큰 값으로 초기화

for (let i = 0; i < prices.length; i++) {
  if (prices[i] < minPrice) {
    minPrice = prices[i]; // 더 작은 값을 만나면 갱신
  }
}
```

- prices[0]가 어떤 값이든, 처음에는 무조건 minPrice보다 작으므로 minPrice가 갱신됩니다.
- 배열을 탐색하면서 더 작은 값이 나타날 때마다 minPrice가 갱신됩니다.
- 최종적으로 minPrice에는 배열에서 가장 작은 값이 저장

<br>
