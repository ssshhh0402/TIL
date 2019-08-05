# WEB 2

## 20190805 Bootstrap

### CDN

* Content Delivery(Distribution) Network
* 컨텐츠(CSS, JS, Image, text등)를 효율적으로 전달하기 위하여 여러노드에 가진 네트워크에 데이터를 제공하는 시스템
* 그냥 데이터 중간 저장소 같은 느낌

### CDN 적용 방법

1) HEAD 태그 안에 STYLE 연결

```HTML
<head>
 ...
 <link
rel="stylesheet"href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"integrity="sha384ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
...
</head>
```

2) BODY 닫는 태그 바로 위에 SCRIPT 연결

```HTML
<body>
 ....
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>
</body>
```



### Spacing

* .m-0

```html
.m-0{
	margin: 0 !important;
}
```

* .mr-0

```html
.mr-0{
	margin-right: 0 !important;
}
```

* .mx-0 

```html
.mx-0{
	margin-left: 0 !important;
	margin-right: 0 !important;
}
```

* .my-0

```html
.my-0{
	margin-top: 0 !important;
	margin-bottom: 0 !important
}
```

* .{0}{1}-{2}

  * {0} : m(margin) | p(padding)

  * {1} : b(bottom) | t(top) | r(right) | l(left) | x(left, right) | y(top, bottom)

  * {2} : 0 (0, 0px)

    ​		1 (0.25, 4px)

    ​		2 (0.5, 8px)

    ​		3 ( 1, 16px)

    ​		4 ( 1.5, 24px)

    ​		5 ( 3, 48px)
    
    		* 1 = 0.25rem = 4px
    		* {2} 앞에 n을 붙일 경우 음수!
    
    

### Color

* 색상 종류
  * primary (#007bff)
  * secondary (#6c757d)
  * success (#28a745)
  * info (#17a2b8)
  * warning (#ffc107)
  * danger (#dc3545)
  * light (#f8f9fa)
  * dark (#343a40)
* 활용법

```html
div{
background-color : primary
}
```

```html
<div class=" bg-primary"></div>
```

```html
p{
	color: primary	
}
```

```html
<p class="text-primary"></p>
```

```html
<p class="alert-warning"></p>
```

![](C:\Users\student\Desktop\캡쳐용\이미지 1.png)

```html
<p class="btn-secondary"></p>
```

![](C:\Users\student\Desktop\캡쳐용\이미지 2.png)



```html
<nav class="navbar-dark bg-primary"
```

![](C:\Users\student\Desktop\캡쳐용\이미지 3.png)



### Border

* 활용법

```html
box{
border-color: primary
}
```

```html
<p class="border border-primary"></p>
```



### Radius

* 종류
  * rounded-circle
  * rounded-pill
  *  a
  * b 
* 활용법

```html
<img src="#" class="rounded-circle">
<img src="#" class="rounded-pill">
```



### Display

* 활용법

```html
a{
display: block
display: inline
display: none
}
```

```html
<a class="d-block"></a>
<a class="d-inline"></a>
<a class="d-none"><</a>
```

* 반응형: d-{0}-{1}  >> 현재 화면에서 {0}이상일 경우 {1}로 출력

```html
<a class="d-sm-none"></a>
<a class="d-lm-none"></a>
```



### Position

* 종류
  * static
  * fixed
  * relative
  * absolute

* 활용법

```html
a{
position: static
position: fixed
position: relative
position: absolute
}
```

```html
<a class="position-static"></a>
<a class="position-fixed"></a>
<a class="position-relatie"></a>
<a class="position-absolute"></a>
```



### Text

* 활용법

```html
p{
text-align: center
font-weight: bold
}
```

```html
<p class="text-center"
```

```html
<p class="font-weight-bold"
```

