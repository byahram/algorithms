function solution(s1, s2) {
    // 1
    // return s1.filter(v => s2.includes(v)).length;
    
    // 2. 교집합
    return s1.length + s2.length - new Set([...s1, ...s2]).size
}