# [level 2] 다리를 지나는 트럭 - 42583 문제 풀이

## **문제 설명**

`progresses`와 `speeds` 배열을 기반으로 작업 완료일을 계산하고 배포 단위별로 기능의 수를 반환

<br>

## **나의 문제 풀이**

```javascript
function solution(bridge_length, weight, truck_weights) {
  let seconds = 0; // 경과 시간
  let bridge = Array(bridge_length).fill(0); // 다리를 나타내는 배열 (다리 길이만큼 0으로 초기화)
  let truckWeightOnBridge = 0; // 다리 위 트럭들의 총 무게

  // 모든 트럭이 다리를 건널 때까지 반복
  while (truck_weights.length > 0 || truckWeightOnBridge > 0) {
    seconds++; // 1초 증가

    // 다리에서 트럭이 한 칸씩 앞으로 이동 (가장 앞의 트럭이 다리를 빠져나감)
    const truckOnBridge = bridge.shift();
    truckWeightOnBridge -= truckOnBridge; // 다리 위 총 무게에서 빠져나간 트럭의 무게를 뺌

    // 대기 중인 트럭이 있는 경우
    if (truck_weights.length > 0) {
      // 다리 위 트럭의 총 무게와 다음 트럭 무게의 합이 다리가 견딜 수 있는 무게 이하인 경우
      if (truckWeightOnBridge + truck_weights[0] <= weight) {
        const enteringTruck = truck_weights.shift(); // 대기 트럭 중 맨 앞 트럭을 꺼냄
        bridge.push(enteringTruck); // 트럭을 다리에 추가
        truckWeightOnBridge += enteringTruck; // 다리 위 총 무게에 추가
      } else {
        bridge.push(0); // 트럭이 다리에 진입하지 못하면 0을 추가
      }
    }
  }

  return seconds; // 모든 트럭이 다리를 건너는 데 걸린 시간 반환
}
```

<br>

## 다른 문제 풀이

```javascript
function solution(bridge_length, weight, truck_weights) {
  // '다리'를 모방한 큐에 간단한 배열로 정리 : [트럭무게, 얘가 나갈 시간].
  let time = 0,
    qu = [[0, 0]],
    weightOnBridge = 0;

  // 대기 트럭, 다리를 건너는 트럭이 모두 0일 때 까지 다음 루프 반복
  while (qu.length > 0 || truck_weights.length > 0) {
    // 1. 현재 시간이, 큐 맨 앞의 차의 '나갈 시간'과 같다면 내보내주고,
    //    다리 위 트럭 무게 합에서 빼준다.
    if (qu[0][1] === time) weightOnBridge -= qu.shift()[0];

    if (weightOnBridge + truck_weights[0] <= weight) {
      // 2. 다리 위 트럭 무게 합 + 대기중인 트럭의 첫 무게가 감당 무게 이하면
      //    다리 위 트럭 무게 업데이트, 큐 뒤에 [트럭무게, 이 트럭이 나갈 시간] 추가.
      weightOnBridge += truck_weights[0];
      qu.push([truck_weights.shift(), time + bridge_length]);
    } else {
      // 3. 다음 트럭이 못올라오는 상황이면 얼른 큐의
      //    첫번째 트럭이 빠지도록 그 시간으로 점프한다.
      //    참고: if 밖에서 1 더하기 때문에 -1 해줌
      if (qu[0]) time = qu[0][1] - 1;
    }
    // 시간 업데이트 해준다.
    time++;
  }
  return time;
}
```

<br>
