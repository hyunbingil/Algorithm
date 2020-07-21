# 🎡 Code Festival
: javascript와 python 문법을 다지기 위한 문제 100개.
> 두 개 너무 헷갈려서 같은 문제를 풀면서 비교해보기.

## 📑 Q3. 변수의 타입
### 💛 JS
: ```object```
> undefined, string, number은 모두 기본 자료형(primitive type).
``` js
var arr = [100, 200, 300];
console.log(typeof(arr));
```
### 💙 PYTHON
: ```class 'list```
``` py
l = [100, 200, 300]
print(type(l))
```

## 📑 Q4. 변수의 타입2
### 💙 PYTHON
: char 아니고 str임. 헷갈 ㄴㄴㄴㄴㄴㄴ

## 📑 Q5. for문 계산
### 💛 JS
``` js
var a = 10;
var b = 2;

for(var i=1; i<5; i+=2){
    a += i;
}

console.log(a+b);
```
> 16
### 💙 PYTHON
: 파이썬 for문이 나한테는 너무 익숙하지 않아서 헷갈림.
> ```range(1, 5, 2)```가 ```(i=1; i<5; i+=2)```와 같다.
``` py
a = 10
b = 2
for i in range(1, 5, 2):
    a += i

print(a+b)
```

## 📑 Q6. False
### 💛 JS
: NaN, "", 0, undefined, null 등
> 1아님.
### 💙 PYTHON
: None, "", 0, bool(0) 등
> 1아님.

## 📑 Q7. 변수명
### 💛 JS
: JavaScript 식별자는 문자, 밑줄(_) 혹은 달러 기호($)로 시작해야하며\
=> 숫자로 시작 불가능.\
: JavaScript 문법에 존재하는 예약어는 사용이 불가능.
> 1age, let
### 💙 PYTHON
: 영문자(대, 소문자 구분), 숫자, 언더바(_)를 사용할 수 있지만, 첫 자리에는 숫자를 사용할 수 없음.\
: 파이썬 키워드는 변수 명으로 사용 X
> 1age, as

## 📑 Q8. 객체 키 이름 중복(딕셔너리 키 이름 중복)
: 객체 키 이름 중복이 되었을 경우, 마지막으로 넣은 값으로 나타남.
### 💛 JS
``` js
var d = {
    'height':180,
    'weight':78,
    'weight':84,
    'temperature':36,
    'eyesight':1
};

console.log(d['weight']);
```
> 84
### 💙 PYTHON
``` py
d = {'height':180,'weight':78,'weight':84,'temparture':36,'eyesight':1}
print(d['weight'])
```
> 84

## 📑 Q21. set은 어떻게 만드나요?
: 헷갈ㄴㄴㄴㄴ
### 💛 JS
``` js
var x = {1, 2, 3, 5, 6, 7};
var x = {};
var x = new Set('javascript'); // 틀림
var x = new Set(range(5));
var x = new Set(); // 틀림
```
### 💙 PYTHON
``` py
x = {1, 2, 3, 5, 6, 7}
x = {} # 틀림
x = set('python')
x = set(range(5))
x = set()
```

## 📑 Q22. 배수인지 확인하기
: 나머지 연산자 사용하기
``` js
i % 6 == 0
```

## 📑 Q23. OX문제
### 💛 JS
```
console.log(10/3)의 출력 결과는 3이다.
```
: X\
> 출력 결과는 3.3333333333333335 이 나온다.\
소숫점이 없는 정수를 출력하고자 할 때는 Math.floor() 함수를 쓰자.
### 💙 PYTHON
```
console.log(10/2)의 출력 결과는 5이다.
```
: X\
> 출력 결과는 5.0이다.\
소숫점이 없는 정수를 출력하고자 할 때는 int() 사용하기.

## 📑 Q31. 자료형의 복잡도(왜 아닌지 모르겠음.......!)
### 💛 JS
: 배열 내장함수의 시간 복잡도가 O(1)인 것들.
``` js
arr[i]
arr.push(5)
arr.slice() // 아님
arr.pop()
arr.includes(5) // 아님
```
### 💙 PYTHON
: 리스트의 내장함수의 시간 복잡도가 O(1)인 것들.
``` py
l[i]
l.append(5)
l[a:b] # 아님
l.pop()
l.clear()
```