from validathon.validations.ivalidation import IValidation
from validathon.result import ValidationResult
from validathon.validations.exceptions import FieldDoesNotExistsExc
from typing import Type, Any
from validathon.config import REQUIRED_KEY

from validathon.config import REQUIRED_KEY


class AbsentFieldValidatedInner(IValidation):

    _validation: Type[IValidation]
    _absent_field_exc: Exception

    def __init__(self, validation: Type[IValidation], absent_field_exc: Exception = None):
        self._validation = validation
        self._absent_field_exc = absent_field_exc

    def _field_does_not_exists(self, key, value):
        if value == REQUIRED_KEY:
            if bool(self._absent_field_exc):
                raise self._absent_field_exc
            raise FieldDoesNotExistsExc(
                ValidationResult(field_name=key, msg=f'Não validado, campo "{key}" inexistente.', valid=False) # TODO: change this portuguese msg
            )

    def validate(self, key: str, value: Any):
        self._field_does_not_exists(key, value)  # TODO: criar testes unitários para validar essa função
        return self._validation.validate(key, value)

    def __repr__(self):
        return f'AbsentFieldValidated({self._validation.__repr__()})'


class AbsentFieldIgnoreValidation(IValidation):

    _validation: Type[IValidation]

    def __init__(self, validation: Type[IValidation]):
        self._validation = validation

    def validate(self, key: str, value: Any) -> ValidationResult:
        if value == REQUIRED_KEY:
            return ValidationResult(
                field_name=key, msg=f'Not Validated. Field "{key}" does not exists.', valid=None,
                validation=self._validation
            )
        return self._validation.validate(key, value)

class AbsentFieldValidated:

    _validation_clss: IValidation

    def __init__(self, clss: IValidation):
        self._validation_clss = clss

    def __call__(self, *args, **kwargs):
        absent_field_exc = None
        raise_absent_field = True
        if 'absent_field_exc' in kwargs.keys():
            absent_field_exc = kwargs.pop('absent_field_exc')

        if 'raise_absent_field' in kwargs.keys():
            raise_absent_field = kwargs.pop('raise_absent_field')

        if raise_absent_field:
            return AbsentFieldValidatedInner(self._validation_clss(*args, **kwargs), absent_field_exc)

        return AbsentFieldIgnoreValidation(self._validation_clss(*args, **kwargs))
