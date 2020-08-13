# Validathon

## Library for data validation customizable and able to raise external exceptions.

- Quick start
    - Valid Data
    - Invalid Data
    - Invalid Data with custom exception
    - Catch exception

- Serializing ValidationResult
- Create your own validation
- Avalable Validations


#### Quick start

##### Valid Data

- If data is valid the validationResult.msg is empty

```python
from validathon.validator import Validator
from validathon.validations import (
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
```

##### Invalid Data

- The default behavior of validations is raise a exception case data is invalid. If you want change this behavior and return a object with validation information see the next section with use of Catch class.

```python
from validathon.validator import Validator
from validathon.validations import (
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
from validathon.validations import Required, MinLengthStr


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


##### Invalid Data: Catch error and returning a information object
```python
from validathon.validator import Validator
from validathon.validations import MinLengthStr
from validathon.catch import Catch



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
        'name': Catch(MinLengthStr(8, exc=CustomException))
    }
}
validator = Validator(vmap)
vresult = validator.validate(data)  # raise default Exception (MinLengthStrExc) for this validation 
print(vresult, end='\n\n')
print(vresult['person']['name']) # ValidationResult
print('field:', vresult['person']['name'].field_name)
print('Is valid:', vresult['person']['name'].valid)
print('Exc MSG:', vresult['person']['name'].msg)
```


#### Serializing Result


##### Invalid Data
```python
from validathon.validator import Validator
from validathon.vtypes import VALIDATION_VALID, VALIDATION_INVALID, NOT_VALIDATED, ALL_VALIDATIONS
from validathon.validations import (
   MaxLengthStr, StrShouldContains, ShouldBeInt
)
from validathon.serialized import ValidationSerialized


data = {
    'person': {
        'name': 'Jemma Valentine', # Invalid in this case
        'age': 28, # Valid in this case
    }
}
vmap = {
    'person': {
        'name': [
            Catch(MaxLengthStr(10)), Catch(StrShouldContains('123')), 
        ],
        'age': ShouldBeInt(required=False), # Case field age not exist the validation not will be 
        'absent_field': ShouldBeInt(required=False) # Case field age not exist the validation not will be executed
    } 
}
validator = Validator(vmap)
vresult = validator.validate(data)
all_validations = ValidationSerialized().map_msgs(vresult) # Return a map with validation messages. only = ALL_VALIDATIONS
valids = ValidationSerialized().map_msgs(vresult, only=VALIDATION_VALID) # only for valid data
invalids = ValidationSerialized().map_msgs(vresult, only=VALIDATION_INVALID) # only for invalid data
not_validateds = ValidationSerialized().map_msgs(vresult, only=NOT_VALIDATED) # only for invalid data
```

- By default, the ValidationSerialized().map_msgs return the keys in root in output dictionary. Case you want keep the structure of data dictionary just use the parameter root=False

```python
invalids = ValidationSerialized().map_msgs(vresult, root=False, only=VALIDATION_INVALID) # only for invalid data
print(invalids)
```


#### Create your own validation

- For create your own validation you need use two resources:
    - Use and respect the IValidation Interface - (DESCRIBE)
    - Use de AbsentFieldValidation decorator. (Optional) - DESCRIBE

- By default you validation should be exception case the data is invalida, because in this form will be possible use Catch class


```python
from validathon.validations.ivalidation import IValidation
from validathon.decorators import AbsentFieldValidated 
from typing import Any



@AbsentFieldValidated
class MyCustomValidation(IValidation):

    def validate(self, key: str, value: Any) -> ValidationResult:
        if isinstance(value, list):
            raise Exception(f'Field "{key}" not should be a list.') # Should be only exception or HTTPException from your framework

        return ValidationResult(field_name=key, msg='', valid=True, validation=self)


data = {
    'person': {
        'child': {
            'name': [],
        }
    }
}
vmap = {
    'person': {
        'child': {
            'name': MyCustomValidation(), # or
            # 'name': Catch(MyCustomValidation()),
        }
    }
}
validator = Validator(vmap)
validator.validate(data) # Will be raised a Exception: Field "person.child.name" not should be a list.
```

- Custom validation with base exception


```python
from validathon.exceptions import ValidathonBaseException

```

#### Avalable Validations

- MinLengthStr
- MaxLengthStr
- CanNotBeAEmptyStr
- CanNotBeNone
- ShouldBeInt
- ShouldContainsOnlyChars
- StrShouldContains
- Required




- The returning object keep the data dictionary structure
- Case you want catch the exception from wach validation you should be pass the validation instance as argumento for Catch object.


- TODO:
- Describe the validation order
- required field in each validation
- required validations
- custom exception from required validation for specific validation
- how required validation works
- AbsentFieldValidation decorator
- Creating a new validations, IValidation Interface 
### Details
- All default validations classes have a decorator for validate if field exists. And also is possible customize the exeception thougth paramer *absent_field_exc*. But, for that not need pass this argument for all validations. Use de *Required* class as the first validation.

 