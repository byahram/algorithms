// input 값 처리
const input = require("fs").readFileSync("/dev/stdin").toString().trim();
var num = input.split(" ").map(Number);
const [a, b] = num;

while(num[0] % num[1] !== 0){
    let rest = num[0] % num[1];    // 두 수의 나머지 저장
    if(rest !== 0) {    // 나머지가 0이 아니라면
        num[0] = num[1];    // 작은 수를 num[0]에 저장하고
        num[1] = rest;    // 나머지 rest값을 num[1]에 저장 후 반복
    }
}
console.log(num[1]);    // 최대공약수
console.log((a * b) / num[1]);    // 최소공배수 a * b / 최대공약수