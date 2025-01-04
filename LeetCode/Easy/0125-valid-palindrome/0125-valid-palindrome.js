/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // 글자 시작(start)과 끝(end) 포인터를 설정
    let start = 0;
    let end = s.length - 1;

    // 시작 포인터와 끝 포인터가 서로 만나거나 교차하기 전까지 반복
    while(start < end) {
        // 시작 포인터가 알파벳/숫자가 아닌 경우
        while(!isAlphaNumeric(s[start])) {
            start ++;
        }

        // 끝 포인터가 알파벳/숫자가 아닌 경우
        while(!isAlphaNumeric(s[end])) {
            end--;
        }

        // 소문자로 변환 후 비교
        if(s[start].toLowerCase() !== s[end].toLowerCase()) {
            return false;
        }

        // 포인터 이동
        start++;
        end--;
    }
    return true;

};

// 알파벳/숫자인지 확인하는 함수
function isAlphaNumeric(char) {
    return /^[a-zA-Z0-9]$/.test(char);
}