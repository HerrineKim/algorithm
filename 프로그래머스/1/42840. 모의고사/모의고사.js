function solution(answers) {
    var answer = [];
    
    const supo1 = [1, 2, 3, 4, 5];
    const supo2 = [2, 1, 2, 3, 2, 4, 2, 5];
    const supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let supo1num = 0;
    let supo2num = 0;
    let supo3num = 0;
    
    for (let i = 0; i < answers.length; i++ ) {
        let index = i % supo1.length;
        if (answers[i] === supo1[index]) {
            supo1num += 1;
        }
    }
    
    for (let i = 0; i < answers.length; i++ ) {
        let index = i % supo2.length;
        if (answers[i] === supo2[index]) {
            supo2num += 1;
        }
    }
    
    for (let i = 0; i < answers.length; i++ ) {
        let index = i % supo3.length;
        if (answers[i] === supo3[index]) {
            supo3num += 1;
        }
    }
    
    const answerArr = [supo1num, supo2num, supo3num];
    const maxVal = Math.max(...answerArr)
    for (let x = 0; x < 3; x++) {
        if (answerArr[x] === maxVal) {
            answer.push(x + 1)
        }
    }

    return answer;
}