let scores = prompt("점수를 입력하세요.").split(' ').map(function(n) {
    return parseInt(n, 10);
}); // 생각도 못한 방법 바로 이렇게 int로 받아올수있다!

scores.sort((a, b) => {
    return a-b;
}); // 오름차순 정렬

let count = 0;
let arr = [];

while (arr.length < 3) {
    let n = scores.pop();
    if (!arr.includes(n)) {
        arr.push(n);
    }
    count += 1;
}

console.log(count);
// 원래 배열에서 pop해서 마지막 원소 얻어오고, 없으면 넣어주고, 있으면 배열에 안넣지만 count를 +1 해주면서 몇개인지까지 세어주기.
// 내가 생각했던 방법은 파이썬에서 간단하게 적용이 가능하지만, js에서는 힘들다. 이러한 다른 방법들도 생각해보아야한다.



