// reduce를 정확하게 어떻게 쓰는 건지 모르겠음.

let vote = prompt("학생들이 뽑은 후보들을 입력하세요.").split(' ');
let result = {};
let winner = "";

for(let index in vote) {
    let kkey = vote[index];
    result[kkey] = result[kkey] === undefined ? 1 : result[kkey] = result[kkey] + 1; 
}

winner = Object.keys(result).reduce(function(a, b) {
    return result[a] > result[b] ? a : b
});

console.log(`${winner}(이)가 총 ${result[winner]}표로 반장이 되었습니다.`);