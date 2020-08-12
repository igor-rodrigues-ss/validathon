# Validathon

## Library for data validation customizable and able to raise external exceptions.

- Quick start
- Validations



#### Quick start

```python
from validathon.validator import Validator
from validathon import StrShouldContains
data = {
    'name1': 'abc-'
}
vmap = {
    'name': StrShouldContains('-')
}
validator = Validator(vmap)
validator.validate(data)
```


### Details
- All default validations classes have a decorator for validate if field exists. And also is possible customize the exeception thougth paramer *absent_field_exc*. But, for that not need pass this argument for all validations. Use de *Required* class as the first validation.

- AbsentFieldValidation 