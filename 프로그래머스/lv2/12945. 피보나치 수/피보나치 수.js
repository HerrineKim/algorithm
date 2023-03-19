function solution(n) {
    var answer = 0;
    if (n === 1) return 1;
    if (n === 2) return 1;
    let arr = [1, 1];
    for (let i = 2; i < n; i++) {
        arr.push((arr[i - 1] + arr[i - 2]) % 1234567);
    }
    answer = arr[n - 1];
    return answer;
}
