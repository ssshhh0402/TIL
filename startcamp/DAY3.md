### Python 내장 함수

* list[index] : index에 -1을 넣을 경우 list의 맨 마지막 원소를 지목한다.

``` bash
 index에 -1을 넣을 경우 맨 마지막을 건드린다.
 string = input('문자를 입력하세요: ')
 print(string[-1]) #=> input이 'abcde'일 경우 e 반환
```

* 값이 무조건 True/False로 나오는 값은 ==0 을 생략해도 상관없다.

```bash
number = int(input('숫자를 입력하세요: '))
	if number % 2 (==0 생략) :
		print ('홀수')
	else
		print ('짝수')
```

* map 함수: map(논리식 1, 반복가능 한 인자)  > 첫번째 인자의 함수를 두번					째 인자를 반복하며 적용

~~~bash
prices = input('물품 가격을 입력하세요: ')
a = prices.split(';')
b = map(int, a)
print(b)   
~~~



* list comprehension : [함수 A for b in c] > 반복하능한 객체 c안의 원소를 하나씩 뽑아(b) 함수 A에 적용한 결과를 반환

```BASH
price = input('물품가격을 입력하세요: ')
price.split(';')
int_price = [int(price) for price in prices]
```



* sort() : 원본 리스트를 변경하며 return은 None

```bash
a = '1,2,4,3,6'
b = a.sort()  #=> a = '1,2,3,4,6' b = None
```



* sorted() : 정렬된 리스트를 return 하며 원본리스트는 변경하지 않는다

```bash
a = '1,2,4,3,6'
b = sorted(a) #=> a = '1,2,4,3,6', b = '1,2,3,4,6'
```



### HTML

# 태그 종류

* `<p>`: 가장 기본적은 태그이며 문단을 나타내는 태그 

```BASH
<P> 문장을 나타냄
```

* `<H1>` ~ `<H6>`: 문장의 크기 및 중요도를 설정하는 태그

```BASH
<H1> H1 </H1>
<H2> H2 </H2>
```

* `<a>` `</a>`: 링크를 설정하여 태그 클릭할 경우 href로 설정한 주소로 이동한다.

``` bash
<a href = "www.naver.com"> A </a> #=> A를 클릭할 경우 											  WWW.NAVER.COM으로 이동
```

* `<img>`: src를 사용하여 사진을 나타내는 태그

```bash
<img src= "a"> #=> a의 주소에 해당하는 이미지를 화면에 출력
```



# STYLE

1.  선택자 : 태그 선택자, 클래스 선택자, 아이디 선택자
   * 태그 선택자: h1{}, p{}





### Day3

	## HTML/CSS

# HTML

`HTML`은 HyperText Markup Language의 약자로 웹 문서를 구조화 하는데 사용되는 언어이다.

1. HTML 기본구조

```BASH
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```

	*  `<head>`, `</head>`는 문서의 정보를 담고 있다.
	*  `<body>`, `</body>` 는 문서의 본문을 담고 있다.

2. 태그의 종류

   1. 기본적으로 태그는 `여는태그`와 `닫는태그`로 구성된다.

   ```bash
   <h1>제목1</h1>
   ```

   	2. `닫는태그`가 없는 경우도 있다.(self-closing tag)

   ``` bash
   <img src = "_________"/>
   ```

   3. 태그의 구성

   ```bash
   <img src = "____" width = "300" height= "300" class= 'blue'/>
   <a href = "_______" class= 'blue'>A</a>
   ```

   * 태그별로 공통적으로 가질 수 있는 속성: `id`, `class`, `style`
   * 각 태그별로 가질 수 있는 속성이 추가적으로 있다.
     * img - `src`, `width`, `height`
     * a = `href`



### CSS

CSS는 Cascading Style Sheets의 약자로,  HTML을 꾸며주는 역활을 한다.

HTML을 꾸며주기 위하여, `선택자(SELECTOR)`을 통해 특정한 element를 지정하여야 한다.

* 태그 선택자

```bash
p{
color: red
}
```



* class 선택자

```bash
.blue{
color: blue;
}
```



* id 선택자

