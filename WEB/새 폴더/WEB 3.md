# WEB 3

## 20190806

## Grid, Flex, Mediaquery

### GRID

* Grid는 기본적으로 12칸을 세로에 대한 Default 값으로 생성

* 활용법

  * 기본 Grid
  * 응용 Grid
  * Offset
  * 반응형


```html
<div class="container">
    <div class="row">
      <div class="col-4 ">
        <div class="bg-primary text-center text-white">1/3</div>
      </div>
      <div class="col-4">
        <div class="bg-secondary text-center text-white">2/3</div>
      </div>
      <div class="col-4">
        <div class="bg-dark text-center text-white">3/3</div>
      </div>
    </div>
  </div>
```
```html
<div class="container">
      <div class="row">
        <div class="col-3 ">
          <div class="bg-primary text-center text-white">1/4</div>
        </div>
        <div class="col-6">
          <div class="bg-secondary text-center text-white">2/4~3/4</div>
        </div>
        <div class="col-3">
          <div class="bg-dark text-center text-white">4/4</div>
        </div>
  </div>
  </div>
```

```html
<div class="container">
    <div class="row">
      <div class="col-6 offset-6">
        <div class="bg-primary">ㅎㅎ</div>
      </div> 
    </div>
  <div class="row">
    <div class="col-2 offset-5">
      <div class="bg-warning">offset-5</div>
    </div>
  </div>
  
    <div class="row">
      <div class="col-2 offset-1">
        <div class="bg-warning"></div>
      </div>
      <div class="col-4 offset-3">
        <div class="bg-primary"></div>
      </div>
      
    </div>
  </div>
```

```html
<div class="container">
    <div class="row">
      <div class="col-6 col-sm-3">
        <div class="bg-primary">ㅎㅎ</div>
      </div>
      <div class="col-6 col-sm-3">
          <div class="bg-primary">ㅎㅎ</div>
      </div>
      <div class="col-6 col-sm-3">
          <div class="bg-primary">ㅎㅎ</div>
      </div>
      <div class="col-6 col-s m-3">
          <div class="bg-primary">ㅎㅎ</div>
      </div>
    </div>
  </div>
  <hr>
  <div class="container">
      <div class="row">
        <div class="col-6 col-lg-3">
          <div class="bg-primary">ㅎㅎ</div>
        </div>
        <div class="col-6 col-lg-3">
            <div class="bg-primary">ㅎㅎ</div>
        </div>
        <div class="col-6 col-lg-3">
            <div class="bg-primary">ㅎㅎ</div>
        </div>
        <div class="col-6 col-lg-3">
            <div class="bg-primary">ㅎㅎ</div>
        </div>
      </div>
    </div>
    <hr>
  <div class="container">
    <div class="row">
      <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <div class="bg-warning">이거 맞냐1</div>
      </div>
      <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <div class="bg-warning">이거 맞냐2</div>
      </div>
      <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <div class="bg-warning">이거 맞냐3</div>
      </div>
      <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <div class="bg-warning">이거 맞냐4</div>
      </div>  
    </div>
  </div>
```

### FLEX

* Flex 선언

```html
<style>
    .container{
        display:flex;
    }</style>
```

* 활용법

  * flex-direction: 아이템들이 쌓이는 방향 및 기준점설정

    * row(기본값, 수평)
    * column(수직)
    * row-reverse(수평 반대로)
    * column-reverse(수직 반대로)

  * flex-wrap: container 내부에 item 배치 방법

    * wrap(다 포함)
    * no-wrap(기본값, 넘치는 값은 버리거나 넘치는 대로 감)
    * wrap-reverse(포함 후 뒤집기)

  * justify-content: 기준점으로부터 쌓이는 순서

    * flex-start(왼쪽-방향시작, 기본값)
    * flex-end(오른쪽 방향시작)
    * center(중앙에서부터)
    * space-between(아이템들 사이에 균등한 여백)
    * space-around(item 좌우 여백 동일)
    * space-evenly(item 및 외각 여백 동일)

  * align-items:

    * center
    * flex-start(시작점)
    * flex-end(끝)
    * baseline

  * flex-grow: 남은 여백 나눠 가지는 정도

    * 0(기본 값)
    * 1~ (부여되는 수치에 따른 여백 획득)

  * order: flex에서 item들의 순서

    * 0(기본값)
    * 1 ~(현재 위치 + 알파)

    

### MEDIAQUERY

* 사전에 정의 되어 있는 값(sl,md,lg,xl)에 따라 유동적으로 CSS 적용
* 활용법

```HTML
@media print{
  h1{
    color:pink;
  }
}
```

