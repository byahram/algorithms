function solution(i, j, k) {
    // 1.
    // let s = '';
    // for (i; i <= j; i++) {
    //     s += i
    // }
    // return s.split(k).length - 1;
    
    // 2.
    return Array(j-i+1).fill(i).map((v, i) => v + i).join('').split(k)
.length - 1;   
}