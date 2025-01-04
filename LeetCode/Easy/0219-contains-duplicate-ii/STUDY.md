# JavaScript `Map` 객체란

## 소개

`Map`은 JavaScript에서 **키-값 쌍**을 저장하고 관리하기 위한 내장 객체이다. 기존의 `Object`와 유사하지만, 몇 가지 중요한 차이점과 장점이 있다.

<br>

## 주요 특징

### 1. 키(Key)의 유연성

- `Map`의 키는 **어떠한 데이터 타입**도 가능하다.
  - 예: 숫자, 문자열, 객체, 함수 등.
- `Object`의 키는 기본적으로 문자열로 변환되지만, `Map`에서는 원시 값과 객체 그대로 사용된다.

  ```javascript
  const map = new Map();
  map.set(1, "number"); // 숫자를 키로 사용
  map.set("1", "string"); // 문자열을 키로 사용
  map.set({ key: "value" }, "object"); // 객체를 키로 사용
  console.log(map); // Map { 1 => 'number', '1' => 'string', { key: 'value' } => 'object' }
  ```

### 2. 순서 유지

- `Map`은 삽입한 순서를 기억해서 데이터의 순차적 처리에 유리하다.

  ```javascript
  const map = new Map();
  map.set("a", 1);
  map.set("b", 2);
  console.log([...map.keys()]); // ['a', 'b']
  ```

### 3. 내장 메서드 제공

- `Map`은 데이터를 추가, 삭제, 검색할 수 있는 다양한 메서드를 제공한다.

### 4. 반복 가능

- `Map`은 반복 가능한(iterable) 객체로, `for...of` 문 또는 `forEach` 메서드를 통해 쉽게 순회할 수 있다.

  ```javascript
  const map = new Map();
  map.set("x", 10);
  map.set("y", 20);
  for (const [key, value] of map) {
    console.log(key, value); // x 10, y 20
  }
  ```

### 5. 효율적이고 빠름

- `Map`은 키를 해시 테이블 기반으로 관리하여 `get` 및 `set` 연산의 평균 시간 복잡도는 **O(1)** 이다.

<br>

## 주요 메서드와 속성

| 메서드/속성         | 설명                                                                              |
| ------------------- | --------------------------------------------------------------------------------- |
| `set(key, value)`   | 특정 키에 값을 설정한다. 반환값은 `Map` 객체 자신이다.                            |
| `get(key)`          | 특정 키에 대한 값을 반환한다. 키가 없으면 `undefined`를 반환한다.                 |
| `has(key)`          | 특정 키가 `Map`에 존재하는지 확인한다. `true` 또는 `false`를 반환한다.            |
| `delete(key)`       | 특정 키를 삭제한다. 성공하면 `true`, 실패하면 `false`를 반환한다.                 |
| `clear()`           | `Map`의 모든 키-값 쌍을 삭제한다.                                                 |
| `size`              | `Map`에 저장된 키-값 쌍의 개수를 반환하는 속성이다.                               |
| `keys()`            | `Map`에 저장된 모든 키를 반복 가능한 객체로 반환한다.                             |
| `values()`          | `Map`에 저장된 모든 값을 반복 가능한 객체로 반환한다.                             |
| `entries()`         | `Map`에 저장된 모든 키-값 쌍을 `[key, value]` 형태로 반복 가능한 객체로 반환한다. |
| `forEach(callback)` | `Map`의 각 키-값 쌍에 대해 지정된 콜백 함수를 호출한다.                           |

<br>

## `Map`과 `Object`의 차이

| 특징                      | `Map`                                        | `Object`                                                 |
| ------------------------- | -------------------------------------------- | -------------------------------------------------------- |
| 키(Key) 타입              | 어떤 데이터 타입도 가능                      | 문자열 또는 심볼(Symbol)만 가능                          |
| 키의 순서 유지            | 유지됨                                       | 보장되지 않음                                            |
| 기본 프로토타입 상속 여부 | 없음 (깨끗한 키-값 저장소)                   | 프로토타입 체인 상속됨 (`toString`, `hasOwnProperty` 등) |
| 데이터 크기 확인          | `size` 속성으로 O(1) 시간 복잡도로 확인 가능 | 수동으로 계산해야 함                                     |
| 성능                      | 키-값 쌍 추가/삭제/조회가 더 빠름            | 약간 느림 (문법적으로 간단하지만 유연성은 적음)          |

<br>

## 사용 예제

### 1. 기본적인 데이터 저장과 검색

```javascript
const map = new Map();
map.set("name", "Alice");
map.set("age", 25);

console.log(map.get("name")); // Alice
console.log(map.has("age")); // true
console.log(map.size); // 2
```

### 2. 객체를 키로 활용

```javascript
const objKey = { id: 1 };
const map = new Map();
map.set(objKey, "value for object");

console.log(map.get(objKey)); // value for object
```

### 3. 키-값 쌍 반복 처리

```javascript
const map = new Map();
map.set("x", 10);
map.set("y", 20);

map.forEach((value, key) => {
  console.log(`${key}: ${value}`);
});
// 출력:
// x: 10
// y: 20
```

### 4. 삽입 순서 유지

```javascript
const map = new Map();
map.set("a", 1);
map.set("b", 2);
map.set("c", 3);

for (const [key, value] of map) {
  console.log(`${key}: ${value}`);
}
// 출력:
// a: 1
// b: 2
// c: 3
```

<br>

## `Map`이 유용한 상황

### 1. 복잡한 키 관리

- 객체나 배열을 키로 사용해야 할 때 유용하다.

```javascript
const map = new Map();
const keyObject = { id: 1 };
map.set(keyObject, "Object Key");
console.log(map.get(keyObject)); // 출력: Object Key
```

### 2. 데이터 순서 유지

- 삽입된 순서대로 데이터를 처리해야 할 때 적합하다.

```javascript
const map = new Map();
map.set("first", 1);
map.set("second", 2);
console.log([...map.keys()]); // 출력: ['first', 'second']
```

### 3. 효율적인 데이터 조회

- 데이터의 추가, 삭제, 검색 작업이 빈번히 이루어질 경우 적합하다.

```javascript
const map = new Map();
map.set("a", 1);
map.set("b", 2);
console.log(map.has("a")); // 출력: true
map.delete("a");
console.log(map.has("a")); // 출력: false
```

### 4. 프로토타입 체인 문제 회피

- `Object`의 기본 메서드(`toString`, `hasOwnProperty`)와의 충돌을 방지하고 싶을 때 유용하다.

```javascript
const map = new Map();
map.set("toString", "value");
console.log(map.get("toString")); // 출력: value
```

<br>
