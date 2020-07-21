let s = prompt("문자열을 입력하세요.");
let f = prompt("입력한 문자열에서 찾을 문자열을 입력하세요.");

result = s.indexOf(f);
console.log(result);

/* indexOf() 메서드는 호출한 스트링 객체나 배열에서 
 * 주어진 값과 일치하는 값 혹은 요소의 첫 번째 인덱스를 반환하고 존재하지 않으면 -1을 반환한다.
*/