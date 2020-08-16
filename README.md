# Validathon

## Customizable utility for data validation recursive in dictionary with injection of exceptions.



- [Resume](#resume)
- [Details](#details)
    - [Default Behavior](#default-behavior)
    - [Customized Validations](#customized-validations)
        - [Validation Interface](#validation-interface)
        - [Absent Field Validation](#absent-field-validation)
    - [Required](#required-for-absent-fields-in-data-dicitionary)
- [Quick start](#quick-start)
    - [Valid Data](#valid-data)
    - [Invalid Data](#invalid-data)
    - [Invalid Data with custom exception](#invalid-data-with-custom-exception)
    - [Invalid Data and catch error (Not Raise Exception)](#invalid-data-and-catch-error-not-raise-exception)

- [Serializing Result of Validation](#serializing-result-of-validation)
- [Create your own validation](#create-your-own-validation)
- [Available Validations](#available-validations)

#### Resume

The Validathon library is a tool to make data validations in python dictionaries. This tool have a lot of validation object and perform recursivly validations over dictionaries. This tool have a customizable strutucture for that de developer create your own validations.

The differential of the *Validathon* is the possibility of the inject a exception object for itself library raise if data is invalid. **Then, case you is developing a web application (independent of the framework - Django, flask, aiohttp and etc.) and want raise a HTTPException just use the exc attribute from validation object passing as value the HTTPException (or any kind exception) object.**


#### Details

##### Default behavior

- Case the data is valid, the *validator.validate* return a dictionary (with same structure from validated data) with *ValidationResult* objects as value, Case is invalid a exception will be raised. [example](#invalid-data).

- Case you not want that a exception be raised, use any *Validation* object as argument to *Cacth* object. [example](#invalid-data-and-catch-error-not-raise-exception).

- By defaut the validation object will be validate a field even though it doesn't exist. if you want that validation be optional, pass the value *False* for *required* parameter in validation object.
When the validation is optional and the field does not exists, will be returned a *ValidationResult* object with attribute *valid=None*.

- By default, case the data validated is valid a ValidationResult will be returned with attriutes:
    - **valid**: Boolean or None. Will be None if data not is validated (case **required=False** and the field not exists in data for validations)
    - **msg**: Message from validation
    - **field_name**: name of field validated
    - **validation**: instance of validation

- If you want add a custom message when the data validation is valid just pass the string for *valid_msg* (*valid_msg='data is valid'*) parameter in Validation object.

- When the data is invalid will be raised the default exception. All default exception has the name of Validation class with *exc* suffix. Example: The default exception from *MinLengthStr* validation is **MinLengthStrExc**.

- By default, all default exceptions has a attribute *validation_result* that contains the data of validations.

##### Customized Validations


###### Absent Field Validation

- All validation object are decorated by *AbsentFieldValidation*. This decorator is responsible for make validation if field does not exists in data for validation or ignore validation of this field case the validation object have a atribute **required=False** (Optional validation). If you create your own validations use this decorator you should decorate your validation with this decorator. [Example]( #create-your-own-validation). The parameters of validation object needed for this decorator are:
    - **required: bool** - Default is **True**. If **required=False** this validation will be optional. This parameter should be used as kwargs.
    - **required_exc: Exception** - Defaul is  **None**. This parameter define a custom exception for validation object if the field that should validated does not exists. **We recommend that use Required(exc=CustomException) validation rather than pass CustomException for each validation object, because, this way you will pass de CustomException only one turn.** Should be used as kwargs.

###### Validation Interface

- All validations implements de *IValidation* interface. This interface standardize the behavior of validation. Case you want create your own validation, you validation class should be implements this interface.

##### Required (For absent fields in data dicitionary)

- If a validation object have a *required=True* (True is the default value)
the validation will be perform and will fail, will be raised a *FieldDoesNotExistsExc* exception. Is possible inject a custom exception case the field dos not exists using the paramenter *required_exc=CustomException()*. For that you not have inject this exception for all validation objects, use the *Required(exc=CustomException())* object for validate if the field exists or no.

#### Quick start


##### Valid Data

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
print(vresult)
```

##### Invalid Data

- The default behavior of validations is raise a exception case data is invalid. If you want change this behavior and return a object with validation information see the next section with use of [Catch](#invalid-data-and-catch-error-not-raise-exception) class.

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
validator.validate(data)  # raise default Exception (MinLengthStrExc) for this validation 
```

##### Invalid Data with Custom Exception
```python
from validathon.validator import Validator
from validathon.validations import Required, MinLengthStr


class CustomException(Exception): # Can be a HTTPException from some web framework. (Django, Flask, aiohttp etc....)
    
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
validator.validate(data) # Raise CustomException
```


##### Invalid Data and Catch Error (Not Raise Exception)

```python
from validathon.validator import Validator
from validathon.validations import MinLengthStr
from validathon.catch import Catch


class CustomException(Exception):  # Can be a HTTPException from some web framework. (Django, Flask aiohttp, etc....)

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


#### Serializing Result of Validation


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
print('All validation types:', ValidationSerialized().map_msgs(vresult)) # Return a map with validation messages. only = ALL_VALIDATIONS
print('Only valid', ValidationSerialized().map_msgs(vresult, only=VALIDATION_VALID)) # only for valid data
print('only invalid', ValidationSerialized().map_msgs(vresult, only=VALIDATION_INVALID)) # only for invalid data
print('only not validated', ValidationSerialized().map_msgs(vresult, only=NOT_VALIDATED)) # only for invalid data
```

- By default, the **ValidationSerialized().map_msgs(vresult: bool, root=True, only=ALL_VALIDATIONS)** *(Signature)* return the keys in the output dictionary root. Case you want keep the structure of validated data dictionary just use the parameter **root=False**.

```python
print('Only invalid keep structure: ', ValidationSerialized().map_msgs(vresult, root=False, only=VALIDATION_INVALID))
```


#### Create your own validation

- For create your own validation you need use two resources:
    - Use and respect the IValidation Interface. [Validation Interface](#validation-interface).
    - Use de AbsentFieldValidation decorator. [Absent Field Validation](#absent-field-validation).

```python
from validathon.validations.ivalidation import IValidation
from validathon.validator import Validator
from validathon.decorators import AbsentFieldValidated 
from validathon.result import ValidationResult
from typing import Any



@AbsentFieldValidated
class MyCustomValidation(IValidation):

    def validate(self, key: str, value: Any) -> ValidationResult:
        if isinstance(value, list):
            raise Exception(f'Field "{key}" not should be a list.') # can be a base exception or a HTTPException from your framework

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


#### Available Validations

All validations are present in module *validathon.validations*.

All validation objects can be receive the kwargs parameter **required** and / or **required_exc** but, these arguments are be from decorator *AbsentFieldValidated* and no from Validation object.

- MinLengthStr
```python
MinLengthStr(min_len: int, exc: Exception = None, valid_msg: str = '')
```
- MaxLengthStr
```python
MaxLengthStr(max_len: int, exc: Exception = None, valid_msg: str = '')
```
- CanNotBeAEmptyStr
```python
CanNotBeAEmptyStr(exc: Exception = None, valid_msg: str = '')
```
- CanNotBeNone
```python
CanNotBeNone(exc: Exception = None, valid_msg: str = '')
```
- ShouldBeInt
```python
ShouldBeInt(exc: Exception = None, valid_msg: str = '')
```
- ShouldContainsOnlyChars
```python
ShouldContainsOnlyChars(exc: Exception = None, valid_msg: str = '')
```
- StrShouldContains
```python
StrShouldContains(string: str, exc: Exception = None, valid_msg: str = '')
```
- Required
```python
Required(exc: Exception = None, valid_msg: str = '')
```
