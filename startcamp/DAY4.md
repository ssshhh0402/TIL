# Day 4

## DICTIONARY 활용법

###  변수 활용 잘 하기

* 변수 초기값 설정

``` BASH
min_temp = 0
max_temp = 0
min_city = ''
max_city = ''
for name, temp in city.items();
	if count == 0:
	min_city = name 		#=> 배열의 첫 번째 값으로 초기값 설정
	max_city = name
	min_temp = temp
	max_temp = temp
```

* in 함수 : Python에서 기본저긍로 제공해 주는 내부함수
  	1. 형태: for x in 반복가능 객체
   	2. 기능 :  반복가능 객체 안에 x가 존재하는지 확인하여 True/False로 반환  

```bash
city = {'서울': [-6, -10, 5]}
for temp in city['서울']:
	if 2 in city['서울']:    #=> False
		print("예")
	 else:
	 	print('아니요')
```

* for key, index in 























# Day 4



```bash 
# 2. key, value
  for key, value in my_dict.items():
  	print(key, value)
# 3. value
for value in my_dict.values();
print(value)

# 4. key
for key in my_dict.key():
print(key)
```

```bash
my_dict = {'apple' : '사과', 'banana': '바나나'}
my_dict['apple']
# => 사과
my_dict.get('apple')
#=> 사과
my_dict.get('cat')
#=> None
my_dict.get('cat', '고양이')
# => Not Found
```



