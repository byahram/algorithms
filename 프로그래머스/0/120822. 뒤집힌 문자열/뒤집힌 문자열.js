function solution(my_string) {
    // 1
    // return Array.from(my_string).reverse().join('');
    
    // 2
    return my_string.split('').reverse().join('');
}