/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let stack = []
    for(i=0 ; i<s.length; i++) {
        if(s[i] == '(' || s[i] == '[' || s[i] == '{'  ) {
            stack.push(s[i])
        }
        if(s[i] == ')' && stack[stack.length -1] == '(') {
            stack.pop()
        }
        if(s[i] == ']' && stack[stack.length -1] == '[') {
            stack.pop()
        }
        if(s[i] == '}' && stack[stack.length -1] == '{') {
            stack.pop()
        }
    }
    
    return stack.length ? false : true
};