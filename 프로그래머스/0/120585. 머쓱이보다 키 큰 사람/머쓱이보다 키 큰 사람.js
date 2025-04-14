function solution(array, height) {
    // 1
    // var answer = 0;
    // for(let i = 0; i < array.length; i++) {
    //     if(array[i] > height) {
    //         answer++;
    //     }
    // }
    // return answer;
    
    // 2
    // let count = 0;
    // for (i of array) {
    //     if (i > height) {
    //         count += 1
    //     }
    // }
    // return count
    
    // 3
    return array.filter(v => v > height).length;
}