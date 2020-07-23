let data = prompt("숫자를 입력하세요. 몫과 나머지 구해드립니다.").split(' ');

result = Math.floor(parseInt(data[0], 10) / parseInt(data[1], 10));
left = parseInt(data[0], 10) % parseInt(data[1], 10);

console.log(result, left);