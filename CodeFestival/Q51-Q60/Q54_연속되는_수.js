let num = prompt("숫자 스탬프를 입력하세요.").split(' ').map((n) => {
    return parseInt(n, 10);
  });
  
  num.sort(function(a, b) { // 오름차순
    return a - b;
  });
  
  result = 0
  
  for (let i=0; i<(num.length-1); i++) {
    if (num[i+1] == (num[i] + 1)) {
        result += 1;
    }
  }
  
  if (result == (num.length - 1)) {
    console.log("YES")
  }
  else {
    console.log("NO")
  }
  
  // function sol(l){
  //   l.sort((a,b) => {
  //     return a-b;
  //   });
  
  //   for (let i=0; i<l.length-1; i++){
  //     if(l[i]+1 !== l[i+1]){
  //       return 'NO';
  //     }
  //   }
  //   return 'YES';
  // }
  
  // const n = prompt('입력해주세요').split(' ').map(n => parseInt(n, 10));
  
  // console.log(sol(n));