function solution(a, b) {
    const formula1 = Number(String(a) + String(b));
    const formula2 = 2 * a * b;

    return formula1 >= formula2 ? formula1 : formula2;
}