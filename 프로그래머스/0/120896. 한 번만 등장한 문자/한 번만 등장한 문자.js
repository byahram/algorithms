function solution(s) {
    // 1. 
    // return [...s].filter(c => s.split(c).length == 2).sort().join("");
    
    // 2.
    
    return [...s].filter(c => s.match(new RegExp(c, "g")).length == 1).sort().join("");
}