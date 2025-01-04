# 242. Valid Anagram 문제 풀이

## **문제 설명**

주어진 두 문자열 `s`와 `t`가 있을 때, `t`가 `s`의 **애너그램(anagram)**이라면 `true`를 반환하고, 그렇지 않다면 `false`를 반환하는 문제입니다.

**애너그램(anagram)**은 문자들의 순서만 다르고, 구성하는 문자는 동일한 두 문자열을 의미한다. 즉, 두 문자열이 `같은 알파벳`으로 이루어져 있고, `문자 개수도 동일`하다면 애너그램이라고 할 수 있다.

<br>

## **나의 문제 풀이**

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  // 두 문자열의 길이가 다르면 애너그램일 가능성이 없으므로 false 반환
  if (s.length !== t.length) return false;

  // hashMap은 각 문자의 등장 횟수를 저장하는 객체
  let hashMap = {};

  // 첫 번째 문자열(s)의 문자를 hashMap에 저장
  for (let i = 0; i < s.length; i++) {
    if (hashMap[s[i]]) {
      // 해당 문자가 hashMap에 이미 존재한다면, 값을 1 증가
      hashMap[s[i]]++;
    } else {
      // 처음 등장한 문자라면, 값을 1로 설정
      hashMap[s[i]] = 1;
    }
  }

  /**
   * s = "anagram"일 경우
   *  hashMap = {
   *    a: 3,
   *    n: 1,
   *    g: 1,
   *    r: 1,
   *    m: 1
   *  };
   */

  // 두 번째 문자열(t)의 문자를 hashMap에서 제거
  for (let i = 0; i < t.length; i++) {
    if (hashMap[t[i]]) {
      // 해당 문자가 hashMap에 존재하고, 등장 횟수가 0보다 크다면, 값을 1 감소
      hashMap[t[i]]--;
      continue;
    }
    // 해당 문자가 hashMap에 없거나, 등장 횟수가 이미 0이면 false를 반환
    return false;
  }
  // 모든 문자가 정상적으로 매칭되면 true를 반환
  return true;
};
```

<br>

## **다른 문제 풀이**

### 1.

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  // 1. 문자열 길이 확인
  if (s.length !== t.length) {
    return false;
  }

  /**
   * 2. 고정 크기 배열 count 사용
   *  - 배열 count는 길이가 26인 정수 배열로, 영어 소문자(a-z)의 빈도
   *  - count[0]은 문자 'a', count[1]은 문자 'b', ..., count[25]은 문자 'z'에 대응
   */
  let count = Array(26).fill(0);

  /**
   * 3. 두 문자열의 문자 빈도 계산
   *  - s.charCodeAt(i)는 문자열 s의 i번째 문자의 ASCII 코드를 반환
   *  - -97을 하면 'a'부터 'z'를 0~25의 배열 인덱스에 매핑할 수 있다
   */
  for (let i = 0; i < s.length; i++) {
    count[s.charCodeAt(i) - 97]++; // s의 문자는 등장할 때마다 빈도를 증가
    count[t.charCodeAt(i) - 97]--; // t의 문자는 등장할 때마다 빈도를 감소
  }

  // 4. 배열 값이 모두 0인지 확인: 모든 값이 0이어야 애너그램
  return count.every((val) => val === 0);
};
```

### 2.

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  // 1. 두 문자열의 길이가 다르면 바로 false를 반환
  if (s.length !== t.length) return false;
  /**
   * 2. 문자열을 배열로 변환 → 정렬 → 다시 문자열로 변환
   *    - s.split(""): 문자열 s를 각 문자를 요소로 가지는 배열로 변환
   *      : 예) "listen" → ["l", "i", "s", "t", "e", "n"]
   *    - .sort(): 배열의 문자들을 알파벳 순으로 정렬
   *      : 예) ["l", "i", "s", "t", "e", "n"] → ["e", "i", "l", "n", "s", "t"]
   *    - .join(""): 정렬된 배열을 다시 문자열로 변환
   *      : 예) ["e", "i", "l", "n", "s", "t"] → "eilnst"
   *    - === 비교: 정렬된 두 문자열을 비교
   *      : 만약 s와 t가 애너그램이라면, 정렬 후 두 문자열은 반드시 같아진다.
   *      : 예) "listen"과 "silent" → 모두 "eilnst"
   */
  return s.split("").sort().join("") === t.split("").sort().join("");
};
```

<br>
