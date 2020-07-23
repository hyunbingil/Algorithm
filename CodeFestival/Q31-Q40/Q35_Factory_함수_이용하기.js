function one(n){
    function two(m){
        let mul = m;
        for(let i=0; i<n-1; i++) {
            m = m * mul;
        }
        return m;
    }
    return two;
}

const a = one(2);
const b = one(3);
const c = one(4);

console.log(a(10));
console.log(b(10));
console.log(c(10));

// Math.pow 사용하면 제곱가능.

// function one(n) {
//     function two(value) {
//       const sq = Math.pow(value, n);
//       return sq;
//     }
//     return two;
//   }
  
//   const a = one(2);
//   const b = one(3);
//   const c = one(4);
  
//   console.log(a(10));
//   console.log(b(10));
//   console.log(c(10));