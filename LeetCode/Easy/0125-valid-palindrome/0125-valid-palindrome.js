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

/**
    시간 복잡도
        - 문자열 정제: replace와 toLowerCase는 각각 O(n)
        - 회문 검사: 두 포인터를 사용하여 문자열 비교 O(n)
        - 총합: O(n) + O(n) = O(n)
    공간 복잡도
        - 정제된 문자열(str)을 저장하므로 O(n)의 추가 메모리가 필요
        - 총합: O(n)
 */