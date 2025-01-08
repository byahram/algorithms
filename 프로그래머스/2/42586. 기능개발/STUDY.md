# 스택(Stack)과 큐(Queue)

스택(Stack)과 큐(Queue)는 데이터를 저장하고 관리하는 데 사용되는 **자료구조**로, 각기 다른 규칙에 따라 데이터를 추가하거나 제거한다.

<br>

## 스택(Stack)

### 특징

- **LIFO (Last In, First Out)**: 마지막에 들어간 데이터가 가장 먼저 나오는 구조.
- 데이터를 쌓아 올리는 것처럼 동작하며, 한쪽 끝에서만 추가(Push)와 제거(Pop)가 이루어진다.

### 주요 연산

1. **Push**: 스택의 맨 위에 데이터를 추가.
2. **Pop**: 스택의 맨 위에 있는 데이터를 제거하고 반환.
3. **Peek/Top**: 스택의 맨 위에 있는 데이터를 제거하지 않고 확인.
4. **isEmpty**: 스택이 비어 있는지 확인.

### 예제 상황

- **웹 브라우저의 뒤로 가기(Back) 기능**: 최근 방문한 페이지가 스택에 쌓이며, 뒤로 가기 할 때는 가장 최근 페이지부터 제거된다.
- **재귀 함수 호출 스택**: 함수 호출 시, 호출된 함수가 스택에 저장되고 함수가 끝나면 스택에서 제거된다.

### 예제 코드

```java
class Stack {
  constructor() {
    this.stack = [];
  }

  // Push: 데이터 삽입
  push(item) {
    this.stack.push(item);
  }

  // Pop: 데이터 제거 및 반환
  pop() {
    if (this.isEmpty()) {
      throw new Error("Stack is empty");
    }
    return this.stack.pop();
  }

  // Peek: 맨 위 데이터 확인
  peek() {
    return this.isEmpty() ? null : this.stack[this.stack.length - 1];
  }

  // isEmpty: 스택이 비어 있는지 확인
  isEmpty() {
    return this.stack.length === 0;
  }
}

// 사용 예시
const stack = new Stack();
stack.push(10);
stack.push(20);
console.log(stack.peek()); // 20
console.log(stack.pop());  // 20
console.log(stack.isEmpty()); // false
```

<br>

## 큐(Queue)

### 특징

- **FIFO (First In, First Out)**: 먼저 들어간 데이터가 먼저 나오는 구조.
- 데이터를 한쪽 끝(Rear)에서 추가하고, 다른 한쪽 끝(Front)에서 제거한다.

### 주요 연산

1. **Enqueue**: 큐의 끝(Rear)에 데이터를 추가.
2. **Dequeue**: 큐의 앞(Front)에서 데이터를 제거하고 반환.
3. **Peek/Front**: 큐의 앞에 있는 데이터를 제거하지 않고 확인.
4. **isEmpty**: 큐가 비어 있는지 확인.

### 예제 상황

- **프린터 대기열**: 먼저 요청된 작업이 먼저 처리된다.
- **콜센터 대기 시스템**: 고객이 문의를 남기면, 가장 먼저 남긴 고객이 먼저 응답을 받는다.

### 예제 코드

```java
class Queue {
  constructor() {
    this.queue = [];
  }

  // Enqueue: 데이터 삽입
  enqueue(item) {
    this.queue.push(item);
  }

  // Dequeue: 데이터 제거 및 반환
  dequeue() {
    if (this.isEmpty()) {
      throw new Error("Queue is empty");
    }
    return this.queue.shift();
  }

  // Peek: 맨 앞 데이터 확인
  peek() {
    return this.isEmpty() ? null : this.queue[0];
  }

  // isEmpty: 큐가 비어 있는지 확인
  isEmpty() {
    return this.queue.length === 0;
  }
}

// 사용 예시
const queue = new Queue();
queue.enqueue(10);
queue.enqueue(20);
console.log(queue.peek()); // 10
console.log(queue.dequeue()); // 10
console.log(queue.isEmpty()); // false
```

<br>

## 스택과 큐의 차이점 요약

| **특징**        | **스택**                  | **큐**                     |
| --------------- | ------------------------- | -------------------------- |
| **데이터 처리** | LIFO (Last In, First Out) | FIFO (First In, First Out) |
| **추가 위치**   | 맨 위 (Top)               | 뒤 (Rear)                  |
| **제거 위치**   | 맨 위 (Top)               | 앞 (Front)                 |

<br>

## JavaScript 예제 코드

### 스택 구현 (배열 사용)

```javascript
const stack = [];

// Push
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack); // [1, 2, 3]

// Pop
console.log(stack.pop()); // 3
console.log(stack); // [1, 2]
```

### 큐 구현 (배열 사용)

```javascript
const queue = [];

// Enqueue
queue.push(1);
queue.push(2);
queue.push(3);
console.log(queue); // [1, 2, 3]

// Dequeue
console.log(queue.shift()); // 1
console.log(queue); // [2, 3]
```
