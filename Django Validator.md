# Django Validator

## 20191029 홍순범

```python
modesl.py
from django.db import models
from django.core.validators import MinValueValidator

class Person(modesl.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(
    validators=[MinValueValidator(20, message='미성년자 출입금지')]
    )
    email = models.CharField(max_length=120)
```

Validator를 활용하여 입력받는 속성 값에 대한 추가적인 검증 가능

Validator는 내가 함수로 선언하여 내가 검증하고 싶은 대로 구현 가능하다





