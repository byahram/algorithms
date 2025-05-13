function solution(my_str, n) {
    // 1. 정규표현식
    return my_str.match(new RegExp(`.{1,${n}}`, 'g'));
    
    // 2. 정규표현식 안쓰고
    // let result = []
    // for (let i = 0; i < my_str.length; i += n) {
    //     result.push(my_str.slice(i, i + n))
    // }
    // return result
}