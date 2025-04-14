function solution(numbers) {
    // 1
    // var sum = 0, answer = 0;
    // for(let i = 0; i < numbers.length; i++) {
    //     sum = sum + numbers[i];
    // }
    // answer = sum / numbers.length;
    // return answer;
    
    // 2
    return numbers.reduce((a, c) => (a + c), 0) / numbers.length;
}