```bash
#pink{
color:pink;
}
```

선택자 우선순위는 id 선택자 > class 선택자> 태그 선택자순으로 적용된다.



## Flask

`Flask`는 파이썬 기반의 micro framework이다

### 기본 활용법

	1. 설치

``` bash
$ pip install flask
```



2. 기본코드

단, app.py라는 실행파일을 만들었다는 조건하에

```bash
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
return 'Hello'

if __name__ == '__main__':
app.run(debug=True)
```



3. 서버 실행

```bash
$flask run
```

* 기본적으로 `flask run`명령어는 `app.py`파일을 실행시킨다. 만약 다른 파일명으로 만들었다면, 옵션을 추가해야한다.
*  마지막 두 줄을 작성해놓았다면, 아래와 같이 실행도 가능하다.

~~~bash
$ python app.py
~~~



## Variable routing

요청 오는 URL을 변수화 하여 값을 사용할 수 있다.

```BASH
@app.route('/hi/<string:name>')
def hi(name):
return f'{name}아 안녕?'
```



## Rendering Template

`HTML` 파일을 만들어 활용할 수 있다. 기본적으로 `templates`폴더에 파일을 만들어야 한다.

```bash
app.py
templates(폴더)/
	hi.html
	lunch.html
	index.html
```

```bash
from flask import Flask, render_template
# 코드들....

@app.route('/hi/')
def hi():
	return render_template('hi.html')
	
```

`HTML` 파일에서 변수의 값을 출력하고자 한다면, 키워드 인자로 그 값을 넘겨줘야한다.

```PYTH
return render_template('hi.html', name=name)
```

그리고 출력을 위해서는 `{{}}`를 사용한다.

```jinja2
<hi>{{name}}야 안녕></h1>
```



## Flask Template Engine - jinja2

Flask는 기본적으로 Template을 만들 때 `jinja2`라는 언어를 사용한다. 기본 문법은 다음과 같다.

1. 값 출력

```jinja2
<h1>{{name}}, 안녕</h1>
```

2. 조건문

~~~jinja2
{% if name == '용흠' %}
	<h1> 반장님 안녕하세요 </h1>
{% else %}
	<h1> 학생들 ㅎㅇㅎㅇ</h1>
{% endif %}
~~~

3. 반복문

```jinja2
{% for menu in menu_list %}
<li> {{menu}} </li>
<% endfor %>
```



​	

## Form Data

HTML에서 사용자로부터 정보를 받기 위해서는 Form 태그를 활용한다.

form 태그 기본구조

```html
<!-- templates/ping.html -->
<form action = "/PONG">
	<input type = "text" name = "say">
    <input type = "submit" value = "전송">
    <input type = "radio" name = "gender" value = "M"> 남자
    <input type = "radio" name = "gender" value = "F"> 여자
  
</form>
```



* Form 태그는 `action`속성으로 해당 폼이 전송될 url을 지정해야 한다.
* form 태그 안에는 `input`태그들을 정의하여, 사용자에게 받을 정보를 만든다.
* `input`태그에는 어떤 종류의 입력을 받을지(`type`)을 정의하고 어떤 변수에 담아서 보낼지 정의한다.

### Flask에서 사용자로부터 정보 받기

1. 사용자가 입력할 수 있는 `Form`보여주기

```python
# app.py
@app.route('/ping')
def ping():
    return render_template('ping.html')
```

~~~html
<!-- templates/ping.html -->
<form action = "/PONG">
	<input type = "text" name = "say">
    <input type = "submit" value = "전송">
 
</form>
~~~





2. 정보입력해서 제출하기(사용자)

~~~html
# app.py
from Flask import render_templates, flask, request
@app.route('/pong')
def pong():
say = request.args.get('say')
return render_templates('pong.html', say(이 아이가 pong.html에서의 변수) = say(이 아이가 app.py에서의 변수))
~~~

```html
<!-- templates/pong.html -->
<hi>{{say}}!!!</hi>
```



* `request.args`는 일종의 `dictionary`이고, `key`는 input에 정의한 `name`속성 값 이고 사용자가 입력한 값은 `value`이다.