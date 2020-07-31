const bracket = prompt("괄호를 입력하세요.").split('');
let left = 0;
let right = 0;
for (let i=0; i<bracket.length; i++) {
    if (bracket[i] == '(') {
        left += 1;
    }
    else if (bracket[i] == ')') {
        right += 1;
    }
}

if (left == right) {
    console.log("YES");
} else {
    console.log("NO");
}

// 굳이 이렇게 복잡하게 할 필요가 있나?
// function math(e){
//     let count = 0;
    
//     //괄호 개수가 같지 않으면 false
//     for (let i=0; i<e.length; i++){
//         if (e[i] === '('){
//             count++;
//         }
//         if (e[i] === ')'){
//             count--;
//         }
//     }
//     if (count !== 0){
//         return false;
//     }
    
//     let 괄호 = [];
//     for (let i in e){
//         if (e[i] === '(') {
//             괄호.push('(');
//         }
            
//         if (e[i] === ')') {
//             if (괄호.length === 0) {
//                 return false;
//             }
//             괄호.pop();
//         }   
//     }
//     return true;
// }
    

// const n = prompt('입력해주세요.').split('');

// if (math(n) === true) {
//     console.log('YES');
// } else {
//     console.log('NO');
// }