let height = prompt("키를 입력하세요.").split(' ');
let tmp = [...height];
height.sort(function(a, b) {
    return a-b;
})

tmp = tmp.join(' ');
height = height.join(' ');
console.log(tmp);
console.log(height);

if (tmp == height) {
    console.log("YES");
} else {
    console.log("NO");
}

// const unsorted = prompt('키를 입력하세요');
// let sorted = "";

// sorted = unsorted
//   .split(" ")
//   .sort(function(a, b) {
//     return a - b;
//   })
//   .join(" ");

// if (unsorted === sorted) {
//   console.log("Yes");
// } else {
//   console.log("No");
// }