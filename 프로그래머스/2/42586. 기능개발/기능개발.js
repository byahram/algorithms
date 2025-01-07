function solution(progresses, speeds) {
    var answer = [];
    for(let i = 0; i < progresses.length; i++) {
        progresses[i] = Math.ceil((100-progresses[i]) / speeds[i]);
        
        if(i != 0 && progresses[i-1] > progresses[i]) {
            progresses[i] = progresses[i-1];
        }
    }

    let i = 0;
    while(progresses.length) {
        answer.push([...progresses].filter(v => v == progresses[i]).length);
        progresses = progresses.filter(v => v !== progresses[i]);
    }
    return answer;
}