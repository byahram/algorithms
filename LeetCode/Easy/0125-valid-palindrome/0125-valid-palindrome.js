/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // 입력된 문자열에서 알파벳(a-z, A-Z)과 숫자(0-9)를 제외한 모든 문자를 제거하고,
    // 남은 문자열을 소문자로 변환한다.
    let str = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();

    // 글자 시작(start)과 끝(end) 포인터를 설정
    let start = 0;
    let end = str.length - 1;

    // 시작 포인터와 끝 포인터가 서로 만나거나 교차하기 전까지 반복
    while(start < end) {
        // 시작 포인터와 끝 포인터가 가리키는 문자가 동일한지 확인
        if(str[start] === str[end]) {
            start++;
            end--;
        } else {
            return false;
        }
    }
    return true;
};