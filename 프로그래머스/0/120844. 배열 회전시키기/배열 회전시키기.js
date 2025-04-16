function solution(numbers, direction) {
    if (direction == 'right') {
        // 1
        // numbers.unshift(numbers.pop())
        
        // 2
        numbers = [numbers.pop(), ...numbers]
    } else {
        // 1
        // numbers.push(numbers.shift())
        
        // 2
        numbers = [...numbers.slice(1), numbers.shift()]
    }
    return numbers;
}