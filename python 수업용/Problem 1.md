# Problem 1

## 상승장? 하락장?

```python
import requests

url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']
print(data)

sell_p = int(data['opening_price'])
max_p = int(data['max_price'])
min_p = int(data['min_price'])
varience = int(data['max_price']) - int(data['min_price'])
if sell_p + varience > max_p:
    print('상승장')
else:
    print('하락장')
```



## 모음 제거하기

```python
my_str = "Life is too short, you need python"
my_str = my_str.replace('a', '')
my_str = my_str.replace('e', '')
my_str = my_str.replace('i', '')
my_str = my_str.replace('o', '')
my_str = my_str.replace('u', '')
print(my_str)                        #같은 코드를 3줄 이상 쓰고있다면 반복문 생각해보기!
```

By 강사님 코드

```python
my_str = "Life is too short, you need python"
result = ""
#my_str를 반복하면서,
for char in my_str:
    #모음이 아니면 result에 추가한다.
  #  if char in ['a','e','i','o','u']:
	 if char not in 'aeiou':
    result += char
   

print(result)
    
 
#반복문이 끝나면 출력한다.
```

```python
my_str = "Life is too short, you need python"
for vowl in 'aeiou':
    my_str = my_str.replace(vowl, '')

print(my_str)
```



## 개인정보보호

```python
phone = input()
star = "*******"

if not phone.startswith('010', 0) and len(phone) == 11:
    print('핸드폰번호를 입력하세요')
else:
    print(star + phone[7:])
```

```python
#강사님 코드
phone = input()
if phone[0:3] == '010' and len(phone) == 11:
    print("*" * 7 + phone[-4:])
    #print(f'{phone[-4:]: * > 11}')       #이 함수 사용법 익혀두기 이건 fString 활용법인거 같다.
else:
    print('핸드폰 번호를 입력하세요')
```



## 정중앙

```python
text = input()
loc = len(text)
if loc % 2 == 0:
    print("가운데 글자 : {0} , {1}".format(text[int(loc / 2) - 1], text[int(loc / 2)]))
    
else:
    print(text[int(loc / 2)])

```

```python
text = input()
num = len(text) //2 
if len(text) %2 = 0 :
    print(text[num])
else:
    print(text[num-1:num+1]) 
```



# Work Shop

1.

```python
n = 5
m = 9
a = (("*" * n + "\n") * m)
print(a)

```



2.

```python
print('"파일은 C:|Windows|Users|내문서|Python에 저장이 되었습니다."\n 나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지\'')

```





3.

```python
a = 0
b = 0

for i in range(-21, 22):
    if i == 0:
        continue
    if 21 % i == 0:
        j = int(-21 / i)
        if i + j == 4:
            a = i
            b = j


print("x의 값은 {0} 과 {1}입니다.".format(-a, -b))
```

