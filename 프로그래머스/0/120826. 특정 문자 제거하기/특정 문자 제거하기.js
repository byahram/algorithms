function solution(my_string, letter) {
    // 1
    // return my_string.replaceAll(letter, '');
    
    // 2
    let reg = new RegExp(letter, 'g');
    return my_string.replace(reg, '');
}

// "BCB234235678678zdfbdbe".replace(/B/g, '')
// "BCB234235678678zdfbdbe".replace(/[123]/g, '')
// "BCB234235678678zdfbdbe".replace(/[1-9]/g, '')
// "BCB234235678678zdfbdbe".replace(/[a-z]/g, '')
// "BCB234235678678zdfbdbe".replace(/[A-Z]/g, '')