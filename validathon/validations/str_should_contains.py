

from typing import Any
from validathon.ivalidate import IValidation
from validathon.validations.exceptions import StrShouldContainsExc
from validathon.validation_result import ValidationResult
from validathon.validations.exceptions import ValidathonBaseException, FieldDoesNotExistsExc


REQUIRED_KEY = 'campo_não_existe_123456'



class InexistingFieldValidated(IValidation):

    _validation_obj: IValidation
    _absent_field_exc: Exception = None

    def __init__(self, clss: IValidation):
        self._validation_clss = clss
        print(clss)

    def _field_does_not_exists(self, key, value):
        if value == REQUIRED_KEY:
            if bool(self._absent_field_exc):
                raise self._absent_field_exc
            raise FieldDoesNotExistsExc(
                ValidationResult(field=key, msg=f'Não validado, campo "{key}" inexistente.', valid=False)
            )

    def __call__(self, *args, **kwargs):
        if 'absent_field_exc' in kwargs.keys():
            self._absent_field_exc = kwargs.pop('absent_field_exc')

        self._validation_obj = self._validation_clss(*args, **kwargs)
        return self

    def validate(self, key: str, value: Any) -> ValidationResult:
        self._field_does_not_exists(key, value) # TODO: criar testes unitários para validar essa função
        return self._validation_obj.validate(key, value)


@InexistingFieldValidated
class StrShouldContains(IValidation):

    # field_does_not_exists_exc: Exception

    # def __init__(self, string: str, custom_exc: Exception=None, field_does_not_exists_exc: Exception = None):
    def __init__(self, string: str, exc: Exception = None):
        # self._field_does_not_exists_exc = field_does_not_exists_exc
        self._custom_exc = exc
        self._string = string

    def validate(self, key: str, value: Any) -> ValidationResult:
        # super().field_does_not_exists(key, value, self._field_does_not_exists_exc) # TODO: criar testes unitários para validar essa função
        assert isinstance(value, str)
        if self._string not in value:
            if bool(self._custom_exc):
                raise self._custom_exc
            raise StrShouldContainsExc(
                ValidationResult(field=key, msg=f'Field "{key}" not contains "{self._string}".', valid=False)
            )
        return ValidationResult(field=key, msg='', valid=True, validation=self)
