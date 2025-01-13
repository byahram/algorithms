/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let reverse = x.toString().split("").reverse().join("");
    return x == reverse ? true : false;
};