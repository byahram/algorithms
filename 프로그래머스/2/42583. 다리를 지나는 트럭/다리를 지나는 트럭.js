function solution(bridge_length, weight, truck_weights) {
  let seconds = 0;
  let bridge = Array(bridge_length).fill(0);
  let truckWeightOnBridge = 0;

  while (truck_weights.length > 0 || truckWeightOnBridge > 0) {
    seconds++;

    const truckOnBridge = bridge.shift();
    truckWeightOnBridge -= truckOnBridge;

    if (truck_weights.length > 0) {
      if (truckWeightOnBridge + truck_weights[0] <= weight) {
        const enteringTruck = truck_weights.shift();
        bridge.push(enteringTruck);
        truckWeightOnBridge += enteringTruck;
      } else {
        bridge.push(0);
      }
    }
  }

  return seconds;
}