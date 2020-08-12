# Validathon

## Library for data validation customizable and able to raise external exceptions.

- Quick start
    - Valid Data
    - Invalid Data
    - Invalid Data with custom exception
- Validations


#### Quick start

##### Valid Data
```python
from validathon.validator import Validator
from validathon import (
    Required, MaxLengthStr, MinLengthStr, StrShouldContains, ShouldBeInt,
)
data = {
    'person': {
        'name': 'Jemma Valentine',
        'age': 28,
    }
}
vmap = {
    'person': {
        'name': [
            Required(), MinLengthStr(2), MaxLengthStr(50), StrShouldContains(' '), 
        ],
        'age': ShouldBeInt(required=False)    
    } 
}
validator = Validator(vmap)
vresult = validator.validate(data)
print(vresult)
```

##### Invalid Data
```python
from validathon.validator import Validator
from validathon import (
    Required, MaxLengthStr, MinLengthStr, StrShouldContains, ShouldBeInt,
)
data = {
    'person': {
        'name': 'Jemma',
        'age': 28,
    }
}
vmap = {
    'person': {
        'name': [
            Required(), MinLengthStr(8) 
        ],
        'age': ShouldBeInt(required=False)    
    } 
}
validator = Validator(vmap)
validator.validate(data) # raise default Exception (MinLengthStrExc) for this validation 
```

##### Invalid Data with Custom Exception
```python
from validathon.validator import Validator
from validathon import (
    Required, MinLengthStr,
)


class CustomException(Exception): # Can be a HTTP Exception from some web framework. (Django, Flaskm aiohttp etc....)
    
    def __init__(self):
        super().__init__('My HTTP Exception') 


data = {
    'person': {
        'name': 'Jemma',
        'age': 28
    }
}
vmap = {
    'person': {
        'name': [
            Required(), MinLengthStr(8, exc=CustomException) 
        ]
    } 
}
validator = Validator(vmap)
validator.validate(data) # raise default Exception (MinLengthStrExc) for this validation 
```


- TODO:
- Describe the validation order
- required field in each validation
- required validations
- how required validation works
- AbsentFieldValidation decorator
- Creating a new validations, IValidation Interface 
### Details
- All default validations classes have a decorator for validate if field exists. And also is possible customize the exeception thougth paramer *absent_field_exc*. But, for that not need pass this argument for all validations. Use de *Required* class as the first validation.

 