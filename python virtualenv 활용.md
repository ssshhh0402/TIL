# python virtualenv 활용

> 가상환경(virtualenv)을 사용하는 이유: 독립적인 패키지 관리
>
> ex) A 프로젝트 : B패키지의 버전을 3.2를 쓰는데 C프로젝트 : B패키지의 버전을 2.8로 쓰는 경우 매번 설치/삭제 할수없기때문에 독립된 가상환경을 만들어준다.
>
> 파이썬에서는 가상환경을 만들어주는 다양한 패키지들이 있는데 우리는 python에 내장되어있는 venv를 사용한다.

## 1. 가상환경 폴더 만들기

~~~bash
$ mkdir ~/내가 원하는 폴더위치
~~~

```bash
$ python -m venv ~/특정위치/버전명(혹은 가상환경 명)
```

해당 폴더를 열어보면, 아래와 같은 파일들 존재

```bash
activate 	#git bash용(3.6 ~)
activate.bat	#cmd용
activate.ps1	#power shell 용	
```

## 2. 가상환경 실행 및 종료

### 1. 실행
```bash
$ source ~/특정위치/버전명혹은 가상환경명)
```
### 2. 종료

```bash
$ deactivate 
```



## Tip

`.bashrc`를 활용하면, 조금 더 편리하게 가상환경을 실행할 수 있다. 

`.bashrc`는 git bash를 켜면 실행되는 스크립트이다.

```bash
$ vi ~/.bashrc
```

vim을 통해서 수정이 가능하다. 편집 모드는 `i`, 저장 및 종료는 `esc + :wq` 이다.

작성을 완료한 이후에는 새로 git bash 창을 열거나 아래의 명령어를 입력한다.

```bash
 $ source ~/.bashrc
```

* 수업용 스크립트 파일

```bash
#~/.bashrc
alias venv="source ~/python-virtualenv/3.7.4/Scripts/activate"
venv
```