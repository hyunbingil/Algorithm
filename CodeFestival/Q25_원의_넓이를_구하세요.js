function circleArea(n) {
    let area = n * n * 3.14;
    return area;
}

let m = prompt("반지름 길이를 적으세요.");
// m = parseInt(m, 10);
// 안해도 되네

console.log(circleArea(m));

