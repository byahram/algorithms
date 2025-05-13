function solution(emergency) {
    let 응급순서 = emergency.slice().sort((a, b) => b - a)      // 큰 수부터 정렬, slice 깊은 복사
    return emergency.map(v => 응급순서.indexOf(v) + 1);
}