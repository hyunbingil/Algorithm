nationWidth = {
    'korea': 220877,
    'Rusia': 17098242,
    'China': 9596961,
    'France': 543965,
    'Japan': 377915,
    'England' : 242900,
}
  
let area = [];
let tmp = [];
for (let key in nationWidth) {
    area.push(nationWidth[key]);
}
  
for (let i=1; i < area.length; i++) {
    let a = area[0] - area[i];
    if (a < 0) {
        a = -(a);
    }
    tmp.push(a);
}
  
let min = tmp[0];
let keyy = 0;
for (let j=1; j < tmp.length; j++) {
    if (min > tmp[j]) {
        min = tmp[j];
        keyy = j;
    }
}
  
console.log(Object.keys(nationWidth)[keyy+1])
  
  // 위에 노가다들을 해결해줄 메소드들.....
  // const nationWidth = {
  // 	'korea': 220877,
  // 	'Rusia': 17098242,
  // 	'China': 9596961,
  // 	'France': 543965,
  // 	'Japan': 377915,
  // 	'England' : 242900,
  // };
  
  // const w = nationWidth['korea'];
  
  // delete nationWidth['korea'];
  
  // const entry = Object.entries(nationWidth);
  // const values = Object.values(nationWidth);
  
  // //gap에 최댓값 저장
  // let gap = Math.max.apply(null, values);
  // let item = [];
  
  // for (let i in entry){
  //   if (gap > Math.abs(entry[i][1] - w)){
  //     gap = Math.abs(entry[i][1] - w);
  //     item = entry[i];
  //   }
  // }
  
  // console.log(item[0],item[1]-220877);