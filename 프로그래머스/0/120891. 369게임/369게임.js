function solution(order) {
    // 1. 정규표현식
    // let value = order.toString().match(/[369]/g) ?? []
    // return value.length;
    
    // 2. 
    // let answer = order.toString().split('').filter(v => v % 3 == 0 ? true : false)
    // return answer.length
    
    // 3
    const s = new Set('369')
    let answer = order.toString().split('').filter(v => s.has(v) ? true : false)
    return answer.length
}