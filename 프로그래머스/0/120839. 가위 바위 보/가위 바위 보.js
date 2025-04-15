function solution(rsp) {
    // 1
    // var answer = '';
    // for (let i of rsp) {
    //     if (i == '0') {
    //         answer += '5'
    //     }
    //     else if (i == '2') {
    //         answer += '0'
    //     }
    //     else if (i == '5') {
    //         answer += '2'
    //     }
    // }
    // return answer;
    
    // 2
    let answer = {'0':'5', '2':'0', '5':'2'};
    return [...rsp].map(v => answer[v]).join('')
}