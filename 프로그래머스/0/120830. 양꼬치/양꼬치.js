function solution(n, k) {
    // 1
  	// let answer = 0;
  	// if (n >= 10) {
  	// k -= Math.floor(n/10);
  	// }
  	// answer = n * 12000 + k * 2000
  	// return answer;
    
    // 2
    if (n >= 10) {
        k -= ~~(n/10);
    }
    return 12000 * n + 2000 * k;
}
