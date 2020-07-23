let s = prompt("문자열을 입력하시면 2-gram 형식으로 출력해드려요.");
s = s.split('');

for (let i=0; i<s.length-1; i++) {
    console.log(s[i], s[i+1]);
}