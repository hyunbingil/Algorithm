// 다음 배열에서 400, 500을 삭제하는 code를 입력하세요.
var nums = [100, 200, 300, 400, 500];
nums = nums.splice(0, 3);

console.log(nums);

// 답안
// nums.pop(); 두 번 사용해서 빼버리기
// => 좀 더 쉬운 방법.