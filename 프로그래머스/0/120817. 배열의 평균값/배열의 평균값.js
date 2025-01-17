function solution(numbers) {
    var sum = 0, answer = 0;
    for(let i = 0; i < numbers.length; i++) {
        sum = sum + numbers[i];
    }
    answer = sum / numbers.length;
    return answer;
}