function solution(age) {
    let char = 'abcdefghij'
    return Array.from(age.toString()).map(v => char[v]).join('');
}