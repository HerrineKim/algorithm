function solution(n, lost, reserve) {
    let students = new Array(n).fill(1);
    
    for (let l of lost) {
        students[l - 1]--;
    }
    
    for (let r of reserve) {
        students[r - 1]++;
    }
    
    for (let i = 0; i < n; i++) {
        if (students[i] === 0) {
            if (i > 0 && students[i - 1] === 2) {
                students[i - 1]--;
                students[i]++;
            } else if (i < n - 1 && students[i + 1] === 2) {
                students[i + 1]--;
                students[i]++;
            }
        }
    }
    
    let count = 0;
    for (let student of students) {
        if (student > 0) {
            count++;
        }
    }
    
    return count;
}
