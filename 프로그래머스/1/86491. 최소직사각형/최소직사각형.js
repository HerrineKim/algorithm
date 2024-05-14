function solution(sizes) {
    var answer = 0;
    for (let i = 0; i < sizes.length; i++) {
        sizes[i].sort((a, b) => a - b);
    }
    
    let firstNum = 0
    let secondNum = 0
    for (let j = 0; j < sizes.length; j++) {
        if (firstNum < sizes[j][0]) {
            firstNum = sizes[j][0]
        }
        if (secondNum < sizes[j][1]) {
            secondNum = sizes[j][1]
        }
    }
    
    answer = firstNum * secondNum
    return answer;
}